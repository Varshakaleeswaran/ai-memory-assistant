from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

MEMORY = []   # temporary storage

@app.post("/webhook")
async def webhook_handler(request: Request):
    data = await request.json()

    action = data.get("action", "")
    message = data.get("text", "")

    if action == "remember":
        MEMORY.append(message)
        return {"reply": f"Saved memory: {message}"}

    if action == "recall":
        results = [m for m in MEMORY if message.lower() in m.lower()]
        if results:
            return {"reply": "\n".join(results)}
        else:
            return {"reply": "No matching memory found."}

    return {"reply": "Unknown command."}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
