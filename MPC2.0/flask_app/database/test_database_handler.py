import database_handler as dh

dh.write_bin("numbers.dat", {"x": 1, "y": 2, "z": 3 , "k" : 1})
print(dh.read_bin("numbers.dat"))

#dh.init_csv("flask_app/database/s.csv")