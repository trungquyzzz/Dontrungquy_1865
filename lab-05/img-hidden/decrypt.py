import sys
from PIL import Image

def decode_image(encoded_image_path):
    # Mở hình ảnh đã mã hóa
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    # Trích xuất bit cuối cùng (LSB) từ mỗi kênh màu của từng pixel
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            for color_channel in range(3): # Duyệt qua các kênh R, G, B
                # Lấy bit cuối cùng của giá trị màu và thêm vào chuỗi nhị phân
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Giải mã chuỗi nhị phân thành ký tự văn bản
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        
        if char == '\0':  # Kết thúc thông điệp khi gặp ký tự null '\0'
            break
        message += char

    return message

def main():
    # Kiểm tra tham số dòng lệnh
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()