
listPasien = [
    {'no_reg' : 10021, 'nama': 'Anita', 'asal' : 'Ambon', 'jenis': 'BPJS'},
    {'no_reg' : 10034, 'nama': 'Bimo ', 'asal' : 'Jambi', 'jenis': 'UMUM'},
    {'no_reg' : 10023, 'nama': 'Ratna', 'asal' : 'Bali', 'jenis':'UMUM'}
]

#menampilkan data
def show_data () :
    menu1 = int(input('''
        \n+++++++++++++++ Report Data Pasien +++++++++++++++\n

        1. Report Seluruh Data
        2. Report Data Terbaru
        3. Kembali ke menu utama

        Masukkan Sub menu yang ingin dijalankan [1-3] : '''))
    if menu1 == 1 :
        print('\n\t\t*** Daftar Pasien ***\n')
        print('no_reg\t| nama Pasien \t| asal Kota \t| jenis Pembiayaan')
        for i in range(len(listPasien)): 
            print (listPasien[i]['no_reg'],'\t|', listPasien[i]['nama'],'\t|', listPasien[i]['asal'],'\t|', listPasien[i]['jenis'])
        if len(listPasien)==0:
            print('Data Masih Kosong')
        else:
            show_data()
    elif menu1 == 2 :
        print(' === cari data pasien ===')
        cari = input('Masukkan no.registrasi pasien yang dicari: ')
        for cari in listPasien:
            print('Data Pasien:', listPasien.get('no_reg', 0))
            count=1
        if count == 0 :
            print (' data pasien tidak ditemukan')
            show_data()
    elif menu1 == 3 :
        menu()
    else :
        show_data()

#menambah data
def insert_data():
    menu2 = int(input('''
        \n+++++++++++++++ Menambah Data Pasien +++++++++++++++\n

        1. Tambah Data Pasien
        2. Kembali ke menu utama
        
        Masukkan Sub menu yang ingin dijalankan [1-2] : '''))
    if menu2 == 1 :
        no_reg = int(input('Masukkan Nomor Registrasi : '))
        nama = input('Masukkan Nama Pasien : ')
        n = nama.capitalize()
        Asal = input('Masukkan Kota Asal : ')
        a = Asal.capitalize()
        jenis = input('Masukkan jenis pembiayaan: ')
        j = jenis.upper()
        listPasien.append({
            'no_reg': no_reg,
            'nama': nama,
            'asal': Asal,
            'jenis' : jenis}) 
        save1 = input('Apakah data akan disimpan? (y/n) : ')
        save = save1.lower()
        if save == 'y' :
            print('== Data berhasil disimpan ==')  
            insert_data()
        elif save == 'n' :
            insert_data()
        else :
            print(save1)


        if n == '':
            print('*** data tidak boleh kosong! ***')
            insert_data()

            menu()
        elif a == '':
            print('*** data tidak boleh kosong! ***')
            insert_data()

        elif j == '':
            print('*** data tidak boleh kosong! ***')
            insert_data()

    elif menu2 == 2:
        menu()
    else :
        insert_data()

#mengedit data
def edit_data():  
    menu3 = int(input('''
        \n+++++++++++++++ Mengubah Data Pasien +++++++++++++++\n

        1. Ubah Data Pasien
        2. Kembali ke menu utama

        Masukkan Sub menu yang ingin dijalankan [1-3] :  '''))
    if menu3 ==1 :
        print ('update data pasien')
        upd = input('masukkan no.registrasi pasien yang ingin di ubah: ')
        upd1 = upd.capitalize()
        nbl = input('nama : ')
        nb = nbl.capitalize()
        jbl = input('asal kota: ')
        jb = jbl.capitalize()
        jn1 = input('jenis pembiayaan: ')
        jn = jn1.upper()

        listPasien.update({'no_reg': upd1})
        listPasien.update({'Nama': nb})
        listPasien.update({'Asal': jb})
        listPasien.update({'jenis ': jn})
        print()
        if count == 0:
            print (' === data pasien tidak ditemukan ==')
            edit_data()
    elif menu3 == 2 :
        menu()
    else :
        insert_data()


#menghapus data
def delete_data():
    menu4 = int(input('''
        \n+++++++++++++++ Menghapus Data Pasien +++++++++++++++\n

        1. Hapus Data Pasien
        2. Kembali ke menu utama

        Masukkan Sub menu yang ingin dijalankan [1-2] : '''))
    if menu4 == 1 :
        print ('=== hapus data pasien ===')
        nhl = input('masukkan nama pasien yang ingin dihapus: ')
        nh = nhl.capitalize
        listPasien.pop(nh)

        d = 0
        for i in isi:
            if nh in i:
                print('\n'+i)
                askl = input ('apakah anda yakin [y/n]? ')
                ask = askl.lower()
                if ask == 'y':
                    print(hapus = nh.remove(isi, i))
                print('== data berhasil dihapus ==')
                delete_data()
                d=1
        if d == 0 :
            print ('== data pasien tidak ditemukan ==')
            delete_data()
    elif menu4 == 2 :
        menu()
    else :
        insert_data()


#menampilkan menu
def menu():
    print('''
        \n========== Database Rumah Sakit Purwadhika ===============\n

        Menu :
        1. Tampilkan Daftar Pasien
        2. Tambah Daftar Pasien
        3. Ubah Data Pasien
        4. Hapus Data Pasien
        5. Exit ''')
    pil = int(input('Masukkan Menu yang ingin dijalankan [1-5] : '))
    pilih(pil)

def pilih (p):
    if p == 1 :
        show_data()
    if p == 2 :
        insert_data()
    if p == 3 :
        edit_data()
    if p == 4 :
        delete_data()
    elif p == 5:
       print ('\n\t=============== Thankyou, have a nice day! ===============\n ')
    else:
        print('\n\t*************** Pilihan yang anda masukkan salah! ***************\n ')
        menu()


menu()
