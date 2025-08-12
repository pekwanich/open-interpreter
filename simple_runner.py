#!/usr/bin/env python3
"""
วิธีรันใช้งานง่ายที่สุด
"""

from interpreter import interpreter

print("🎯 กำลังตั้งค่า Open Interpreter + Ollama...")

# ตั้งค่า
interpreter.llm.model = "ollama/llama3.2:latest"
interpreter.llm.api_base = "http://localhost:11434"
interpreter.auto_run = True
interpreter.offline = True

print("✅ พร้อมใช้งาน!")
print("💡 พิมพ์คำสั่งที่ต้องการ หรือ 'exit' เพื่อออก")
print("=" * 50)

# ตัวอย่างคำสั่งที่ใช้ได้
examples = [
    "สร้างไฟล์ test.txt",
    "แสดงรายการไฟล์",
    "เขียนโปรแกรม Python ง่ายๆ",
    "คำนวณ 2+2"
]

print("ตัวอย่างคำสั่ง:")
for ex in examples:
    print(f"  • {ex}")
print()

# รับคำสั่งจากผู้ใช้
while True:
    try:
        user_input = input("👤 คำสั่ง: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("👋 ขอบคุณที่ใช้งาน!")
            break
            
        if user_input:
            print(f"🤖 กำลังประมวลผล: {user_input}")
            interpreter.chat(user_input)
            print("\n" + "="*50)
        
    except KeyboardInterrupt:
        print("\n👋 ออกจากโปรแกรม")
        break
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        print("💡 ลองใหม่อีกครั้ง")
