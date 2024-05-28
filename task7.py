import random
import matplotlib.pyplot as plt

# Кількість симуляцій
num_simulations = 1000000

# Ініціалізація словника для підрахунку випадінь кожної суми
sums_count = {i: 0 for i in range(2, 13)}

# Виконання симуляцій
for _ in range(num_simulations):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll_sum = die1 + die2
    sums_count[roll_sum] += 1

# Обчислення ймовірностей
sums_prob = {key: (value / num_simulations) * 100 for key, value in sums_count.items()}

# Аналітичні ймовірності
analytical_prob = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Виведення результатів
print("Сума\tІмовірність (Монте-Карло)\tІмовірність (Аналітична)")
for sum_val in range(2, 13):
    print(f"{sum_val}\t{sums_prob[sum_val]:.2f}%\t\t\t{analytical_prob[sum_val]}%")

# Побудова графіка
sums = list(sums_prob.keys())
mc_probs = list(sums_prob.values())
an_probs = list(analytical_prob.values())

plt.figure(figsize=(10, 6))
plt.bar(sums, mc_probs, color='skyblue', alpha=0.7, label='Монте-Карло')
plt.plot(sums, an_probs, color='red', marker='o', linestyle='-', label='Аналітичні')
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірності сум чисел на двох кубиках (Метод Монте-Карло vs Аналітичні)')
plt.legend()
plt.grid(True)
plt.show()
