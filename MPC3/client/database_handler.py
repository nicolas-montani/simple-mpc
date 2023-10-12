import pandas as pd
from shamir import encrypt
import random
from shamir import PRIME

#initiate databases

DATABASE_PATH = "client/database/s.csv"
# PRIME = 340282366920938463463374607431768211297


def init_s_db():
    print(f"""initiating database with prime \np = {PRIME}""")
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

    for i in range(1,201):
        r = random.randint(1,PRIME-1)
        print(f"r = {r}")
        secret = pow(r,2,PRIME)
        print(f"s{i} = " + str(secret))

        s = encrypt(secret, threshold=3, total_shares=7)

        database_init["index"].append(i)
        database_init["s1"].append(s[0][1])
        database_init["s2"].append(s[1][1])
        database_init["s3"].append(s[2][1])
        database_init["s4"].append(s[3][1])
        database_init["s5"].append(s[4][1])
        database_init["s6"].append(s[5][1])
        database_init["s7"].append(s[6][1])

    df = pd.DataFrame(database_init)
    df.to_csv(DATABASE_PATH, index=False)


def get_database():
    df = pd.read_csv(DATABASE_PATH)
    return df

def init_simple_db():
    print(f"""initiating simple database """)
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

    for i in range(1,201):
        secret = i
        print(f"s{i} = " + str(secret))

        s = encrypt(secret, threshold=3, total_shares=7)

        database_init["index"].append(i)
        database_init["s1"].append(s[0][1])
        database_init["s2"].append(s[1][1])
        database_init["s3"].append(s[2][1])
        database_init["s4"].append(s[3][1])
        database_init["s5"].append(s[4][1])
        database_init["s6"].append(s[5][1])
        database_init["s7"].append(s[6][1])

    df = pd.DataFrame(database_init)
    df.to_csv(DATABASE_PATH, index=False)
    
if __name__ ==  "__main__":
    init_s_db()
    #init_simple_db()
    pass