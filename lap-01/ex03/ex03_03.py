def tao_tuple_tu_list(lst):
    """Chuyển đổi một list thành một tuple.

    Args:
        lst (list): List cần chuyển đổi.

    Returns:
        tuple: Tuple sau khi chuyển đổi từ list.
    """
    return tuple(lst)


if __name__ == "__main__":
    input_list = input("Nhập danh sách các phần tử, cách nhau bởi dấu phẩy: ")
    # Loại bỏ khoảng trắng và các phần tử rỗng
    items = [s.strip() for s in input_list.split(',') if s.strip() != '']
    try:
        numbers = list(map(int, items))
    except ValueError:
        # Nếu không chuyển được sang int, giữ nguyên dưới dạng chuỗi
        numbers = items

    my_tuple = tao_tuple_tu_list(numbers)
    print("list:", numbers)
    print("tuple từ list:", my_tuple)
