from nestipy.common import Module

from app_controller import AppController
from app_service import AppService
from nestipy_peewee import PeeweeConfig, PeeweeModule
from src.user.user_module import UserModule


@Module(
    imports=[
        PeeweeModule.for_root(
            PeeweeConfig(
                driver='mysql',
                host='localhost',
                user='root',
                password='',
                port=3306,
                database='nestipy'
            )
        ),
        UserModule
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
