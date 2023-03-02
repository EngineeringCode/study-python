example_list = ["a", "b", "c"]

i = 0

while i < len(example_list):
    if i < 0:
        break
    print(example_list[i])
    i += 1
    continue
