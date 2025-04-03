import pdb

def calculate_total(price, quantity):
    total = price * quantity  # Line 3
    return total  # Line 4

def apply_discount(total, discount):
    return total - (total * discount)  # Line 6

def main():
    price = 100
    quantity = 5
    discount = 0.1  # 10% discount
    total = calculate_total(price, quantity)  # Line 10
    total_after_discount = apply_discount(total, discount)  # Line 11
    print(f"Total after discount: {total_after_discount}")  # Line 12

pdb.set_trace()  # Pause the program here

main()

#1. Breakpoint and Next (n):
    #It runs the whole program and prints the total after the discount then ends the program

#2. Single Line Stepping (s)
    #It prints each line starting from def main()

#3. Compare the next (n) command with the step (s) command.
    #The breakpoint runs the whole program, while single line stepping runs each line one by one.

#4. Watch, whatis and print (p)
    #It selects a section of the code and runs it. The code gave us the final answer of 500

#5. Done