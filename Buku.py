import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

buku_list = [
    {'id_buku': 1, 'judul': 'Buku A', 'pengarang': 'Pengarang A', 'stok': 5},
    {'id_buku': 2, 'judul': 'Buku B', 'pengarang': 'Pengarang B', 'stok': 3},
]

peminjaman_list = []

def tampilkan_buku():
    buku_listbox.delete(0, tk.END)
    for buku in buku_list:
        buku_listbox.insert(tk.END, f"ID: {buku['id_buku']} | Judul: {buku['judul']} | Pengarang: {buku['pengarang']} | Stok: {buku['stok']}")

def tambah_buku():
    judul = simpledialog.askstring("Input", "Masukkan Judul Buku:")
    pengarang = simpledialog.askstring("Input", "Masukkan Pengarang Buku:")
    stok = simpledialog.askinteger("Input", "Masukkan Jumlah Stok Buku:")
    
    if judul and pengarang and stok:
        id_buku = len(buku_list) + 1
        buku_list.append({'id_buku': id_buku, 'judul': judul, 'pengarang': pengarang, 'stok': stok})
        tampilkan_buku()
        messagebox.showinfo("Berhasil", "Buku berhasil ditambahkan!")
    else:
        messagebox.showwarning("Data Tidak Lengkap", "Pastikan semua data sudah dimasukkan!")

def pinjam_buku():
    try:
        selected = buku_listbox.curselection()
        if not selected:
            messagebox.showwarning("Pilih Buku", "Pilih buku yang ingin dipinjam.")
            return

        buku_terpilih = buku_list[selected[0]]
        if buku_terpilih['stok'] > 0:
            nama_peminjam = simpledialog.askstring("Input", "Masukkan Nama Peminjam:")
            if nama_peminjam:
                buku_terpilih['stok'] -= 1
                peminjaman_list.append({
                    'id_buku': buku_terpilih['id_buku'],
                    'nama_peminjam': nama_peminjam,
                    'judul_buku': buku_terpilih['judul'],
                    'tanggal_pinjam': "2024-11-19"
                })
                tampilkan_buku()
                tampilkan_peminjaman()
                messagebox.showinfo("Peminjaman Berhasil", f"Buku '{buku_terpilih['judul']}' berhasil dipinjam!")
            else:
                messagebox.showwarning("Nama Peminjam", "Nama peminjam tidak boleh kosong.")
        else:
            messagebox.showwarning("Stok Habis", "Stok buku sudah habis.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

def balikin_buku():
    try:
        selected = peminjaman_listbox.curselection()
        if not selected:
            messagebox.showwarning("Pilih Peminjaman", "Pilih peminjaman yang ingin dikembalikan.")
            return

        peminjaman_terpilih = peminjaman_list[selected[0]]
        buku_terpilih = next(buku for buku in buku_list if buku['id_buku'] == peminjaman_terpilih['id_buku'])
        
        buku_terpilih['stok'] += 1
        peminjaman_list.remove(peminjaman_terpilih)
        
        tampilkan_buku()
        tampilkan_peminjaman()
        
        messagebox.showinfo("Pengembalian Berhasil", f"Buku '{buku_terpilih['judul']}' berhasil dikembalikan!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

def hapus_buku():
    try:
        selected = buku_listbox.curselection()
        if not selected:
            messagebox.showwarning("Pilih Buku", "Pilih buku yang ingin dihapus.")
            return
        
        buku_terpilih = buku_list[selected[0]]
        buku_list.remove(buku_terpilih)
        
        tampilkan_buku()
        
        messagebox.showinfo("Buku Dihapus", f"Buku '{buku_terpilih['judul']}' berhasil dihapus!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

def tampilkan_peminjaman():
    peminjaman_listbox.delete(0, tk.END)
    for peminjaman in peminjaman_list:
        peminjaman_listbox.insert(tk.END, f"Nama: {peminjaman['nama_peminjam']} | Buku: {peminjaman['judul_buku']}")

def exit_program():
    root.quit()

root = tk.Tk()
root.title("Sistem Peminjaman Buku Perpustakaan")

root.configure(bg="Grey")

frame_buku = tk.Frame(root, bg="Grey")
frame_buku.pack(padx=10, pady=5)

label_buku = tk.Label(frame_buku, text="Daftar Buku", font=("Arial", 10, 'bold'), bg="Grey")
label_buku.pack()

buku_listbox = tk.Listbox(frame_buku, width=60, height=10, font=("Arial", 9))
buku_listbox.pack(padx=10, pady=5)

frame_peminjaman = tk.Frame(root, bg="Grey")
frame_peminjaman.pack(padx=10, pady=5)

label_peminjaman = tk.Label(frame_peminjaman, text="Daftar Peminjaman", font=("Arial", 10, 'bold'), bg="Grey")
label_peminjaman.pack()

peminjaman_listbox = tk.Listbox(frame_peminjaman, width=60, height=5, font=("Arial", 9))
peminjaman_listbox.pack(padx=10, pady=5)

frame_buttons = tk.Frame(root, bg="Grey")
frame_buttons.pack(padx=10, pady=5)

btn_tambah_buku = tk.Button(frame_buttons, text="Tambah Buku", command=tambah_buku, width=12, height=1, bg="lightblue", activebackground="red", font=("Arial", 9))
btn_tambah_buku.grid(row=0, column=0, padx=5, pady=5)

btn_pinjam_buku = tk.Button(frame_buttons, text="Pinjam Buku", command=pinjam_buku, width=12, height=1, bg="lightblue", activebackground="red", font=("Arial", 9))
btn_pinjam_buku.grid(row=0, column=1, padx=5, pady=5)

btn_balikin_buku = tk.Button(frame_buttons, text="Balikin Buku", command=balikin_buku, width=12, height=1, bg="lightblue", activebackground="red", font=("Arial", 9))
btn_balikin_buku.grid(row=1, column=0, padx=5, pady=5)

btn_hapus_buku = tk.Button(frame_buttons, text="Hapus Buku", command=hapus_buku, width=12, height=1, bg="lightblue", activebackground="red", font=("Arial", 9))
btn_hapus_buku.grid(row=1, column=1, padx=5, pady=5)

btn_exit = tk.Button(frame_buttons, text="Exit", command=exit_program, width=12, height=1, bg="red", activebackground="red", font=("Arial", 9))
btn_exit.grid(row=2, column=0, columnspan=2, pady=5)

tampilkan_buku()
tampilkan_peminjaman()

root.mainloop()
