def my_split(sentence, separator):
    items = []
    current_item = ""
    for char in sentence:
        if char == separator:
            items.append(current_item)
            current_item = ""
        else:
            current_item += char
    if current_item:  # Add the last item
        items.append(current_item)
    return items


def my_join(items, separator):
    return separator.join(items)


def main():
    sentence = input("Please enter sentence:")
    split_result = my_split(sentence, " ")
    print(",".join(split_result))

    for word in split_result:
        print(word)


if __name__ == "__main__":
    main()
