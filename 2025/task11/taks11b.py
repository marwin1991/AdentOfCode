FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

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

    total_paths = 0
    dac_fft_paths = 0
    steps = 0

    def dfs(node, visited_dac, visited_fft):
        nonlocal total_paths, dac_fft_paths, steps

        steps += 1
        if steps % 100000 == 0:
            print("Steps:", steps, "Paths so far:", total_paths, "dac+fft:", dac_fft_paths)

        if node == "dac":
            visited_dac = True
        if node == "fft":
            visited_fft = True

        # Finish
        if node == "out":
            total_paths += 1
            if visited_dac and visited_fft:
                dac_fft_paths += 1
            return

        for nxt in graph.get(node, []):
            dfs(nxt, visited_dac, visited_fft)

    dfs("svr", False, False)

    print("svr to out:", total_paths)
    print("dac and fft:", dac_fft_paths)

if __name__ == '__main__':
    main()
