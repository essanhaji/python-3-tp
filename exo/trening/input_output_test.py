

# try:
#     file = open("data.txt")
# except FileNotFoundError:
#     print("Le fichier est introuvable")
# except IOError:
#     print("Erreur d’ouverture")



# try:
#     file = open('data.txt', 'w') 
#     # Ouverture en écriture
# except FileNotFoundError:
#     print('Le fichier est introuvable')
# except IOError:
#     print("Erreur d’ouverture")



# try:
#     file = open('data.txt', 'rt')
#     # Mode par défaut
# except FileNotFoundError:
#     print('Le fichier est introuvable')
# except IOError:
#     print("Erreur d’ouverture")



# try:
#     with open('data.txt') as file:
#       print(file.read())
# except FileNotFoundError:
#     print('Le fichier est introuvable')
# except IOError:
#     print("Erreur d’ouverture")


# try:
#     with open('data.txt', 'w') as file:
#         file.write("Hello World !!")
# except FileNotFoundError:
#     print('Le fichier est introuvable')
# except IOError:
#     print("Erreur d’ouverture")



# with open('data.txt', 'r') as src, open('copy.txt', 'w') as dest:
#     dest.write(src.read())


# import pickle
# name = "Temperatures (2019)"
# data = [12, -9, 7, 112, 99]
# try:
#     with open('data.txt', 'wb') as file:
#         pickle.dump(name, file, pickle.HIGHEST_PROTOCOL)
#         pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)
# except pickle.PicklingError: 
#     print("Erreur d’écriture")





# import pickle
# try:
#     with open('data.txt', 'rb') as file:
#         name = pickle.load(file)
#         data = pickle.load(file)
#         print(name, data, sep='\n')
# except pickle.UnpicklingError:
#     print("Erreur de lecture")


# s = "Hello"
# data = s.encode('utf-8')
# print(type(data))
# print(data)
# print(data.decode('utf-8'))


import gzip
with gzip.open('data.txt.gz', mode='wb') as file:
    file.write('Hello Valerian! Ready for a beer ?'.encode('utf-8'))

