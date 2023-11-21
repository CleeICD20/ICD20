def input_bug_counts(bug_type):
   bug_count = int(input(f"Enter the number of {bug_type}: "))
   return bug_count

def calculate_percent(total, count):
   percent = f"{count/total * 100:.2f}%"
   return percent

def input_bug_type_and_count():
   bug_type = input("Enter the bug type: ")
   return bug_type, input_bug_counts(bug_type)
    
def display_table(bug1, count1, bug2, count2, bug3, count3): 
   b = "Bug Type"
   c = "Count"
   p = "Percentage"
   t = "Total"
   tp = "100%"
   row1 = f"{b:<11} {c:<9} {p}"
   row2 = 32 * "="
   row3 = f"{bug1:<11} {count1:<9} {calculate_percent(count1 + count2 + count3, count1)}"
   row4 = f"{bug2:<11} {count2:<9} {calculate_percent(count1 + count2 + count3, count2)}"
   row5 = f"{bug3:<11} {count3:<9} {calculate_percent(count1 + count2 + count3, count3)}"
   row6 = 32 * "=" 
   row7 = f"{t:<11} {count1 + count2 + count3:<9} {tp}"
   print(row1)
   print(row2)
   print(row3)
   print(row4)
   print(row5)
   print(row6)
   print(row7)

bug1, count1 = input_bug_type_and_count()
bug2, count2 = input_bug_type_and_count()
bug3, count3 = input_bug_type_and_count()

print(display_table(bug1, count1, bug2, count2, bug3, count3))