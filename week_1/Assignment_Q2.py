#Create a program to take as input 5 student records in the following format:
#**roll_num** | **name** | **age** | **marks**(out of 100)
#And then output the records in a tabular form with class average, 
# class highest and class lowest at end in the following format.

#Use dictionaries (list of dictionaries in exact)
#Insert atleast 5 records
#Input must be user-given (Optional) validate the user input, i.e marks aren't
#  greater 100 and other such validations you think there might be
import pandas as pd
rolln = list()
name = list()
age = list()
marks = list()
n_range = int(input('How many records you want to save: '))
for a in range(n_range):
    student_data = input('Enter your roll number,name,age and marks( | separated): ')
    r,n,a,m = student_data.split('|')
    marks.append(int(m))
    rolln.append(int(r))
    name.append(n)
    age.append(a)

data = { 'ROLLN':rolln , 'NAME':name , 'AGE':age , 'MARKS':marks }
pd.DataFrame(data)

b = max(data['MARKS'])
a = data['MARKS'].index(b)
pd.DataFrame({'Class Highest':[data['ROLLN'][a],data['NAME'][a],data['AGE'][a],data['MARKS'][a]]})

b = min(data['MARKS'])
a = data['MARKS'].index(b)
pd.DataFrame({'Class Lowest':[data['ROLLN'][a],data['NAME'][a],data['AGE'][a],data['MARKS'][a]]})

for a in data['MARKS']:
    if a>40 and a<50:
        a = data['MARKS'].index(b)
        print(pd.DataFrame({'Class Average':[data['ROLLN'][a],data['NAME'][a],data['AGE'][a],data['MARKS'][a]]}))