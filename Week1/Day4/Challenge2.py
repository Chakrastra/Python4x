#Stack oprations with user interactions

def stack_operations():
    stack = []

    def push(stack, item):
        stack.append(item)
        print(f"Pushed {item} into the stack.")

    def pop(stack):
        if is_empty(stack):
            print("Stack is empty. Cannot pop.")
        else:
            item = stack.pop()
            print(f"Popped {item} from the stack.")
            return item

    def peek(stack):
        if is_empty(stack):
            print("Stack is empty. Nothing to peek.")
        else:
            item = stack[-1]
            print(f"Peeked {item} from the stack.")
            return item

    def is_empty(stack):
        return len(stack) == 0

    def size(stack):
        return len(stack)

    while True:
        print("\nChoose operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Get size")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to be push in stack: ")
            push(stack, item)
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            peek(stack)
        elif choice == '4':
            if is_empty(stack):
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == '5':
            print(f"Size of the stack is {size(stack)}.")
        elif choice == '6':
            print("Exiting stack.")
            break
        else:
            print("Invalid choice.")

stack_operations()



































