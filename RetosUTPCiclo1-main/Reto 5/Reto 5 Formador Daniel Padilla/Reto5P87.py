def contaminantes(url, codAnio, codest):
    import pandas as pd
    try:
        df = pd.read_csv(url, sep=";")
    except:
        return 'Error con la url del archivo de datos'
    listrest = []

    if codest == 1:
        sumCont1 = 0
        sumCont2 = 0
        sumCont3 = 0
        for i in range(len(df.index)):
            if df["codAnio"][i] == codAnio:
                sumCont1 += df["Cont1"][i]
                sumCont2 += df["Cont2"][i]
                sumCont3 += df["Cont3"][i]
        listrest.append(sumCont1)
        listrest.append(sumCont2)
        listrest.append(sumCont3)

    if codest == 2:
        sumCont1 = 0
        sumCont2 = 0
        sumCont3 = 0
        n = 0
        for i in range(len(df.index)):
            if df["codAnio"][i] == codAnio:
                sumCont1 += df["Cont1"][i]
                sumCont2 += df["Cont2"][i]
                sumCont3 += df["Cont3"][i]
                n += 1
        listrest.append(float(round(sumCont1/n, 1)))
        listrest.append(float(round(sumCont2/n, 1)))
        listrest.append(float(round(sumCont3/n, 1)))

    if codest == 3:
        listtemp = []
        mycont1 = -1
        mycont2 = -1
        mycont3 = -1
        codciucont1 = 0
        codciucont2 = 0
        codciucont3 = 0
        for i in range(len(df.index)):
            if df["codAnio"][i] == codAnio:
                if df["Cont1"][i] > mycont1:
                    mycont1 = df["Cont1"][i]
                    codciucont1 = df["CodCiud"][i]

                if df["Cont2"][i] > mycont2:
                    mycont2 = df["Cont2"][i]
                    codciucont2 = df["CodCiud"][i]

                if df["Cont3"][i] > mycont3:
                    mycont3 = df["Cont3"][i]
                    codciucont3 = df["CodCiud"][i]

        listrest.append(codciucont1)
        listrest.append(codciucont2)
        listrest.append(codciucont3)

    return listrest
