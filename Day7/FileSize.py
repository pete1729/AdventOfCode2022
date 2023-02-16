class Directory(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.file_names = []
        self.file_sizes = []
        self.directory_size = 0

    def add_file(self, file_name, file_size):
        self.file_names.append(file_name)
        self.file_sizes.append(file_size)

    def add_child(self, obj):
        self.children.append(obj)
        obj.parent = self

    def set_directory_sizes(self):
        file_size_sum = 0
        file_size_sum += sum(self.file_sizes)
        for child in self.children:
            file_size_sum += child.set_directory_sizes()
        self.directory_size = file_size_sum
        print("Directory name:", self.name)
        print("Directory size:", self.directory_size)
        return self.directory_size

    def get_cond_file_sizes(self):
        file_size_sum = 0
        if self.directory_size < 100000:
            file_size_sum += self.directory_size
        for child in self.children:
            file_size_sum += child.get_cond_file_sizes()
        return file_size_sum
    
    def print_all_directories(self):
        print("Directory name:", self.name)
        print("File sizes:", sum(self.file_sizes))
        print()
        for child in self.children:
            child.print_all_directories()

    def find_smallest_directory(self, current_min, threshold):
        if self.directory_size > threshold and self.directory_size < current_min:
            current_min = self.directory_size
        for child in self.children:
            current_min = child.find_smallest_directory(current_min, threshold)
        return current_min



root_dir = Directory("/")
current_dir = root_dir

with open('/home/peter/Code/AdventOfCode2022/Day7/input', 'r') as reader:
    lines = reader.readlines()
    for i in range(1,len(lines)):
    #for i in range(1,20):
        print()
        print("Next line", lines[i][:-1])

        if lines[i][0] == "$":
            if lines[i][2:4] == "ls":
                pass
            elif "cd" in lines[i]:

                target = lines[i][5:-1]
                print("Target directory", target)
                if target == "..":
                    current_dir = current_dir.parent
                else:
                    for child in current_dir.children:

                        if child.name == target:
                            current_dir = child
                            print("Changed directory to", current_dir.name)
        elif lines[i][0:3] == "dir":
            direct_name = lines[i][4:-1]
            directory_already_exists = False
            for child in current_dir.children:
                if child.name == direct_name:
                    directory_already_exists = True
            if directory_already_exists == False:
                current_dir.add_child(Directory(direct_name))
                print("Created new directory", direct_name)

        else:
            next_line = lines[i][:-1].split(" ")
            print("Next line:", next_line)
            current_dir.add_file(next_line[1], int(next_line[0]))
            print("Current Directory:", current_dir.name)
            print("Added file to directory")

root_dir.set_directory_sizes()
print(root_dir.get_cond_file_sizes())

unused_space = 70000000 - root_dir.directory_size
print("Unused Space", unused_space)
minimum_space_to_delete = 30000000 - unused_space
print("Minimum space to delete:", minimum_space_to_delete)
#print(root_dir.print_all_directories())

smallest_directory_size = 70000000
print(root_dir.find_smallest_directory(smallest_directory_size, minimum_space_to_delete))