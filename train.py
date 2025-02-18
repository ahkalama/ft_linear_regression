import csv
import matplotlib.pyplot as plt

mileage = []
price = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        mileage.append(float(row["km"]))
        price.append(float(row["price"]))

def normalize(data):
    mean = sum(data) / len(data)
    std = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [(x - mean) / std for x in data], mean, std

mileage_normalized, mileage_mean, mileage_std = normalize(mileage)
price_normalized, price_mean, price_std = normalize(price)

theta0 = 0
theta1 = 0
learning_rate = 0.01
epochs = 1000
m = len(mileage_normalized)

for _ in range(epochs):
    error_sum = 0
    error_mileage_sum = 0
    for i in range(m):
        estimatePrice = theta0 + theta1 * mileage_normalized[i]
        error = estimatePrice - price_normalized[i]
        error_sum += error
        error_mileage_sum += error * mileage_normalized[i]
    
    tmp_theta0 = learning_rate * (1/m) * error_sum
    tmp_theta1 = learning_rate * (1/m) * error_mileage_sum
    theta0 -= tmp_theta0
    theta1 -= tmp_theta1

with open("theta.txt", "w") as file2:
    file2.write(f"{theta0}\n{theta1}\n{mileage_mean}\n{mileage_std}\n{price_mean}\n{price_std}")

plt.title("My Bonus Part, Made by ahkalama")
plt.scatter(mileage_normalized, price_normalized, color="blue", label="Real Data")
plt.plot(mileage_normalized, [theta0 + theta1 * x for x in mileage_normalized], color="red", label="Regression Line")
plt.xlabel("Mileage (Normalized)")
plt.ylabel("Price (Normalized)")
plt.legend()
plt.show()

print(f"Completed training! theta0: {theta0:.2f}, theta1: {theta1:.2f}")