# Array Operations 
array = []

# Input 5 elements
print("Enter 5 array elements:")
for i in range(5):
 num = int(input(f"array[{i}] = "))
 array.append(num)
 
while True:
 print("\n===== ARRAY MENU =====")
 print("1. Display Array")
 print("2. Insert Element")
 print("3. Delete Element")
 print("4. Search Element")
 print("5. Exit")
 
 choice = int(input("Enter your choice: "))
 
 match choice:
     
  case 1:
   print("\nArray Elements:")
   for i in range(len(array)):
     print(f"array[{i}] = {array[i]}")
    
  case 2:
   pos = int(input("Enter position: "))
   value = int(input("Enter value: "))
   if pos >= 0 and pos <= len(array):
     array.insert(pos, value)
     print("Element inserted successfully.")
   else:
     print("Invalid position.")
    
  case 3:
   pos = int(input("Enter position to delete: "))
   if pos >= 0 and pos < len(array):
     del array[pos]
     print("Element deleted successfully.")
   else:
     print("Invalid position.")
    
  case 4:
   value = int(input("Enter element to search: "))
   if value in array:
     print("Element found at index", array.index(value))
   else:
     print("Element not found.")
   
  case 5:
   print("Program Ended.")
   break
  case _:
   print("Invalid Choice!")
