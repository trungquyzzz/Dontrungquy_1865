#ham kiem tra so nhi phan co chia het cho 5 hay khong
def kiem_tra_so_nhi_phan(so_nhi_phan):
    #chuyen so nhi phan sang thap phan
    so_thap_phan = int(so_nhi_phan, 2)
    #kiem tra so thap phan co chia het cho 5 hay khong
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
#nhap so nhi phan tu nguoi dung
so_nhi_phan = input("Nhap so nhi phan(phan cach boi dau phay): ")
#tach chuoi thanh cac so nhi phan va kiem tra tung so chia het cho 5
ds_so_nhi_phan = so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in ds_so_nhi_phan if kiem_tra_so_nhi_phan(so)]
#in ket qua
if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Cac so nhi phan chia het cho 5 la:", ket_qua)
else:
    print("Khong co so nhi phan nao chia het cho 5.")