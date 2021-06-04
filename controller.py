import sys


class Bank:
    # A bank has a default cash bin and accounts
    def __init__(self):
        self.card_info = {}

    def update_card_info(self, card_number, account, balance):
        if card_number not in self.card_info:
            self.card_info[card_number] = {account: balance}

        else:
            self.card_info[card_number][account] += balance

    def transfer(self, card_number, account, amt, flag):
        card = self.card_info[card_number]
        if flag == 0:
            card[account] += amt
        else:
            if card[account] >= amt:
                card[account] -= amt
            else:
                raise Exception(
                    "Unable to withdraw. Insufficient cash in your account")


class AtmController:
    def __init__(self, bank, cash):
        self.bank = bank
        self.cash_bin = cash
        self.card_number = ""
        self.account = ""

    # insert a card. A customer press his/her card number and pin number
    def insert_card(self, card_number):
        if len(card_number) != 8:
            raise Exception("Type Error: Card Number Should Be 8 Digits")

        self.card_number = card_number
        if self.card_number not in self.bank.card_info:
            raise Exception(
                "Invalid Card Number: Please Check Your Card Number Again")

        else:
            return True

    def check_pin(self, flag):
        # You only knows whether the PIN number is correct or not.
        if flag != True:
            raise Exception(
                "Wrong PIN Number: Please Press Correct PIN Number")
        else:
            print("Welcome! Please Select Your Account")
            accounts = list(self.bank.card_info[self.card_number].keys())
            for i, v in enumerate(accounts):
                print("{}.{}".format(i, v))

            return True

    def select_account(self, account):

        accounts = list(self.bank.card_info[self.card_number].keys())

        if account not in accounts:
            raise Exception("Invalid Account: Please Select A Valid Account")

        else:
            print("Account Selected.")
            self.account = account
            return True, "Please Select A Number on Your Desired Transaction \n 1.SEE BALANCE \n 2.DEPOSIT \n 3.WITHDRAW \n"

    def make_transaction(self, num, amt=0):

        if num == 1:
            self.see_balance()
        elif num == 2:
            self.deposit(amt)
        elif num == 3:
            self.withdraw(amt)
        else:
            raise Exception(
                "Index Out Of Range: Please Choose Between 1 and 3")

    def see_balance(self):
        print("Balance : ${}".format(
            self.bank.card_info[self.card_number][self.account]))

    def deposit(self, amt):
        if amt <= 0:
            raise Exception("Unable to deposit: Minimum is $1")
        else:
            self.bank.transfer(self.card_number, self.account, amt, 0)
            print("${} Saved Successfully".format(amt))

    def withdraw(self, amt):
        if amt <= 0:
            raise Exception("Unable to withdraw: Minimum is $1")
        else:
            try:
                self.bank.transfer(self.card_number, self.account, amt, 1)
                print("${} Withdrawn From Your Account. Thank You.".format(amt))
            except Exception as e:
                print(e)


def main():

    if sys.version_info < (3, 8, 3):
        sys.exit("Please Use Python 3.8.3 or Above")

    # Initialize Bank class -- a card number should be 8 digits
    ibank = Bank()
    ibank.update_card_info('12341234', '123-123-1234', 100)
    ibank.update_card_info('23452345', '123-234-3456', 500)
    ibank.update_card_info('34567890', '123-456-4567', 300)
    ibank.update_card_info('12341234', '123-123-1234', 200)

    # Create an atem controller connected to ibank, which has $100 in cash bin.
    atm = AtmController(ibank, 100)

    res = atm.insert_card('12341234')
    res = atm.check_pin(res)
    res, msg = atm.select_account('123-123-1234')
    print(msg)

    atm.make_transaction(1)
    # Deposit $100 and See the balance
    atm.make_transaction(2, 100)
    atm.make_transaction(1)

    # Withdraw $200 and See The Balance
    atm.make_transaction(3, 200)
    atm.make_transaction(1)


if __name__ == '__main__':
    main()
