
class Bank:
    # A bank has a default cash bin and accounts
    def __init__(self):
        self.cash_bin = 0
        self.card_info = {}

    def update_card_info(self, card_number, account, balance):
        if card_number not in self.card_info:
            self.card_info[card_number] = {account: balance}

        else:
            self.card_info[card_number][account] = balance

    def transfer(self, card_number, account, amt, flag):
        card = self.card_info[card_number]
        if flag == 0:
            card[account] += amt
            self.cash_bin += amt
        else:
            if card[account] >= amt:
                card[account] -= amt
                self.cash_bin -= amt
            else:
                raise Exception("Unable to withdraw. Insufficient cash")


class AtmController:
    def __init__(self, bank):
        # Is it Ok to initialize the bank system every time when a atm controller is newly created?
        self.bank = bank
        self.card_number = ""
        self.account = ""

    # insert a card. A customer press his/her card number and pin number
    def insert_card(self):
        self.card_number = input("Please Press Your Card Number : ")

        if self.card_number not in self.bank.card_info:
            print("Invalid card number. Please Check Your Card Number Again")
            return self.insert_card()

        else:
            # This variable would be replaced with using a bank api. Only shows the result now.
            self.check_pin(True)

    def check_pin(self, flag):
        # You only knows whether the PIN number is correct or not.
        if flag != True:
            "Wrong PIN Number. Please Press Correct PIN Number"
        else:
            # Go to select account
            self.select_account()

    def select_account(self):
        print("Please Select Your Account")

        accounts = list(self.bank.card_info[self.card_number].keys())
        for i, v in enumerate(accounts):
            print("{}.{}".format(i, v))

        try:
            s = int(input("Press : "))
            self.account = accounts[s]
        except:
            print("Index Out Of Range. Please Choose Valid Number")
            self.select_account()

        self.make_transaction()

    def make_transaction(self):
        print("Please Select A Number on Your Desired Transaction \n 1.SEE BALANCE \n 2.DEPOSIT \n 3.WITHDRAW \n")

        # functions = [self.seeBalance, self.deposit, self.withdraw]

        try:
            choice = int(input("Press : "))
        except:
            print("Value Error Occurs. Please Press A Correct Number")
            self.make_transaction()

        if choice == 1:
            self.see_balance()
        elif choice == 2:
            self.deposit()
        else:
            self.withdraw()

    def see_balance(self):
        print("Balance : {}".format(
            self.bank.card_info[self.card_number][self.account]))

    def deposit(self):

        amt = int(input("Deposit Amount : "))

        if amt <= 0:
            print("Invalid Amount. Minimum Amount is $1")
            self.deposit()
        else:
            self.bank.transfer(self.card_number, self.account, amt, 0)
            print("{} Deposited Successfully".format(amt))

    def withdraw(self):

        try:
            amt = int(input("Amount Of Withdrawal : "))

            self.bank.transfer(self.card_number, self.account, amt, 1)
            print("${} withdrawn from your account. Thank you.".format(amt))
        except ValueError as e:
            print("Unable to handle : Please Press Number")
            self.withdraw()
        except Exception as e:
            print("Unable to withdraw : Insufficient Cash.")
            self.withdraw()


def main():
    bank = Bank()
    bank.update_card_info('12341234', '123-123-1234', 100)

    atm = AtmController(bank)
    atm.insert_card()


if __name__ == '__main__':
    main()
