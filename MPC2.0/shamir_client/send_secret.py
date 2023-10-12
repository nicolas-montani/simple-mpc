from shamir import encrypt, decrypt
from api_handler import post, create_serverlist_array
from database_handler import get_column
#ask for user input here

serverlist = create_serverlist_array()

def send_k(): 

    k = 1234

    threshold = 3
    total_shares = len(serverlist)

    k_shares = encrypt(k, threshold, total_shares)

    print(k_shares)

    for i in range(len(serverlist)):
        print("sending K to server : " + serverlist[i] )
        post(serverlist[i], "k", k_shares[i][0])
        post(serverlist[i], "y", k_shares[i][1])
        print("k : " + str(k_shares[i][0]))
        print("y : " + str(k_shares[i][1]))
        


def send_column():

    for i in range(len(serverlist)):

        column_name = "s" + str(i+1)
        column = get_column(column_name, "shamir_client/database/s.csv")
        print("sending column " + column_name + " to server : " + serverlist[i] )
        #post(serverlist[i], column_name, column)
send_column()