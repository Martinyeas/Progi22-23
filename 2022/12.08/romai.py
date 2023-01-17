tallies = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

def RomanNumeralToDecimal(r):
    sum = 0
    for i in range(len(r)-1):
        left = r[i]
        right = r[i+1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[r[-1]]
    return sum
roman = input("Írj be római számokat: ")
RomanNumeralToDecimal(roman)
print(RomanNumeralToDecimal(roman))