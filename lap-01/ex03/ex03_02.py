def dao_nguoc_list(lst):
    """Đảo ngược một danh sách.

    Args:
        lst (list): Danh sách cần đảo ngược.

    Returns:
        list: Danh sách đã được đảo ngược.
    """
    return lst[::-1]

# Nhập danh sách từ người dùng và xử lý chuỗi (loại bỏ khoảng trắng)
input_list = input("Nhập danh sách các phần tử, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, [s.strip() for s in input_list.split(',') if s.strip() != '']))

# Sử dụng hàm và in kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược:", list_dao_nguoc)
