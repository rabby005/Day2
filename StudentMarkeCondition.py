# qusrion 1 
# Grade students based on marks
# marks >= 90, grade = "A"
# 90 > marks >= 80, grade = "B"
# 80 > marks >= 70, grade = "C"
# 70 > marks, grade = "D"


mark = "45"

if(mark >= 90):
    print("Grade A")
elif(mark < 90 and mark >= 80):
    print("Grade B")
elif(mark < 80 and mark >= 70):
    print("Grade C")
elif(mark < 70 and mark >= 60):
    print("Grade D")
elif(mark < 60 and mark >= 50):
    print("Grade E")
elif(mark < 50 and mark >= 40):
    print("Grade F")
    
    
    
 
# input niye ki kore kora hoy

mark = (int(input("Enter your mark: ")))

if(mark >= 90):
    print("Grade A")
elif(mark < 90 and mark >= 80):
    print("Grade B")
elif(mark < 80 and mark >= 70):
    print("Grade C")
elif(mark < 70 and mark >= 60):
    print("Grade D")
elif(mark < 60 and mark >= 50):
    print("Grade E")
elif(mark < 50 and mark >= 40):
    print("Grade F")

