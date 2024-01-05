class stock :
    def __init__(self,nama,harga):
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama} - Rp{self.harga}"
    
class alatTulis(stock):
    def __init__(self, nama, harga,jenis):
        super().__init__(nama, harga)
        self.jenis = jenis

    def info(self):
        return f"{super().info()} ({self.jenis})"
    
class Buku(stock):
    def __init__(self, nama, harga,tipe):
        super().__init__(nama, harga)
        self.tipe = tipe

    def info(self):
        return f"{super().info()} ({self.tipe})"
    
class Kasir:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self,produk):
        self.daftar_produk.append(produk)

    def tampil_produk(self):
        print("Daftar Produk : ")
        for idX, stock in enumerate(self.daftar_produk, start=1):
            print(f"{idX} . {stock.tampil_produk()}")

    def pembelian(self,pilih_produk, jumlah):
        total_harga = self.daftar_produk[pilih_produk - 1].harga*jumlah
        print(f"Total Harga : Rp[total_harga]")

if __name__== "__main__":
    kasir = Kasir()

    alattulis = alatTulis("pupen Faster",2500,"Pulpen Faster G300")
    buku = Buku("Sang Pemimpi",100000,"Novel")

    kasir.tambah_produk(alattulis)
    kasir.tambah_produk(buku)

    kasir.tampil_produk()

    pilih_produk = int(input("Pilih Produk (Masukan Nomor Produk): "))
    jumlah = int(input("Jumlah Pembelian : "))

    kasir.pembelian(pilih_produk, jumlah)

