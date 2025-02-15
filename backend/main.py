from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
os.environ['GROQ_API_KEY']=""
app = FastAPI()

class ChatRequest(BaseModel):
    chat_text: str

@app.post("/generate_reply")
def generate_reply(request: ChatRequest):
    try:
        # openai.api_key = "your-openai-api-key"
        # response = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=[{"role": "user", "content": request.chat_text}]
        # )
        keyword_prompt="""
        Give a suitable reply to the text:
        question:{query}
        """
        llm = ChatGroq(model="llama-3.2-1b-preview",temperature=0,max_tokens=None,timeout=None,max_retries=2)
        prompt_template = ChatPromptTemplate.from_template(keyword_prompt)
        prompt_template2 = prompt_template.format_messages(query= request.chat_text)
        bs=llm(prompt_template2)
        summary=bs.content

        # return {"reply": response["choices"][0]["message"]["content"]}
        return {"reply": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
