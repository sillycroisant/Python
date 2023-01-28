import random

surname = ["Nguyễn", "Trần", "Lê", "Phạm", "Võ", "Mai", "Hoàng", "Huỳnh", "Đỗ", 
           "Vũ", "Lưu", "Đặng", "Phan", "Bùi", "Trương", "Ngô", "Hồ", "Dương", "Đinh"]

male_name = ["An", "Anh", "Bảo", "Bắc", "Chính", "Dương", "Duy", "Dũng", "Đạt", "Đôn", "Giang", "Hải", "Hậu", "Hiền", "Huy", "Hoàng", "Hiếu", "Khoa", 
             "Kha", "Khôi", "Khang", "Long", "Phụng", "Phúc", "Ý", "Minh", "Trọng", "Nhàn", "Cảnh", "Vĩnh", "Ân", "Hưng", "Lân", "Quý", "Tình", "Thiên",
             "Zôn", "Trực", "Lộc", "Nguyên", "Nhật", "Phát", "Phi", "Tài", "Thái", "Toàn", "Thông", "Tuấn", "Tuân", "Thịnh", "Triều", "Sơn", "Vũ", "Vĩ"]

female_name = ["Anh", "Ánh", "Châu", "Duyên", "Giang", "Hà", "Hạnh", "Hằng", "Hân", "Khánh", "Linh", "Lan", "Lam", "Ly", "Loan", "Mai", "My", "Ngân",
               "Nhã", "Ngọc", "Nguyên", "Nhi", "Pha", "Quỳnh", "Thảo", "Thư", "Thy", "Trang", "Trâm", "Trân", "Thanh", "Tâm", "Tiên", "Tường",
               "Vân", "Vi", "Xinh", "Uyên", "Phụng", "Ý", "Tuyết", "Yến", "Phương", "Dung", "Cúc","Huệ", "Phượng", "Thúy" ]

gender = input("Chọn giới tính (male/female)").upper()
num = int(input("Chọn số lượng tên : "))
    

if gender == "MALE" or gender == 'M':
    name = male_name
else:
    name = female_name
    
for i in range(num):
    print('{} {}'.format(random.choice(surname),random.choice(name)))