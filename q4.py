class BankAccount:
    def __init__(self, initial_balance, interest_rate):
        self.initial_balance = initial_balance
        self.interest_rate = interest_rate
        self.transactions = {i: [] for i in range(1, 7)}  # Stores transactions for 6 months

    def add_transaction(self, month, amount):
        """
        Add a transaction (deposit or withdrawal) to a specific month.
        Positive amount for deposits, negative for withdrawals.
        """
        if 1 <= month <= 6:
            self.transactions[month].append(amount)
        else:
            print("Invalid month. Please enter a month between 1 and 6.")

    def calculate_minimum_balance(self, month):
        """
        Calculate the minimum balance for a specific month based on transactions.
        """
        balance = self.initial_balance
        min_balance = balance

        # Loop through each transaction in the given month
        for transaction in self.transactions[month]:
            balance += transaction
            if balance < min_balance:
                min_balance = balance

        return min_balance

    def calculate_interest(self):
        """
        Calculate interest over 6 months based on minimum monthly balances.
        """
        total_min_balances = 0

        # Find the total of minimum balances for each month
        for month in range(1, 7):
            min_balance = self.calculate_minimum_balance(month)
            total_min_balances += min_balance

        # Calculate total interest based on the interest rate
        total_interest = (total_min_balances * self.interest_rate) / 100

        # Monthly interest (divide by 12) and interest for 6 months (multiply by 6)
        monthly_interest = total_interest / 12
        six_month_interest = monthly_interest * 6

        return {
            "Total Minimum Balances": round(total_min_balances, 2),
            "Total Interest": round(total_interest, 2),
            "Monthly Interest": round(monthly_interest, 2),
            "6-Month Interest": round(six_month_interest, 2)
        }
