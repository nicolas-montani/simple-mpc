import pandas as pd

VALUES_DATABASE_PATH = "database/values.csv"
S_DATABASE_PATH = "database/s.csv"

#initiate databases
def init_values_db():
    values = ["x", "y", "z", "k"]
    empty = [0, 0, 0, 0]
    df = pd.Series(empty, index=values)
    df.to_csv("flask_app/database/values.csv", header=False)

def init_s_db():
    values = []
    empty = []
    for i in range(1, 201):
        values.append(f"s{i}")
        empty.append(0)

    df = pd.Series(empty, index=values)
    df.to_csv("flask_app/database/s.csv", header=False)
#get value from database

def get_value(index):
    if 's' in index:
        df = pd.read_csv(S_DATABASE_PATH, header=None)
        
    else:
        df = pd.read_csv(VALUES_DATABASE_PATH, header=None)
    return (df[df[0] == index][1].values[0])
    

#set value in database

def set_value(index, value):
    if 's' in index:
        df = pd.read_csv(S_DATABASE_PATH, header=None)
        df.loc[df[0] == index, 1] = value
        df.to_csv(S_DATABASE_PATH, header=False, index=False)
      
    else :
        df = pd.read_csv(VALUES_DATABASE_PATH, header=None)
        df.loc[df[0] == index, 1] = value
        df.to_csv(VALUES_DATABASE_PATH, header=False, index=False) 


if __name__ == "__main__":
    init_values_db()
    init_s_db()