# Đọc dãy số từ file
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return list(map(int, data.split()))

# Ghi dãy số vào file
def write_numbers_to_file(file_path, numbers):
    with open(file_path, 'w') as file:
        file.write(' '.join(map(str, numbers)))

# Thực hiện đổi chỗ phần tử lớn nhất và nhỏ nhất, sau đó sắp xếp
def swap_max_min_and_save(input_file, output_file):
    # Đọc dãy số từ file input
    numbers = read_numbers_from_file(input_file)

    # Tìm chỉ số của phần tử lớn nhất và nhỏ nhất đầu tiên
    max_index = numbers.index(max(numbers))
    min_index = numbers.index(min(numbers))

    # Đổi chỗ phần tử lớn nhất và nhỏ nhất
    numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

    # Sắp xếp dãy số
    numbers.sort()

    # Ghi dãy mới vào file output
    write_numbers_to_file(output_file, numbers)

# Đường dẫn file
input_file = r'D:/Documents/DHCNDA/Python/Class/TH04/TH04BT_BinhHP/dayso1_bai17.txt'        # File chứa dãy số ban đầu
output_file = r'D:/Documents/DHCNDA/Python/Class/TH04/TH04BT_BinhHP/dayso2_bai17.txt'  # File chứa dãy số sau khi đổi chỗ và sắp xếp

# Thực thi
swap_max_min_and_save(input_file, output_file)
print(f"Dãy mới đã được lưu vào {output_file}")
