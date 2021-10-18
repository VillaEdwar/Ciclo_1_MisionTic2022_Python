def empleados(url, codUn, codest):
    import pandas as pd
    try:
        df = pd.read_csv(url, sep=";")
    except:
        return 'Error con la url del archivo de datos'
    listrest = []

    if codest == 1:
        sumSal = 0
        sumBon = 0
        sumEva = 0
        for i in range(len(df.index)):
            if df["codUn"][i] == codUn:
                sumSal += df["Salario"][i]
                sumBon += df["Bonificacion"][i]
                sumEva += df["EvalDes"][i]
        listrest.append(sumSal)
        listrest.append(sumBon)
        listrest.append(sumEva)

    if codest == 2:
        sumSal = 0
        sumBon = 0
        sumEva = 0
        n = 0
        for i in range(len(df.index)):
            if df["codUn"][i] == codUn:
                sumSal += df["Salario"][i]
                sumBon += df["Bonificacion"][i]
                sumEva += df["EvalDes"][i]
                n += 1
        listrest.append(float(round(sumSal/n, 1)))
        listrest.append(float(round(sumBon/n, 1)))
        listrest.append(float(round(sumEva/n, 1)))

    if codest == 3:
        listtemp = []
        maysal = -1
        maybon = -1
        mayeva = -1
        codidSal = 0
        codidBon = 0
        codidEva = 0
        for i in range(len(df.index)):
            if df["codUn"][i] == codUn:
                if df["Salario"][i] > maysal:
                    maysal = df["Salario"][i]
                    codidSal = df["IdEmpl"][i]

                if df["Bonificacion"][i] > maybon:
                    maybon = df["Bonificacion"][i]
                    codidBon = df["IdEmpl"][i]

                if df["EvalDes"][i] > mayeva:
                    mayeva = df["EvalDes"][i]
                    codidEva = df["IdEmpl"][i]

        listrest.append(codidSal)
        listrest.append(codidBon)
        listrest.append(codidEva)

    return listrest
