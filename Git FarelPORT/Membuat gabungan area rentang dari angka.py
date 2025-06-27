#Gabungan area rentang dari angka
import time
import sys

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)    
try: 
    slow_print(41*"=", delay=0.01)
    print("\n", 5*"=","SELAMAT DATANG DI GAME ANGKA",5*"=")
    slow_print(41*"=", delay=0.01)
    print("\nISI ANGKA : \nKURANG DARI 50 \n| \nLEBIH DARI 100\n")
    inputan = float(input("Masukkan angka : "))
except ValueError:
    print("Kamu tidak boleh mengisi huruf disini!")
    exit()
print("\n")
if inputan == 50 or inputan == 100:
    slow_print("SAYA MEMINTA AGAR ANDA MENGISI ANGKA YANG KURANG DARI (50) DAN LEBIH DARI (100) ! ")
    exit()
#Memeriksa angka kurang dari 100
isKd = (inputan < 50)
print("Apakah angka yang kamu masukkan kurang dari 50? ", isKd, "\n")

#Memeriksa angka lebih dari 100
isLb = (inputan > 100)
print("Apakah angka yang kamu masukkan Lebih dari 100? ", isLb, "\n")

#Memeriksa angka 50.0 dan 100.0
isBnr = isLb or isKd 
print("Angka yang anda isi termasuk","[",isBnr,"]", "Karena anda memasukkan angka selain (50) dan (100)")

print("\n", 41*"=")

time.sleep(5)
slow_print("Sekarang kita lanjut ke permainan kedua..\n", delay=0.05)
print("\nISI ANGKA : \nLEBIH DARI 50 \n| \nKURANG DARI 100\n")
inputan = float(input("Masukkan angka : "))
print("\n")
if inputan == 50 or inputan == 100:
    print("SAYA MEMINTA AGAR ANDA MENGISI ANGKA YANG LEBIH DARI (50) DAN KURANG DARI (100) ! ")
    exit()

#Memeriksa angka lebih dari 50 
isKd = (inputan > 50)
print("Apakah angka yang kamu masukkan lebih dari 50? ", isKd, "\n")

#Memeriksa angka kurang dari 100
isLb = (inputan < 100)
print("Apakah angka yang kamu masukkan kurang dari 100? ", isLb, "\n")

isBnr = isLb and isKd
print("Angka yang anda isi termasuk", "[",isBnr,"]", "Karena anda memasukkan angka lebih dari (50) dan kurang dari (100)")
print("\n", 41*"=")
print("\n", 41*"=")