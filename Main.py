from data_coffee import resources, MENU

machine_off = False
while not machine_off:
    def condition():
        expression_result = resources["water"] > MENU["espresso"]["ingredients"]["water"] and resources["coffee"] > \
                MENU["espresso"]["ingredients"]["coffee"] and resources["milk"] > MENU["latte"]["ingredients"]["milk"]
        return expression_result

    def calculation_bill():
        cur = cash_coins()
        cost = cur[0] * 0.01 + cur[1] * 0.05 + cur[2] * 0.10 + cur[3] * 0.25
        return cost

    def cash_coins():
        print("Please insert coins.")
        coins_quarters = int(input("How many quarters? : "))
        coins_dimes = int(input("How many dimes? : "))
        coins_nickles = int(input("How many nickles? : "))
        coins_pennies = int(input("How many pennies? : "))
        cur = [coins_pennies, coins_dimes, coins_nickles, coins_quarters]
        return cur

    def not_possible():
        print("Insufficient Resources available")
        print("Come back after a while")

    def coffee_espresso():
        if resources["water"] > MENU["espresso"]["ingredients"]["water"] and resources["coffee"] > \
                MENU["espresso"]["ingredients"]["coffee"]:
            change = calculation_bill() - MENU["espresso"]["cost"]
            resources["money"] += MENU["espresso"]["cost"]
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print(f"Here is ${change} in change")
            print("Here is your espresso ☕ Enjoy!")
        else:
            not_possible()

    def coffee_latte():
        if condition():
            change = calculation_bill() - MENU["espresso"]["cost"]
            resources["money"] += MENU["latte"]["cost"]
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print(f"Here is ${change} in change")
            print("Here is your cappuccino ☕ Enjoy!")
        else:
            not_possible()

    def coffee_cappuccino():
        if condition():
            cur = cash_coins()
            cost = cur[0] * 0.01 + cur[1] * 0.05 + cur[2] * 0.10 + cur[3] * 0.25
            change = cost - MENU["cappuccino"]["cost"]
            resources["money"] += MENU["cappuccino"]["cost"]
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print(f"Here is ${change} in change")
            print("Here is your cappuccino ☕ Enjoy!")
        else:
            not_possible()

    def report():
        print("Milk : ", resources["milk"])
        print("Water : ", resources["water"])
        print("Coffee : ", resources["coffee"])
        print("Money : ", resources["money"])


    def start():
        like_to_have = input("What would you like?(Espresso/Latte/Cappuccino) or N: ").lower()
        if like_to_have == "espresso":
            coffee_espresso()
        elif like_to_have == "latte":
            coffee_latte()
        elif like_to_have == "cappuccino":
            coffee_cappuccino()
        elif like_to_have == "report":
            report()
    if start() == "n":
        break
