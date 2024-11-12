#Purpose of the function is gather two float values from each line in the text file and add it up to get the sum
#Input is the command line argument or the file name in this case it is test.txt
#Output is the added the sum of the values within the file. Ex. if one line had 1 2  then the output would be 3.0
def openfile():
    try: #Try function to test if the file is valid
        filename=input("Enter file name") #user inputs the file the want
        file=open(filename,"r") #variable to open and read the file
        for line in file: #For loop to check within each line
            try: #try exception function to see if values are valid and if not it goes to the exception function
                splitline=line.rstrip("\n") #rstrip removes any trailing characters at the end of the string
                lst=splitline.split(" ")  #split function creates the individual values into a list separated by a space
                add=float(lst[0])+float(lst[1]) #Add the two values after converting it to a float
                print(add)
            except:
                print("Value is invalid, can't add it in")

    except IOError as e: #Error will show up if the file doesn't exist
        print("Error: ",e)

openfile()




