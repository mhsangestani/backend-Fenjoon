from cgi import print_exception
from sqlalchemy.orm import Session
import models
import schema


# CATEGORIES
def get_all_categories(db: Session):
    # SELECT * FROM categories;
    return db.query(models.Category).all()


def create_category(db: Session, category: schema.CreateCategory):
    # INSERT INTO categories (id, name) VALUES (category.id, category.name);
    db_cat = models.Category(
        id=category.id,
        name=category.name
    )
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


# SUBCATEGORIES
def get_subcats(db: Session, category_id: int = 1):
    return db.query(models.SubCategory).filter(models.SubCategory.cat_id == category_id).all()


def create_subcat(db: Session, subcat: schema.CreateSubcat):
    # INSERT INTO SubCategory (id, name, cat_id) VALUES (subcat.id, subcat.name, subcat.cat_id);
    db_subcat = models.SubCategory(
        id=subcat.id,
        name=subcat.name,
        cat_id=subcat.cat_id
    )
    db.add(db_subcat)
    db.commit()
    db.refresh(db_subcat)
    return db_subcat


# PRODUCTS
def get_products(db: Session):
    return db.query(models.Product).all()


def create_product(db: Session, product: schema.CreateProduct):
    # INSERT INTO Product (id, name, picture, price) VALUES (product.id, product.name, product.picture, product.price);
    db_product = models.Product(
        id=product.id,
        name=product.name,
        picture=product.picture,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_association(db: Session):
    return db.query(models.Association).all()


#pcs = product_sub_cat
def create_association(db: Session, psc: schema.CreateProductSubCat):
    # INSERT INTO Association (id, sub_cat_id, product_id) VALUES (psc.id, psc.sub_cat_id, psc.product_id);
    db_product_sub_cat = models.Association(
        id=psc.id,
        sub_cat_id=psc.sub_cat_id,
        product_id=psc.product_id
    )
    db.add(db_product_sub_cat)
    db.commit()
    db.refresh(db_product_sub_cat)
    return db_product_sub_cat


# USER
def create_user(db: Session, user: schema.LoginUser):
    # INSERT INTO User (id, phone_number) VALUES (user.id, user.phone_number);
    db_user = models.User(
        id=user.id,
        phone_number=user.phone_number,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Frequently Asked Question
def get_faq(db: Session):
    return db.query(models.faq).all()


def create_faq(db: Session, aq: schema.Ask_Question):
    # INSERT INTO faq (id, questions, answers) VALUES (aq.id, aq.questions, aq.answers);
    db_faq = models.faq(
        id=aq.id,
        questions=aq.questions,
        answers=aq.answers
    )
    db.add(db_faq)
    db.commit()
    db.refresh(db_faq)
    return db_faq


def get_category_by_id(db: Session, req: schema.Change_cat, category_id: int):
    # SELECT * FROM Category WHERE id = x;
    row_with_id = db.query(models.Category).get(category_id)
    row_with_id.name = req.new_name
    db.commit()
    db.refresh(row_with_id)
    return row_with_id


def get_subcat_by_id(db: Session, req: schema.Change_Subcat, subcat_id: int):
    # SELECT * FROM SubCategory WHERE id = x;
    row_with_id = db.query(models.SubCategory).get(subcat_id)
    row_with_id.name = req.new_name
    db.commit()
    db.refresh(row_with_id)
    return row_with_id