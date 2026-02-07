def dao_nguoc_list(lst):
    """Đảo ngược một danh sách.

    Args:
        lst (list): Danh sách cần đảo ngược.

    Returns:
        list: Danh sách đã được đảo ngược.
    """
    return lst[::-1]
#nhap danh sach tu  nguoi dung va xu ly chuoi
input_list = input("Nhập danh sách các phần tử, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
#su dung ham va in ket qua
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược:", list_dao_nguoc)
