#!/usr/bin/env python3
"""
Open Interpreter + Ollama Demo
การใช้งาน Open Interpreter กับ Ollama Local Models
"""

from interpreter import interpreter
import os
import requests

def check_ollama_status():
    """ตรวจสอบสถานะ Ollama server"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"✅ Ollama server ทำงานอยู่ - พบ {len(models)} models")
            return True, models
        else:
            print("❌ Ollama server ไม่ตอบสนอง")
            return False, []
    except requests.exceptions.ConnectionError:
        print("❌ ไม่สามารถเชื่อมต่อ Ollama server")
        print("💡 ลองรัน: ollama serve")
        return False, []
    except Exception as e:
        print(f"❌ ข้อผิดพลาด: {e}")
        return False, []

def setup_ollama_interpreter(model_name="llama3.2:latest"):
    """ตั้งค่า Open Interpreter ให้ใช้ Ollama"""
    print(f"🔧 ตั้งค่า Open Interpreter ให้ใช้ {model_name}")
    
    # ตั้งค่า Ollama
    interpreter.llm.model = f"ollama/{model_name}"
    interpreter.llm.api_base = "http://localhost:11434"
    interpreter.llm.temperature = 0.3
    interpreter.auto_run = True
    interpreter.offline = True
    
    print(f"✅ Model: {interpreter.llm.model}")
    print(f"✅ API Base: {interpreter.llm.api_base}")
    print(f"✅ Temperature: {interpreter.llm.temperature}")
    print(f"✅ Auto run: {interpreter.auto_run}")

def demo_simple_conversation():
    """ทดสอบการสนทนาเบื้องต้น"""
    print("\n💬 ทดสอบการสนทนาเบื้องต้น")
    print("=" * 40)
    
    try:
        print("กำลังถาม AI...")
        response = interpreter.chat("สวัสดี! แนะนำตัวสั้นๆ เป็นภาษาไทย", display=False)
        print("✅ การสนทนาสำเร็จ!")
    except Exception as e:
        print(f"❌ ข้อผิดพลาด: {e}")

def demo_code_execution():
    """ทดสอบการรันโค้ด"""
    print("\n🐍 ทดสอบการรันโค้ด Python")
    print("=" * 40)
    
    try:
        print("กำลังให้ AI เขียนและรันโค้ด...")
        response = interpreter.chat("""
        เขียนโค้ด Python ที่:
        1. สร้างรายการตัวเลข 1-10
        2. คำนวณผลรวม
        3. แสดงผลลัพธ์
        """, display=False)
        print("✅ การรันโค้ดสำเร็จ!")
    except Exception as e:
        print(f"❌ ข้อผิดพลาด: {e}")

def demo_file_operations():
    """ทดสอบการทำงานกับไฟล์"""
    print("\n📁 ทดสอบการทำงานกับไฟล์")
    print("=" * 40)
    
    try:
        print("กำลังให้ AI สร้างไฟล์...")
        response = interpreter.chat("""
        สร้างไฟล์ชื่อ 'ollama_test.txt' ที่มีข้อความ:
        'สวัสดีจาก Open Interpreter + Ollama!'
        จากนั้นอ่านเนื้อหาในไฟล์กลับมาแสดง
        """, display=False)
        print("✅ การทำงานกับไฟล์สำเร็จ!")
    except Exception as e:
        print(f"❌ ข้อผิดพลาด: {e}")

def demo_system_info():
    """ทดสอบการดูข้อมูลระบบ"""
    print("\n🖥️  ทดสอบการดูข้อมูลระบบ")
    print("=" * 40)
    
    try:
        print("กำลังให้ AI ดูข้อมูลระบบ...")
        response = interpreter.chat("""
        แสดงข้อมูลระบบพื้นฐาน:
        1. ระบบปฏิบัติการ
        2. จำนวนไฟล์ในโฟลเดอร์ปัจจุบัน
        3. เวลาปัจจุบัน
        """, display=False)
        print("✅ การดูข้อมูลระบบสำเร็จ!")
    except Exception as e:
        print(f"❌ ข้อผิดพลาด: {e}")

def list_available_models():
    """แสดงรายการ models ที่มีใน Ollama"""
    print("\n📋 รายการ Ollama Models ที่พร้อมใช้งาน:")
    print("=" * 50)
    
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = response.json().get('models', [])
            for i, model in enumerate(models[:10], 1):  # แสดง 10 ตัวแรก
                name = model.get('name', 'Unknown')
                size = model.get('size', 0) / (1024**3)  # Convert to GB
                print(f"{i:2d}. {name:<25} ({size:.1f} GB)")
            
            if len(models) > 10:
                print(f"    ... และอีก {len(models) - 10} models")
        else:
            print("❌ ไม่สามารถดึงรายการ models ได้")
    except Exception as e:
        print(f"❌ ข้อผิดพลาด: {e}")

def main():
    """ฟังก์ชันหลัก"""
    print("🎯 Open Interpreter + Ollama Demo")
    print("=" * 60)
    
    # ตรวจสอบ Ollama
    is_running, models = check_ollama_status()
    
    if not is_running:
        print("\n💡 วิธีเริ่ม Ollama:")
        print("1. เปิด terminal ใหม่")
        print("2. รัน: ollama serve")
        print("3. รันสคริปต์นี้อีกครั้ง")
        return
    
    # แสดงรายการ models
    list_available_models()
    
    # เลือก model (สามารถเปลี่ยนได้)
    available_models = [
        "llama3.2:latest",
        "qwen2.5:latest", 
        "phi3:latest",
        "codestral:22b",
        "deepseek-coder:33b"
    ]
    
    print(f"\n🤖 เลือก Model สำหรับทดสอบ:")
    for i, model in enumerate(available_models, 1):
        print(f"{i}. {model}")
    
    try:
        choice = input("\nเลือกหมายเลข model (หรือ Enter สำหรับ llama3.2): ").strip()
        if choice and choice.isdigit() and 1 <= int(choice) <= len(available_models):
            selected_model = available_models[int(choice) - 1]
        else:
            selected_model = "llama3.2:latest"
    except:
        selected_model = "llama3.2:latest"
    
    print(f"\n🚀 ใช้ model: {selected_model}")
    
    # ตั้งค่า interpreter
    setup_ollama_interpreter(selected_model)
    
    # รันการทดสอบ
    print("\n" + "="*60)
    print("🧪 เริ่มการทดสอบ...")
    
    demo_simple_conversation()
    demo_code_execution()
    demo_file_operations()
    demo_system_info()
    
    print("\n" + "="*60)
    print("✅ เสร็จสิ้นการทดสอบ Open Interpreter + Ollama!")
    print("💡 คุณสามารถใช้งาน Open Interpreter กับ Ollama แล้ว")
    
    # แสดงวิธีใช้งานต่อ
    print(f"\n🔧 วิธีใช้งานต่อ:")
    print(f"interpreter --model ollama/{selected_model}")
    print(f"interpreter --api-base http://localhost:11434")

if __name__ == "__main__":
    main()
