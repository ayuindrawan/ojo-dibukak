#nama program
print ("Alat Terjemahan Angka Sederhana \n")
#database terjemahan
Dictionary = {1:"one", 2:"two", 3:"three",4:"four",5:"five",6:"six",7:"seven", 8:"eight", 9:"nine", 10:"ten"}
Kamus_Palembang = {1:"sikok", 2:"duo", 3:"tigo", 4:"empat", 5:"limo", 6:"enem", 7:"tojo", 8:"lapan", 9:"sembilan", 10:"sepulo"}
Kamus_Mandarin = {1:"Yi", 2:"Er", 3:"San", 4:"Si", 5:"Wu", 6:"Liu", 7:"Qi", 8:"Ba", 9:"Jiu", 10:"Shi"}

#Fungsi untuk mendefinisikan option yang akan dipilih
def option ():
   print("\n")
   print("Pilihan bahasa")
   print("1.Inggris")
   print("2.Palembang")
   print("3.Mandarin")
   print("4.Exit")
   pilihan = int(input("Masukan pilihan Anda: "))
   return pilihan

#Fungsi untuk mendefinisikan bahasa ingrris
def Inggris():
    pilih= int(input("Input number :"))
    pilih in Dictionary
    print (Dictionary.get(pilih))
    return pilih

#Fungsi untuk mendefinisikan bahasa jawa
def Palembang():
    pilih=int(input("Masoke angko:"))
    pilih in Kamus_Palembang
    print(Kamus_Palembang.get(pilih))
    return pilih
	
#Fungsi untuk mendefinisikan bahasa mandarin
def Mandarin():
	pilih=int(input("Shuru haoma:"))
	pilih in Kamus_Mandarin
	print (Kamus_Mandarin.get(pilih))
	
#Program inti pemanggil function option dan function inggris 
pilihan = True
while(pilihan<4):
	pilihan = option()
	if (pilihan ==4):
		break;
	else:
		if (pilihan==1):
			Inggris ()
		if (pilihan==2):
			Palembang()
		elif (pilihan==3):
			Mandarin()