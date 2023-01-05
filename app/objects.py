import strawberry


@strawberry.type
class ContactType:
    id: int
    name: str
    email: str
    phone: str
    created: str
