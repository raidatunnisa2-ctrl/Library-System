import csv

FILE = "books.csv"

# ======================
# LOAD DATA DARI CSV
# ======================
def load_data():
    books = []
    with open(FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append(row)
    return books

# ======================
# SIMPAN KE CSV
# ======================
def save_data(books):
    with open(FILE, "w", newline="") as f:
        fieldnames = ["id", "judul", "penulis", "tahun", "jumlah"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

# ======================
# CREATE
# ======================
def tambah_buku():
    books = load_data()

    books.append({
        "id": input("ID: "),
        "judul": input("Judul: "),
        "penulis": input("Penulis: "),
        "tahun": input("Tahun: "),
        "jumlah": input("Jumlah: ")
    })

    save_data(books)  # 🔥 INI WAJIB
    print("Buku berhasil ditambah")

# ======================
# READ
# ======================
def lihat_buku():
    books = load_data()
    for b in books:
        print(b)

# ======================
# UPDATE
# ======================
def update_buku():
    books = load_data()
    id = input("ID yang diupdate: ")

    for b in books:
        if b["id"] == id:
            b["judul"] = input("Judul baru: ")
            b["penulis"] = input("Penulis baru: ")
            b["tahun"] = input("Tahun baru: ")
            b["jumlah"] = input("Jumlah baru: ")

    save_data(books)  # 🔥 WAJIB
    print("Data berhasil diupdate")

# ======================
# DELETE
# ======================
def hapus_buku():
    books = load_data()
    id = input("ID yang dihapus: ")

    books = [b for b in books if b["id"] != id]

    save_data(books)  # 🔥 WAJIB
    print("Data berhasil dihapus")