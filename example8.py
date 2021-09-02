def skip_elements(elements):
    list = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            list.insert(index, element)
    # code goes here

    return list


print(
    skip_elements(["a", "b", "c", "d", "e", "f", "g"])
)  # Should be ['a', 'c', 'e', 'g']
print(
    skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"])
)  # Should be ['Orange', 'Strawberry', 'Peach']
