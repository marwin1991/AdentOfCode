FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


class Present:
    def __init__(self, index, shape):
        self.index = index
        self.shape = shape
        self.area = self.__get_area()

    def __get_area(self):
        count = 0
        for line in self.shape:
            line_area = line.count("#")
            count += line_area
        return count

    def __repr__(self):
        shape_str = "\n".join(self.shape)
        return f"Present(index={self.index}, area={self.area}, shape=\n{shape_str}\n)"


class Region:
    def __init__(self, x, y, presents_count_list):
        self.x = x
        self.y = y
        self.presents_count_list = presents_count_list
        self.total_area = x * y

    def __repr__(self):
        return f"Reg(x={self.x}, y={self.y}, presents_count_list={self.presents_count_list})"



def main():
    lines = read_file()

    regions = []
    presents = []

    shape_holder = []
    shape_holder_index = 0
    for line in lines:
        if "x" in line:
            p1, p2 = line.split(":")
            region_x_y = p1.strip().split("x")
            presents_count_list = []
            presents_count_list_tmp = p2.strip().split(" ")
            for pc in presents_count_list_tmp:
                presents_count_list.append(int(pc))
            regions.append(Region(int(region_x_y[0]), int(region_x_y[1]), presents_count_list))
        else:
            if line.count(":") == 1:
                shape_holder_index = int(line.split(":")[0].strip())
                continue
            elif line.strip() == "":
                presents.append(Present(shape_holder_index, shape_holder))
                shape_holder = []
                continue
            else:
                shape_holder.append(line.strip())

    good_regions = 0

    for region in regions:
        total_area = region.total_area
        for idx in range(len(region.presents_count_list)):
            number_of_presents = region.presents_count_list[idx]
            present = presents[idx]
            total_area -= present.area * number_of_presents

        if total_area >= 0:
            good_regions += 1


    print(f"good regions: {good_regions}")



    print(regions)

if __name__ == '__main__':
    main()