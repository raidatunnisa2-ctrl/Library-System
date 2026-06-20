import csv

FILE_NAME = "books.csv"

def load_data():
    books = []
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

def save_data(books):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["id", "judul", "penulis", "tahun", "jumlah"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)