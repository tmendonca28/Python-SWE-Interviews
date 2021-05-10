from typing import List


def MathOp():
    classic_division = 3/2
    floor_division = 3//2
    modulus = 3 % 2
    power = 3**2
    return [classic_division, floor_division, modulus, power]


[classic_division, floor_division, modulus, power] = MathOp()
print(classic_division)
print(floor_division)
print(modulus)
print(power)


def checkParity(n: int) -> int:
    result = -1
    if n % 2 == 0:
        result = 0
    else:
        result = 1
    return result


print(checkParity(4))


def inRange(x: int, y: int) -> bool:
    return (x < 1/3 < y)


print(inRange(2, 3))


def getStr(s: str) -> str:
    return ''.join(map(lambda x: x*3, s))


print(getStr('abc'))


# NB: we can also use s.find(substr)
def findOccurence(s: str) -> List[int]:
    occ_b = s.index("b")
    occ_ccc = s.index("ccc")
    return [occ_b, occ_ccc]


print(findOccurence('aaabbbccc'))


def changeCase(s: str) -> List[str]:
    return [s.upper(), s.lower()]


print(changeCase('AAA bbb CCC'))
