#MadLib.py
#Name: Marc Anthony Williams
#Date: 08/31/2024
#Assignment: Lab 1 
#Purpose: Ask user for words to create a story

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  noun2 = input("Enter a noun: ")

  #Print the story with the user supplied words.
  print("I saw a" + noun1 + "when riding my bike" + noun2 + "oh what a scene.")
  print("I saw a" , noun1 , "when riding my bike" , noun2 , "oh what a scene.")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
