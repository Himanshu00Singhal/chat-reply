#!/bin/bash
# Start Backend
cd backend && uvicorn main:app --host 0.0.0.0 --port 8000 &

# Start Frontend
cd frontend && streamlit run app.py
