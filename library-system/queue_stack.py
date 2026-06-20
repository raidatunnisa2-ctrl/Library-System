from collections import deque

queue = deque()
stack = []

# ======================
# QUEUE (PINJAM BUKU)
# ======================
def pinjam_buku():
    id = input("ID buku dipinjam: ")
    queue.append(id)
    print("Buku masuk antrian (Queue)")
    print("Antrian:", list(queue))

# ======================
# STACK (KEMBALI BUKU)
# ======================
def kembalikan_buku():
    id = input("ID buku dikembalikan: ")
    stack.append(id)
    print("Buku masuk riwayat (Stack)")
    print("Riwayat:", stack)