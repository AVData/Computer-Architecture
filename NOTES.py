import sys

# memory = [0] * 256

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3  # if we want to save a value in register we say R1, 37
              # this says we save the value 37 in register 1. register[1] = 37
PRINT_REG = 4 # PRINT_REG R1 we run the code print(register[1])


# who to store the instructions
memory = [
    PRINT_BEEJ,
    SAVE_REG,   # SAVE_REG
    1,          # REGISTER 1
    37,         # 37
    PRINT_REG,  # PRINT_REG, R1
    1,
    HALT
]

# new concept, the registers
# this CPU has 8 variables, in low level languages
# variables are fewer, in high level languages
# you can have many languages.
# registers are fixed bedause they are made of hardware.
# general purpose register
register = [0] * 8

# adding the program counter (pc) which is
# the index of the running instruction
# pc is called a special purpose register:
pc = 0
running = True

while running:
    ir = memory[pc]  # instruction register which
                     # is the instruction that came out of
                     # memory at the pc
    if ir == PRINT_BEEJ:
        print('Beej')
        pc += 1
    elif ir == SAVE_REG:
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        register[reg_num] = value
        pc += 3
    elif ir == PRINT_REG:
        reg_num = memory[pc + 1]
        print(register[reg_num])
        pc += 2
    elif ir == HALT:
        running = False
        pc += 1
    else:
        print(f'Unknown instruction {ir} at address {pc}')
        sys.exit(1)
