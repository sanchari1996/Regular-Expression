#you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
import re
print sum([int(i) for i in re.findall('[0-9]+',open("regex_sum_286723.txt").read())])
