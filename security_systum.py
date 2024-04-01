def count_upper(check_upper):
    count=0
    for i in check_upper:
        if i.isupper():
            count+=1
    if count<2:
        print('Your password contains less than 2 uppercase letters')
    return count

def count_lower(check_lower):
    count=0
    for i in check_lower:
        if i.islower():
            count+=1
    if count<2:
        print('Your password contains less than 2 lowercase letters')
    return count

def count_digit(check_digit):
    count=0
    for i in check_digit:
        if i.isdigit():
            count+=1
    if count<2:
        print('Your password contains less than 2 Numbers')
    return count

def count_scharacter(check_scharacter):
    count=0
    for i in check_scharacter:
        if not i.isalnum():
            count+=1
    if count<2:
        print('Your password contains less than 2 special character')
    return count


#checking if a letter occurs more than three times consecutively
def consecutiveletters(password):
    count=1
    for i in range(len(password)):
      for j in range(1,len(password)):
       if password[i]==password[j]:
           count+=1
       else :
           i=j
           break
       
       
    if count>3:
           print('Your password contains three letters which are same and repeat consecutively')
           return False
    return True


def password_check(password):
    if(len(password_list)>3):
      for i in range(len(password_list),len(password_list)-3):
          if password_list[i]==password:
              return False
      return True
    else :
        for i in password_list:
            if i==password:
                print('Your password matches the perivious password')
                return False
        return True
    

def consecutive_username_letters(password):
    for i in range(len(password)-2):
        for j in range(len(username)-2):
          if password[i] == username[j] and password[i+1]==username[j+1] and password[i+2]==username[j+2]:
             print('Your password matches the username letters ')
             return False
    
    return True

        
            

  #Verifying the conditions     

def verify_password(password) :
    lenght=len(password)
    upper_count= count_upper(password)
    lower_count=count_lower(password)
    digit_count=count_digit(password)
    Scharacter_count= count_scharacter(password)  
    check_consicutiveletters=consecutiveletters(password)
    pervious_passwordcheck=password_check(password)
    check_username=consecutive_username_letters(password)
    if lenght>=10 and  upper_count>1 and lower_count>1 and digit_count>1 and Scharacter_count>1 and check_consicutiveletters==True and pervious_passwordcheck==True and check_username==True:
        return True
    if(lenght<10):
        print("Your password is too short")

def condition_verification(password):
    print('Enter your password:')
    password=input()
    check=verify_password(password)
    if(check==True):
        password_list.append(password)
        print("Excepted")
        return password
    else:
     retry=condition_verification(password)

print("Enter your username:")
username=input()
print('. Character Variety: It must contain at least: ')
print('● Two uppercase letters.,● Two lowercase letters.,● Two digits.● Two special characters (e.g., @, #, $, %, &, *, !). ')
password='none'
password_list=['VB*@vansh123']
final_password=condition_verification(password)
print(final_password)
