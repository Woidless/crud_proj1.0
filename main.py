from views import *

def main():
    while True:
        print('Choose a command\n1-create\t2-listing\t3-retrieve\t4-update\t5-delete\n'+'-'*50)
        choice_ = input('Enter a command: ')
        print('-'*100)
        if choice_ == '1': print(create())

        elif choice_ == '2': print(listing())

        elif choice_ == '3': print(retrieve())

        elif choice_ == '4': print(update())

        elif choice_ == '5': print(delete())

        else: print('The command not found')

        print('-'*100)
        next_ = input('continue work?(no): ')
        if next_.lower() == 'no':
            break
        print('-'*1020)
        
# вызов функции
main()
print('-'*100+'\nGoodbye')