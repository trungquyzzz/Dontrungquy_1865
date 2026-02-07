def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
#su dung ham va in ket qua
input_string = input("Nhap vao mot chuoi can dao nguoc: ")
print("Chuoi sau khi dao nguoc la:", dao_nguoc_chuoi(input_string))
