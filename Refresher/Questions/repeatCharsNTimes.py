from itertools import cycle

def repeatStringNumTimes(n):
    text = "abc"
    result = []

    for i, c in enumerate(cycle(list(text))):
        if i > n-1:
            break
        result.append(c)

    print("".join(result))

if __name__=="__main__":
    repeatStringNumTimes(5)