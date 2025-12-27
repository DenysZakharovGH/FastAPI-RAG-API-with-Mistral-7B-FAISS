import uvicorn
from fastapi import FastAPI
from starlette.responses import HTMLResponse

from app.core.app import llm_route
from app.core.config import settings, FRONTEND_STORAGE
from app.core.middleware import RequestLoggingMiddleware

app = FastAPI()
app.include_router(llm_route)
app.add_middleware(RequestLoggingMiddleware)

app.get("/health")
def health_check():
    return {"msg": "OK"}

@app.get("/", response_class=HTMLResponse)
async def root():
    with open(f"{FRONTEND_STORAGE}/chat.html") as f:
        return f.read()


if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.run.host,
                port=settings.run.port)
