from qlsinhvien import QLSinhVien
qlsv=QLSinhVien()
while(1==1):
    print("-----Quan ly sinh vien-----")
    print("1. Nhap sinh vien")
    print("2. Hien thi danh sach sinh vien")
    print("3. Cap nhat thong tin sinh vien")
    print("4. Sap xep sinh vien theo id")
    print("5. Sap xep sinh vien theo ten")
    print("6. Sap xep sinh vien theo diem trung binh")
    print("7. Tim kiem sinh vien theo id")
    print("8. Tim kiem sinh vien theo ten")
    print("9. Thoat chuong trinh")
    choice = input("Nhap lua chon cua ban: ")
    if (choice == '1'):
        qlsv.nhapsinhvien()
    elif (choice == '2'):
        qlsv.hienthisinhvien()
    elif (choice == '3'):
        id = int(input("Nhap id sinh vien can cap nhat: "))
        qlsv.updatesinhvien(id)
    elif (choice == '4'):
        qlsv.sortbyid()
    elif (choice == '5'):
        qlsv.sortbyname()
    elif (choice == '6'):
        qlsv.sortbydiemtb()
    elif (choice == '7'):
        id = int(input("Nhap id sinh vien can tim kiem: "))
        sv = qlsv.findbyid(id)
        if (sv != None):
            print(sv)
        else:
            print("Khong tim thay sinh vien co id =", id)
    elif (choice == '8'):
        keyword = input("Nhap ten hoac chuoi can tim kiem: ")
        listsv = qlsv.findbyname(keyword)
        if (len(listsv) > 0):
            for sv in listsv:
                print(sv)
        else:
            print("Khong tim thay sinh vien voi tu khoa:", keyword)
    elif (choice == '9'):
        break
    else:
        print("Lua chon khong hop le, vui long chon lai!")