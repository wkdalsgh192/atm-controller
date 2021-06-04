import controller
import sys


class Test:
    def __init__(self, bank, atm):
        self.bank = bank
        self.atm = atm

    def card_swipe_test(self, card_number):
        try:
            return self.atm.insert_card(card_number)
        except Exception as e:
            print(e)

    def pin_number_test(self, flag):
        try:
            return atm.check_pin(flag)
        except Exception as e:
            print(e)

    def select_account_test(self, account):
        try:
            return atm.select_account(account)
        except Exception as e:
            print(e)

    def make_transaction_test(self, num, amt=0):
        try:
            return atm.make_transaction(num, amt)
        except Exception as e:
            print(e)


if __name__ == '__main__':

    if sys.version_info < (3, 8, 3):
        sys.exit("Please Use Python 3.8.3 or above")

    ibank = controller.Bank()
    ibank.update_card_info('12341234', '123-123-1234', 100)
    ibank.update_card_info('23452345', '123-234-3456', 500)
    ibank.update_card_info('34567890', '123-456-4567', 300)
    ibank.update_card_info('12341234', '123-123-1234', 200)

    atm = controller.AtmController(ibank, 100)

    test = Test(ibank, atm)
    # Card Swipe Test 1. Invalid Card Number -- Fail
    test.card_swipe_test('0000')

    # Card Swipe Test 2. Unavailable Card Number -- Fail
    test.card_swipe_test('12340000')

    # Check PIN Test. API tells you the PIN number is wrong -- Fail
    test.pin_number_test(False)

    # Select Account Test 1. Invalid Account Format -- Fail
    res = test.card_swipe_test('12341234')
    test.pin_number_test(res)
    test.select_account_test('123')

    # Select Account Test 2. Unavailable Account -- Fail
    test.select_account_test('234-234-2345')

    # Make Transaction Test 1. Out Of Range Exception -- Fail.
    test.make_transaction_test(4)

    # Make Transaction Test 2. Attempt To Deposit Less Than $1 -- Fail
    test.make_transaction_test(2, -1)

    # Make Transaction Test 3. Attempt To Withdraw Less Than $1 -- Fail
    test.make_transaction_test(3)

    # Make Transaction Test 3. Attempt To Withdraw More than The Remaining Balance -- Fail
    res = test.card_swipe_test('12341234')
    test.pin_number_test(res)
    res, msg = test.select_account_test('123-123-1234')
    print(msg)
    test.make_transaction_test(3, 400)
