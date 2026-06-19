def build_report(rows):

    if not rows:
        print("No data available.")
        return
   

    print("\nCrypto Price Report")
    print("=" * 30)


    for row in rows:

        name = row[1].capitalize()
        price = row[2]

        print(f"{name:<12} ${price:.2f}")



