from shamir import encrypt
from api_handler import post
from database_handler import get_database
import threading

# Create shares to k 


def init_k(k):

    shares = encrypt(secret=k, threshold=3, total_shares=7)

    # Send shares to servers
    for i in range(7):
        print(i+5000, shares[i][0], shares[i][1])
        #Post shares to all serverserver, key, value
        post(server=i+5000, key="y", value=shares[i][0])
        post(server=i+5000, key="k", value=shares[i][1])

    print("Shares sent to servers on variable k")

def send_secret(secret,key):

    shares = encrypt(secret=secret, threshold=3, total_shares=7)

    # Send shares to servers
    for i in range(7):
        print(i+5000, shares[i][0], shares[i][1])
        #Post shares to all serverserver, key, value
        post(server=i+5000, key=key, value=shares[i][1])

    print(f"Shares sent to servers on variable {key}")
    

def send_s():
    df = get_database()

    def send_to(i):
        index = df["index"]
        column = df[f"s{i+1}"]
        server = i+5000


        for j in range(len(index)):
            
            print (f"{server} : s{index[j]} : {column[j]}")
            post(server=server, key=f"s{index[j]}", value=column[j])

        
    t1 = threading.Thread(target=send_to, args=(0,))
    t2 = threading.Thread(target=send_to, args=(1,))
    t3 = threading.Thread(target=send_to, args=(2,))
    t4 = threading.Thread(target=send_to, args=(3,))
    t5 = threading.Thread(target=send_to, args=(4,))
    t6 = threading.Thread(target=send_to, args=(5,))
    t7 = threading.Thread(target=send_to, args=(6,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()

    print("All shares sent to servers on variable s")

if __name__ == "__main__":
    init_k(3)
    send_secret(5,"x")
    send_s()

