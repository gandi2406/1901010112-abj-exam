file = open ("db-inventory.txt","a")
while True:
    tidak = input ("Input data inventory baru ? (ya/tidak)")
    if tidak == 'tidak' or tidak == 'Tidak':
        file = open ("db-inventory.txt","r")
        for item in file:
            item=item.strip()
            print(item)
        break
    elif tidak == 'ya' or tidak == 'Ya':
        print("-----------ok------------------")
        x = input ("Masukkan nama perangkat : ")
        y = input ("Masukkan lokasi : ")
        file.write("Nama Perangkat : " +x + ", Lokasi : " + y +"\n")
        print("-----------ok------------------")

file.close()