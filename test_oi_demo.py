#!/usr/bin/env python3
"""
Open Interpreter Demo Script
แสดงการใช้งาน Open Interpreter ในรูปแบบต่างๆ
"""

from interpreter import interpreter
import os

def setup_ollama():
    """ตั้งค่า Ollama model"""
    print("🔧 ตั้งค่า Ollama Model...")
    
    # ตั้งค่าให้ใช้ Ollama
    interpreter.llm.model = "ollama/llama3.2:latest"  # หรือ model อื่นที่คุณต้องการ
    interpreter.llm.api_base = "http://localhost:11434"
    interpreter.auto_run = True
    interpreter.offline = True
    
    print(f"✅ Model: {interpreter.llm.model}")
    print(f"✅ API Base: {interpreter.llm.api_base}")
    print(f"✅ Auto run: {interpreter.auto_run}")
    print(f"✅ Offline mode: {interpreter.offline}")

def demo_basic_usage():
    """Demo การใช้งานพื้นฐาน"""
    print("🚀 Open Interpreter Demo - การใช้งานพื้นฐาน")
    print("=" * 50)
    
    # ตั้งค่า Ollama
    setup_ollama()
    
    print(f"✅ Auto run: {interpreter.auto_run}")
    print(f"✅ Offline mode: {interpreter.offline}")
    print(f"✅ Current directory: {os.getcwd()}")
    
    # ทดสอบการทำงานของ Ollama
    print("\n📊 ทดสอบ Ollama:")
    try:
        response = interpreter.chat("สวัสดี! คุณเป็น AI model อะไร? ตอบเป็นภาษาไทยสั้นๆ", display=False)
        print("✅ Ollama ทำงานได้ปกติ!")
    except Exception as e:
        print(f"❌ ปัญหากับ Ollama: {e}")
        print("💡 ลองรัน: ollama serve ใน terminal อีกหน้าต่างหนึ่ง")

def demo_programming_tasks():
    """Demo งานเขียนโปรแกรม"""
    print("\n💻 Open Interpreter Demo - งานเขียนโปรแกรม")
    print("=" * 50)
    
    # สร้างไฟล์ Python ง่ายๆ
    print("สร้างไฟล์ Python ตัวอย่าง...")
    interpreter.chat("สร้างไฟล์ hello_world.py ที่แสดงข้อความ 'สวัสดีจาก Open Interpreter!'")
    
    # รันไฟล์ที่สร้าง
    print("\nรันไฟล์ที่สร้างไว้...")
    interpreter.chat("รันไฟล์ hello_world.py")

def demo_data_analysis():
    """Demo การวิเคราะห์ข้อมูล"""
    print("\n📈 Open Interpreter Demo - การวิเคราะห์ข้อมูล")
    print("=" * 50)
    
    # สร้างและวิเคราะห์ข้อมูล
    interpreter.chat("""
    สร้างข้อมูลตัวอย่าง 100 รายการด้วย Python และสร้างกราฟแสดงผล
    ใช้ pandas และ matplotlib ในการสร้างกราฟ
    """)

def demo_system_info():
    """Demo การดูข้อมูลระบบ"""
    print("\n🖥️  Open Interpreter Demo - ข้อมูลระบบ")
    print("=" * 50)
    
    # ดูข้อมูลระบบ
    interpreter.chat("แสดงข้อมูลระบบปฏิบัติการ RAM CPU และพื้นที่เก็บข้อมูล")

if __name__ == "__main__":
    print("🎯 Open Interpreter - ตัวอย่างการใช้งานทั้งหมด")
    print("=" * 60)
    
    try:
        # ทดสอบการทำงานพื้นฐาน
        demo_basic_usage()
        
        # ทดสอบงานเขียนโปรแกรม
        demo_programming_tasks()
        
        # ทดสอบการวิเคราะห์ข้อมูล (ถ้ามี libraries)
        try:
            demo_data_analysis()
        except Exception as e:
            print(f"⚠️  Data analysis demo ต้องการ pandas และ matplotlib: {e}")
        
        # ทดสอบการดูข้อมูลระบบ
        demo_system_info()
        
        print("\n✅ เสร็จสิ้นการทดสอบ Open Interpreter!")
        
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        print("หมายเหตุ: Open Interpreter ต้องการ API key สำหรับ LLM เพื่อทำงานได้เต็มประสิทธิภาพ")
