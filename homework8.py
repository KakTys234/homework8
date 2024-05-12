grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(grades)
print(students)
print('-------------------------------------------------------------------------------------------')

# Первый способ
# Самый простой

print('Первый вариант')
print('==============')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(grades)
print(students)
sred_ball = {'Aaron': (5 + 3 + 3 + 5 + 4) / 5, 'Bilbo': (2 + 2 + 2 + 3) / 4, 'Johnny': (4 + 5 + 5 + 2) / 4, 'Khendrik': (4 +  4 + 3) / 3,
             'Steve': (5 + 5 + 5 + 4 + 5) / 5}
print('Средний балл')
print(sred_ball)
print('-------------------------------------------------------------------------------------------')

# Второй способ
#  Этим способом можно добавлять оценки и менять число слогаемых

print('Второй вариант')
print('==============')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(grades)
print(students)
grades[0] = (5 + 3 + 3 + 5 + 4) / 5
grades[1] = (2 + 2 + 2 + 3) / 4
grades[2] = (4 + 5 + 5 + 2) / 4
grades[3] = (4 +  4 + 3) / 3
grades[4] = (5 + 5 + 5 + 4 + 5) / 5
sred_ball = {'Aaron': grades[0], 'Bilbo': grades[1], 'Johnny': grades[2], 'Khendrik': grades[3], 'Steve': grades[4]}
print('Средний балл')
print(sred_ball)
print('-------------------------------------------------------------------------------------------')

# Третий способ
#  Этим способом можно тоже добавлять оценки и менять число слогаемых

print('Третий вариант')
print('==============')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(grades)
print(students)
names_students = list(students)
print(names_students)
names_students[4] = 'Aaron'
names_students[1] = 'Bilbo'
names_students[0] = 'Johnny'
names_students[3] = 'Khendrik'
names_students[2] = 'Steve'
grades[0] = (5 + 3 + 3 + 5 + 4) / 5
grades[1] = (2 + 2 + 2 + 3) / 4
grades[2] = (4 + 5 + 5 + 2) / 4
grades[3] = (4 +  4 + 3) / 3
grades[4] = (5 + 5 + 5 + 4 + 5) / 5
sred_ball = {names_students[4]: grades[0], names_students[1]: grades[1], names_students[0]: grades[2],
             names_students[3]: grades[3], names_students[2]: grades[4]}
print('Средний балл')
print(sred_ball)
print('-------------------------------------------------------------------------------------------')

# Четвертый способ

print('Четвертый вариант')
print('=================')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
names_students = list(students)
print(names_students)
names_students[4] = 'Aaron'
names_students[1] = 'Bilbo'
names_students[0] = 'Johnny'
names_students[3] = 'Khendrik'
names_students[2] = 'Steve'
sred_ball = {names_students[4]: (grades[0][0] + grades[0][1] + grades[0][2] + grades[0][3] + grades[0][4]) / 5,
             names_students[1]: (grades[1][0] + grades[1][1] +grades[1][2] +grades[1][3]) / 4,
             names_students[0]: (grades[2][0] + grades[2][1] + grades[2][2] + grades[2][3]) / 4,
             names_students[3]: (grades[3][0] + grades[3][1] + grades[3][2]) / 3,
             names_students[2]: (grades[4][0] + grades[4][1] + grades[4][2] + grades[4][3] + grades[4][4]) / 5}
print('Средний балл')
print(sred_ball)
print('-------------------------------------------------------------------------------------------')

# Пятый способ

print('Пятый вариант')
print('=============')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
sred_ball = {'Aaron': (grades[0][0] + grades[0][1] + grades[0][2] + grades[0][3] + grades[0][4]) / 5,
             'Bilbo': (grades[1][0] + grades[1][1] +grades[1][2] +grades[1][3]) / 4,
             'Johnny': (grades[2][0] + grades[2][1] + grades[2][2] + grades[2][3]) / 4,
             'Khendrik': (grades[3][0] + grades[3][1] + grades[3][2]) / 3,
             'Steve': (grades[4][0] + grades[4][1] + grades[4][2] + grades[4][3] + grades[4][4]) / 5}
print('Средний балл')
print(sred_ball)
print('-------------------------------------------------------------------------------------------')

# Шестой способ

print('Шестой вариант')
print('==============')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(grades)
print(students)
names_students = list(students)
print(names_students)
names_students[4] = 'Aaron'
names_students[1] = 'Bilbo'
names_students[0] = 'Johnny'
names_students[3] = 'Khendrik'
names_students[2] = 'Steve'
sred_ball = {names_students[4]: (5 + 3 + 3 + 5 + 4) / 5, names_students[1]: (2 + 2 + 2 + 3) / 4, names_students[0]: (4 + 5 + 5 + 2) / 4,
             names_students[3]: (4 +  4 + 3) / 3, names_students[2]: (5 + 5 + 5 + 4 + 5) / 5}
print('Средний балл')
print(sred_ball)
print('-------------------------------------------------------------------------------------------')