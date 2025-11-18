from fastapi import FastAPI

app = FastAPI(title="Flowwatch", version="0.1.0")

@app.get("/health")
async def health_check():
  return {"status": "ok"}
  
