import function

# input internal persamaanA, persamaanB, persamaanC
function.garis()
persamaan_A = (1, 2, 1)
persamaan_B = (3, -4, -2)
persamaan_C = (5, 3, 5)
persamaan_Z = (4, 2, -1)

# menampilkan matriks yang ada
print("Matriks : ")
print(persamaan_A)
print(persamaan_B)
print(persamaan_C)
print("persamaan Z : ", persamaan_Z)
function.garis()

# mencari determinan kemudian menampilkan hasilnya
hasil_determinan = function.determinan(persamaan_A, persamaan_B, persamaan_C)

# menampilkan hasil determinan
print("Hasil determinan adalah", hasil_determinan)
function.garis()

# menampilkan hasil kofaktor
print("Hasil Kofaktor")
kofakfaktor_A = function.kofaktor(persamaan_A, persamaan_B, persamaan_C, "A")
kofakfaktor_B = function.kofaktor(persamaan_A, persamaan_B, persamaan_C, "B")
kofakfaktor_C = function.kofaktor(persamaan_A, persamaan_B, persamaan_C, "C")

# menampilkan hasil kofaktor
print(kofakfaktor_A)
print(kofakfaktor_B)
print(kofakfaktor_C)
function.garis()

# adjoin kofaktor a, b, dan c
adjoin_A = function.adjoin(kofakfaktor_A, kofakfaktor_B, kofakfaktor_C, "A")
adjoin_B = function.adjoin(kofakfaktor_A, kofakfaktor_B, kofakfaktor_C, "B")
adjoin_C = function.adjoin(kofakfaktor_A, kofakfaktor_B, kofakfaktor_C, "C")

# menampilkan hasil adjoin
print("Adjoin : ")
print(adjoin_A)
print(adjoin_B)
print(adjoin_C)

# Invers 
hasil_invers = function.invers_A(adjoin_A, adjoin_B, adjoin_C, persamaan_Z, hasil_determinan)
function.garis()
print("Hasil Invers : ")
print(hasil_invers)
function.garis()
