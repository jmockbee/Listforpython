animals = ["lion", "zebra", "dolphin", "monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("total characters:{}, averge length: {}".format(chars, chars / len(animals)))
