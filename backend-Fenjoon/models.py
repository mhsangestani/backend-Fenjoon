from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# Creating a table Category
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    cat = relationship("SubCategory", back_populates="sub_cat_1")


# Creating a table of subcategories
class SubCategory(Base):
    __tablename__ = "sub_cat"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # This means the "ID" column from the categories table
    cat_id = Column(Integer, ForeignKey("categories.id"))
    # Its relationship with table categories
    sub_cat_1 = relationship("Category", back_populates="cat")
    # Relationship with table product Subkat
    sub_cat_2 = relationship("Association", back_populates="sub_cat_id_1")


# Creating a table of products
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    picture = Column(String)
    price = Column(Integer)
    pro = relationship("Association", back_populates="sub_cat_id_2")


# Creating a table of product subcategories
class Association(Base):
    __tablename__ = "product_sub_cat"

    id = Column(Integer, primary_key=True, index=True)
    sub_cat_id = Column(Integer, ForeignKey("sub_cat.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    sub_cat_id_1 = relationship("SubCategory", back_populates="sub_cat_2")
    sub_cat_id_2 = relationship("Product", back_populates="pro")


# Creating a table of users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True)


# Creating a table of frequently asked questions
class faq(Base):
    __tablename__ = "faq"

    id = Column(Integer, primary_key=True, index=True)
    questions = Column(String)
    answers = Column(String)
