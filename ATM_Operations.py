import menu
from exceptions import DepositError,WithdrawError,InsuffFundError
bal=500
def deposit():
    global bal
    amount = int(input('enter the deposit Amount:'))
    if amount<=0:
        raise DepositError
    else:
        global bal
        bal=bal+amount
        print('ur account credited with INR:{}'.format(amount))
        print('now Ur current balance:{}'.format(bal))
def withdraw():
    global bal
    want=int(input('enter the withdraw amount:'))
    if want<=0:
        raise WithdrawError
    elif want+500>bal:
        raise InsuffFundError
    else:
        bal=bal-want
        print('ur amount debited with INR:{}'.format(bal))
        print('now ur current bal in INR:{}'.format(bal))
def balance():
    print('total balance={}'.format(bal))