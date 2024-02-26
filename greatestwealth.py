def maximum_wealth(accounts):
    result = list()
    for j in range(0, len(accounts[0])):
        current_cust_wealth = 0
        for i in range(0, len(accounts)):
            current_cust_wealth = current_cust_wealth + accounts[i][j]
            result.append(current_cust_wealth)
        print(result)
        return max(result)


accounts = [[1, 2, 3], [3, 2, 1]]
print(maximum_wealth(accounts))
