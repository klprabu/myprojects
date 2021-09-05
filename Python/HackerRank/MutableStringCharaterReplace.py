#We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
#Let's try to understand this with an example.
#You are given an immutable string, and you want to make changes to it.


def mutate_string(string, position, character):
    new_str = ''
    for i in range(len(string)):
        tmp = string[i]
        if i == position:
            tmp = character

        new_str = new_str + tmp

    return new_str


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)