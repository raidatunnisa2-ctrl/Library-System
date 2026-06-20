import csv

FILE = "books.csv"

def load_data():
    with open(FILE, "r") as f:
        return list(csv.DictReader(f))

# ======================
# SEARCH
# ======================
def cari_buku():
    books = load_data()
    id = input("Masukkan ID buku: ")

    for b in books:
        if b["id"] == id:
            print("Buku ditemukan:")
            print(b)
            return

    print("Buku tidak ditemukan")

# ======================
# SORTING
# ======================
def sort_buku():
    books = load_data()

    print("1. Urutkan Judul (A-Z)")
    print("2. Urutkan Tahun (Terbaru)")

    pilih = input("Pilih: ")

    if pilih == "1":
        hasil = sorted(books, key=lambda x: x["judul"])
    elif pilih == "2":
        hasil = sorted(books, key=lambda x: x["tahun"], reverse=True)
    else:
        print("Pilihan tidak valid")
        return

    for b in hasil:
        print(b)