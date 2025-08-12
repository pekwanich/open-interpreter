#!/usr/bin/env python3
"""
Simple Ollama + Open Interpreter Test
"""

from interpreter import interpreter

def test_ollama_connection():
    """ทดสอบการเชื่อมต่อ Ollama อย่างง่าย"""
    print("🔧 ตั้งค่า Open Interpreter สำหรับ Ollama...")
    
    # ตั้งค่าพื้นฐาน
    interpreter.llm.model = "ollama/llama3.2:latest"
    interpreter.llm.api_base = "http://localhost:11434"
    interpreter.auto_run = True
    interpreter.offline = True
    
    print(f"✅ Model: {interpreter.llm.model}")
    print(f"✅ API Base: {interpreter.llm.api_base}")
    
    print("\n💬 ทดสอบการสนทนา...")
    try:
        # ทดสอบง่ายๆ
        result = interpreter.chat("Hello! Please respond in Thai with just 'สวัสดี'", display=True)
        print("\n✅ การเชื่อมต่อ Ollama สำเร็จ!")
        return True
    except Exception as e:
        print(f"\n❌ ข้อผิดพลาด: {e}")
        print("\nวิธีแก้ไข:")
        print("1. ตรวจสอบว่า ollama serve ทำงานอยู่")
        print("2. ตรวจสอบว่ามี model llama3.2:latest")
        print("3. ลองรัน: ollama run llama3.2:latest")
        return False

if __name__ == "__main__":
    print("🎯 ทดสอบ Open Interpreter + Ollama")
    print("=" * 40)
    test_ollama_connection()
