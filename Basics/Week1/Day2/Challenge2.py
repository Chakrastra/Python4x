#Writing a Python program to determine if a student is eligible to sit for exams 
#based on their attendance percentage. The criteria for eligibility is that the
#student must have a minimum attendance of 75%.

def calculate_attendance_percentage(classes_attended, total_classes):
    if total_classes == 0:
        return 0  #so we can avoid division by zero 
    attendance_percentage = (classes_attended / total_classes) * 100
    return attendance_percentage

while True:
    total_classes_held = input("Enter the total number of classes held: ")
    if not total_classes_held.isdigit() or int(total_classes_held) <= 0:
        print("Total number of classes must be a positive integer. Please try again.")
    else:
        total_classes_held = int(total_classes_held)
        attended_classes = input("Enter the number of classes you had attended: ")
        if not attended_classes.isdigit() or int(attended_classes) < 0:
            print("Number of attended classes cannot be negative. Please try again.")
        elif int(attended_classes) > total_classes_held:
            print("Number of attended classes cannot be greater than total classes held. Please try again.")
        else:
            attended_classes = int(attended_classes)
            attendance_percentage = calculate_attendance_percentage(attended_classes, total_classes_held)
            if attendance_percentage >= 75:
                print(f"You are Eligible to sit for the exams.\nYour attendance percentage is: {attendance_percentage:.2f}%")
            else:
                print(f"You are Not Eligible to sit for the exams.\nYour attendance percentage is: {attendance_percentage:.2f}%")
            break



























