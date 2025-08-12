"""
🚀 คู่มือการใช้งาน Open Interpreter กับ Ollama
==================================================

## ✅ การตั้งค่าเรียบร้อยแล้ว!

Ollama models ที่พร้อมใช้งาน:

- llama3.2:latest (2.0 GB) ⭐ แนะนำ
- qwen2.5:latest (4.7 GB)
- phi3:latest (2.2 GB)
- codestral:22b (12 GB) - เหมาะสำหรับการเขียนโค้ด
- deepseek-coder:33b (18 GB) - เหมาะสำหรับการเขียนโค้ด

## 🔧 วิธีการใช้งาน

### 1. Terminal Command:

```bash
interpreter --model ollama/llama3.2:latest --api-base http://localhost:11434
```

### 2. Python Script:

```python
from interpreter import interpreter

# ตั้งค่า Ollama
interpreter.llm.model = "ollama/llama3.2:latest"
interpreter.llm.api_base = "http://localhost:11434"
interpreter.auto_run = True
interpreter.offline = True

# ใช้งาน
interpreter.chat("สร้างไฟล์ hello.py")
```

### 3. เปลี่ยน Model:

```python
# สำหรับการเขียนโค้ด
interpreter.llm.model = "ollama/codestral:22b"

# สำหรับงานทั่วไป (เร็ว)
interpreter.llm.model = "ollama/phi3:latest"

# สำหรับงานที่ต้องการความแม่นยำสูง
interpreter.llm.model = "ollama/qwen2.5:latest"
```

## 🎯 ตัวอย่างคำสั่งที่ทดสอบแล้ว

### การเขียนโปรแกรม:

```
"สร้างโปรแกรม Python คำนวณเลขฟีโบนักชี"
"เขียนเว็บไซต์ HTML แสดงเวลาปัจจุบัน"
"สร้างเกม Guess Number ด้วย Python"
```

### การจัดการไฟล์:

```
"สร้างไฟล์ CSV จากข้อมูลที่กำหนด"
"หาไฟล์ .txt ทั้งหมดในโฟลเดอร์"
"แปลงไฟล์ JSON เป็น Excel"
```

### การวิเคราะห์ข้อมูล:

```
"สร้างกราฟจากข้อมูลตัวเลข"
"วิเคราะห์ไฟล์ CSV และสรุปสถิติ"
"สร้างรายงาน PDF จากข้อมูล"
```

## 🛠️ การแก้ไขปัญหา

### ปัญหา: Connection Error

```bash
# แก้ไข: เริ่ม Ollama server
ollama serve
```

### ปัญหา: Model ไม่มี

```bash
# ดาวน์โหลด model ใหม่
ollama pull llama3.2:latest
ollama pull codestral:22b
```

### ปัญหา: ช้า

```python
# ใช้ model เล็กกว่า
interpreter.llm.model = "ollama/phi3:latest"
```

## ⚡ Tips การใช้งาน

1. **เลือก Model ตามงาน:**

   - งานทั่วไป: phi3:latest, llama3.2:latest
   - เขียนโค้ด: codestral:22b, deepseek-coder:33b
   - งานหนัก: qwen2.5:latest

2. **ประหยัด RAM:**

   - ใช้ model เล็ก (phi3, llama3.2)
   - ปิด model ที่ไม่ใช้: `ollama stop model_name`

3. **เพิ่มความเร็ว:**
   ```python
   interpreter.llm.temperature = 0.1  # ลดความสุ่ม
   interpreter.llm.max_tokens = 1000  # จำกัด output
   ```

## 🎪 Demo Scripts ที่พร้อมใช้

1. **simple_ollama_test.py** - ทดสอบการเชื่อมต่อ
2. **ollama_demo.py** - Demo ครบครัน
3. **test_oi_demo.py** - Demo แบบอัปเดต

## 🚀 วิธีรันใช้งาน (เลือกวิธีที่ชอบ)

### วิธีที่ 1: รันแบบง่าย (แนะนำ)

```bash
python simple_runner.py
```

### วิธีที่ 2: รันทดสอบเบื้องต้น

```bash
python simple_ollama_test.py
```

### วิธีที่ 3: รัน Demo ครบครัน

```bash
python ollama_demo.py
```

### วิธีที่ 4: รันงานด่วน

```bash
python quick_runner.py
```

### วิธีที่ 5: รันผ่าน Command Line

```bash
python -c "from interpreter import interpreter; interpreter.llm.model='ollama/llama3.2:latest'; interpreter.llm.api_base='http://localhost:11434'; interpreter.auto_run=True; interpreter.chat()"
```

## 💡 ตัวอย่างการใช้งานจริง

เมื่อรันแล้ว ให้ลองพิมพ์:

- "สร้างไฟล์ hello.txt"
- "แสดงรายการไฟล์ในโฟลเดอร์"
- "เขียนโปรแกรม Python คำนวณ 1+1"
- "แสดงเวลาปัจจุบัน"

🎉 **คุณพร้อมใช้งาน Open Interpreter กับ Ollama แล้ว!**
"""
