#Create a program to take as input 5 student records in the following format:
#**roll_num** | **name** | **age** | **marks**(out of 100)
#And then output the records in a tabular form with class average, 
# class highest and class lowest at end in the following format.

#Use dictionaries (list of dictionaries in exact)
#Insert atleast 5 records
#Input must be user-given (Optional) validate the user input, i.e marks aren't
#  greater 100 and other such validations you think there might be

def Calculation(std1, std2, std3, std4, std5):
    avg = ((std1+std2+std3+std4+std5)/500)*100
    return print("Class Average = "+avg+" %")

def ShowDetails():
    print("Roll Number = ",(roll_num))
    print("Name = "+name)
    print("Age = ",(age))
    print("Marks = ",(marks))


roll_num = int(input("Enter Student Roll Num"))    
name = input("Enter Student Name ")
age = int(input("Enter Your Age "))
marks = float(input("Enter Your Marks"))
if marks < 100:
    ShowDetails()
else:
    print("Marks Should be less than 100")

