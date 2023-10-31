import function

# menjalankan program
run_main()

def run_main():
    # input internal persamaanA, persamaanB, persamaanC
    persamaan_A = (1, 2, 1)
    persamaan_B = (3, -4, -2)
    persamaan_C = (5, 3, 5)

    # menampilkan matriks yang ada
    print("Matriks : ")
    print(persamaan_A)
    print(persamaan_B)
    print(persamaan_C)
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