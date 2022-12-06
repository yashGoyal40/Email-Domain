def valid_mail(mail):
    m=len(mail)-1                                                                                                 
    n=0                                                                     
    for i in range(0,len(mail)):
        if mail[i]=="@":                                            
            n+=1                                                        
        elif mail[i]=="." and mail[i:]==".com":
            n+=1
        else:
            continue
    if n==2:
        return True
    else:
        return False




def main(data,v):
    print("\nEMAIL DOMAIN SYSTEM\n")
    while True:
        mail=input("\nPlease Enter Your Email Account\\\nTYPE\'records\'To preview the entered mail ID's\\\nTYPE\'exit\'To Stop The Process:\n")
        if mail=="exit" or mail== "Exit":
            break
        elif mail=="records":
            while True:
                c=(input("\nEnter the sequrity PIN\\\nPress\'B\' or \'b\'To go back:\n"))                          
                if c=='4051':
                    print("\nData\n")                                               
                    print(data)
                    print()
                    print("############################")
                    break
                elif c=="b"or c=="B":
                    v=0
                    print("############################")
                    print()
                    break
                else:
                    v+=1
                    if v==2:
                        exit()
                    else:
                        print("\nPlease enter correct PIN\nWARNING: Program Will Be Terminated If Wrong PIN Is Entered Again\n")
        else:        
            if valid_mail(mail):
                for i in range(0,len(mail)):
                    if mail[i]=="@":
                        print("\nusername:",mail[0:i],"\n")                            
                        print("domain name:",mail[i+1:len(mail)],"\n")
                        print("--------------")
                if mail not in data:
                    data.append(mail)
            else:
                print("\nSorry Please Enter A Valid Account\n")


                


'''-------------MAIN--------------'''


'''
1:This python program is to check wether the mail id is valid or not,ie:
1.1:It must contain only one "@"
1.2:It must contain ".com" at the end

2:If the id is valid program will print username and domain name seprately

3:Program will also save the entered mail in a list and that list can only be displayed after giving the security PIN
3.1:A mail will be saved only if its not saved before(if not in the list already)
3.2:PIN is been taken as '4051'
3.3:If the wrong pin is entered once the program will show the warning message
3.4:If the wrong pin entered again the program will be terminated

4:Program will work on loop untill the user triggers 'exit' statement
'''


data=[]
v=0
main(data,v)


