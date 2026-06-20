import crud
import search_sort
import queue_stack

def menu():
    print("\n===== SISTEM PERPUSTAKAAN =====")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Update Buku")
    print("4. Hapus Buku")
    print("5. Cari Buku")
    print("6. Sorting Buku")
    print("7. Pinjam Buku (Queue)")
    print("8. Kembalikan Buku (Stack)")
    print("9. Keluar")

while True:
    menu()
    pilih = input("Pilih menu: ")

    if pilih == "1":
        crud.tambah_buku()
    elif pilih == "2":
        crud.lihat_buku()
    elif pilih == "3":
        crud.update_buku()
    elif pilih == "4":
        crud.hapus_buku()
    elif pilih == "5":
        search_sort.cari_buku()
    elif pilih == "6":
        search_sort.sort_buku()
    elif pilih == "7":
        queue_stack.pinjam_buku()
    elif pilih == "8":
        queue_stack.kembalikan_buku()
    elif pilih == "9":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid")