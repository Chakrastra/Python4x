# calculate_average(numbers)

def calculate_average(numbers):
    try:
        average = sum(numbers) / len(numbers)
    except TypeError:
        print("Unsupported operation: Check if all elements in the list are numbers.")
    except ZeroDivisionError:
        print("Division by zero error.")    
    else:
        print(average)
    finally:
        print("Calculation completed")
        
numbers = [76, 58, 44, 23, 89]
calculate_average(numbers)
numbers= [76, 'a', 58, 44, 89]
calculate_average(numbers)
empty_list = []
calculate_average(empty_list)









