from nestipy.common import Module

from nestipy_peewee import PeeweeModule
from .user_controller import UserController
from .user_model import User
from .user_service import UserService


@Module(
    imports=[
        PeeweeModule.for_feature(User)
    ],
    providers=[UserService],
    controllers=[UserController]
)
class UserModule:
    ...
