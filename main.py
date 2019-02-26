import sys
from EffWordList import LongWordList, ShortWordList1, ShortWordList2
from Data import DBfunctions


def main():
    if len(sys.argv) < 2:
        show_help()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-l' or sys.argv[1] == '--longwordlist':
            generated_password = LongWordList.LongWordList(False, 5)
            print(generated_password)
            save(generated_password.generated_password)
        elif sys.argv[1] == '-s1' or sys.argv[1] == '--shortwordlist1':
            generated_password = ShortWordList1.ShortWordList1(False, 4)
            print(generated_password)
            save(generated_password.generated_password)
        elif sys.argv[1] == '-s2' or sys.argv[1] == '--shortwordlist2':
            generated_password = ShortWordList2.ShortWordList2(False, 4)
            print(generated_password)
            save(generated_password.generated_password)
        elif sys.argv[1] == '-ga' or sys.argv[1] == '--getall':
            for i in DBfunctions.getallkey_db():
                print(i)
        elif sys.argv[1] == '-da' or sys.argv[1] == '--delall':
            DBfunctions.delete_db()
        else:
            show_help()
    elif len(sys.argv) == 3 and sys.argv[2] == '--online':
        if sys.argv[1] == '-l' or sys.argv[1] == '--longwordlist':
            generated_password = LongWordList.LongWordList(True, 5)
            print(generated_password)
            save(generated_password.generated_password)
        elif sys.argv[1] == '-s1' or sys.argv[1] == '--shortwordlist1':
            generated_password = ShortWordList1.ShortWordList1(True, 4)
            print(generated_password)
            save(generated_password.generated_password)
        elif sys.argv[1] == '-s2' or sys.argv[1] == '--shortwordlist2':
            generated_password = ShortWordList2.ShortWordList2(True, 4)
            print(generated_password)
            save(generated_password.generated_password)
        else:
            show_help()
    elif len(sys.argv) == 3 and sys.argv[1] == '-gk' or sys.argv[1] == '--getkey':
        print(DBfunctions.getkey_db(sys.argv[2]))
    elif len(sys.argv) == 3 and sys.argv[1] == '-dk' or sys.argv[1] == '--delkey':
        print(DBfunctions.delkey_db(sys.argv[2]))
    else:
        show_help()


def show_help():
    msg = 'Usage: \n' \
          '\tmain.py [GENERATOR] [MODE] [SAVE]\n' \
          'Generator: \n' \
          '\tFor more information about generators: https://www.eff.org/dice \n' \
          '\t\t-l  --longwordlist\n' \
          '\t\t-s1 --shortwordlist1\n' \
          '\t\t-s2 --shortwordlist2\n' \
          '\tExample: \n' \
          '\t\tpython main.py -l\n' \
          'Mode: \n' \
          '\tDefault mode offline\n' \
          '\t\t--online \n' \
          '\t\t--offline \n' \
          '\tExample:\n' \
          '\t\tpython main.py -l --online\n' \
          'Save: \n' \
          '\tSaves the key value pair in the database. Keys produced in this way are always available.\n' \
          '\t\t-ga --getall\n' \
          '\t\t-gk --getkey\n' \
          '\t\t-da --delall\n' \
          '\t\t-dk --delkey\n' \
          '\tExample:\n' \
          '\t\tmain.py -ga\n' \
          '\t\tmain.py -gk name\n' \
          '\t\tmain.py -da\n' \
          '\t\tmain.py -dk name\n'
    print(msg)


def save(generated_password):
    save_input = str(input('Want to save the password?(y/n) '))
    if save_input.lower() == 'y':
        key = input('Create a key name: ')
        DBfunctions.setkey_db(key, generated_password)


if __name__ == '__main__':
    main()
