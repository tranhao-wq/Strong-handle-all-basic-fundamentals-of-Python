#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ứng dụng GUI thực hành Python cơ bản
Giao diện desktop với tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
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

class PythonPracticeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Ứng dụng thực hành Python cơ bản")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Set window icon
        try:
            self.root.iconbitmap(default='python_icon.ico')
        except:
            pass  # Icon file not found, continue without icon
        
        self.students = []
        self.data_file = "students_data.json"
        self.load_data()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill='x', padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🐍 THỰC HÀNH PYTHON CƠ BẢN", 
                              font=('Arial', 18, 'bold'), fg='white', bg='#2c3e50')
        title_label.pack(expand=True)
        
        # Main content
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Left panel - Menu
        left_frame = tk.Frame(main_frame, bg='#ecf0f1', width=250)
        left_frame.pack(side='left', fill='y', padx=(0, 10))
        left_frame.pack_propagate(False)
        
        menu_label = tk.Label(left_frame, text="CHỌN BÀI TẬP", font=('Arial', 12, 'bold'), 
                             bg='#ecf0f1', fg='#2c3e50')
        menu_label.pack(pady=10)
        
        # Menu buttons
        buttons = [
            ("1. Biến & Kiểu dữ liệu", self.show_variables_frame),
            ("2. Toán tử", self.show_operators_frame),
            ("3. Điều kiện", self.show_conditions_frame),
            ("4. Vòng lặp", self.show_loops_frame),
            ("5. Hàm", self.show_functions_frame),
            ("6. Cấu trúc dữ liệu", self.show_datastructures_frame),
            ("7. File", self.show_file_frame),
            ("8. OOP", self.show_oop_frame),
            ("9. Danh sách HS", self.show_students_list)
        ]
        
        for text, command in buttons:
            btn = tk.Button(left_frame, text=text, command=command, 
                           font=('Arial', 10), width=20, height=2,
                           bg='#3498db', fg='white', relief='flat')
            btn.pack(pady=2, padx=10, fill='x')
        
        # Right panel - Content
        self.content_frame = tk.Frame(main_frame, bg='white', relief='sunken', bd=1)
        self.content_frame.pack(side='right', fill='both', expand=True)
        
        # Welcome screen
        self.show_welcome()
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_welcome(self):
        self.clear_content()
        welcome_label = tk.Label(self.content_frame, 
                                text="Chào mừng đến với ứng dụng thực hành Python!\n\nChọn một bài tập từ menu bên trái để bắt đầu.",
                                font=('Arial', 14), bg='white', fg='#2c3e50')
        welcome_label.pack(expand=True)
    
    def show_variables_frame(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="BÀI TẬP 1: BIẾN VÀ KIỂU DỮ LIỆU", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        # Input fields
        fields_frame = tk.Frame(self.content_frame, bg='white')
        fields_frame.pack(pady=10)
        
        tk.Label(fields_frame, text="Tên:", bg='white').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        name_entry = tk.Entry(fields_frame, width=20)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(fields_frame, text="Tuổi:", bg='white').grid(row=1, column=0, sticky='w', padx=5, pady=5)
        age_entry = tk.Entry(fields_frame, width=20)
        age_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(fields_frame, text="Chiều cao (m):", bg='white').grid(row=2, column=0, sticky='w', padx=5, pady=5)
        height_entry = tk.Entry(fields_frame, width=20)
        height_entry.grid(row=2, column=1, padx=5, pady=5)
        
        is_student_var = tk.BooleanVar()
        tk.Checkbutton(fields_frame, text="Là học sinh", variable=is_student_var, bg='white').grid(row=3, column=0, columnspan=2, pady=5)
        
        # Result area
        result_text = scrolledtext.ScrolledText(self.content_frame, width=50, height=10)
        result_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        def analyze_data():
            try:
                name = name_entry.get()
                age = int(age_entry.get())
                height = float(height_entry.get())
                is_student = is_student_var.get()
                
                scores = [random.uniform(7, 10) for _ in range(3)]
                
                info = {
                    "name": name,
                    "age": age,
                    "height": height,
                    "is_student": is_student,
                    "scores": scores
                }
                
                result = f"PHÂN TÍCH KIỂU DỮ LIỆU:\n\n"
                result += f"Tên: {info['name']} (kiểu: {type(info['name']).__name__})\n"
                result += f"Tuổi: {info['age']} (kiểu: {type(info['age']).__name__})\n"
                result += f"Chiều cao: {info['height']}m (kiểu: {type(info['height']).__name__})\n"
                result += f"Là học sinh: {info['is_student']} (kiểu: {type(info['is_student']).__name__})\n"
                result += f"Điểm số: {info['scores']} (kiểu: {type(info['scores']).__name__})\n\n"
                result += f"Điểm trung bình: {sum(scores)/len(scores):.2f}\n"
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result)
                
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số!")
        
        tk.Button(self.content_frame, text="Phân tích dữ liệu", command=analyze_data,
                 bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(pady=5)
    
    def show_operators_frame(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="BÀI TẬP 2: TOÁN TỬ", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        input_frame = tk.Frame(self.content_frame, bg='white')
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Số thứ nhất:", bg='white').grid(row=0, column=0, padx=5, pady=5)
        a_entry = tk.Entry(input_frame, width=15)
        a_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Số thứ hai:", bg='white').grid(row=0, column=2, padx=5, pady=5)
        b_entry = tk.Entry(input_frame, width=15)
        b_entry.grid(row=0, column=3, padx=5, pady=5)
        
        result_text = scrolledtext.ScrolledText(self.content_frame, width=50, height=15)
        result_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        def calculate():
            try:
                a = int(a_entry.get())
                b = int(b_entry.get())
                
                result = f"KẾT QUẢ TÍNH TOÁN:\n\n"
                result += f"Phép toán cơ bản:\n"
                result += f"{a} + {b} = {a + b}\n"
                result += f"{a} - {b} = {a - b}\n"
                result += f"{a} * {b} = {a * b}\n"
                result += f"{a} / {b} = {a / b:.2f}\n" if b != 0 else f"{a} / {b} = Không thể chia cho 0\n"
                result += f"{a} // {b} = {a // b}\n" if b != 0 else f"{a} // {b} = Không thể chia cho 0\n"
                result += f"{a} % {b} = {a % b}\n" if b != 0 else f"{a} % {b} = Không thể chia cho 0\n"
                result += f"{a} ** {b} = {a ** b}\n\n"
                
                result += f"So sánh:\n"
                result += f"{a} == {b}: {a == b}\n"
                result += f"{a} != {b}: {a != b}\n"
                result += f"{a} > {b}: {a > b}\n"
                result += f"{a} < {b}: {a < b}\n"
                result += f"{a} >= {b}: {a >= b}\n"
                result += f"{a} <= {b}: {a <= b}\n\n"
                
                result += f"Logic:\n"
                result += f"{a} > 0 and {b} > 0: {a > 0 and b > 0}\n"
                result += f"{a} > 0 or {b} > 0: {a > 0 or b > 0}\n"
                result += f"not ({a} > {b}): {not (a > b)}\n"
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result)
                
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên!")
        
        tk.Button(self.content_frame, text="Tính toán", command=calculate,
                 bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(pady=5)
    
    def show_conditions_frame(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="BÀI TẬP 3: CẤU TRÚC ĐIỀU KIỆN", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        input_frame = tk.Frame(self.content_frame, bg='white')
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Điểm số (0-10):", bg='white').grid(row=0, column=0, padx=5, pady=5)
        score_entry = tk.Entry(input_frame, width=15)
        score_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Năm:", bg='white').grid(row=1, column=0, padx=5, pady=5)
        year_entry = tk.Entry(input_frame, width=15)
        year_entry.grid(row=1, column=1, padx=5, pady=5)
        
        result_text = scrolledtext.ScrolledText(self.content_frame, width=50, height=10)
        result_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        def check_conditions():
            try:
                score = float(score_entry.get())
                year = int(year_entry.get())
                
                # Xếp loại điểm
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
                
                # Kiểm tra năm nhuận
                is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                
                result = f"KẾT QUẢ KIỂM TRA:\n\n"
                result += f"Điểm {score} xếp loại: {grade}\n\n"
                result += f"Năm {year}: {'Năm nhuận' if is_leap else 'Không phải năm nhuận'}\n\n"
                
                # Thêm logic phân loại tuổi
                if score >= 8:
                    result += "Nhận xét: Học sinh giỏi, cần duy trì!\n"
                elif score >= 6.5:
                    result += "Nhận xét: Cần cố gắng thêm để đạt loại giỏi!\n"
                else:
                    result += "Nhận xét: Cần học tập chăm chỉ hơn!\n"
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result)
                
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng!")
        
        tk.Button(self.content_frame, text="Kiểm tra", command=check_conditions,
                 bg='#f39c12', fg='white', font=('Arial', 10, 'bold')).pack(pady=5)
    
    def show_loops_frame(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="BÀI TẬP 4: VÒNG LẶP", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        # Bảng cửu chương
        table_frame = tk.Frame(self.content_frame, bg='white')
        table_frame.pack(pady=10)
        
        tk.Label(table_frame, text="Bảng cửu chương:", bg='white').grid(row=0, column=0, padx=5, pady=5)
        table_entry = tk.Entry(table_frame, width=10)
        table_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Game đoán số
        game_frame = tk.Frame(self.content_frame, bg='white')
        game_frame.pack(pady=10)
        
        tk.Label(game_frame, text="Game đoán số (1-100):", bg='white').grid(row=0, column=0, padx=5, pady=5)
        guess_entry = tk.Entry(game_frame, width=10)
        guess_entry.grid(row=0, column=1, padx=5, pady=5)
        
        result_text = scrolledtext.ScrolledText(self.content_frame, width=50, height=15)
        result_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        def show_multiplication_table():
            try:
                n = int(table_entry.get())
                result = f"BẢNG CỬU CHƯƠNG {n}:\n\n"
                for i in range(1, 11):
                    result += f"{n} x {i} = {n * i}\n"
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result)
                
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên!")
        
        def guess_number():
            try:
                guess = int(guess_entry.get())
                self.attempts += 1
                
                current_text = result_text.get(1.0, tk.END)
                
                if guess == self.secret_number:
                    result = f"🎉 Chính xác! Số bí mật là {self.secret_number}\n"
                    result += f"Bạn đã đoán đúng sau {self.attempts} lần thử!\n\n"
                    # Reset game
                    self.secret_number = random.randint(1, 100)
                    self.attempts = 0
                    result += "Game mới đã bắt đầu!\n"
                elif guess < self.secret_number:
                    result = f"Lần thử {self.attempts}: {guess} - Số cần tìm LỚN HƠN!\n"
                else:
                    result = f"Lần thử {self.attempts}: {guess} - Số cần tìm NHỎ HƠN!\n"
                
                result_text.insert(tk.END, result)
                result_text.see(tk.END)
                guess_entry.delete(0, tk.END)
                
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên!")
        
        btn_frame = tk.Frame(self.content_frame, bg='white')
        btn_frame.pack(pady=5)
        
        tk.Button(btn_frame, text="Hiện bảng cửu chương", command=show_multiplication_table,
                 bg='#9b59b6', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Đoán số", command=guess_number,
                 bg='#1abc9c', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
    
    def show_functions_frame(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="BÀI TẬP 5: HÀM", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        input_frame = tk.Frame(self.content_frame, bg='white')
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Cân nặng (kg):", bg='white').grid(row=0, column=0, padx=5, pady=5)
        weight_entry = tk.Entry(input_frame, width=15)
        weight_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Chiều cao (m):", bg='white').grid(row=0, column=2, padx=5, pady=5)
        height_entry = tk.Entry(input_frame, width=15)
        height_entry.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(input_frame, text="Fibonacci n:", bg='white').grid(row=1, column=0, padx=5, pady=5)
        fib_entry = tk.Entry(input_frame, width=15)
        fib_entry.grid(row=1, column=1, padx=5, pady=5)
        
        result_text = scrolledtext.ScrolledText(self.content_frame, width=50, height=12)
        result_text.pack(pady=10, padx=20, fill='both', expand=True)
        
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
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
        
        def calculate_all():
            try:
                result = "KẾT QUẢ TÍNH TOÁN:\n\n"
                
                # BMI
                if weight_entry.get() and height_entry.get():
                    weight = float(weight_entry.get())
                    height = float(height_entry.get())
                    bmi = calculate_bmi(weight, height)
                    category = bmi_category(bmi)
                    result += f"BMI: {bmi:.1f} - {category}\n\n"
                
                # Fibonacci
                if fib_entry.get():
                    n = int(fib_entry.get())
                    if n >= 0:
                        fib_result = fibonacci(n)
                        result += f"Fibonacci({n}) = {fib_result}\n\n"
                        
                        # Hiển thị dãy Fibonacci
                        result += f"Dãy Fibonacci đến {n}:\n"
                        fib_sequence = [fibonacci(i) for i in range(min(n + 1, 20))]
                        result += ", ".join(map(str, fib_sequence))
                        if n > 19:
                            result += "..."
                        result += "\n"
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result)
                
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số!")
        
        tk.Button(self.content_frame, text="Tính toán", command=calculate_all,
                 bg='#34495e', fg='white', font=('Arial', 10, 'bold')).pack(pady=5)
    
    def show_datastructures_frame(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="BÀI TẬP 6: CẤU TRÚC DỮ LIỆU", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        input_frame = tk.Frame(self.content_frame, bg='white')
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Nhập danh sách (cách nhau bởi dấu phẩy):", bg='white').pack()
        list_entry = tk.Entry(input_frame, width=50)
        list_entry.pack(pady=5)
        
        result_text = scrolledtext.ScrolledText(self.content_frame, width=50, height=15)
        result_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        def analyze_data_structures():
            try:
                input_text = list_entry.get()
                if not input_text:
                    messagebox.showwarning("Cảnh báo", "Vui lòng nhập dữ liệu!")
                    return
                
                # Tạo list từ input
                items = [item.strip() for item in input_text.split(',')]
                
                result = "PHÂN TÍCH CẤU TRÚC DỮ LIỆU:\n\n"
                
                # List
                result += f"1. LIST:\n"
                result += f"   Dữ liệu gốc: {items}\n"
                result += f"   Số phần tử: {len(items)}\n"
                result += f"   Phần tử đầu: {items[0] if items else 'Không có'}\n"
                result += f"   Phần tử cuối: {items[-1] if items else 'Không có'}\n\n"
                
                # Set (loại bỏ trùng lặp)
                unique_items = list(set(items))
                result += f"2. SET (loại bỏ trùng lặp):\n"
                result += f"   Dữ liệu: {unique_items}\n"
                result += f"   Số phần tử duy nhất: {len(unique_items)}\n\n"
                
                # Dictionary (đếm số lần xuất hiện)
                count_dict = {}
                for item in items:
                    count_dict[item] = count_dict.get(item, 0) + 1
                
                result += f"3. DICTIONARY (đếm số lần xuất hiện):\n"
                for key, value in count_dict.items():
                    result += f"   '{key}': {value} lần\n"
                result += "\n"
                
                # Tuple
                items_tuple = tuple(items)
                result += f"4. TUPLE:\n"
                result += f"   Dữ liệu: {items_tuple}\n"
                result += f"   Không thể thay đổi sau khi tạo\n\n"
                
                # Thao tác với list
                result += f"5. THAO TÁC VỚI LIST:\n"
                if len(items) > 1:
                    result += f"   Sắp xếp: {sorted(items)}\n"
                    result += f"   Đảo ngược: {items[::-1]}\n"
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result)
                
            except Exception as e:
                messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")
        
        tk.Button(self.content_frame, text="Phân tích", command=analyze_data_structures,
                 bg='#16a085', fg='white', font=('Arial', 10, 'bold')).pack(pady=5)
    
    def show_file_frame(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="BÀI TẬP 7: XỬ LÝ FILE", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        input_frame = tk.Frame(self.content_frame, bg='white')
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Nhập ghi chú:", bg='white').pack()
        note_entry = tk.Entry(input_frame, width=50)
        note_entry.pack(pady=5)
        
        result_text = scrolledtext.ScrolledText(self.content_frame, width=50, height=15)
        result_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        filename = "practice_notes.txt"
        
        def save_note():
            note = note_entry.get()
            if not note:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập ghi chú!")
                return
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(f"[{timestamp}] {note}\n")
                
                messagebox.showinfo("Thành công", f"Đã lưu ghi chú vào {filename}")
                note_entry.delete(0, tk.END)
                load_notes()
                
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể lưu file: {str(e)}")
        
        def load_notes():
            try:
                if os.path.exists(filename):
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, f"NỘI DUNG FILE {filename}:\n\n{content}")
                else:
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, f"File {filename} chưa tồn tại.")
                    
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể đọc file: {str(e)}")
        
        def clear_notes():
            try:
                if os.path.exists(filename):
                    os.remove(filename)
                    messagebox.showinfo("Thành công", "Đã xóa file ghi chú!")
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, "File đã được xóa.")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể xóa file: {str(e)}")
        
        btn_frame = tk.Frame(self.content_frame, bg='white')
        btn_frame.pack(pady=5)
        
        tk.Button(btn_frame, text="Lưu ghi chú", command=save_note,
                 bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Tải ghi chú", command=load_notes,
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Xóa file", command=clear_notes,
                 bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        # Load notes on start
        load_notes()
    
    def show_oop_frame(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="BÀI TẬP 8: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        input_frame = tk.Frame(self.content_frame, bg='white')
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Tên học sinh:", bg='white').grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(input_frame, width=20)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Tuổi:", bg='white').grid(row=1, column=0, padx=5, pady=5)
        age_entry = tk.Entry(input_frame, width=20)
        age_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Điểm (cách nhau bởi dấu phẩy):", bg='white').grid(row=2, column=0, padx=5, pady=5)
        scores_entry = tk.Entry(input_frame, width=20)
        scores_entry.grid(row=2, column=1, padx=5, pady=5)
        
        result_text = scrolledtext.ScrolledText(self.content_frame, width=50, height=12)
        result_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        def create_student():
            try:
                name = name_entry.get()
                age = int(age_entry.get())
                scores_text = scores_entry.get()
                
                if not name:
                    messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên!")
                    return
                
                scores = []
                if scores_text:
                    scores = [float(score.strip()) for score in scores_text.split(',')]
                
                student = Student(name, age, scores)
                self.students.append(student)
                self.save_data()
                
                result = f"ĐÃ TẠO ĐỐI TƯỢNG STUDENT:\n\n"
                result += f"Thông tin: {student.info()}\n\n"
                result += f"Thuộc tính:\n"
                result += f"- name: {student.name}\n"
                result += f"- age: {student.age}\n"
                result += f"- scores: {student.scores}\n\n"
                result += f"Phương thức:\n"
                result += f"- get_average(): {student.get_average():.2f}\n"
                result += f"- info(): {student.info()}\n\n"
                result += f"Tổng số học sinh đã tạo: {len(self.students)}"
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result)
                
                # Clear inputs
                name_entry.delete(0, tk.END)
                age_entry.delete(0, tk.END)
                scores_entry.delete(0, tk.END)
                
                messagebox.showinfo("Thành công", "Đã tạo và lưu học sinh!")
                
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng!")
        
        tk.Button(self.content_frame, text="Tạo học sinh", command=create_student,
                 bg='#8e44ad', fg='white', font=('Arial', 10, 'bold')).pack(pady=5)
    
    def show_students_list(self):
        self.clear_content()
        
        tk.Label(self.content_frame, text="DANH SÁCH HỌC SINH", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        result_text = scrolledtext.ScrolledText(self.content_frame, width=50, height=20)
        result_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        if not self.students:
            result_text.insert(tk.END, "Chưa có học sinh nào được tạo.\n\nHãy sử dụng bài tập OOP để tạo học sinh!")
        else:
            result = f"DANH SÁCH {len(self.students)} HỌC SINH:\n\n"
            for i, student in enumerate(self.students, 1):
                result += f"{i}. {student.info()}\n"
                result += f"   Điểm chi tiết: {student.scores}\n\n"
            
            # Thống kê
            all_scores = []
            for student in self.students:
                all_scores.extend(student.scores)
            
            if all_scores:
                result += f"THỐNG KÊ:\n"
                result += f"- Tổng số điểm: {len(all_scores)}\n"
                result += f"- Điểm cao nhất: {max(all_scores):.2f}\n"
                result += f"- Điểm thấp nhất: {min(all_scores):.2f}\n"
                result += f"- Điểm trung bình chung: {sum(all_scores)/len(all_scores):.2f}\n"
            
            result_text.insert(tk.END, result)
        
        def clear_all_students():
            if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa tất cả học sinh?"):
                self.students.clear()
                self.save_data()
                self.show_students_list()
                messagebox.showinfo("Thành công", "Đã xóa tất cả học sinh!")
        
        tk.Button(self.content_frame, text="Xóa tất cả", command=clear_all_students,
                 bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(pady=5)
    
    def save_data(self):
        try:
            data = []
            for student in self.students:
                data.append({
                    "name": student.name,
                    "age": student.age,
                    "scores": student.scores
                })
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except:
            pass
    
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

def main():
    root = tk.Tk()
    app = PythonPracticeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()