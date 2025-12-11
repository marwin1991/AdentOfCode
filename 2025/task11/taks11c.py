FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

def find_paths(graph, start, end):
    count = 0
    stack = [(start, [])]

    while stack:
        node, path = stack.pop()

        if node == end:
            count += 1
            continue

        for nxt in graph.get(node, []):
            stack.append((nxt, path + [node]))

    return count

def main():
    lines = read_file()

    graph = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        name, rest = line.split(":")
        name = name.strip()
        outs = rest.strip().split()
        graph[name] = outs

    total_paths = find_paths(graph, "fft", "dac") # 3952
    print(f"{total_paths}")
    # svr -> fft # 3952
    # fft -> dac #

if __name__ == '__main__':
    main()
