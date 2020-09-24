inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
students = []
for line in inFile.readlines():
    temp = line.split()
    students.append('{} {} {}\n'.format(temp[0], temp[1], temp[3]))
students.sort()
outFile.writelines(students)
