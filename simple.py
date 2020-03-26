#using simple base 10

import sys


#op codes are name of operations


PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4 #Save a value to a register
PRINT_REGISTER = 5 #Print value from register
ADD = 6 #regA += regB (like ls8)
PUSH = 7
POP = 8
CALL = 9
RET = 10

memory = [0] *256

#register are in hardware, extremely fast but small. Can only hold one word(base unit of data measurement) 64 bit -> each register will hold a 64 bit architecture
register = [0] * 8

#program counter -> what instruction to run
pc = 0

SP = 7 #means it points to register 7 (this is the stack pointer)
#flag
running = True

def load_memory(filename):
    address = 0
    try:
        with open(filename) as f:
            for line in f:
​
                # Ignore comments
                comment_split = line.split("#")
​
                # Strip out whitespace
                num = comment_split[0].strip()
​
                # Ignore blank lines
                if num == '':
                    continue
​
                val = int(num)
                memory[address] = val
                address += 1
​
    except FileNotFoundError:
        print("File not found")
        sys.exit(2)
​
​
if len(sys.argv) != 2:
    print("usage: simple.py filename")
    sys.exit(1)
​
filename = sys.argv[1]
load_memory(filename)
while running:
    print(memory)
    print(register)
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("BEEJ!")
    
    elif command == HALT:
        running = False

    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2 #by incrementing it by 2, we skip the print beej after the 1

    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3 #opcode, number and register

    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2 
    
    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3 

    elif command == PUSH:
        reg = memory[pc+1]
        value = register[reg]
        #Decrement the stack pointer
        register[SP] -= 1 #= (Register[SP]-1 % (len(memory)))
        #Copy the value  in given register tot he address pointed to by stack pointer
        memory[register[SP]] = value
        pc += 2 #because one argument

    elif command == POP:
        reg = memory[pc+1]
        value = memory[register[SP]] #calls memory and gets the F5 value
        #Copy the value
        register[reg] = value
        #increment the stack pointer
        register[SP] += 1
        pc += 2

    elif command == CALL:
        # The address of the instruction directly after CALL is pushed onto the stack.
        # This allows us to return to where we left off when the subroutine finishes executing.
        register[SP] -= 1
        memory[register[SP]] = pc + 2
​
        # The PC is set to the address stored in the given register.
        # We jump to that location in RAM and execute the first instruction in the subroutine.
        # The PC can move forward or backwards from its current location.
        reg = memory[pc + 1]
        pc = register[reg]
​
    elif command == RET:
        # Return from subroutine.
        # Pop the value from the top of the stack and store it in the PC.
        pc = memory[register[SP]]
        register[SP] += 1


    else:
        print(f"Unknown instruction: {command}")
        sys.exit(1)

    pc += 1