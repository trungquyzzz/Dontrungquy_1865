from SInhVien import SinhVien

class QLSinhVien:
    listSV = []
    def generateid(self):
        maxid = 1
        if (self.soluongsv() > 0):
            maxid = self.listSV[0].id
            for sv in self.listSV:
                if (sv.id > maxid):
                    maxid = sv.id
            maxid += 1
        return maxid
    
    def soluongsv(self):
        return self.listSV.__len__()
    
    def nhapsinhvien(self):
        id = self.generateid()
        name = input("Nhap ho va ten sinh vien: ")
        sex= input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh sinh vien: ")
        diemtb = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(id, name, sex, major, diemtb)
        self.xeploaihocluc(sv)
        self.listSV.append(sv)

    def updatesinhvien(self, id):
        sv: SinhVien = self.findbyid(id)
        if (sv != None):
            name = input("Nhap ho va ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh sinh vien: ")
            diemtb = float(input("Nhap diem trung binh sinh vien: "))
            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.diemtb = diemtb
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemtb = diemtb
            self.xeploaihocluc(sv)
        else:
            print("sinh vien co id =", id, " khong ton tai")

    def sortbyid(self):
        self.listSV.sort(key=lambda x: x.id, reverse=False)

    def sortbyname(self):
        self.listSV.sort(key=lambda x: x.name, reverse=False)

    def sortbydiemtb(self):
        self.listSV.sort(key=lambda x: x.diemtb, reverse=True)
            
    def findbyid(self, id):
        searchresult = None
        if (self.soluongsv() > 0):
            for sv in self.listSV:
                if (sv.id == id):
                    searchresult = sv
        return searchresult

    def findbyname(self, keyword):
        listsv = []
        if (self.soluongsv() > 0):
            for sv in self.listSV:
                if (keyword.upper() in sv.name.upper()):
                    listsv.append(sv)
        return listsv

    def deletebyid(self, id):
        isdeleted = False
        sv = self.findbyid(id)
        if (sv != None):
            self.listSV.remove(sv)
            isdeleted = True
        return isdeleted
    def xeploaihocluc(self, sv:SinhVien):
        if (sv.diemtb < 5):
            sv.hocluc = "Yeu"
        elif (sv.diemtb >= 5 and sv.diemtb < 6.5):
            sv.hocluc = "Trung Binh"
        elif (sv.diemtb >= 6.5 and sv.diemtb < 7.5):
            sv.hocluc = "Kha"
        elif (sv.diemtb >= 7.5 and sv.diemtb < 9):
            sv.hocluc = "Gioi"
        else:
            sv.hocluc = "Xuat Sac"

    def showsinhvien(self, listSV):
        print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10}".format("ID", "Ho va Ten", "Gioi Tinh", "Chuyen Nganh", "Diem TB", "Hoc Luc"))
        if (len(listSV) > 0):
            for sv in listSV:
                print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10}".format(sv.id, sv.name, sv.sex, sv.major, sv.diemtb, sv.hocluc))
            print("\n")

    def hienthisinhvien(self):
        self.showsinhvien(self.listSV)

    def getlistsv(self):
        return self.listSV
    

