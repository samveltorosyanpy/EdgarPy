def funkcia1(text):
    data = {}
    words = text.split()

    data['worlds_count'] = len(words)
    data['char_count'] = len(text.replace(' ', ''))
    data["new_text"] = text.lower()

    return data


# print(funkcia1("Hello World"))


def funkcia2(text):
    data = {}
    worlds_count = 1

    for t in text:
        if t == ' ':
            worlds_count += 1

    data['worlds_count'] = worlds_count

    char_count = 0

    for t in text:
        if t == " ":
            continue
        char_count += 1

    data['char_count'] = char_count

    data["new_text"] = text.lower()

    return data


# print(funkcia2("Hello World"))


lists = [5, 345, 56, 34, 67, 2]

for i in range(0, len(lists)):
    max_num_ind = i

    for x in range(i+1, len(lists)):
        if lists[i] > lists[x]:
            man_num_ind = x


    lists[i], lists[max_num_ind] = lists[max_num_ind], lists[i]

print(lists)

