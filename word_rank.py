#	DAVID WELLS

#	WORD RANKING
#	Prompts user to enter a word and prints out the number.
#	Number corresponds to where the word falls on an alphabetically sorted list of
#	all permutations of these letters.

#	Data structure used:  The Python Counter() class, from the collections data types.
#	A Counter is a dict subclass for counting hashable objects. 
#	It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
#	Counts are allowed to be any integer value including zero or negative counts. 

#	Basic error checking:  checked is the string entered is greater than 25 characters, if so asks user to try again.
#	All strings are converted to upper-case letters

from collections import Counter
import resource
import time
start_time = time.time()


def wordrank(myWord):

	rank = 1
	permutations = 1

	stringLength = len(myWord)
	myCounter = Counter()

	for i in range(stringLength):
		permutationContainer = myWord[((stringLength - 1) - i)]
		myCounter[permutationContainer] += 1

		for j in myCounter:

			if (j < permutationContainer):
				rank += (permutations * myCounter[j] // myCounter[permutationContainer])

		permutations = ( (permutations * (i +1)) // myCounter[permutationContainer])
	return rank


continueProgram = True
while(continueProgram):
	input_string = input("Enter a string of characters (25 max): ")
	input_string =input_string.upper()

	if (len(input_string) > 25):
		print('String greater than 25 characters, please try again')

	else:
		print(input_string, " = ", wordrank(input_string) )
		continueProgram = False


#	Check execution time of program - rough estimate - uncomment print statement to view time
#print("--- %s seconds ---", time.time() - start_time)

#	Check memory usage  - uncomment print statement to view memory print out
memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
#print('Memory usage: (in bytes) ', memory_usage)
