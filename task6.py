items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = {}
    
    for item, data in sorted_items:
        if budget >= data['cost']:
            num_items = budget // data['cost']
            budget -= num_items * data['cost']
            total_calories += num_items * data['calories']
            if num_items > 0:
                selected_items[item] = num_items

    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected_items = {}
    total_calories = dp[n][budget]
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = names[i - 1]
            if item not in selected_items:
                selected_items[item] = 0
            selected_items[item] += 1
            w -= costs[i - 1]

    return selected_items, total_calories

# Тестування
budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Greedy Algorithm Result:", greedy_result)

dp_result = dynamic_programming(items, budget)
print("Dynamic Programming Result:", dp_result)
