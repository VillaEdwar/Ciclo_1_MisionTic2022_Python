def aplicaciones(url, codDep, codest):
    import pandas as pd
    try:
        df = pd.read_csv(url, sep=";")
    except:
        return 'Error con la url del archivo de datos'
    listrest = []

    if codest == 1:
        tiempLat = 0
        tiempred = 0
        tiempExp = 0
        for i in range(len(df.index)):
            if df["CodDep"][i] == codDep:
                tiempLat += df["Latencia"][i]
                tiempred += df["Rendimiento"][i]
                tiempExp += df["ExpUs"][i]
        listrest.append(tiempLat)
        listrest.append(tiempred)
        listrest.append(tiempExp)

    if codest == 2:
        tiempLat = 0
        tiempred = 0
        tiempExp = 0
        n = 0
        for i in range(len(df.index)):
            if df["CodDep"][i] == codDep:
                tiempLat += df["Latencia"][i]
                tiempred += df["Rendimiento"][i]
                tiempExp += df["ExpUs"][i]
                n += 1
        listrest.append(float(round(tiempLat/n, 1)))
        listrest.append(float(round(tiempred/n, 1)))
        listrest.append(float(round(tiempExp/n, 1)))

    if codest == 3:
        listtemp = []
        maylat = -1
        mayred = -1
        mayexp = -1
        codApplat = 0
        codAppred = 0
        codAppexp = 0
        for i in range(len(df.index)):
            if df["CodDep"][i] == codDep:
                if df["Latencia"][i] > maylat:
                    maylat = df["Latencia"][i]
                    codApplat = df["App"][i]

                if df["Rendimiento"][i] > mayred:
                    mayred = df["Rendimiento"][i]
                    codAppred = df["App"][i]

                if df["ExpUs"][i] > mayexp:
                    mayexp = df["ExpUs"][i]
                    codAppexp = df["App"][i]

        listrest.append(codApplat)
        listrest.append(codAppred)
        listrest.append(codAppexp)

    return listrest
