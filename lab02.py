#Nama       = Muhammad Rifqi Adli Gumay
#NPM        = 2106752224
#Kelas      = DDP 1G
print("Selamat datang di kalkulator IPK!")
mutu_ipk = 0
mutu_ipt = 0
total_sks_ipk = 0
total_sks_ipt = 0 
'''
membuat pengulangan apabila masukan salah dan tidak mengambil matkul jika masukan bernilai 0 
dan berhenti apabila masukan > 0
'''
while True:
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
    if (jumlah_matkul < 0):
        print("Nilai yang kamu masukkan tidak valid")
    elif(jumlah_matkul > 0):
        break
    else:
        print("Tidak ada mata kuliah yang diambil")

print()
#Membuat conditional kasus jumlah_matkul > 0
if (jumlah_matkul > 0 ):
    for i in range (1,jumlah_matkul+1):
        nama_matkul = str(input("Masukkan nama mata kuliah ke %d: " %i))
        a = "Masukkan jumlah sks "+(nama_matkul)+": "
        sks_matkul = int(input(a))
        while True: #Sama seperti tadi, membuat pengulangan apabila masukan < 0 dan berhenti ketika >= 0
            nilai_matkul = float(input("Masukkan nilai yang kamu dapatkan: "))
            if (nilai_matkul<0):
                print("Nilai yang kamu masukkan tidak valid")
            else:
                break
        if(0 <= nilai_matkul < 40):         #melakukan conditional saat 0 <= nilai_matkul < 40
            nilai = sks_matkul*0.00
            mutu_ipt += nilai
            total_sks_ipt += sks_matkul
        elif(40 <= nilai_matkul < 55):      #melakukan conditional saat 40 <= nilai_matkul < 55
            nilai = sks_matkul*1.00
            mutu_ipt += nilai
            total_sks_ipt += sks_matkul
        elif(55 <= nilai_matkul < 60):      #melakukan conditional saat 55 <= nilai_matkul < 60
            nilai = sks_matkul*2.00
            mutu_ipt += nilai
            mutu_ipk += nilai
            total_sks_ipt += sks_matkul
            total_sks_ipk += sks_matkul
        elif(60 <= nilai_matkul < 65):      #melakukan conditional saat 60 <= nilai_matkul < 65    
            nilai = sks_matkul*2.30
            mutu_ipt += nilai
            mutu_ipk += nilai
            total_sks_ipt += sks_matkul
            total_sks_ipk += sks_matkul
        elif(65 <= nilai_matkul < 70):      #melakukan conditional saat 65 <= nilai_matkul < 70
            nilai = sks_matkul*2.70
            mutu_ipt += nilai
            mutu_ipk += nilai
            total_sks_ipt += sks_matkul
            total_sks_ipk += sks_matkul
        elif(70 <= nilai_matkul < 75):      #melakukan conditional saat 70 <= nilai_matkul < 75
            nilai = sks_matkul*3.00
            mutu_ipt += nilai
            mutu_ipk += nilai
            total_sks_ipt += sks_matkul
            total_sks_ipk += sks_matkul
        elif(75 <= nilai_matkul < 80):      #melakukan conditional saat 75 <= nilai_matkul < 80
            nilai = sks_matkul*3.30
            mutu_ipt += nilai
            mutu_ipk += nilai
            total_sks_ipt += sks_matkul
            total_sks_ipk += sks_matkul
        elif(80 <= nilai_matkul < 85):      #melakukan conditional saat 80 <= nilai_matkul < 85
            nilai = sks_matkul*3.70
            mutu_ipt += nilai
            mutu_ipk += nilai
            total_sks_ipt += sks_matkul
            total_sks_ipk += sks_matkul
        elif(nilai_matkul >= 85):           #melakukan conditional saat 80 nilai_matkul >= 85
            nilai = sks_matkul*4.00
            mutu_ipt += nilai
            mutu_ipk += nilai
            total_sks_ipt += sks_matkul
            total_sks_ipk += sks_matkul
        
        '''
        Agar tidak terjadi division zero by zero, maka diperlukan conditional case khusus
        '''
        if (mutu_ipk == 0 ):            
            nilai_ipk = 0.00
        else: 
            nilai_ipk = (mutu_ipk)/(total_sks_ipk)
        
 
#determine rumus nilai ipt dan sks lulus
nilai_ipt = (mutu_ipt)/(total_sks_ipt)
sks_lulus = (total_sks_ipk)/(total_sks_ipt)

#mencetak hasil sks lulus, mutu lulus, total ipak, total ipt
print("Jumlah SKS lulus: ",(total_sks_ipk),"/",(total_sks_ipt))
print("Jumlah mutu lulus: ","{:.2f}".format(mutu_ipk),"/","{:.2f}".format(mutu_ipt))
print("Total IPK kamu adalah ","{:.2f}".format(nilai_ipk))
print("Total IPT kamu adalah ","{:.2f}".format(nilai_ipt))
        

        



        

       
        
