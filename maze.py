class Maze():
    def __init__(self, filename):
        self.filename = filename
        self.contents = self.open_file()
        self.start = self.find_start()
        self.end = self.find_end()
        self.height = len(self.contents)
        self.withd = len(self.contents[0])
        self.collection = list()

    def find_start(self):
        for y in range(len(self.contents)):
            for x in range(len(self.contents[0])):
                if self.contents[y][x]== "A":
                    return (x, y)

    def find_end(self):
        for y in range(len(self.contents)):
            for x in range(len(self.contents[0])):
                if self.contents[y][x]== "B":
                    return (x, y)
    
    def valid(self, x, y):
        return (
            0 <= x < self.withd
            and 0 <= y < self.height
            and (x, y) not in self.collection
            and self.contents[y][x] != "#"
        )


    def open_file(self):
        with open(self.filename, "r") as file:
            file_content = file.read()
            return file_content.split("\n")

    def solve(self):
        stack = [self.start]
        visited = set()

        while stack:
            x, y = stack.pop()
            self.collection.append((x, y))
            visited.add((x, y))

            if (x, y) == self.end:
                break

            if self.valid(x - 1, y) and (x - 1, y) not in visited:
                stack.append((x - 1, y))
            if self.valid(x, y - 1) and (x, y - 1) not in visited:
                stack.append((x, y - 1))
            if self.valid(x + 1, y) and (x + 1, y) not in visited:
                stack.append((x + 1, y))
            if self.valid(x, y + 1) and (x, y + 1) not in visited:
                stack.append((x, y + 1))

        positions = list(self.collection)
        if positions[-1] != self.end:
            print("No solution found.")
            return []

        return positions
    def print(self):
        positions = self.solve()
        for x, y in positions:
            a = list(self.contents[y])
            if a[x] == "B":
                continue
            a[x] = "*"
            a = "".join(a)
            self.contents[y] = a
        for i in self.contents:
            print(i)

if __name__ == "__main__":
    a = Maze("a.txt")
    a.print()
            