cd backend
uvicorn main:app --reload

cd frontend
streamlit run app.py

python utils/monitor.py

Step Next: Load Browser Extension
Open Chrome → Extensions
Enable Developer Mode
Click "Load unpacked"
Select the extension/ folder
Open WhatsApp Web and test it! 

NGrok:

streamlit run app.py
http://localhost:8501

ngrok config add-authtoken YOUR_NGROK_AUTH_TOKEN
token at:  https://dashboard.ngrok.com/get-started/your-authtoken

ngrok http 8501
