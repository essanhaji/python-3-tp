# echo"hello world" > file.txt  => create file.txt with contente hello world
# cat file.txt => read file.txt
# dir(object)

def first_half(a):
    return a[:len(a) // 2]


def last_half(a):
    return a[len(a) // 2:]


if __name__ == '__main__':
    assert first_half("abcde") == "ab", "the first half is failing"
    assert last_half("hello") == "llo", "the last half is failing"
