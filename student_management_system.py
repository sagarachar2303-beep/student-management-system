#function to add student details 
def add_std():
    print()
    print("----------------------------")
    print()
    #Taking roll number from user
    rollno=input("Enter roll number: ")
    #checking duplicate roll number
    for o in student:
        
        if rollno==o["rollno"]:
            print()
            print("Roll number already exists")
            print()
            return
    #Taking student details        
    name=input ("Enter name: ")
    phone=input("Enter phone number: ")
    #Phone number validation
    if not phone.isdigit() or len(phone)!=10:
       print("Invalid phone number.")
       return 
    #Taking Course name   
    course=input("Enter course name: ")
    print()
    print("Student added successfully")
    print()
    print("----------------------------")
    print()
    #Crating dictionary to store Student data
    mix={
         "rollno":rollno,
         "name":name,
         "phone": phone,
         "course": course
        }
    #Adding Student data into list    
    student.append(mix)
    #Saving data into file 
    save_data()

#Function to display all students   
def dis_std():
    #Checking if student list is empty 
    if len(student) == 0:
         print("No students found\n")
         return
    #Displaying all students ditails  
    for i in student:
        print()
        print("--------------------------")
        print()
        print("Rollno: ",i["rollno"])
        print("Name: ",i["name"])
        print("Phone: ",i["phone"])
        print("Course: ",i["course"])
        print()
        print("--------------------------")
        print()
#Function to search a student by roll number      
def search_std():
    print()
    print("----------------------------")
    print()
    #Taking roll number from user 
    find=input("Enter roll number: ")
    print()
    found= False
    
    #searching student
    for j in student:
      if find == j["rollno"]:
          
        print()
        print("--------------------------")
        print()  
        print("Rollno: ",j["rollno"])
        print("Name: ",j["name"])
        print("Phone: ",j["phone"])
        print("Course: ",j["course"])
        print()
        print("--------------------------")
        print()
        found = True
    if found == False:
       #If student not found 
      print()
      print("Invalid roll number")
      print()   
      
#Function to search Student by name    
def search_name_std():
    print()
    print("----------------------------")
    print()
    #Taking name input from user
    search=input("Enter name: ")
    print()
    found = False
    #Searching student name
    for p in student:
       #Avoiding Case insensitive while searching 
      if search.lower() == p["name"].lower():
        print()
        print("--------------------------")
        print()
        print("Name: ",p["name"])
        print("Rollno: ",p["rollno"])
        print("Phone: ",p["phone"])
        print("Course: ",p["course"])
    
        print()
        print("--------------------------")
        print()
        
        found = True
        #If student not found 
    if found == False:
      print()
      print("Student not found")
      print()                    
 
 #Function to update student     
def update_std():
    
    print()
    print("----------------------------")
    print()
    #Taking roll number from user 
    update=input("Enter roll number: ")
    print()
    print("----------------------------")
    print()
    found= False
    #Searching student
    for k in student:
       if update == k["rollno"]:
           print()
           print("----------------------------")
           print()
           #Taking updated details 
           newroll=input("Enter new roll number: ")
           
             #Cheking duplicate numbers
           for x in student:  
             if newroll == x["rollno"] and update != newroll:

               print()
               print("Roll number already exists")
               print()

               return
           newname=input("Enter new name: ")
           newphone=input("Enter new phone number: ")
           #Phone validation 
           if not newphone.isdigit() or len(newphone) != 10:
               print("Invalid phone number")
               return
               
           newcourse=input("Enter new course: ")
           print()
           print("Student updated successfully")
 
           #Updating students details 
           if update==k["rollno"]:
       
              k["rollno"] = newroll
              k["name"] = newname
              k["phone"] = newphone
              k["course"] = newcourse
              print()
              print("--------------------------")
              print() 
              found = True
    #If roll number not found         
    if found == False:
        print("Invalid roll number") 
        print() 
    save_data()     
    
