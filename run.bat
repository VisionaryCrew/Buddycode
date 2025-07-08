@echo off
echo 🚀 Activating virtual environment...
call venv\Scripts\activate

echo 📦 Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo 🔥 Starting BuddyCode backend...
cd backend
py app.py

echo ✅ Server stopped.
pause
