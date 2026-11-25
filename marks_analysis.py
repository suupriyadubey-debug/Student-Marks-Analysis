import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading csv file

df = pd.read_csv("students.csv")
print("STUDENTS MARKS DATA")
print(df)

#calculating total marks
subjects = ["Maths","Science","English"]
df["Total"] = df[subjects].sum(axis=1)

#calculating percentage
df["Percentage"] = (df["Total"]/300)*100

#ASSIGNING GRADES

def calculate_grade(Percentage):

    if Percentage>=90:
        return "A+"
    elif Percentage>=80:
            return "A"
    elif Percentage>=70:
            return "B"
    elif Percentage>=60:
            return "C"
    elif Percentage>=33:
            return "D"
    else: 
            return "F"


df["Grade"]=df["Percentage"].apply(calculate_grade)

#checking pass or fail
df["Result"]=np.where(df[subjects].ge(33).all(axis=1),"Pass","Fail")

#displaying final results
print("\nFINAL STUDENT RESULTS")
print(df)

#class average 
average = df["Percentage"].mean()
print("\nClass Average: ",average)

#highest scorer
topper = df.loc[df["Percentage"].idxmax()]
print("\nTopper: ",topper["Name"])
print("Highest Percentage:", topper["Percentage"])

#saving analyzed data
df.to_csv("final_student_results.csv",index=False)

#creating visuslaization
plt.figure(figsize=(10,6))
plt.bar(df["Name"],df["Percentage"])
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.title("Student Performance Analysis ")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("marks_analysis_chart.png")
plt.show()