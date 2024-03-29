
class SimpleGradebook(object ):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum (grades) / len (grades)

book = SimpleGradebook()
book.add_student('Isaac Newton' )
book.report_grade('Isaac Newton' , 90 )
print (book.average_grade('Isaac Newton' ))

class BySubjectGradebook(object ):
    def __init__(self):
        self._grades = {}
    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0 , 0
        for grades in by_subject.values():
            total += sum (grades)
            count += len (grades)
        return total / count

book = BySubjectGradebook()
book.add_student('Albert Einstein' )
book.report_grade('Albert Einstein' , 'Math' , 75 )
book.report_grade('Albert Einstein' , 'Math' , 65 )
book.report_grade('Albert Einstein' , 'Gym' , 90 )
book.report_grade('Albert Einstein' , 'Gym' , 95 )

print (book.average_grade('Albert Einstein' ))

class WeightedGradebook(BySubjectGradebook):
    # ...
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
       by_subject = self._grades[name]
       score_sum, score_count = 0 , 0
       for subject, scores in by_subject.items():
           subject_avg, total_weight = 0 , 0
           for score, weight in scores:
               continue
       return score_sum / score_count

#book.report_grade('Albert Einstein' , 'Math' , 80 , 0.10 )
import collections
Grade = collections.namedtuple('Grade' , ('score' , 'weight' ))

class Subject(object ):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0 , 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student(object ):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0 , 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Gradebook(object ):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

book = Gradebook()
albert = book.student('Albert Einstein' )
math = albert.subject('Math' )
math.report_grade(80 , 0.10 )
print (albert.average_grade())
