def menu():
    print("Pilih Menu")
    print("1. Games (Kasino)")
    print("2. Calculator")
    print("3. Exit")

def games():
    acak=int(input("Input angka [1-10]: "))
    import random
    n = random.randint(1,10)
    print("The random number : ", n)
    if acak==n:
        print("You Win")
        print("")
    else:
        print("Try Again Later")
        print("")

def calculatorbiasa():
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    n = int(input("Pilih Calculator: "))
    angka1 = int(input("Angka Pertama: "))
    angka2 = int(input("Angka Kedua: "))
    if n==1:
      
        print("Penjumlahannya adalah : ", angka1+angka2)
        print("")
    elif n==2:
      
        print("Pengurangannya adalah : ", angka1-angka2)
        print("")
    elif n==3:
      
        print("Perkaliannya adalah : ", angka1*angka2)
        print("")
    elif n==4:
        
        print("Pembagiannya adalah : ", angka1/angka2)
        print("") 
    elif n==5:

        print("Pangkat: ", angka1**angka2)
        print("")

def calculatorDatar():
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    datar = int(input("Pilih Bangun Datar: "))
    if datar==1:
        print("1. Luas")
        print("2. Keliling")
        rumus1=int(input(">> "))
        sisi = int(input("Panjang Sisi: "))
        if rumus1==1:
            print("Luas Persegi: ", sisi*sisi)
            print("")
        elif rumus1==2:
            print("Keliling Persegi: ", 4*sisi)
            print("")  
    elif datar == 2:
        print("1. Luas")
        print("2. Keliling")
        rumus2 = int(input(">> "))
        panjang = int(input("Panjang: "))
        lebar = int(input("Lebar: "))
        if rumus2==1:
            print("Luas Persegi Panjang: ", panjang*lebar)
            print("")
        elif rumus2==2:
            print("Keliling Persegi Panjang: ", 2*(panjang+lebar))
            print("")
    elif datar ==3:
        print("1. Luas")
        print("2. Keliling")
        print("3. Degenerate Checker")
        rumus3 = int(input(">> "))
        if rumus3==1:
            tinggi = int(input("Tinggi: "))
            alas = int(input("Alas: "))
            print("Luas Segitiga: ",(alas*tinggi)/2)
            print("")
        elif rumus3==2:
            sisi1=int(input("Sisi A: "))
            sisi2=int(input("Sisi B: "))
            sisi3=int(input("Sisi C: "))
            print("Keliling Segitiga: ", sisi1+sisi2+sisi3)
            print("")
        elif rumus3==3:
            a=int(input("Sisi A: "))
            b=int(input("Sisi B: "))
            c=int(input("Sisi C: "))
            if a+b<=c or b+c<=a or c+a<=b:
                print("Segitiga Tidak Valid")
            else:
                if(a==b and b==c):
                    print("Segitiga Sama Sisi")
                    print("")
                elif((a==b and b!=c) or (b==c and c!=a) or (a==c and c!=b)):
                    print("Segitiga Sama Kaki")
                    print("")
                elif(a!=b and b!=c):
                    print("Segitiga Sembarang")
                    print("")

    elif datar ==4:
        print("1. Luas")
        print("2. Keliling")
        rumus4 = int(input(">> "))
        jari=int(input("Jari-jari: "))
        if rumus4==1:
            print("Luas Lingkaran: ", 22/7*jari**2)
        elif rumus4==2:
            print("Keliling Lingkaran: ", 2*22/7*jari )


            

            


        


def calculator():
    print("1. Calculator Biasa")
    print("2. Calculator Bangun Datar")
    pilih = int(input("Pilih Angka: "))
    if pilih == 1:
        calculatorbiasa()
    if pilih==2:
        calculatorDatar()





menu()
n = int(input(">> "))
while (n!=3):
    match(n):
        case 1:
            games()
        case 2:
            calculator()
   
            
        

    
