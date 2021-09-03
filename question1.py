filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = [names.replace(".hpp", ".h") for names in filenames]

print(newfilenames)
