

#program- Naive method to find a pair in a list with the given sum


def findPair(nums, target):
    # consider each element except the last
    for i in range(len(nums) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(nums)):

            # if the desired sum is found, print it
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return

    # No pair with the given sum exists in the list
    print('Pair not found')


if __name__ == '__main__':
    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    findPair(nums, target)

#Program -to calculate Roman values
class roman:
    def intToRoman(num):
    # Storing roman values of digits from 0-9
    # when placed at different places
       m = ["", "M", "MM", "MMM"]
       c = ["", "C", "CC", "CCC", "CD", "D",
           "DC", "DCC", "DCCC", "CM "]
       x = ["", "X", "XX", "XXX", "XL", "L",
            "LX", "LXX", "LXXX", "XC"]
       i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    # Converting to roman
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]

    ans = (thousands + hundreds +
           tens + ones)
           return ans

r=roman()
if __name__ == "__main__":
    number = 3549
    print(r.intToRoman(number))