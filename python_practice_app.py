#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ứng dụng thực hành Python cơ bản
Bao gồm các bài tập về biến, toán tử, điều kiện, vòng lặp, hàm, cấu trúc dữ liệu và OOP
"""

import random
import json
import os
from datetime import datetime

class Student:
    def __init__(self, name, age, scores=None):
        self.name = name
        self.age = age
        self.scores = scores or []
    
    def add_score(self, score):
        self.scores.append(score)
    
    def get_average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0
    
    def info(self):
        return f"Tên: {self.name}, Tuổi: {self.age}, Điểm TB: {self.get_average():.1f}"

class PythonPracticeApp:
    def __init__(self):
        self.students = []
        self.data_file = "students_data.json"
        self.load_data()
    
    def save_data(self):
        data = []
        for student in self.students:
            data.append({
                "name": student.name,
                "age": student.age,
                "scores": student.scores
            })
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data:
                        student = Student(item["name"], item["age"], item["scores"])
                        self.students.append(student)
            except:
                pass
    
    def practice_variables_datatypes(self):
        print("\n=== BÀI TẬP 1: BIẾN VÀ KIỂU DỮ LIỆU ===")
        
        # Input từ user
        name = input("Nhập tên của bạn: ")
        age = int(input("Nhập tuổi: "))
        height = float(input("Nhập chiều cao (m): "))
        is_student = input("Bạn có phải học sinh không? (y/n): ").lower() == 'y'
        
        # Tạo list điểm số
        scores = []
        for i in range(3):
            score = float(input(f"Nhập điểm môn {i+1}: "))
            scores.append(score)
        
        # Tạo dictionary thông tin
        info = {
            "name": name,
            "age": age,
            "height": height,
            "is_student": is_student,
            "scores": scores
        }
        
        print(f"\nThông tin của bạn:")
        print(f"Tên: {info['name']} (kiểu: {type(info['name']).__name__})")
        print(f"Tuổi: {info['age']} (kiểu: {type(info['age']).__name__})")
        print(f"Chiều cao: {info['height']}m (kiểu: {type(info['height']).__name__})")
        print(f"Là học sinh: {info['is_student']} (kiểu: {type(info['is_student']).__name__})")
        print(f"Điểm số: {info['scores']} (kiểu: {type(info['scores']).__name__})")
    
    def practice_operators(self):
        print("\n=== BÀI TẬP 2: TOÁN TỬ ===")
        
        a = int(input("Nhập số thứ nhất: "))
        b = int(input("Nhập số thứ hai: "))
        
        print(f"\nKết quả các phép toán:")
        print(f"{a} + {b} = {a + b}")
        print(f"{a} - {b} = {a - b}")
        print(f"{a} * {b} = {a * b}")
        print(f"{a} / {b} = {a / b:.2f}")
        print(f"{a} // {b} = {a // b}")
        print(f"{a} % {b} = {a % b}")
        print(f"{a} ** {b} = {a ** b}")
        
        print(f"\nSo sánh:")
        print(f"{a} == {b}: {a == b}")
        print(f"{a} > {b}: {a > b}")
        print(f"{a} < {b}: {a < b}")
        
        print(f"\nLogic:")
        print(f"{a} > 0 and {b} > 0: {a > 0 and b > 0}")
        print(f"{a} > 0 or {b} > 0: {a > 0 or b > 0}")
    
    def practice_conditions(self):
        print("\n=== BÀI TẬP 3: CẤU TRÚC ĐIỀU KIỆN ===")
        
        score = float(input("Nhập điểm số (0-10): "))
        
        if score >= 9:
            grade = "Xuất sắc"
        elif score >= 8:
            grade = "Giỏi"
        elif score >= 6.5:
            grade = "Khá"
        elif score >= 5:
            grade = "Trung bình"
        else:
            grade = "Yếu"
        
        print(f"Điểm {score} xếp loại: {grade}")
        
        # Bài tập thêm
        year = int(input("Nhập năm để kiểm tra năm nhuận: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} là năm nhuận")
        else:
            print(f"{year} không phải năm nhuận")
    
    def practice_loops(self):
        print("\n=== BÀI TẬP 4: VÒNG LẶP ===")
        
        # For loop
        print("Bảng cửu chương 5:")
        for i in range(1, 11):
            print(f"5 x {i} = {5 * i}")
        
        # While loop - đoán số
        print("\nTrò chơi đoán số (1-10):")
        secret = random.randint(1, 10)
        attempts = 0
        
        while True:
            guess = int(input("Đoán số: "))
            attempts += 1
            
            if guess == secret:
                print(f"Chính xác! Bạn đoán đúng sau {attempts} lần thử.")
                break
            elif guess < secret:
                print("Số cần tìm lớn hơn!")
            else:
                print("Số cần tìm nhỏ hơn!")
    
    def practice_functions(self):
        print("\n=== BÀI TẬP 5: HÀM ===")
        
        def calculate_bmi(weight, height):
            return weight / (height ** 2)
        
        def bmi_category(bmi):
            if bmi < 18.5:
                return "Gầy"
            elif bmi < 25:
                return "Bình thường"
            elif bmi < 30:
                return "Thừa cân"
            else:
                return "Béo phì"
        
        def fibonacci(n):
            if n <= 1:
                return n
            return fibonacci(n-1) + fibonacci(n-2)
        
        weight = float(input("Nhập cân nặng (kg): "))
        height = float(input("Nhập chiều cao (m): "))
        
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        print(f"BMI của bạn: {bmi:.1f} - {category}")
        
        n = int(input("Nhập n để tính Fibonacci: "))
        print(f"Fibonacci({n}) = {fibonacci(n)}")
    
    def practice_data_structures(self):
        print("\n=== BÀI TẬP 6: CẤU TRÚC DỮ LIỆU ===")
        
        # List
        fruits = ["táo", "chuối", "cam"]
        print(f"Danh sách trái cây: {fruits}")
        
        new_fruit = input("Thêm trái cây mới: ")
        fruits.append(new_fruit)
        print(f"Sau khi thêm: {fruits}")
        
        # Dictionary
        student_scores = {}
        for i in range(3):
            name = input(f"Nhập tên học sinh {i+1}: ")
            score = float(input(f"Nhập điểm của {name}: "))
            student_scores[name] = score
        
        print("\nBảng điểm:")
        for name, score in student_scores.items():
            print(f"{name}: {score}")
        
        # Set
        numbers = [1, 2, 2, 3, 3, 4, 5]
        unique_numbers = set(numbers)
        print(f"Số ban đầu: {numbers}")
        print(f"Số không trùng: {list(unique_numbers)}")
        
        # Tuple
        coordinates = (10, 20)
        print(f"Tọa độ: {coordinates}")
    
    def practice_file_operations(self):
        print("\n=== BÀI TẬP 7: XỬ LÝ FILE ===")
        
        filename = "practice_notes.txt"
        
        # Ghi file
        note = input("Nhập ghi chú của bạn: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {note}\n")
        
        print(f"Đã lưu ghi chú vào {filename}")
        
        # Đọc file
        if os.path.exists(filename):
            print("\nNội dung file:")
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content)
    
    def practice_oop(self):
        print("\n=== BÀI TẬP 8: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG ===")
        
        name = input("Nhập tên học sinh: ")
        age = int(input("Nhập tuổi: "))
        
        student = Student(name, age)
        
        # Thêm điểm
        num_scores = int(input("Nhập số môn học: "))
        for i in range(num_scores):
            score = float(input(f"Nhập điểm môn {i+1}: "))
            student.add_score(score)
        
        print(f"\n{student.info()}")
        
        # Lưu vào danh sách
        self.students.append(student)
        self.save_data()
        print("Đã lưu thông tin học sinh!")
    
    def show_all_students(self):
        print("\n=== DANH SÁCH HỌC SINH ===")
        if not self.students:
            print("Chưa có học sinh nào.")
            return
        
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student.info()}")
    
    def run(self):
        while True:
            print("\n" + "="*50)
            print("🐍 ỨNG DỤNG THỰC HÀNH PYTHON CƠ BẢN")
            print("="*50)
            print("1. Biến và Kiểu dữ liệu")
            print("2. Toán tử")
            print("3. Cấu trúc điều kiện")
            print("4. Vòng lặp")
            print("5. Hàm")
            print("6. Cấu trúc dữ liệu")
            print("7. Xử lý File")
            print("8. Lập trình hướng đối tượng")
            print("9. Xem danh sách học sinh")
            print("0. Thoát")
            
            choice = input("\nChọn bài tập (0-9): ")
            
            if choice == '1':
                self.practice_variables_datatypes()
            elif choice == '2':
                self.practice_operators()
            elif choice == '3':
                self.practice_conditions()
            elif choice == '4':
                self.practice_loops()
            elif choice == '5':
                self.practice_functions()
            elif choice == '6':
                self.practice_data_structures()
            elif choice == '7':
                self.practice_file_operations()
            elif choice == '8':
                self.practice_oop()
            elif choice == '9':
                self.show_all_students()
            elif choice == '0':
                print("Cảm ơn bạn đã sử dụng ứng dụng!")
                break
            else:
                print("Lựa chọn không hợp lệ!")
            
            input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    app = PythonPracticeApp()
    app.run()