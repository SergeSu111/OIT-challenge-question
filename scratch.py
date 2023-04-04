def romanToInt(s: str) -> int:
    length = len(s)
    answer = 0
    roma = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,

    }
# If the first Roman numeral is smaller than the second Roman numeral, add a negative number, otherwise add a positive
# number.
    for i in range(length - 1):
        if roma[s[i + 1]] > roma[s[i]]:
            answer = answer - roma[s[i]]
        else:
            answer = answer + roma[s[i]]
    answer = answer + roma[s[length - 1]]
    return answer


def intToRoman(num: int) -> str:
    # Put all possible cases and correspondences between Arabic numerals and Roman numerals in two arrays
    # in descending order of Arabic numerals, which is the greedy choice of mind
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    index = 0
    res = ''
    # index is from 0 to 12, length is 13
    while index < 13:
        # we use the bigger option first
        while num >= nums[index]:
            res += romans[index]
            num -= nums[index]
        index += 1
    return res


# Example usage:
roman_numeral = 'XIV'
decimal_num = romanToInt(roman_numeral)
print(f"{roman_numeral} = {decimal_num}")


decimal_num = 20
roman_numeral = intToRoman(decimal_num)
print(f"{decimal_num} = {roman_numeral}")
# Output: 1984 = MCMLXXXIV

