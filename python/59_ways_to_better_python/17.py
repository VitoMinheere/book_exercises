"""Be defensive when iterating over arguments"""

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)

class ReadVisits(object ):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open (self.data_path) as f:
            for line in f:
                yield int (line)

# visits = ReadVisits(path)
# percentages = normalize(visits)
# print (percentages)

def normalize_defensive(numbers):
    if iter (numbers) is iter (numbers):  # An iterator -- bad!
        raise TypeError('Must supply a container' )
    total = sum (numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

normalize_defensive(visits)
it = iter(visits)
normalize_defensive(it)
