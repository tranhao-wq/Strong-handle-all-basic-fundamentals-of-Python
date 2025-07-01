#!/usr/bin/env python3
import tkinter as tk
from tkinter import Canvas
import os

def create_app_icon():
    root = tk.Tk()
    root.withdraw()
    
    # Create canvas
    canvas = Canvas(root, width=64, height=64, bg='#2c3e50')
    
    # Draw Python logo-inspired icon
    # Snake body
    canvas.create_oval(10, 15, 35, 40, fill='#3498db', outline='#2980b9', width=2)
    canvas.create_oval(25, 25, 50, 50, fill='#f1c40f', outline='#f39c12', width=2)
    
    # Eyes
    canvas.create_oval(18, 22, 22, 26, fill='white')
    canvas.create_oval(19, 23, 21, 25, fill='black')
    
    canvas.create_oval(33, 32, 37, 36, fill='white')
    canvas.create_oval(34, 33, 36, 35, fill='black')
    
    # Save as PostScript then convert
    canvas.postscript(file="app_icon.eps")
    
    print("Icon created successfully!")
    root.destroy()

if __name__ == "__main__":
    create_app_icon()