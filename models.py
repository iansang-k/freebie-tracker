from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

  
    freebies = relationship("Freebie", back_populates="company")

    def __repr__(self):
        return f"<Company {self.name}>"

    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()

    def give_freebie(self, dev, item_name, value):
        return Freebie(
            item_name=item_name, value=value, dev_id=dev.id, company_id=self.id
        )

  
    @property
    def devs(self):
        return [freebie.dev for freebie in self.freebies]


class Dev(Base):
    __tablename__ = "devs"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    freebies = relationship("Freebie", back_populates="dev")

    def __repr__(self):
        return f"<Dev {self.name}>"

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        if freebie.dev_id == self.id:
            freebie.dev_id = dev.id
            return True
        return False

    @property
    def companies(self):
        return [freebie.company for freebie in self.freebies]


class Freebie(Base):
    __tablename__ = "freebies"

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey("devs.id"))
    company_id = Column(Integer(), ForeignKey("companies.id"))

 
    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

    def __repr__(self):
        return f"<Freebie {self.item_name}>"
