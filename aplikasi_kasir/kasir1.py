import tkinter as tk
from tkinter import ttk

class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        return f"{self.nama} - Rp{self.harga}"

class Makanan(Produk):
    def __init__(self, nama, harga, jenis):
        super().__init__(nama, harga)
        self.jenis = jenis

    def tampilkan_info(self):
        return f"{super().tampilkan_info()} ({self.jenis})"

class Minuman(Produk):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self.ukuran = ukuran

    def tampilkan_info(self):
        return f"{super().tampilkan_info()} ({self.ukuran} mL)"

class AplikasiKasir(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Kasir")
        self.geometry("400x300")

        self.kasir = Kasir()

        self.label_produk = ttk.Label(self, text="Daftar Produk")
        self.label_produk.pack(pady=10)

        self.tree_produk = ttk.Treeview(self, columns=("Nama", "Harga"))
        self.tree_produk.heading("#0", text="Jenis")
        self.tree_produk.heading("Nama", text="Nama")
        self.tree_produk.heading("Harga", text="Harga")

        self.tree_produk.pack(padx=10, pady=10)

        self.tambah_produk_awal()

        self.label_total_harga = ttk.Label(self, text="Total Harga: Rp0")
        self.label_total_harga.pack(pady=10)

        self.button_proses_pembelian = ttk.Button(self, text="Proses Pembelian", command=self.proses_pembelian)
        self.button_proses_pembelian.pack(pady=10)

    def tambah_produk_awal(self):
        makanan1 = Makanan("Nasi Goreng", 15000, "Makanan Ringan")
        minuman1 = Minuman("Es Teh", 5000, 300)

        self.kasir.tambah_produk(makanan1)
        self.kasir.tambah_produk(minuman1)

        for produk in self.kasir.daftar_produk:
            self.tree_produk.insert("", "end", text=type(produk).__name__, values=(produk.nama, produk.harga))

    def proses_pembelian(self):
        selected_item = self.tree_produk.selection()
        if selected_item:
            index = int(selected_item[0][1:]) - 1
            jumlah = 1  # Misalnya, untuk sederhana, jumlah selalu 1
            total_harga = self.kasir.proses_pembelian(index, jumlah)
            self.label_total_harga.config(text=f"Total Harga: Rp{total_harga}")

class Kasir:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def proses_pembelian(self, index, jumlah):
        total_harga = self.daftar_produk[index].harga * jumlah
        return total_harga

if __name__ == "__main__":
    app = AplikasiKasir()
    app.mainloop()
