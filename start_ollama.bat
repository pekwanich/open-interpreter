@echo off
echo 🚀 เริ่ม Open Interpreter + Ollama
echo ===============================

echo ✅ กำลังตรวจสอบ Ollama...
ollama list

echo.
echo ✅ เริ่ม Open Interpreter...
C:/Users/UsEr/AppData/Local/Programs/Python/Python310/python.exe -c "from interpreter import interpreter; interpreter.llm.model='ollama/llama3.2:latest'; interpreter.llm.api_base='http://localhost:11434'; interpreter.auto_run=True; interpreter.offline=True; interpreter.chat()"

pause
