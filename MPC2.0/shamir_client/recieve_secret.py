from shamir import decrypt
from api_handler import get, create_serverlist_array

serverlist = create_serverlist_array()
threshold = 3
total_shares = len(serverlist)
shares = []

for i in range(len(serverlist)):
    print("getting from server : " + serverlist[i] )
    shares.append((get(serverlist[i], "x"), get(serverlist[i], "y")))

secret = decrypt(shares, threshold, total_shares)


print("Your secret is : " + str(secret))


