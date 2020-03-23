"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        pass

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


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
        pass


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
    # consider HLY similar to exit()

# Add the LDI instruction 
    # This instruction sets a specified register to a specified value

# Add the PRN instruction
    # Similar to adding LDI, but the handler is simpler
    # At this point, you can run the program and have it print 8 to console.