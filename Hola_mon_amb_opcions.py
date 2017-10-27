#!/usr/bin/python3.6
while True:
    print("""Això es un 'Hola mon des de Catalunya!' amb opcions 
            1) Si vols dir Hola al mon
            2) Si vols que ho digui en angles
            155) Si vols que digui 'Hola mundo' i marxi cap a Espanya""")
    o = input()
    if o == "1" :
        print("Hola mon desde Catalunya")
        print(" ")
    elif o == "2":
        print("Hello world from Catalonia")
        print(" ")
    elif o == "155" :
        print("Hola mundo desde España")
        print(" ")
        break
    else:
        print("No han quedat clares les opcions que tens?")
        print(" ")
