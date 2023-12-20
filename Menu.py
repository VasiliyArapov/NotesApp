import Service
import Console_UI


def run():
    command = ''
    while command != '7':
        Console_UI.menu()
        command = input().strip()
        if command == '1':
            Service.show('all')
        elif command == '2':
            Service.add()
        elif command == '3':
            Service.show('id')
            Service.id_delete()
        elif command == '4':
            Service.show('id')
            Service.id_rewrite()
        elif command == '5':
            Service.show('date')
            Service.date_show()
        elif command == '6':
            Service.show('id')
            Service.id_show()
        elif command == '7':
            bye()
            break
        else:
            print('There is no such command. Please check your input.')


def bye():
    print('See you soon!')
