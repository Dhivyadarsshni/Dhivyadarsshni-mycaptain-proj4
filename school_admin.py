import csv                             #importing csv structure

def writing_into_csv_file(info_list):  #defining a function to write as csv files

    with open('student_info.csv','a',newline='') as csv_file:    #naming a new file and opening to append our datas
        writer=csv.writer(csv_file)                              #defining writer function to access clasess associated to csv files
        
        if csv_file.tell()==0:                                   #checking the initial is 0
            writer.writerow(["Name","Age","Contact_number","E-mail ID"])  #writing the index
        writer.writerow(info_list)
        
if __name__=='__main__':                                         #defining main class
    condition=True                                               #To access the particulars again,we are defining condition=True
    student_num=1                                                #giving index value for students

    while(condition):
        student_info=input("Enter the Student's Information for student {} in the following format (Name Age Contact_number E-mail ID)\n".format(student_num)) 
                        #appending the students' data with the help of format function to store the data correspondingly
     
        student_info_list=student_info.split(' ')            #splitting up the datas that are separated by spaces
        
        print('\n The Entered information is=\n Name: {}\n Age: {}\n Contact_number: {}\n E-mail ID: {}'.format(student_info_list[0],
                                                                            student_info_list[1],student_info_list[2],student_info_list[3]))
                     #to print the data by the above mentioned condition: indenting by spaces
        choice_check=input("Is the entered information is errorless? (yes/no): ")
                      #checking whether the data is correctly entered
        if choice_check=='yes':             #if yes returning to access again
            writing_into_csv_file(student_info_list)
            condition_check=input("Do you want to enter more information? (yes/no): ") #asking whether to append more datas
            if condition_check=='yes':                 #if yes,returning to the condition=True: where the particulars below it can be accesssed
                condition=True
                student_num=student_num+1              #index is increased by 1
            elif condition_check=='no':                #if no,return none
                condition=False                       
        elif choice_check=='no':            #if no re enter the values
            print("\nPlease re-enter your information values!")
