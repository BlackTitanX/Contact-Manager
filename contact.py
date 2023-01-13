import os 

#Path 
FOLDER = 'Numbers/'

#Extention
EXT  = '.txt'


class Contacts:
    def __init__(self, name, number, category):
        self.name = name
        self.number = number
        self.category = category




#Makes the whole thing work G
def app():
    #Initiates the folder
    create_dir()
     
    #Shows the menu
    showmenuOptions()

    #Ask the user what to do 

    ask = True
    while ask:
        option = input('Select input an Option please \r\n')
        option = int(option)

        #excecuting different options 
        if option == 1:
            addContact()
            ask = False

        elif option == 2:
            editContact()   
            ask = False

        elif option == 3:
            searchContactAll()   
            ask = False

        elif option == 4:
            searchContact()   
            ask = False    

        elif option == 5:
            deleteContact()   
            ask = False

        elif option == 6:
            print('Thanks for using our app')
            exit()  

        else:
            print('Invalid Option')

def deleteContact():
    name = input('Type the contact name you that you wish to delete \r\n')
    exist = contactExist(name)
   
    try:
        if exist:
            os.remove(FOLDER + name + EXT)
            print('This contact has been deleted succesfully')
            app()
        else:
            print('Bruh') 
            app() 
    except:
        print("The contact does not exist")
        app() 
    


def searchContact():
    nameX = input('contact contact name \r\n')
    exist = contactExist(nameX)
    if exist:
        with open(FOLDER + nameX + EXT) as contacx:
            for con in contacx:
                print(con.rstrip())
        app()
    else:
        print('this contact does not exist \r\n')        
    app()

def searchContactAll():  
    files = os.listdir(FOLDER) 

    rightFiles = [i for i in files if i.endswith(EXT)]

    #Get all content
    for filee in files:
        with open(FOLDER + filee) as contactx:
            for line in contactx:
                print(line.rstrip())
            print('\r\n')
            print('-----------------------------------')    
    app()        

def editContact():
    print('Write the contact that you wish to edit \r\n')    
    prev_name = input('Enter new Name of the contact \r\n')
    
    #verify before editing
    exist = contactExist(prev_name)
    if exist:
        os.remove(FOLDER + prev_name + EXT)
        contact_newName = input('Input new name: \r\n')
        with open(FOLDER + contact_newName + EXT,'w' ) as fileX:
            
            contact_newNumber = input('Contact new number: \r\n')
            contact_newCategory = input('Contact New category: \r\n')
         
            contact = Contacts(contact_newName, contact_newNumber, contact_newCategory)

            fileX.write('Name:' + contact.name + '\r\n')
            fileX.write('Number:' + contact.number + '\r\n' )
            fileX.write('Category:' + contact.category +'\r\n')
           
            
    else:
        print('This number does not exist')
    app()       

def addContact():
    print('Enter the Data for the contact \r\n')
    contact_name = input('Contact Name: \r\n')
    
    # Variable name that checks if the file existes
    exist = os.path.isfile(FOLDER + contact_name + EXT)  

  
    if not exist:
    # Creates the folder with the given name
        with open(FOLDER + contact_name + EXT,'w' ) as workPlace:
        
             contact_number = input('Contact number: \r\n')
             contact_category = input('Contact category: \r\n')



             contact = Contacts(contact_name, contact_number, contact_category)

             workPlace.write('Name: ' + contact.name + '\r\n')
             workPlace.write('Number: ' + contact.number + '\r\n')
             workPlace.write('Number: ' + contact.category + '\r\n')


             #Success message

             print('The contact has been successfully created')
    else:
        print('The number already')

    app()    

#Menu
def showmenuOptions():
    print('Type one of thus options to perform an operation')
    print('1- to Add a New Number')
    print('2- to edit a new Number')
    print('3- to  show all contacts')
    print('4- to search for a contact')
    print('5- to delete a contact')
    print('6- to quit using the app')


def create_dir():
    # Checks if the Folder exist or not G
    if not os.path.exists(FOLDER):
        #Creates the number path 
       os.makedirs(FOLDER)   


#checks if the contact exist
def contactExist(name):
    return os.path.exists(FOLDER + name + EXT)




# Initiates the Operation      
app()