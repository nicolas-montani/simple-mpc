from shamir import decrypt
from api_handler import get, get_out
from database_handler import PRIME


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
    return s


def calculate_out():
    array = []
    result = []
    out_array = []
    

    for i in range(7):
        print(f"getting out server {5000+i}")
        array.append(list(map(lambda x : int(x) % PRIME, get_out(5000+i))))
        

    for i in range(len(array[0])):
        shares = []
        for j in range(7):
            shares.append((j, array[j][i]))
        result.append(decrypt(shares=shares, threshold=3, total_shares=7))

    print(result)
    n_pow = int((PRIME-1)//2) 
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

    output = "".join(map(str,out_array))
    print(output)
    return out_array
    
if __name__ == "__main__":
    # recieve_k()
    # recieve_s()
    calculate_out()