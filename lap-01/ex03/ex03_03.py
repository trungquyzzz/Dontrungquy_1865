def tao_tuple_tu_list(lst):
    """Chuyển đổi một tuple thành một list.

    Args:
        lst (tuple): Tuple cần chuyển đổi.

    Returns:
        list: List sau khi chuyển đổi từ tuple.
    """
    return list(lst)
input_list = input("Nhập danh sách các phần tử, cách nhau bởi dấu phẩy: ")
numbers = list (map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("list:", numbers)
print("tuple tu list:", my_tuple)
