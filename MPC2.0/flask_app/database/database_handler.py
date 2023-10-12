import pickle
import pandas as pd


# database : {"x": 1, "y": 2, "z": 3 , "k" : 1}

# read binary file with pickle
def read_bin(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)
        
# write binary file with pickle
def write_bin(file_name, data):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)

def create_serverlist_array():
    serverlist = []
    with open("database/serverlist.txt", "r") as f:
        for line in f:
            serverlist.append(line.strip())
    return serverlist

# read csv file
def read_csv(file_name,line):
    pass

#write to csv file 
def write_csv(file_name, data): 

    pass

def init_csv(file_name):
    

    ####rewrite 

    database_init = {
        "index" : [],
        "s1" : [],


    }

    threshold = 3
    total_shares = 7

    for i in range(1,200):

        database_init["index"].append(i)
        database_init["s1"].append("")


    df = pd.DataFrame(database_init)
    df.to_csv(file_name, index=False)

