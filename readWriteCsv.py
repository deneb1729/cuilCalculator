import csv 

cuilMultiplicators = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

def completeCuil(previusCuil, rest):

    if rest == 0:
        return previusCuil[0:2] + '-' + previusCuil[2:] + '-0'
    elif rest == 1:
        if previusCuil[0:2] == '20':
            return '23-' + previusCuil[2:] + '-9'
        if previusCuil[0:2] == '27':
            return '23-' + previusCuil[2:] + '-4'
        
    return previusCuil[0:2] + '-' + previusCuil[2:] + '-' + str(11 - rest)

with open('test.csv', newline='') as File:
    reader = csv.reader(File)

    newData = []

    for data in reader:
        if data[0] != 'dni':

            if len(data[0]) == 7 or len(data[0]) == 8:

                dni = '0' + data[0] if (len(data[0]) < 8) else data[0]
                previusCuil = '20' + dni if (data[1] == 'M') else '27' + dni

                acumulator = 0
                for element, digit in zip(cuilMultiplicators, previusCuil):
                    acumulator += element * int(digit)

                data[2] = completeCuil(previusCuil, acumulator % 11)

                newData.append(data)
            else:
                newData.append(data)

        else:
            newData.append(data)

    with open('result.csv', 'w') as writeFile:

        writer = csv.writer(writeFile, delimiter=',')
        writer.writerows(newData)


