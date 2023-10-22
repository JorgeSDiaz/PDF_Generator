from fastapi import FastAPI
from pdf import render_pdf

app = FastAPI()


@app.get("/", status_code=200)
async def root():
    return {"message": "Works!"}

@app.get("/pdf", status_code=200)
async def pdf():
    return FileResponse(render_pdf(), media_type="application/pdf")
