import pandas as pd
from newPerson import Person
from newStudent import Student
from newEmployee import Employee
import utilities
from MenuEnum import Menu

def saveNewEntry(users_dict, users_list, sum):
    id = input("ID: ")
    if utilities.digitisok(id) == False:
        return -1
    name = input("Name: ")
    age = input("Age: ")
    if utilities.digitisok(age) == False:
        return -1    
    if id in users_dict:
        print("Error: ID " + id + "is alredy use. try again")
        return -1
    try:
        person_type = input("Student or Employee ").lower().strip()
        if person_type == "student":
            users_dict[id] = Student(name, age)
        elif person_type == "employee":    
            users_dict[id] = Employee(name, age)
        else:    
            users_dict[id] = Person(name, age)
        
        users_list.append(id)
        print("ID [" + id + "] saved successfuly ")
        sum += int(age)
        return sum
    except ValueError:
       print("Error: Enter just numbers not somthing else") 
       return -1 
    
def searchById(users_dict):
    id_choice = input("Please Enter your ID you look for: ")
    if id_choice in users_dict:
        printElegant(users_dict,id_choice)
    else:
        print("Error: Id is wrong")
            
def printAgesAvarage(users_dict, avarage):
    if len(users_dict) != 0:
        print(avarage / len(users_dict))
    else:
        print("Error: Cant divide by zero")
        return       

def printAllNames(users_dict):
    for index, id  in  enumerate(users_dict):
        print(str(index) + " . Name: " + users_dict[id].getName())

def printElegant(users_dict, id):
    if id in users_dict:
        print("ID: " + id)
        users_dict[id].printMySelf()

def printAllIds(users_dict): 
    for index, id in enumerate(users_dict):
        print(str(index) + " Id: " +  id )

def printAllEntries(users_dict):
     for index, id in enumerate(users_dict):
         print(str(index) + ". ")
         printElegant(users_dict, id)

def printUsersByIndex(users_list,users_dict):
    choose_index = int(input("Please Choose index: "))
    if choose_index > len(users_list):
        print("Error: index out of range ")  
        return -1
    else:
       id = users_list[choose_index]
       printElegant(users_dict, id) 
        
def saveAllData(users_dict):
    output = []
    for id in users_dict:
        output.append(users_dict[id].newCsv())
    output_file_name = input("What is your output file name? ")    
    user_dict_df = pd.DataFrame(output)
    user_dict_df.to_csv(output_file_name, index = False)
    
    
def main():
    sum = 0
    users_dict = {}
    users_list = []
    while True:
         
        for name in Menu:
            print(str(name.value) + ". " + name.name ) 
        try:
            menu_choice  = input("Choose from Menu: ")
            menu_choice_enum = Menu(int(menu_choice))     
            if menu_choice_enum == Menu.SAVE_A_NEW_ENTRY:
                temp = saveNewEntry(users_dict,users_list, sum)
                if temp != -1:
                    sum = temp
            elif menu_choice_enum == Menu.SEARCH_BY_ID:
                searchById(users_dict) 
            elif menu_choice_enum == Menu.PRINT_AGES_AVERAGE:
                printAgesAvarage(users_dict, sum)
            elif menu_choice_enum == Menu.PRINT_ALL_NAMES:
                printAllNames(users_dict)
            elif menu_choice_enum == Menu.PRINT_ALL_IDS:
                printAllIds(users_dict)
            elif menu_choice_enum == Menu.PRINT_ALL_ENTRIES:
                printAllEntries(users_dict)
            elif menu_choice_enum == Menu.PRINT_USERS_BY_INDEX:
                printUsersByIndex(users_list, users_dict)
            elif menu_choice_enum == Menu.SAVE_ALL_DATA:
                saveAllData(users_dict)
            elif menu_choice_enum == Menu.EXIT: 
                exit_input = input("Are you sure? (y/n)")
                if exit_input == "n":
                    continue 
                else:
                    print("Goodbye")
                    break      
            else:
                print("Error: choose number between 1-8 and not something else...")
            continue_input = input("Press Enter to continue: ")
        except ValueError:   
            print("Error: please choose somthing from the menu ! ")              
try:
    main() 
except KeyboardInterrupt:
    print("goodbye")            
