from pydantic import BaseModel


class Login(BaseModel):
    user_name: str


class Password(BaseModel):
    password: str


class CreateCategory(BaseModel):
    id: int
    name: str


class CreateSubcat(BaseModel):
    id: int
    name: str
    cat_id: int


class CreateProduct(BaseModel):
    id: int
    name: str
    picture: str
    price: int


class CreateProductSubCat(BaseModel):
    id: int
    sub_cat_id: int
    product_id: int


class LoginUser(BaseModel):
    id: int
    phone_number: str
    verification_code: str


class Ask_Question(BaseModel):
    id: int
    questions: str
    answers: str


class Change_cat(BaseModel):
    new_name: str


class Change_Subcat(BaseModel):
    new_name: str

