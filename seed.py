# seed.py
from config import session
from models import Company, Dev, Freebie


def seed_database():
    # Clear existing data
    session.query(Freebie).delete()
    session.query(Dev).delete()
    session.query(Company).delete()
    session.commit()

    # Create companies
    c1 = Company(name="Google", founding_year=1998)
    c2 = Company(name="Facebook", founding_year=2004)
    c3 = Company(name="Amazon", founding_year=1994)

    # Create devs
    d1 = Dev(name="John")
    d2 = Dev(name="Jane")
    d3 = Dev(name="Bob")

    # Create freebies
    f1 = Freebie(item_name="T-shirt", value=20, dev=d1, company=c1)
    f2 = Freebie(item_name="Stickers", value=5, dev=d1, company=c2)
    f3 = Freebie(item_name="Laptop", value=1000, dev=d2, company=c1)
    f4 = Freebie(item_name="Water Bottle", value=15, dev=d3, company=c3)

    session.add_all([c1, c2, c3, d1, d2, d3, f1, f2, f3, f4])
    session.commit()
    print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
