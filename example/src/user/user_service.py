from dataclasses import asdict

from nestipy.common import Injectable
from playhouse.shortcuts import model_to_dict

from .user_dto import CreateUserDto
from .user_model import User


@Injectable()
class UserService:

    async def list(self):
        return list(User.select().dicts())

    async def create(self, data: CreateUserDto):
        user = User.create(**asdict(data))
        return model_to_dict(user)

    async def update(self, _id: int, data: CreateUserDto):
        User.update(asdict(data), id=_id).execute()
        return True

    async def delete(self, _id: int):
        return User.delete_by_id(_id)
