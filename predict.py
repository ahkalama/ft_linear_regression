from colorama import Fore, init

init(autoreset=True)

try:
    with open("theta.txt", "r") as f:
        theta0 = float(f.readline().strip())
        theta1 = float(f.readline().strip())
        mileage_mean = float(f.readline().strip())
        mileage_std = float(f.readline().strip())
        price_mean = float(f.readline().strip())
        price_std = float(f.readline().strip())
except FileNotFoundError:
    print(Fore.RED + "[Warning], Training program has not started")
    theta0, theta1, mileage_mean, mileage_std, price_mean, price_std = 0, 0, 0, 1, 0, 1

while True:
    try:
        mileage_input = float(input(Fore.GREEN + "Enter the mileage you want to estimate: "))
        break
    except ValueError:
        print(Fore.RED + "[Error], Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        print(Fore.CYAN + "\n[Successful exit]")
        exit()
        

mileage_normalized = (mileage_input - mileage_mean) / mileage_std

guessvalue = theta0 + theta1 * mileage_normalized

guess_price = guessvalue * price_std + price_mean

print(f"Estimated price: {guess_price:.0f}")