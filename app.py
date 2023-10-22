from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

from pdf import render_pdf

app = FastAPI()

class Student(BaseModel):
    Full_Name: str
    Date_of_Birth: str
    City_of_Residence: str
    Contact_Address: str
    Phone_Number: str
    Email: str
    Area_of_Interest: str
    University_Major: str
    Semester: str
    Skills: list
    Knowledge: list
    Soft_Skills: list
    ID_Number: str
    English_Level: str
    University_Degree: dict
    High_School_Degree: dict
    Work_Experience: list


@app.get("/", status_code=200)
async def root():
    return {"message": "Works!"}

@app.post("/pdf", status_code=200)
async def pdf(context: Student):
    context_dict = context.dict()
    render_pdf("template.html", context_dict)
    return FileResponse('pdfs/' + context_dict["Full_Name"].replace(" ", "_") + '.pdf' , media_type="application/pdf")
