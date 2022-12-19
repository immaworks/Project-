listBarang = {
    'tkn01': {
        'Nama Barang': 'Biskuat',
        'Stock' : 100,
        'Jenis': 'Makanan',
        'Harga Satuan' : 10000
    },

    'tkn02':{
        'Nama Barang': 'Indomie',
        'Stock' : 100,
        'Jenis': 'Sembako',
        'Harga Satuan' : 15000
    },

    'tkn03':{
        'Kode Barang' : 'tkn03', 
        'Nama Barang': 'Pop ice',
        'Stock' : 100,
        'Jenis': 'Minuman',
        'Harga Satuan' : 5000
    },

    'tkn04':{
        'Kode Barang' : 'tkn04', 
        'Nama Barang': 'Biskuat',
        'Stock' : 100,
        'Jenis': 'Makanan',
        'Harga Satuan' : 12000
    },

    'tkn05':{
        'Kode Barang' : 'tkn05', 
        'Nama Barang': 'Aqua Gelas',
        'Stock' : 100,
        'Jenis': 'Minuman',
        'Harga Satuan' : 1000
    }
}

#menampilkan data
def dataToko() :
    menu1 = int(input('''
        
        ==================== Toko Kelontong Namiya ====================

        1. Tampilkan seluruh barang
        2. Cari barang berdasarkan Kode
        3. Kembali ke menu utama
        Masukkan Sub menu yang ingin dijalankan [1-3] : '''))
    if menu1 == 1 :
        print('''

            ==================== Daftar Barang Toko Kelontong Namiya ====================

        KODE BARANG\t| NAMA BARANG\t| STOCK\t\t| JENIS\t \t| HARGA SATUAN ''')

        for i in listBarang:
            print(f"\t{i}\t\t| {listBarang[i]['Nama Barang']}\t| {listBarang[i]['Stock']}\t\t| {listBarang[i]['Jenis']}\t| {listBarang[i]['Harga Satuan']}")
        if len(listBarang)==0:
            print('\n*************** Data Masih Kosong ***************\n ')
        else:
            dataToko()

    elif menu1 == 2 :
            print(' \n==================== Cari Barang ===================\n')
            cari = input('Masukkan kode barang yang ingin dicari: ')
            if cari in listBarang:
                print('\nKODE BARANG\t| NAMA BARANG\t| STOCK\t\t| JENIS\t \t| HARGA SATUAN')
                print(f"\t{cari}\t| {listBarang[cari]['Nama Barang']}\t| {listBarang[cari]['Stock']}\t\t| {listBarang[cari]['Jenis']}\t| {listBarang[cari]['Harga Satuan']}")
                dataToko()
            if cari not in listBarang :
                print ('\n=*************** data barang tidak dapat ditemukan ***************\n')
                dataToko()
    elif menu1 == 3 :
        menu()
    else :
        dataToko()

#menambah data 
def tambahToko():
    menu2 = int(input('''

        \n==================== Tambah Daftar Barang ====================\n
        1. Tambah Data Barang
        2. Kembali ke menu utama
        
        Masukkan Sub menu yang ingin dijalankan [1-2] : '''))

    while True:
        if menu2 == 1 :
            kode = input('Masukkan Kode Barang : ')
            for i in listBarang:
                if kode in listBarang :
                    print('\n=*************** Kode Barang sudah ada ***************\n')
                    tambahToko()
            nama = input('Masukkan Nama Barang : ')
            stock = input('Masukkan jumlah stock Barang : ')
            jenis = input('Masukkan jenis Barang : ')
            harga = input('Masukkan harga Barang : ')
            while True:
                ask = input('Apakah data yang anda masukan telah benar (y/t) :').lower()
                if (ask == 'y'):
                    listBarang.update({
                        kode:{
                            'Nama Barang': nama,
                            'Stock' : stock,
                            'Jenis': jenis,
                            'Harga Satuan' : harga
                        }})
                    print('\n*************** Data tersimpan ***************\n')
                    tambahToko()
                elif (ask == 't'):
                    tambahToko()
        elif menu2 == 2 :
            menu()
            break
        else :
            dataToko()

# mengubah data 
def editToko():  
    while True:
        menu3 = int(input('''
            
            \n==================== Mengubah Data Barang ====================\n
                1. Ubah nama barang
                2. Kembali ke menu utama
                Masukkan Sub menu yang ingin dijalankan [1-2] :  '''))

        if menu3 == 1 :
            kode = input('Masukkan kode barang yang ingin di ubah: ')
            if kode not in listBarang:
                print('\n*************** Kode yang anda masukkan tidak tersedia. Silakan coba lagi ***************\n')
                editToko()
            nama = input('Masukkan Nama Barang : ')
            stock = input('Masukkan jumlah stock Barang : ')
            jenis = input('Masukkan jenis Barang : ')
            harga = input('Masukkan harga Barang : ')
            ask = input('Apakah data yang anda masukan telah benar (y/t) :').lower()
            if (ask == 'y'):
                listBarang.update({
                    kode:{
                    'Nama Barang': nama,
                    'Stock' : stock,
                    'Jenis': jenis,
                    'Harga Satuan' : harga}})
                print('\n*************** Data tersimpan ***************\n')
            elif (ask == 't'):
                editToko()
        elif menu3 == 2 :
            menu()
            break
        else :
            editToko()

                        


#menghapus data
def hapusToko():
    menu4 = int(input('''
        ==================== Menghapus Data Barang ====================\n
        1. Hapus Data Barang
        2. Kembali ke menu utama
        Masukkan Sub menu yang ingin dijalankan [1-2] : '''))
    if menu4 == 1 :
        print ('\n=========== hapus data barang ===========\n')
        hapus = input('masukkan kode barang yang ingin dihapus: ')
        if hapus in listBarang:
            ask = input('Apakah anda yakin ingin menghapus data? (y/t) :').lower()
            if ask == 'y':
                del listBarang[hapus]
                print('\n*************** data berhasil dihapus ***************\n')
                menu()
            elif (ask == 't'):
                hapusToko()
            else:
                ask = input ('apakah anda yakin ingin menghapus data? [y/t]? ').lower()
        else:
            print ('\n*************** data barang tidak ditemukan ***************\n')
            hapusToko()
    elif menu4 == 2:
        menu()
    else:
        hapusToko()


#menampilkan menu
def menu(): 
    while True:
        pil = int(input( '''
        \n========== SELAMAT DATANG DI TOKO KELONTONG NAMIYA ===============\n
        Menu :
        1. Tampilkan Daftar Barang
        2. Tambah Daftar Barang
        3. Ubah Data Barang
        4. Hapus Data Barang
        5. Exit 
        
        Masukkan Menu yang ingin dijalankan [1-5] :  '''))

        if pil == 1 :
            dataToko()
            break
        elif pil == 2 :
            tambahToko()
            break
        elif pil == 3 :
            editToko()
            break
        elif pil == 4 :
            hapusToko()
            break
        elif pil == 5 :
            print ('\n\t=============== Thankyou, have a nice day! ===============\n ')
            break
        else :
            print('\n*************** Pilihan yang anda masukkan salah! ***************\n')
menu()