from collections import defaultdict

names = ['Socrates' , 'Archimedes' , 'Plato' , 'Aristotle' ]
names.sort(key= lambda x: len (x))
print (names)

def log_missing():
   print ('Key added' )
   return 0

current = {'green' : 12 , 'blue' : 3 }
increments = [
    ('red' , 5 ),
    ('blue' , 17 ),
    ('orange' , 9 ),
]
result = defaultdict(log_missing, current)
print ('Before:' , dict (result))
for key, amount in increments:
    result[key] += amount
print ('After: ' , dict (result))


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2
