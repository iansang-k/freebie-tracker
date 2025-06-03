from config import session
from models import Company, Dev, Freebie


def seed_database():
    session.query(Freebie).delete()
    session.query(Dev).delete()
    session.query(Company).delete()
    session.commit()

    company = Company(name="Google", founding_year=1998)

    developer = Dev(name="John")

    freebie = Freebie(item_name="T-shirt", value=20, dev=developer, company=company)

    session.add_all([company, developer, freebie])
    session.commit()
    print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
