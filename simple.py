#using simple base 10

import sys


#op codes are name of operations


PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4 #Save a value to a register
PRINT_REGISTER = 5 #Print value from register
ADD = 6 #regA += regB (like ls8)


memory = [
  PRINT_BEEJ,
  SAVE,
  65,
  2,
  SAVE,
  20,
  3,
  ADD,
  2,
  3,
  PRINT_REGISTER,
  2,
  HALT

]

#register are in hardware, extremely fast but small. Can only hold one word(base unit of data measurement) 64 bit -> each register will hold a 64 bit architecture
register = [0] * 8

#program counter -> what instruction to run
pc = 0

#flag
running = True

while running:
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

    else:
        print(f"Unknown instruction: {command}")
        sys.exit(1)

    pc += 1