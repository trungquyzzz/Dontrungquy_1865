so_gio_lam=float(input("Nhập số giờ làm moi tuan: "))
tien_luong_gio=float(input("Nhập tiền lương mỗi giờ: "))
gio_tieu_chuan=40
gio_vuot_chuan= max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh= gio_tieu_chuan * tien_luong_gio + gio_vuot_chuan * tien_luong_gio * 1.5
print("Thực lĩnh của công nhân là: ", thuc_linh)
# Tính lương công nhân với giờ làm tiêu chuẩn và giờ làm vượt chuẩn