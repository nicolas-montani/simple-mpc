import pandas as pd
from shamir import encrypt

def init_s_csv(file_name):

    database_init = {
        "index" : [],
        "s1" : [],
        "s2" : [],
        "s3" : [],
        "s4" : [],
        "s5" : [],
        "s6" : [],
        "s7" : [],

    }

    threshold = 3
    total_shares = 7

    for i in range(1,201):
        s = encrypt(i, threshold, total_shares)
        database_init["index"].append(i)
        database_init["s1"].append(s[0][1])
        database_init["s2"].append(s[1][1])
        database_init["s3"].append(s[2][1])
        database_init["s4"].append(s[3][1])
        database_init["s5"].append(s[4][1])
        database_init["s6"].append(s[5][1])
        database_init["s7"].append(s[6][1])

    df = pd.DataFrame(database_init)
    df.to_csv(file_name, index=False)

#init_s_csv("shamir_client/database/s.csv")

def get_column(colum_name, file_name):

    df = pd.read_csv(file_name)
    column = df[colum_name]
    return column
    


get_column("s1", "shamir_client/database/s.csv")

