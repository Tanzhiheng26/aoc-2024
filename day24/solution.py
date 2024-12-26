def read_input(file):
    values = {}
    with open(file, 'r') as f:
        section1, section2 = f.read().split("\n\n")
        for line in section1.split("\n"):
            gate, val = line.split(": ")
            values[gate] = int(val)
        equations = section2.split("\n")
        return values, equations

def parse_eqn(operand1, operator, operand2, gate, values):
    if operator == "AND":
        values[gate] = values[operand1] & values[operand2]
    elif operator == "OR":
        values[gate] = values[operand1] | values[operand2]
    elif operator == "XOR":
        values[gate] = values[operand1] ^ values[operand2]

def part1(file):
    values, equations = read_input(file)    
    evaluated = set()

    while len(evaluated) < len(equations):
        for i, eqn in enumerate(equations):
            if i in evaluated:
                continue
            lhs, rhs = eqn.split(" -> ")
            operand1, operator, operand2 = lhs.split()
            if operand1 in values and operand2 in values:
                parse_eqn(operand1, operator, operand2, rhs, values)
                evaluated.add(i)
    
    result = 0
    for gate, bit in values.items():
        if gate[0] == 'z' and bit == 1:
            weight = int(gate[1:])
            result += 2**weight
    
    return result

print(part1("input.txt"))

def flip(lhs):
    operand1, operator, operand2 = lhs.split()
    return f"{operand2} {operator} {operand1}"

"""
Full adder boolean expression

For the SUM (S) bit:
SUM = (A ⊕ B) ⊕ Cin

For the CARRY-OUT (Cout) bit:
CARRY-OUT = A.B + (A ⊕ B).Cin
"""
def part2(file):
    equations = read_input(file)[1]
    output = {}
    input = {}

    for eqn in equations:
        lhs, rhs = eqn.split(" -> ")
        output[lhs] = rhs
        output[flip(lhs)] = rhs
        input[rhs] = [lhs, flip(lhs)]
    
    z0 = output["x00 XOR y00"] == "z00" # no carry in, carry out is just x00 AND y00
    z1 = output[f"{output['x01 XOR y01']} XOR {output['x00 AND y00']}"] == "z01"     
    for i in range(2, 45):
        x_xor_y = output[f"x{i:02d} XOR y{i:02d}"] # x ⊕ y
        # carry in of current bit is carry out of previous bit
        cin1 = output[f'x{(i - 1):02d} AND y{(i - 1):02d}'] # prev x.y
        cin2 = output[input[f'z{(i - 1):02d}'][0].replace('XOR', 'AND')] # prev (x ⊕ y).Cin
        carry_in = output[f"{cin1} OR {cin2}"]
        passed = f"{x_xor_y} XOR {carry_in}" in input[f"z{i:02d}"] 
        if not passed:
            print(i, x_xor_y, carry_in) # Correct the input based on whatever is printed here
            break
    # final carry out
    z45 = f"{output[f'x44 AND y44']} OR {output[input['z44'][0].replace('XOR', 'AND')]}" in input["z45"] 
    print(z0, z1, z45)

"""
gvm OR smt -> z10
mbv XOR hks -> ggn

x17 AND y17 -> ndw
x17 XOR y17 -> jcb

rmn XOR whq -> grm
rmn AND whq -> z32

x39 AND y39 -> z39
pqv XOR bnv -> twr

ggn,grm,jcb,ndw,twr,z10,z32,z39
"""
part2("corrected_input.txt")