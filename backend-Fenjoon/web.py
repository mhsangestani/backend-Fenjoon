# The code is run from this file
from fastapi import FastAPI, status, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schema
import exceptions
from database import SessionLocal, engine
from pydantic import BaseModel

# This line creates the database
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Checking the correctness of the user
@app.post("/login/")
async def user_name(req: schema.Login):

    if req.user_name == "12345":
        raise HTTPException(status.HTTP_200_OK, detail=f"{req.user_name}")
    else:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=f"{req.user_name}")


# Checking the correctness of the password
@app.post("/login/password")
async def password(req: schema.Password):
    if req.password == "12345":
        raise HTTPException(status.HTTP_200_OK, detail=f"{req.password}")
    else:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=f"{req.password}")


# Adding new category in the database
@app.post("/category/")
async def create_category(req: schema.CreateCategory, db: Session = Depends(get_db)):
    new_cat = crud.create_category(db, category=req)
    return new_cat


#  Adding new subcategories in the database
@app.post("/subcategories/")
async def create_subcat(req: schema.CreateSubcat, db: Session = Depends(get_db)):
    new_subcat = crud.create_subcat(db, subcat=req)
    return new_subcat


#  Adding new frequent questions in the database
@app.post("/faq/")
async def create_faq(req: schema.Ask_Question, db: Session = Depends(get_db)):
    new_faq = crud.create_faq(db, aq=req)
    return new_faq


# Show all Frequently Asked Question
@app.get("/faq/")
async def get_faq(db: Session = Depends(get_db)):
    return crud.get_faq(db)


# Show all categories and subcategories
@app.get("/GetMenu")
async def get_manu(db: Session = Depends(get_db)):
    menu = []
    for cat in list(crud.get_all_categories(db)):
        menu.append(
            {
                "cat_id": cat.id,
                "cat_name": cat.name,
                "items": crud.get_subcats(db, cat.id)
            }
        )
    return menu


# Changing the name of the category with ID
@app.post("/category/{category_id}")
async def update_category(req: schema.Change_cat, category_id: str, db: Session = Depends(get_db)):
    return crud.get_category_by_id(db, req, category_id)


# Changing the name of the subcategories with ID
@app.post("/subcategories/{subset_id}")
async def update_category(req: schema.Change_Subcat, subcat_id: str, db: Session = Depends(get_db)):
    return crud.get_subcat_by_id(db, req, subcat_id)