class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        sum_grade = 0
        count_grade = 0
        if len(self.grades == 0):
            return 0
        else:
            for grades in self.grades:
                if len(grades) > 0:
                    for grade in grades:
                        sum_grade += grade
                        count_grade += 1
            return sum_grade // count_grade

    def rate_lecturer(self, lecturer, course, grade, student=None):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in student.courses_in_progress and 1 <= grade <= 10:
            lecturer.grade +=[grade]
        else:
            return None

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()

    def __str__(self):
        return f"Имя: {self.name} \n \
                 Фамилия: {self.surname} \n \
                 Средняя оценка за домашние задания: {self.average_grade} \n \
                 Курсы в процессе изучения: {self.courses_in_progress} \n \
                 Завершенные курсы: {self.finished_courses}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grade = grade

    def average_grade(self):
        sum_grade = 0
        count_grade = 0
        if len(self.grades == 0):
            return 0
        else:
            for grades in self.grades:
                if len(grades) > 0:
                    for grade in grades:
                        sum_grade += grade
                        count_grade += 1
            return sum_grade // count_grade

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()

    def __str__(self):
        return (f"Имя: {self.name} \n \
                  Фамилия: {self.surname} \n \
                  Средняя оценка за лекции: {self.average_grade}")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name} \n \
                 Фамилия: {self.surname}"

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return None

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy', '9.9')
cool_lecturer.courses_attached += ['Python']

reviewer = Reviewer('Some', 'Buddy')

print(best_student)
print(cool_lecturer)
print(reviewer)