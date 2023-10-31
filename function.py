def determinan(persamaanA, persamaanB, persamaanC):
    # mengambil 3 variabel masing-masing dari persamaanA, persamaanB, persamaanC
    A1, A2, A3 = persamaanA
    B1, B2, B3 = persamaanB
    C1, C2, C3 = persamaanC

    # membuat nilai variabel menjadi positif
    abs(A1)
    abs(A3)

    # menyelesaikan determinan dengan persamaanA
    hasil = A1 * ((B2 * C3)-(B3 * C2)) - A2 * ((B1 * C3)-(B3 * C1)) + A3 * ((B1 * C2)-(B2 * C1))

    return hasil

def kofaktor(persamaanA, persamaanB, persamaanC, status):
    # mengambil 3 variabel masing-masing dari persamaanA, persamaanB, persamaanC
    A1, A2, A3 = persamaanA
    B1, B2, B3 = persamaanB
    C1, C2, C3 = persamaanC

    # mencari hasil persamaanA
    hasil_A1 = 1 * ((B2 * C3) - (B3 * C2))
    hasil_A2 = -1 * ((B1 * C3) - (B3 * C1))
    hasil_A3 = 1 * ((B1 * C2) - (B2 * C1))

    # mencari hasil persamaanB
    hasil_B1 = 1 * ((A2 * C3) - (A3 * C2))
    hasil_B2 = -1 * ((A1 * C3) - (A3 * C1))
    hasil_B3 = 1 * ((A1 * C2) - (A2 * C1))

    # mencari hasil persamaanC
    hasil_C1 = 1 * ((A2 * B3) - (A3 * B2))
    hasil_C2 = -1 * ((A1 * B3) - (A3 * B1))
    hasil_C3 = 1 * ((A1 * B2) - (A2 * B1))

    # mengambalikan nilai sesuai dengan nilai status
    if(status == "A"):
        hasil_tuple = (hasil_A1, hasil_A2, hasil_A3)
    elif(status == "B"): 
        hasil_tuple = (hasil_B1, hasil_B2, hasil_B3)
    elif(status == "C"):
        hasil_tuple = (hasil_C1, hasil_C2, hasil_C3)

    return hasil_tuple

def garis():
    print("=========================================")
