from sqlmodel import SQLModel, create_engine, Field, Session
from sqlalchemy.exc import IntegrityError


engine = create_engine("sqlite:///products.db", echo=False)


class Product(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(unique=True)
    price: float
    regular_price: float
    discount_percentage: float
    rating: float
    rating_count: int
    reviews_count: int

    class Config:
        orm_mode = True
        database = engine


SQLModel.metadata.create_all(engine)


def product_inserter(product: Product):
    try:
        with Session(engine) as session:
            session.add(product)
            session.commit()
            session.refresh(product)
            print(f"New product added with id: {product.id}")
    except IntegrityError:
        print("Product Already exist")
