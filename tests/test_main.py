from unittest.mock import MagicMock, patch

from app.api.main import create_application


def create_fake_dependencies():
    return {
        "logger": MagicMock(),
        "create_table": MagicMock(),
        "fetch_crypto_price": MagicMock(),
        "insert_price": MagicMock(),
        "get_all_prices": MagicMock(),
        "build_report": MagicMock(),
        "send_email": MagicMock(),
    }


def test_application_when_workflow_succeeds():
    dependencies = create_fake_dependencies()

    with patch(
        "app.api.main.run_crypto_workflow",
        return_value=True,
    ) as mock_workflow:
        application = create_application(dependencies)

        application()

    logger = dependencies["logger"]

    mock_workflow.assert_called_once_with(
        logger,
        dependencies["create_table"],
        dependencies["fetch_crypto_price"],
        dependencies["insert_price"],
        dependencies["get_all_prices"],
        dependencies["build_report"],
        dependencies["send_email"],
    )

    logger.info.assert_any_call("Application started")
    logger.info.assert_any_call("Crypto workflow completed successfully")
    logger.info.assert_any_call("Application finished execution")


def test_application_when_workflow_fails():
    dependencies = create_fake_dependencies()

    with patch(
        "app.api.main.run_crypto_workflow",
        return_value=False,
    ) as mock_workflow:
        application = create_application(dependencies)

        application()

    logger = dependencies["logger"]

    mock_workflow.assert_called_once()

    logger.warning.assert_called_once_with("Crypto workflow failed")


def test_application_when_workflow_raises_exception():
    dependencies = create_fake_dependencies()

    with patch(
        "app.api.main.run_crypto_workflow",
        side_effect=Exception("Workflow crashed"),
    ) as mock_workflow:
        application = create_application(dependencies)

        application()

    logger = dependencies["logger"]

    mock_workflow.assert_called_once()

    logger.error.assert_called_once_with(
        "Unexpected error in main application: Workflow crashed"
    )
