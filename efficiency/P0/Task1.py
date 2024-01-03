"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
telephones = {}
for i in calls:
    telephones[i[0]] = 1
    telephones[i[1]] = 1

for i in texts:
    telephones[i[0]] = 1
    telephones[i[1]] = 1
    
print(f"There are {len(telephones)} different telephone numbers in the records.")
'''
Output:
There are 570 different telephone numbers in the records.
'''
'''
The algorithm is O(n) because it runs once for each row in calls and texts.
CPU times: user 3 µs, sys: 1e+03 ns, total: 4 µs
Wall time: 7.63 µs
'''