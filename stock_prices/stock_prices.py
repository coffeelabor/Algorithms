#!/usr/bin/python

import argparse


def find_max_profit(prices):  # that receives as input a list of stock prices
    smallest_num = {}
    largest_num = []
    for i in range(0, len(prices)):
        smallest_num.update({i: prices[i]})
    for k, v in smallest_num.items():
        print(f'keys values {k, v}')
        for j in range(0, len(prices)):
            if j > k:
                print(f'j is greater than k here: {j, k, v}')
                temp = prices[j] - v
                largest_num.append(temp)
            # elif j > k:
            #     temp = prices[j]-v
            #     largest_num.append(0)
            # if j > k and prices[j] > v:
            #     print(f'j is greater than k here: {j, k, v}')
            #     temp = prices[j] - v
            #     largest_num.append(temp)
            # elif j > k:
            #     temp = prices[j]-v
            #     largest_num.append(0)
        # for j in range(0, len(prices)):
        #     if j > smallest_num.keys():
        #         print('in the j')

    print(f'smallest number: {smallest_num}')
    print(f'largest number pre sort: {largest_num}')
    largest_num.sort()
    print(f'largest number array: {largest_num}')
    # print(f'largest number last: {largest_num[-1]}')
    answer = largest_num[-1]
    print(f'answer {answer}')
    return answer


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))


'''
### understand

- Im going to need to find the smallest number
- Im going to need to find the larges number
- Im going to need to compare the difference between the two
- the smallest number has to be BEFORE the largest number

- I need to loop through the array and find the smallest number that occurs before the largest number

### planning

first I need variable to store the smallest number and an index of where the smallest number occured

Maybe it would be better to sort the numbers from smallest to largest and keep track of their indexes
Then I could compare against numbers that are greater than the index
  -I would need a variable for a dictionary sorted numbers from smallest to largest and to keep track of their index.
  -Im going to need to loop through the dictionary and compare high prices that occure after the key (index of smallest occurenc)
  -I think I can just return the largest number after the comparison and that should pass the test
  - I need a way to loop through the original array again on only compare numbers that have a higher index then the key of the object
    -If i do a j loop I can nest an if statement that compares the index of the array to the key of my dict


'''

'''
first attempt:

print(f'prices {prices}')
    for i in range(0, len(prices)-1):
        current_index = i
        smallest_num = current_index
        largest_num = current_index
        stock_pivot = i
        for j in range(current_index+1, len(prices)):
            if prices[j] < prices[smallest_num]:
                smallest_num = j
            elif prices[j] > prices[largest_num]:
                largest_num = j
        print(f'smallest number: {prices[smallest_num]}')
        print(f'largest number: {prices[largest_num]}')

        low_num = prices[current_index]
        # high_num = prices[current_index]
        prices[current_index] = prices[smallest_num]
        # prices[current_index] = prices[largest_num]
        prices[smallest_num] = low_num
        # prices[largest_num] = high_num

        print(f'low number: {low_num}')
        # print(f'high number: {high_num}')
    # should return the maximum profit that can be made from a single buy and sell

    # You must buy first before selling; no shorting is allowed here
'''
