FILE_PATH = "input.txt"

from ortools.sat.python import cp_model

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

def parse_line(line):
    diag_part, rest = line.split("]", 1)
    i = 0
    buttons = []
    while True:
        start = rest.find("(", i)
        if start == -1:
            break
        end = rest.find(")", start)
        group = rest[start+1:end]
        if group.strip():
            buttons.append([int(x) for x in group.split(",")])
        i = end + 1
    brace_start = rest.find("{")
    brace_end = rest.find("}", brace_start)
    req = [int(x) for x in rest[brace_start+1:brace_end].split(",")]
    return req, buttons

def solve_machine(lights, buttons):
    len_ligths = len(lights)
    len_buttons = len(buttons)

    model = cp_model.CpModel()

    x = []
    min_domena = 0
    max_domena = sum(lights)
    for x_indeks in range(len_buttons):
        x.append(model.NewIntVar(min_domena, max_domena, "x" + str(x_indeks)))

    for i in range(len_ligths):
        wspl = []
        for j in range(len_buttons):
            if i in buttons[j]:
                wspl.append(x[j])
        rownanie = sum(wspl) == lights[i]
        model.Add(rownanie)

    model.Minimize(sum(x))
    solver = cp_model.CpSolver()
    solver.Solve(model)

    return solver.ObjectiveValue()

def main():
    lines = [l.strip() for l in read_file() if l.strip()]
    total = 0
    for line in lines:
        req, buttons = parse_line(line)
        total += solve_machine(req, buttons)
    print(int(total))

    # wynik 1 -- 14677

if __name__ == '__main__':
    main()
