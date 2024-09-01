#FirstProgram.py
#Name: Marc Anthony Williams
#Date: 08/31/2024
#Assignment: Lab 1 
#Purpose: To obtain users name and birth year. 

def main():
  print("First Program")
  #Say hello 
  print("hello")
  
  #Ask for the user's name
  name = input("Enter name here: ")
  

  #Use the user's name in the program.
  print("HOw is your day going", name)
  #Ask the user for their age.
  age = input("Enter your age:")
  age = int(age) 
  #Tell the user what year they were born in.
  born = 2022 - age

  #Assume that they have not had their birthday yet this year.
  print("You were born in", born)


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
