def getMarks():
    marks = []
    mark = int(input(" Enter mark (or -1 to stop): "))

    while mark != -1:
        marks.append(mark)
        mark = int(input(" Enter mark (or -1 to stop): "))
        
    return marks

def printListSize(marks):
    print(f"Our list has {len(marks)} elements")
    
def printMarks(marks):
    for x in range(len(marks)):
        print(f"Mark {x+1} is {marks[x]}")
        
    for x in range(len(marks)):
        mark = marks[x]
        sum = sum + mark
    
def determineHighest(marks):
    highest = 0
    for i in range (len(marks)):
        currentMark = marks[i]
        if (currentMark > highest):
            highest = currentMark
    
    print(f"The highest mark is {highest}")
    
menu = "Enter 1: Capturing marks/n"
menu += "Enter 2: Check number of marks/n"
menu += "Enter 3: To calculate average of marks/n"
menu += "Enter 4: To find highest mark/n"
menu += "Enter -1: To exit/"

print(menu)
choice = int(input("make your choice: "))

entered_marks = []
if choice == 1:
    entered_marks =  getMarks()
    print(entered_marks)
elif choice ==2:
    print_list_size(entered_marks)
elif choice ==3:
    calc_sum = get_sum_of_marks(entered_marks)
    print("Sum of all marks = ", calc_sum)
elif choice ==4:
    determine_highest(entered_marks)
else: print("not on the menu")
    

    