#Function to delete student   
def delete_std():
    print("----------------------------")
    print()
    delete=input ("Enter roll number: ")
    found = False
    for m in student:
        if delete== m["rollno"]:
            student.remove(m)
            print()
            print("Student deleted successfully") 
            print()
            print("----------------------------")
            print() 
            found = True
            break
    if found == False:
        print("----------------------------")
        print()         
        print("Student not found")
        print()  
    save_data()

#Function to save data in file           
def save_data():
    with open("student.txt", "w") as file:
        for n in student:
            file.write(n["rollno"]+",")
            file.write(n["name"]+",")
            file.write(n["phone"]+",")
            file.write(n["course"]+"\n")
#Function for continue or exit option          
def continue_exit():
    try:
       print()
       print("----------------------------")
       print()
       #Taking user choice
       choice = int(input("1.Continue  2.Exit: "))
       print()
       print("----------------------------")
       print()
       
       return choice 
    except:
        print("Invalid choice\n")
        return 1
        
#Function to count Total students 
def total_std():
    print("Total students are: ",len(student))
    print()
     
#Function to exit program    
def exit_std():
    print("Exited successfully")
 
 #Empty list to store Student 
student=[]
#Loding students data from file
try:
    file = open("student.txt", "r")

    for line in file:
        #Splitting data using comma
        data = line.strip().split(",")
        
        #Checking valid data
        if len(data) == 4:
            #Creating dictionary 
            mix = {
                "rollno": data[0],
                "name": data[1],
                "phone": data[2],
                "course": data[3]
            }
            #Adding into list 
            student.append(mix)

    file.close()
#If file not found 
except FileNotFoundError:
    pass

print("==∆==STUDENTS MANAGEMENT SYSTEM==∆==\n")
print()

#Login attempts counter 
attempt=0
#Main program loop
while True:
    #Taking input username and password 
    username = input("Enter username: ")
    password = input("Enter password: ")
    print()
    #Checking login details 
    if username=="admin" and password=="1234":
        #Menu loop
        while True:
            print()
            print("--------------------------")
            print()
            #menu option 
            print("1.Add student")
            print("2.Search specific student")
            print("3.Display all students")
            print("4.Update student details")
            print("5.Delete student details")
            print("6.Total students")
            print("7.Exit")
            print()
            print("--------------------------")
            print()

            try:
                #Taking menu choice
                val = int(input("Enter your choice: "))
                print()

            except:
                print("Invalid choice")
                continue
            #Add student   
            if val == 1:
                add_std()
                print()
                choice = continue_exit()

                if choice == 2:
                  print("Exit successfully")
                  exit()
            #Search student     
            elif val == 2:
                print()
                print("----------------------------")
                print()
                print("1.Search by roll number")
                print("2.Search by name\n")
                print()
                print("----------------------------")
                print()
                search=int(input("Enter your choice: "))
                print()
                
                if search==1:
                    search_std()
                elif search==2:
                    search_name_std()
                else:
                    print("Invalid choice")
                    print()
                choice = continue_exit()

                if choice == 2:
                  print("Exit successfully\n")
                  exit()
            #Dislpay student     
            elif val == 3:
                dis_std()
                print()
                choice = continue_exit()
        
                if choice == 2:
                  print("Exit successfully")
                  exit()
            
            #Update student     
            elif val == 4:
                update_std()
                print()
                choice = continue_exit()
        
                if choice == 2:
                  print("Exit successfully")
                  exit()
            
            #Delete student     
            elif val == 5:
                delete_std()
                print()
                choice = continue_exit()
            
            #Totlw student 
            elif val == 6:

                total_std()

                choice = continue_exit()

                if choice == 2:
                    print("Exit successfully")
                    exit()
            #Exit program           
            elif val == 7:
                exit_std()
                exit()
            
     
            #Invalid menu choice
            else:
                print()
                print("--------------------------")
                print()
                print("Invalid choice")
                print()
                print("--------------------------")
                print()
                choice = continue_exit()

                if choice == 2:
                  print("Exit successfully")
                  exit() 
    #Invalid  login  
    else:
        attempt += 1
        
        print("Attempts left:", 3 - attempt)
        print()
        #Maximum attempts check 
        if attempt == 3:           
            print("Too many attempts")
            print()
            print("Login failed")
            exit()
    