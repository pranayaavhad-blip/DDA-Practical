stack = []

while True:
 print("\n----- STACK MENU -----")
 print("1. Push")
 print("2. Pop")
 print("3. Peek")
 print("4. Display")
 print("5. Exit")
 
 choice = int(input("Enter your choice: "))

 match choice:
  case 1:
   item = input("Enter element: ")
   stack.append(item)
   print("Element Inserted")
  case 2:
   if len(stack) == 0:
    print("Stack Underflow")
   else:
    print("Deleted Element =", stack.pop())
  case 3:
   if len(stack) == 0:
    print("Stack is Empty")
   else:
    print("Top Element =", stack[-1])
  case 4:
   if len(stack) == 0:
    print("Stack is Empty")
   else:
    print("Stack =", stack)
  case 5:
   print("Program Ended")
   break
  case _:
   print("Invalid Choice")
