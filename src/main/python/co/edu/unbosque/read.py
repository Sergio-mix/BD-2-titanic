import pandas as pd


def readExcelTitanic(url):
    try:
        list = []
        df = pd.read_excel(url)
        for i in range(len(df)):
            survived = df['survived'].values[i]
            name = df['name'].values[i]
            sex = df['sex'].values[i]
            age = df['age'].values[i]
            list.append(
                {
                    'survived': survived,
                    'name': name,
                    'sex': sex,
                    'age': age
                }
            )
        return list
    except Exception as e:
        print(e)
