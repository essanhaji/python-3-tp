numbers = list(range(10))

iteratorNumbers = iter(numbers)

while True:
    try:
        val = next(iteratorNumbers)
        print(val)
    except:
        break
    # finally:
    # print("hello")