def get_change(money_given, price):
    change = money_given - price
    coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
    result = [0, 0, 0, 0, 0, 0]

    for i in range(len(coins)):
        coin_value = coins[i]
        coin_count = int(change / coin_value)

        result[i] = coin_count
        change -= coin_count * coin_value

    return result



print(get_change(5, 0.99))
print(get_change(3.14, 1.99))
print(get_change(4, 3.14))
print(get_change(0.45, 0.34))
