import strawberry
from models.contact import Contact
from objects import ContactType
from database import session


@strawberry.type
class Query:
    @strawberry.field
    def contact(self, info, id: int) -> ContactType:
        return session.query(Contact).get(id)

    @strawberry.field
    def contacts(self, info) -> list[ContactType]:
        return session.query(Contact).all()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_contact(self, info, name: str, email: str, phone: str) -> ContactType:
        contact = Contact(name, email, phone)
        session.add(contact)
        session.commit()
        return contact

    @strawberry.mutation
    def update_contact(
        self, info, id: int, name: str, email: str, phone: str
    ) -> ContactType:
        contact: Contact = session.query(Contact).get(id)
        contact.name = name
        contact.email = email
        contact.phone = phone
        session.commit()
        return contact

    @strawberry.mutation
    def delete_contact(self, info, id: int) -> bool:
        contact = session.query(Contact).get(id)
        session.delete(contact)
        session.commit()
        return True


schema = strawberry.Schema(query=Query, mutation=Mutation)
