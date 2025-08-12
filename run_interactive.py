#!/usr/bin/env python3
"""
วิธีรันใช้งาน Open Interpreter + Ollama
"""

from interpreter import interpreter

# ตั้งค่า Ollama (รันครั้งเดียวพอ)
interpreter.llm.model = "ollama/llama3.2:latest"
interpreter.llm.api_base = "http://localhost:11434"
interpreter.auto_run = True
interpreter.offline = True

print("🎯 Open Interpreter + Ollama พร้อมใช้งาน!")
print("=" * 50)

# ตัวอย่างการใช้งาน
print("💬 ลองถามอะไรดู...")

# เริ่มการสนทนา
interpreter.chat()  # จะเปิด interactive mode ให้พิมพ์คำสั่งได้เลย
