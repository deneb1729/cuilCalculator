import csv
import argparse
import os

cuilMultiplicators = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

def completeCuil(previusCuil, rest):

    if rest == 0:
        return previusCuil[0:2] + previusCuil[2:] + '0'
    elif rest == 1:
        if previusCuil[0:2] == '20':
            return '23' + previusCuil[2:] + '9'
        if previusCuil[0:2] == '27':
            return '23' + previusCuil[2:] + '4'
        
    return str(previusCuil[0:2]) + str(previusCuil[2:]) + str(11 - rest)

def cuilFormat(cuil, typeCuil):
    if typeCuil == 'sin':
        return cuil
    if typeCuil == 'con':
        return cuil[:2] + '-' + cuil[2:10] + '-' + cuil[10:]

def loteCuils(parameters):

    fileCsv = parameters.file
    formatCuil = args.format

    with open(fileCsv, newline='') as File:
        reader = csv.reader(File)

        newData = []

        for data in reader:
            if data[0].upper() != 'DNI':

                if len(data[0]) == 7 or len(data[0]) == 8:

                    dni = '0' + data[0] if (len(data[0]) < 8) else data[0]
                    previusCuil = '20' + dni if (data[1] == 'M') else '27' + dni

                    acumulator = 0
                    for element, digit in zip(cuilMultiplicators, previusCuil):
                        acumulator += element * int(digit)

                    data[2] = cuilFormat(completeCuil(previusCuil, acumulator % 11), formatCuil)

                    newData.append(data)
                else:
                    newData.append(data)

            else:
                newData.append(data)

        with open('result.csv', 'w') as writeFile:

            writer = csv.writer(writeFile, delimiter=',')
            writer.writerows(newData)
            print('Success!!!')

# Getting a cuil with dni and sex give.
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dni", help="número de documento (debe tener mínimo 7 dígitos)", type=int)
parser.add_argument("-s", "--sex", help="F: femenino; M: masculino", type=str, choices=['F','M'])
parser.add_argument("-f", "--file", help="ruta absoluta del archivo .csv con los datos", type=str)
parser.add_argument("-F", "--format", help="formato que debera tener el cuil/cuit, ['con','sin'] guiones", type=str, choices=['con','sin'], default='sin')

args = parser.parse_args()

if args.file and os.path.isfile(args.file):
    loteCuils(args)