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
    hasil_B1 = -1 * ((A2 * C3) - (A3 * C2))
    hasil_B2 = 1 * ((A1 * C3) - (A3 * C1))
    hasil_B3 = -1 * ((A1 * C2) - (A2 * C1))

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

def adjoin(kofakfaktor_A, kofakfaktor_B, kofakfaktor_C, status):
    # mengambil 3 variabel masing-masing persamaan
    A1, A2, A3 = kofakfaktor_A
    B1, B2, B3 = kofakfaktor_B
    C1, C2, C3 = kofakfaktor_C

    #melakukan adjoin
    if(status == "A"):
        hasil_adjoin = (A1, B1, C1)
    elif(status == "B"):
        hasil_adjoin = (A2, B2, C2)
    elif(status == "C"):
        hasil_adjoin = (A3, B3, C3)
    
    return hasil_adjoin

def invers_A(adjoin_A, adjoin_B, adjoin_C, persamaan_Z, hasil_determinan):
    # mengambil 3 variabel masing-masing persamaan
    A1, A2, A3 = adjoin_A
    B1, B2, B3 = adjoin_B
    C1, C2, C3 = adjoin_C
    Z1, Z2, Z3 = persamaan_Z

    # mengalikan persamaan Z dengan adjoin_A
    hasil_invers_A = (A1 * Z1) + (A2 * Z2) + (A3 * Z3)
    hasil_invers_B = (B1 * Z1) + (B2 * Z2) + (B3 * Z3)
    hasil_invers_C = (C1 * Z1) + (C2 * Z2) + (C3 * Z3)

    # melakukan langkah invers terakhir
    hasil_A = hasil_invers_A / hasil_determinan
    hasil_B = hasil_invers_B / hasil_determinan
    hasil_C = hasil_invers_C / hasil_determinan

    invers = (hasil_A, hasil_B, hasil_C)
    return invers

def garis():
    print("=========================================")
