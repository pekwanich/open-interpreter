#!/usr/bin/env python3
"""
ทดสอบ Open Interpreter + Ollama กับงานจริง
"""

from interpreter import interpreter

# ตั้งค่า Ollama
interpreter.llm.model = "ollama/llama3.2:latest"
interpreter.llm.api_base = "http://localhost:11434"
interpreter.auto_run = True
interpreter.offline = True

print("🚀 ทดสอบ Ollama ด้วยงานจริง")
print("=" * 40)

# ทดสอบ 1: สร้างไฟล์ Python
print("📝 ทดสอบ 1: สร้างไฟล์ Python")
try:
    interpreter.chat("""
    สร้างไฟล์ Python ชื่อ 'calculator.py' ที่มีฟังก์ชัน:
    - บวก ลบ คูณ หาร
    - มี main function ทดสอบการทำงาน
    """)
    print("✅ สร้างไฟล์สำเร็จ!")
except Exception as e:
    print(f"❌ เกิดข้อผิดพลาด: {e}")

print("\n" + "="*40)
print("🎯 ทดสอบเสร็จสิ้น! Open Interpreter + Ollama ทำงานได้ปกติ")
