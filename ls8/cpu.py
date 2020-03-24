"""CPU functionality."""

import sys

#Opcodes = instructions
LDI = 0b10000010 # Set the value of a register to an integer.
PRN = 0b01000111 # Print numeric value stored in the given register.
HLT = 0b00000001 # Halt the CPU (and exit the emulator).

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8 #general purpose register (has 8 bits)
        self.ram = [0] * 256 #to hold 256 bytes of memory
        self.pc = 0 #program counter

    def ram_read(self, mar): 
        #should accept the address to read and 
        mdr = self.ram[mar] #MAR = contains ADDRESS that is being read or written to
        #return the value stored there
        return mdr #MDR = contains the DATA that was read or the data to write

    def ram_write(self, mar, value):
        #should accept a value to write, and address to write it to
        self.ram[mar] = value #can put mdr instead of value

    def load(self, program):
        """Load a program into memory."""

        address = 0

        try:
            with open(program) as p:
                for line in p:
                    # Ignore comments
                    comment_split = line.split("#")
                    # Strip out whitespace
                    num = comment_split[0].strip()
                    # Ignore blank lines
                    if num == '':
                        continue
                    opcode = int(num)
                    self.ram[address] = opcode
                    address += 1
        except FileNotFoundError:
            print("File not found")
            sys.exit(2)


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running: 
            opcode = self.ram[self.pc] #needs to read memory address that's stored in register
            operand_a = self.ram_read(self.pc + 1) 
            operand_b = self.ram_read(self.pc + 2)

            if opcode == LDI: # sets a specified register to a specified value
                self.reg[operand_a] = operand_b
                self.pc += 3 # skip down 3 to PRN

            elif opcode == PRN: # prints the numeric value stored in a register
                print(self.reg[operand_a])
                self.pc += 2 #skip down 2 to HLT

            elif opcode == HLT:
                running = False 

            else:
                print(f"Unknown instruction: {opcode}")
                sys.exit(1)


# Add list properties to the CPU class to hold 256 bytes of memory and general-purpose registers
    #Also add properties for any internal registers

#In CPU, add method ram_read() and ram_write() that access the RAM inside the CPU object
    #ram_read() should accept the address to read and return the value stored there
    #ram_write() should accept a value to write, and address to write it to

#Implement the core of the CPU's run() method
    # needs to read to memory address that's stored in register PC -> store that result in IR, the Instruction Register. This can just be a local variable in run()
    # some instructions requires up to the next bytes of data after the PC in memory
    # using ram_read(), read the bytes at pc + 1 and pc + 2 from RAM into variables operand_a and operand_b in case the instruction needs them
    # Depending on the value of the opcode, perform the actions needed for the instruction per the LS-8 spec. (if-elif)
    # the PC needs to be updated to point to the next instruction for the next iteration of the loop in run()

#Implement the HLT instruction handler to cpu.py
    # So that you can refer to it by name instead of by numeric value
    # in run() in your switch, exit the loop if a HLT instruction is encountered, regardless of whether or not there are more lines of code in the LS-8 program 
    # consider HLT similar to exit()
    # halt the CPU and exits the emulator

# Add the LDI instruction handler
    # This instruction sets a specified register to a specified value
    # load "immediate", store a value in a register, or "set this register to this value"

# Add the PRN instruction handler
    # Similar to adding LDI, but the handler is simpler
    # At this point, you can run the program and have it print 8 to console.
    # a pseudo-instruction that prints the numeric value stored in a register

