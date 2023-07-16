class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = "{:.2f}".format(item["amount"]).rjust(7)
            items += f"{description}{amount}\n"
            total += item["amount"]
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    category_names = []
    spent_percentages = []
    spent_amounts = []
    total_spent = 0

    for category in categories:
        total_spent_category = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent_category -= item["amount"]
        spent_amounts.append(total_spent_category)
        total_spent += total_spent_category
        category_names.append(category.name)

    for amount in spent_amounts:
        spent_percent = amount / total_spent
        spent_percentage = int(spent_percent * 100)
        spent_percentages.append(spent_percentage)

    graph = "Percentage spent by category\n"

    for i in range(100, -10, -10):
        graph += str(i).rjust(3) + "| "
        for percentage in spent_percentages:
            if percentage >= i:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    " + "-" * (3 * len(category_names) + 1) + "\n"

    max_length = max([len(name) for name in category_names])

    for i in range(max_length):
        graph += "    "
        for name in category_names:
            if i < len(name):
                graph += name[i] + "  "
            else:
                graph += "   "
        graph += "\n"

    return graph
