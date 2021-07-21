from prisma import Client
from prisma.models import User


async def main(client: Client) -> None:
    user = await client.query_first('', model=User)
    reveal_type(user)  # T: User | None
    assert user is not None
    reveal_type(user)  # T: User
    reveal_type(user.id)  # T: str

    user.foo  # E: Cannot access member "foo" for type "User"

    result = await client.query_first('')
    reveal_type(result)  # T: Any
