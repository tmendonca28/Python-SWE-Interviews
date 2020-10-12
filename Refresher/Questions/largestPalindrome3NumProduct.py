# Write a Python program to find the largest palindrome made from the product of two 3-digit numbers.

def palindrome3Num():
    minVal = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            sumij = i * j
            if sumij > minVal:
                s = str(sumij)
                if s == s[::-1]:
                    minVal = sumij
    print(minVal)

if __name__ == "__main__":
    palindrome3Num()