#!/usr/bin/env python3
"""
รันงานเฉพาะด้วย Open Interpreter + Ollama
"""

from interpreter import interpreter

def setup_ollama():
    """ตั้งค่า Ollama"""
    interpreter.llm.model = "ollama/llama3.2:latest"
    interpreter.llm.api_base = "http://localhost:11434"
    interpreter.auto_run = True
    interpreter.offline = True
    print("✅ ตั้งค่า Ollama เรียบร้อย")

def quick_task(task):
    """รันงานด่วน"""
    setup_ollama()
    print(f"🎯 กำลังทำงาน: {task}")
    result = interpreter.chat(task)
    return result

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    print("🚀 Open Interpreter - Quick Task Runner")
    print("=" * 50)
    
    # ตัวอย่างงานต่างๆ
    tasks = [
        "แสดงรายการไฟล์ในโฟลเดอร์ปัจจุบัน",
        "สร้างไฟล์ hello.txt ที่มีข้อความ 'สวัสดี Ollama!'",
        "แสดงเวลาปัจจุบัน",
        "สร้างตัวเลขสุ่ม 10 ตัว"
    ]
    
    print("เลือกงานที่ต้องการ:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    choice = input("\nเลือกหมายเลข (1-4) หรือพิมพ์งานเอง: ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(tasks):
        selected_task = tasks[int(choice) - 1]
    else:
        selected_task = choice
    
    # รันงาน
    quick_task(selected_task)
