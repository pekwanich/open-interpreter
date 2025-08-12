"""
🚀 Open Interpreter - คู่มือการใช้งานและตัวอย่าง
==================================================

Open Interpreter เป็นเครื่องมือที่ให้ AI สามารถรันโค้ดได้บนเครื่องของเรา
สามารถใช้งานได้หลายรูปแบบ:

## 1. การติดตั้งและการตั้งค่า ✅

```bash
pip install open-interpreter
```

## 2. วิธีการรัน 🏃‍♂️

### รันแบบ Terminal Interface:

```bash
interpreter
interpreter --help
interpreter --auto-run  # รันโค้ดอัตโนมัติ
interpreter --offline   # ใช้งานแบบ offline
interpreter --local     # ใช้ local model
```

### รันแบบ Python Script:

```python
from interpreter import interpreter

# ตั้งค่า
interpreter.auto_run = True
interpreter.offline = False

# ใช้งาน
interpreter.chat("สร้างไฟล์ hello.py")
```

## 3. โหมดการทำงานต่างๆ 🔧

### A. โหมด OS Control:

```bash
interpreter --os
```

- ควบคุมเมาส์และคีย์บอร์ด
- จับภาพหน้าจอ
- ทำงานกับแอปพลิเคชัน

### B. โหมด Vision:

```bash
interpreter --vision
```

- วิเคราะห์รูปภาพ
- OCR (อ่านข้อความจากรูป)
- Computer Vision

### C. โหมด Local:

```bash
interpreter --local
```

- ใช้ Local LLM
- ไม่ต้องการ internet
- ความเป็นส่วนตัวสูง

### D. โหมด Fast:

```bash
interpreter --fast
```

- ใช้ GPT-4o-mini
- เร็วและประหยัด

## 4. ตัวอย่างการใช้งาน 💡

### สร้างและรันโปรแกรม:

```
"สร้างเกม Snake ด้วย Python"
"สร้างเว็บไซต์ธรรมดาด้วย HTML/CSS"
"วิเคราะห์ข้อมูล CSV และสร้างกราฟ"
```

### ทำงานกับไฟล์:

```
"หาไฟล์ทั้งหมดที่มี .txt ในโฟลเดอร์นี้"
"สร้างไฟล์ Excel จากข้อมูล JSON"
"แปลงรูปภาพทั้งหมดเป็น PDF"
```

### ควบคุมระบบ:

```
"เปิด Chrome และไปที่ YouTube"
"สร้าง shortcut บน desktop"
"ตั้งเวลาปลุกในคอมพิวเตอร์"
```

## 5. โครงสร้างโปรเจค 📁

```
open-interpreter/
├── interpreter/
│   ├── core/               # โค้ดหลัก
│   │   ├── core.py        # คลาส OpenInterpreter หลัก
│   │   ├── llm/           # การจัดการ Language Model
│   │   ├── computer/      # การควบคุมคอมพิวเตอร์
│   │   └── utils/         # เครื่องมือช่วย
│   ├── terminal_interface/ # Interface สำหรับ Terminal
│   │   ├── terminal_interface.py
│   │   ├── profiles/      # โปรไฟล์การตั้งค่า
│   │   └── components/    # UI Components
│   └── computer_use/      # ฟีเจอร์ควบคุมคอมพิวเตอร์
├── docs/                  # เอกสาร
├── examples/              # ตัวอย่าง
├── tests/                 # การทดสอบ
└── scripts/              # สคริปต์ช่วย
```

## 6. คุณสมบัติเด่น ⭐

### ภาษาที่รองรับ:

- Python, JavaScript, Shell/Bash
- HTML, CSS, R, Java
- PowerShell, AppleScript, Ruby

### ความสามารถพิเศษ:

- รันโค้ดแบบ real-time
- ดูและแก้ไขโค้ดก่อนรัน
- รองรับ multimodal (ข้อความ + รูปภาพ)
- ควบคุมระบบปฏิบัติการ
- ทำงานแบบ offline ได้

## 7. การตั้งค่า API Keys 🔑

### OpenAI:

```bash
export OPENAI_API_KEY="your-api-key"
interpreter
```

### Anthropic Claude:

```bash
export ANTHROPIC_API_KEY="your-api-key"
interpreter --model claude-3.5
```

### Local Models:

```bash
interpreter --local
```

## 8. เคล็ดลับการใช้งาน 💡

1. **ใช้ --auto-run เมื่อมั่นใจ**: ประหยัดเวลา
2. **ใช้ --safe-mode เมื่อไม่แน่ใจ**: ปลอดภัยกว่า
3. **ใช้ profiles**: จัดการการตั้งค่าง่าย
4. **ใช้ magic commands**: %%shell, %reset, %undo

## 9. ปัญหาที่พบบ่อยและวิธีแก้ 🔧

### ต้องการ API Key:

```bash
interpreter --api-key "your-key"
interpreter --local  # หรือใช้ local model
```

### โค้ดไม่รัน:

```bash
interpreter --auto-run=false  # ให้ถามก่อนรัน
interpreter --safe-mode=ask   # ตรวจสอบความปลอดภัย
```

### ความเร็ว:

```bash
interpreter --fast          # ใช้โมเดลเร็ว
interpreter --max-tokens 1000  # จำกัด output
```

## 10. การใช้งานขั้นสูง 🚀

### สร้าง Custom Profile:

```python
# ~/.config/open-interpreter/profiles/my_profile.py
interpreter.auto_run = True
interpreter.llm.model = "gpt-4"
interpreter.custom_instructions = "เป็นผู้ช่วยเขียนโปรแกรม Python"
```

### ใช้งานผ่าน API:

```python
from interpreter import AsyncInterpreter
import asyncio

async def main():
    interpreter = AsyncInterpreter()
    async for chunk in interpreter.chat("สร้างไฟล์ test.py"):
        print(chunk)

asyncio.run(main())
```

---

🎯 **สรุป**: Open Interpreter เป็นเครื่องมือที่ทรงพลังสำหรับให้ AI ทำงานบนคอมพิวเตอร์ของเรา
สามารถใช้งานได้ตั้งแต่งานง่ายๆ ไปจนถึงการควบคุมระบบที่ซับซ้อน!
"""
