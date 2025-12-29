from menu import menu
from exceptions import DepositError,WithdrawError,InsuffFundError
from ATM_Operations import deposit,withdraw,balance
while(True):
    menu()
    try:
        ch=int(input('enter your choices:'))
        match(ch):
            case 1:
                try:
                    deposit()
                    break
                except ValueError:
                    print("don't try to deposit alnum,str and symbol--invaild")
                except DepositError:
                    print("don't try to negative and zero values")
            case 2:
                try:
                    withdraw()
                    break
                except ValueError:
                    print("don't try to deposit alnum,str and symbol--invalid")
                except WithdrawError:
                    print("don't try to deposit negative and zero value")
                except InsuffFundError:
                    print('InsuffundError')
            case 3:
                balance()
                break
            case 4:
                print('Txs for using this program')
                break
            case _:
                print('your selection of operation is wrong--try again')
    except ValueError:
        print("don't enter the alnum,symbols,strs and float as choice")