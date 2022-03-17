"""
File: boggle.py
Name: Yu-Ju Fang
----------------------------------------
Find all the words that exist in the boggle game
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Go through all the permutations of words by using recurssion in the boggle and check whether it exists, if it truly
	exists then we printed out
	"""
	start = time.time()

	find = True
	lst = []
	num = 0
	for i in range(1, 5):
		row = input(f'{i} row of letters: ')
		row = row.split()
		if check(row) is False: # check if the inputs are input correctly
			find = False
			break
		lst.append(row)

	if find is True:  # we will find all the permutations only when all the inputs are input correctly
		for x in range(4):
			for y in range(4):
				num += find_word(x, y, lst) # calculate the total numbers of existed- word we find

		print(f'There are {num} words in total.')

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(x, y, lst):
	"""
	:param x:  int, the x coordinate of boggle
	:param y:  int, the y coordinate of boggle
	:param lst: list, boggle
	:return: int, the number of existed-word starts with lst[x][y]
	"""

	dicts = read_dictionary()
	ans_lst = []

	neighbor_explore([], x, y, lst, [], dicts, ans_lst)

	return len(ans_lst)


def neighbor_explore(current_lst, x, y, lst, record_lst, dicts, ans_lst):
	if len(current_lst) > 16:  # Base Case
		return

	else:

		current_lst.append(lst[x][y])  # Choose
		record_lst.append((x,y))  # record the coordinates that has been through

		word = assemble(current_lst)
		if has_prefix(word, dicts):
			if len(word) >= 4:
				if word not in ans_lst:  # check whether the word is already in the ans_lst
					if word in dicts:
						ans_lst.append(word)
						print(f'Found: "{word}"')

			# Go through the neighbors in different directions
			if 4 > x - 1 >= 0 and 4 > y - 1 >= 0:
				if (x-1, y-1) not in record_lst:
					neighbor_explore(current_lst, x - 1, y - 1, lst, record_lst, dicts, ans_lst)  # Explore
					record_lst.pop()
					current_lst.pop()  # Un-choose

			if 4 > x - 1 >= 0 and 4 > y >= 0:
				if (x - 1, y) not in record_lst:
					neighbor_explore(current_lst, x - 1, y, lst, record_lst, dicts, ans_lst)  # Explore
					record_lst.pop()
					current_lst.pop()  # Un-choose

			if 4 > x - 1 >= 0 and 4 > y + 1 >= 0:
				if (x - 1, y + 1) not in record_lst:
					neighbor_explore(current_lst, x - 1, y + 1, lst, record_lst, dicts, ans_lst)  # Explore
					record_lst.pop()
					current_lst.pop()  # Un-choose

			if 4 > x >= 0 and 4 > y - 1 >= 0:
				if (x, y - 1) not in record_lst:
					neighbor_explore(current_lst, x, y - 1, lst,record_lst, dicts, ans_lst)  # Explore
					record_lst.pop()
					current_lst.pop()  # Un-choose

			if 4 > x >= 0 and 4 > y + 1 >= 0:
				if (x, y + 1) not in record_lst:
					neighbor_explore(current_lst, x, y + 1, lst, record_lst, dicts, ans_lst)  # Explore
					record_lst.pop()
					current_lst.pop()  # Un-choose

			if 4 > x + 1 >= 0 and 4 > y - 1 >= 0:
				if (x + 1, y - 1) not in record_lst:
					neighbor_explore(current_lst, x + 1, y - 1, lst, record_lst, dicts, ans_lst)  # Explore
					record_lst.pop()
					current_lst.pop()  # Un-choose

			if 4 > x + 1 >= 0 and 4 > y >= 0:
				if (x + 1, y) not in record_lst:
					neighbor_explore(current_lst, x + 1, y, lst, record_lst, dicts, ans_lst)  # Explore
					record_lst.pop()
					current_lst.pop()  # Un-choose

			if 4 > x + 1 >= 0 and 4 > y + 1 >= 0:
				if (x + 1, y + 1) not in record_lst:
					neighbor_explore(current_lst, x + 1, y + 1, lst, record_lst, dicts, ans_lst)  # Explore
					record_lst.pop()
					current_lst.pop() # Un-choose

			return
		else:
			return


def check(row):
	"""
	:param row: list, list of inputs of a row
	:return: bool, the result of whether inputs are input correctly
	"""
	for ch in row:
		if len(ch) != 1:
			print('Illegal input')
			return False
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dicts = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split()
			dicts.append(word[0])

	return dicts


def has_prefix(sub_s, dicts):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dicts:
		if word.startswith(sub_s):
			return True
	return False


def disassemble(s):
    """
    :param s: string
    :return: list of string
    """
    str_lst = []
    for chr in s:
        str_lst.append(chr)
    return str_lst


def assemble(current_lst):
    """
    :param current_lst: list of index for the string list
    :return: str, assemble list as string
    """

    string = ''
    for alphabet in current_lst:
        string += alphabet

    return string


if __name__ == '__main__':
	main()
