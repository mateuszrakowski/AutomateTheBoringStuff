def main():
    spam = ["ELO", "toja"]
    result = comma(spam)
    print(result)


def comma(lista):
    text = ""
    if len(lista) > 1:
        for i in range(len(lista)):
            if i < len(lista) - 2:
                text += lista[i] + ", "
            else:
                text += lista[i] + " and " + lista[i+1]
                return text
    return text


if __name__ == "__main__":
    main()