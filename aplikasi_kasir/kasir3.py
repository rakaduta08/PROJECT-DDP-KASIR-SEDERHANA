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

class StrukPembelian(tk.Toplevel):
    def __init__(self, parent, transaksi):
        super().__init__(parent)

        self.title("Struk Pembelian")
        self.geometry("300x400")

        self.transaksi = transaksi

        self.label_judul = ttk.Label(self, text="Struk Pembelian")
        self.label_judul.pack(pady=10)

        self.label_produk = ttk.Label(self, text="Daftar Produk")
        self.label_produk.pack(pady=5)

        self.tree_produk = ttk.Treeview(self, columns=("Nama", "Harga", "Jumlah", "Total"))
        self.tree_produk.heading("#0", text="Jenis")
        self.tree_produk.heading("Nama", text="Nama")
        self.tree_produk.heading("Harga", text="Harga")
        self.tree_produk.heading("Jumlah", text="Jumlah")
        self.tree_produk.heading("Total", text="Total")

        self.tree_produk.pack(padx=10, pady=10)

        self.tampilkan_struk()

    def tampilkan_struk(self):
        total_harga = 0

        for idx, item in enumerate(self.transaksi, start=1):
            jenis_produk, produk, jumlah = item
            total_item = produk.harga * jumlah
            total_harga += total_item
            self.tree_produk.insert("", "end", text=jenis_produk, values=(produk.nama, produk.harga, jumlah, total_item))

        self.label_total_harga = ttk.Label(self, text=f"Total Harga: Rp{total_harga}")
        self.label_total_harga.pack(pady=10)

class AplikasiKasir(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Kasir")
        self.geometry("400x300")

        self.kasir = Kasir()

        self.label_produk = ttk.Label(self, text="Daftar Produk")
        self.label_produk.pack(pady=10)

        self.tree_produk = ttk.Treeview(self, columns=("Nama", "Harga", "Jumlah"))
        self.tree_produk.heading("#0", text="Jenis")
        self.tree_produk.heading("Nama", text="Nama")
        self.tree_produk.heading("Harga", text="Harga")
        self.tree_produk.heading("Jumlah", text="Jumlah")

        self.tree_produk.pack(padx=10, pady=10)

        self.tambah_produk_awal()

        self.label_total_harga = ttk.Label(self, text="Total Harga: Rp0")
        self.label_total_harga.pack(pady=10)

        self.button_tambah_produk = ttk.Button(self, text="Tambah Produk", command=self.tambah_produk)
        self.button_tambah_produk.pack(pady=5)

        self.button_kurangi_produk = ttk.Button(self, text="Kurangi Produk", command=self.kurangi_produk)
        self.button_kurangi_produk.pack(pady=5)

        self.button_proses_pembelian = ttk.Button(self, text="Proses Pembelian", command=self.proses_pembelian)
        self.button_proses_pembelian.pack(pady=10)

    def tambah_produk_awal(self):
        makanan1 = Makanan("Nasi Goreng", 15000, "Makanan Ringan")
        minuman1 = Minuman("Es Teh", 5000, 300)

        self.kasir.tambah_produk(makanan1)
        self.kasir.tambah_produk(minuman1)

        for produk in self.kasir.daftar_produk:
            self.tree_produk.insert("", "end", text=type(produk).__name__, values=(produk.nama, produk.harga, 0))

    def tambah_produk(self):
        selected_item = self.tree_produk.selection()
        if selected_item:
            index = int(selected_item[0][1:]) - 1
            self.kasir.tambah_jumlah_produk(index)
            self.update_tree_produk()

    def kurangi_produk(self):
        selected_item = self.tree_produk.selection()
        if selected_item:
            index = int(selected_item[0][1:]) - 1
            self.kasir.kurangi_jumlah_produk(index)
            self.update_tree_produk()

    def update_tree_produk(self):
        for idx, produk in enumerate(self.kasir.daftar_produk):
            self.tree_produk.item(f"#0{idx+1}", values=(produk.nama, produk.harga, produk.jumlah))

    def proses_pembelian(self):
        transaksi = self.kasir.proses_pembelian()
        if transaksi:
            StrukPembelian(self, transaksi)
            self.kasir.reset_jumlah_produk()
            self.update_tree_produk()
            self.label_total_harga.config(text="Total Harga: Rp0")

class Kasir:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def tambah_jumlah_produk(self, index):
        self.daftar_produk[index].jumlah += 1

    def kurangi_jumlah_produk(self, index):
        if self.daftar_produk[index].jumlah > 0:
            self.daftar_produk[index].jumlah -= 1

    def proses_pembelian(self):
        transaksi = [(type(produk).__name__, produk, produk.jumlah) for produk in self.daftar_produk if produk.jumlah > 0]
        return transaksi

    def reset_jumlah_produk(self):
        for produk in self.daftar_produk:
            produk.jumlah = 0

if __name__ == "__main__":
    app = AplikasiKasir()
    app.mainloop()
