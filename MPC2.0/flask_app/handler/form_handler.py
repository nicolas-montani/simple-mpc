from handler.api_handler import get, post, put
from database.database_handler import create_serverlist_array

def form_handler(cast, server, method, key, value, operator):

    response = []

    if cast == "broadcast":
        serverlist = create_serverlist_array()
    else: 
        serverlist = [server]

    if method == "POST":
        for server in serverlist:
            response.append(post(server, key , value))
    elif method == "PUT":
        for server in serverlist:
            response.append(put(server, operator))
    elif method == "GET":
        for server in serverlist:
            response.append(get(server, key))
    
    return response
    
        
if __name__ == "__main__":
    pass
