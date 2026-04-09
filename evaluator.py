print("Welcome to your notes evaluator")
### grades and codes###
print("Before we begin evaluating your grades, you need to tell us what year of high school you are in!")
Year = int(input("Input your school year (1 or 2 or 3)"))
while Year not in [1, 2, 3]:
    print("Your year is incorrect, please type it again")
    Year = int(input("Input your school year (1 or 2 or 3)"))
Notes = {}
Subject = str(input("Input your subject")).upper()
NSubjects = len(Subject)
while NSubjects != 1:
   print ("Your subject is either missing or incorrect, please type it again")
   Subject = str(input("Input your subject")).upper()
Quarter = int(input("Input the Quarter"))
while Quarter not in [1, 2, 3, 4]:
    print("Your quarter is incorrect, please type it again")
    Quarter = int(input("Input the Quarter"))
Code = f"{Subject}{Year}{Quarter}"
### menu ###
while True:
    print ("1 - Add grade")
    print("2- Remove grade")
    print("3- Averege grade (at Etapa school)")
    print("4- Show the menu again")
    print("5- Exit")
    x = int (input("Input the wished option"))
    if x != 1 and x !=2 and x !=3 and x !=4 and x != 5:
        print("this option does not exist yet")
    elif x == 4:
        print("1 - Add grade\n2- Remove grade\n3- Averege grade (at Etapa school)\n4- Show the menu again\n5- Exit")
    elif x == 5:
        print("thanks for using my notes evaluator")
        break
