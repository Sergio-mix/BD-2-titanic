import read
import re

if '__main__' == __name__:
    print('')

datos = read.readExcelTitanic(
    url='C:/Users/alejo/IdeaProjects/bd-2 titanic/src/resource/titanic.xlsx',
)


def imprimirDatos(datos):
    for i in range(len(datos)):
        print(datos[i])


imprimirDatos(datos)
