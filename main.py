import sys
from EffWordList import LongWordList, ShortWordList1, ShortWordList2


def main():
    if len(sys.argv) < 2:
        show_help()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-l' or sys.argv[1] == '--longwordlist':
            generated_password = LongWordList.LongWordList(False, 5)
            print(generated_password)
        elif sys.argv[1] == '-s1' or sys.argv[1] == '--shortwordlist1':
            generated_password = ShortWordList1.ShortWordList1(False, 4)
            print(generated_password)
        elif sys.argv[1] == '-s2' or sys.argv[1] == '--shortwordlist2':
            generated_password = ShortWordList2.ShortWordList2(False, 4)
            print(generated_password)
        else:
            show_help()
    elif len(sys.argv) == 3 and sys.argv[2] == '--online':
        if sys.argv[1] == '-l' or sys.argv[1] == '--longwordlist':
            generated_password = LongWordList.LongWordList(True, 5)
            print(generated_password)
        elif sys.argv[1] == '-s1' or sys.argv[1] == '--shortwordlist1':
            generated_password = ShortWordList1.ShortWordList1(True, 4)
            print(generated_password)
        elif sys.argv[1] == '-s2' or sys.argv[1] == '--shortwordlist2':
            generated_password = ShortWordList2.ShortWordList2(True, 4)
            print(generated_password)
        else:
            show_help()
    else:
        show_help()


def show_help():
    msg = 'Usage: \n' \
          '\tmain.py [GENERATOR] [MODE]\n' \
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
          '\t\tpython main.py -l --online\n'
    print(msg)


if __name__ == '__main__':
    main()
