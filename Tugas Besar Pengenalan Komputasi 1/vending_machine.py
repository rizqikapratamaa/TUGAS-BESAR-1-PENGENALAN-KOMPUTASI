# TUGAS BESAR 1 PENGENALAN KOMPUTASI
# PROGRAM VENDING MACHINE

# KELOMPOK 4
# Jason Fernando (19622254)
# Rizqika Mulia Pratama (19622258)
# Alfaza Naufal Zakiy (19622264)
# Chelvadinda (19622276)

# Deskripsi:
# Membuat program vending machine dengan fitur:
# 1. Meminta memasukkan uang
# 2. Memilih menu dan jumlahnya
# 3. Mengecek apakah saldo kurang atau tidak
# 4. Menampilkan menu dan kembaliannya
# 5. Menawarkan tambahan menu?

# KAMUS

# ALGORITMA
def main():
  print("=======================")
  print("VENDING MACHINE DARMAJI")
  print("=======================")
  saldo = int(input("Masukkan sejumlah uang: "))
  
def kategori():
  print("Pilih kategori:")
  print("1. Makanan")
  print("2. Minuman")
  pil_kategori = int(input("Masukkan nomor kategori: "))
  if pil_kategori == 1:
    clear
    return makanan()
  elif pil_kategori == 2:
    clear
    return minuman()
  else:
    clear
    print("Pilihan kategori tidak tersedia, silahkan masukkan ulang")
    return main()
  
  def makanan():
    print()
    
  def minuman():
    print()
    
