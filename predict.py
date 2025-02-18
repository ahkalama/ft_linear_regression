with open("theta.txt", "r") as f:
    theta0 = float(f.readline().strip())
    theta1 = float(f.readline().strip())
    mileage_mean = float(f.readline().strip())
    mileage_std = float(f.readline().strip())
    price_mean = float(f.readline().strip())
    price_std = float(f.readline().strip())

mileage_input = float(input("Enter the mileage you want to estimate: "))

mileage_normalized = (mileage_input - mileage_mean) / mileage_std

guessvalue = theta0 + theta1 * mileage_normalized

guess_price = guessvalue * price_std + price_mean

print(f"Estimated price: {guess_price:.2f}")