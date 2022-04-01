import read
import statistics as stat

if '__main__' == __name__:
    print('')

datos1 = read.readExcelTitanic(
    url='C:/Users/alejo/IdeaProjects/bd-2 titanic/src/resource/titanic1.xlsx',
)

datos2 = read.readExcelTitanic(
    url='C:/Users/alejo/IdeaProjects/bd-2 titanic/src/resource/titanic2.xlsx',
)

datos3 = read.readExcelTitanic(
    url='C:/Users/alejo/IdeaProjects/bd-2 titanic/src/resource/titanic3.xlsx',
)


def imprimirDatos(datos):
    for i in range(len(datos)):
        print('{')
        print('   survived:', datos[i]['survived'])
        print('   name:', datos[i]['name'])
        print('   sex:', datos[i]['sex'])
        print('   age:', datos[i]['age'])
        print('}')


def evaluarDatos(datos):
    try:
        listnull = []
        listSex = []
        for dato in datos:
            sex = str(dato['sex'])
            if sex == 'nan':
                listnull.append(dato)
            else:
                listSex.append(sex)

        moda = stat.mode(listSex)

        if len(listnull) != 0:
            for i in listnull:
                i['sex'] = moda

        print('--------------------------------------------')
        imprimirDatos(listnull)
        print('Numero de datos modificados:', len(listnull))
        print('Numero de datos totales:', len(datos))
        print('La moda es =', moda)
        print('--------------------------------------------')
    except Exception as ex:
        print(ex)


# Caso normal
evaluarDatos(datos1)

# Caso faltan algunos
evaluarDatos(datos2)

# Caso falta uno
evaluarDatos(datos3)
