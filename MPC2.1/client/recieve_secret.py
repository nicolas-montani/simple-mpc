from shamir import decrypt
from api_handler import get, get_out
from database_handler import PRIME,PRIME


# Get shares from servers
def recieve_k():
    shares = []
    for i in range(7):
        share = get(server=i+5000, key="y"), get(server=i+5000, key="k")
        print(f"{i+5000}: {share}")
        shares.append(share)
    return decrypt(shares, threshold=3, total_shares=7)


def recieve_s():
    s = get(server=5000, key="s1")
    print(s)


def calculate_out():
    result = []
    out_array = []

    array1 = get_out(5000)
    print("getting out server 5000")
    array2 = get_out(5001)
    print("getting out server 5001")
    array3 = get_out(5002)
    print("getting out server 5002")
    array4 = get_out(5003)
    print("getting out server 5003")
    array5 = get_out(5004)
    print("getting out server 5004")
    array6 = get_out(5005)
    print("getting out server 5005")
    array7 = get_out(5006)
    print("getting out server 5006")

    print(f"len {len(array1)}")

    for i in range(len(array1)):
        shares = [(1, int(array1[i])),(2, int(array2[i])),(3, int(array3[i])),(4, int(array4[i])),(5, int(array5[i])),(6, int(array6[i])),(7, int(array7[i]))]
        result.append(decrypt(shares=shares, threshold=3, total_shares=7)) 
        print(f"adding shares to {i}")
    
    
    n_pow = int((PRIME-1)/2) #use double division
    print(f"prime : {PRIME}")
    print(f"n_pow : {n_pow}")
        
    for i in range(len(result)):
        out = pow(result[i],n_pow,PRIME)
        print(f"{i+1} : {result[i]} =>> {out}")

        if out == 0:
            out_array.append(None)

        elif out == 1 : 
            out_array.append(0)

        elif out == (PRIME-1): 
            out_array.append(1)
        
        else :
            out_array.append(out)

    
        
    print(f"array = {''.join([str(x) for x in out_array])}")


if __name__ == "__main__":
    #print(recieve_k())
    #print(recieve_s())
    calculate_out()
    
    pass