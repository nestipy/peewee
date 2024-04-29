from nestipy.common import Module
from nestipy_config import ConfigModule, ConfigOption, ConfigService

from app_controller import AppController
from app_service import AppService
from nestipy_peewee import PeeweeConfig, PeeweeModule
from src.user.user_module import UserModule


async def peewee_factory(config: ConfigService) -> PeeweeConfig:
    return PeeweeConfig(
        driver='mysql',
        host=config.get('DB_HOST'),
        user=config.get('DB_USER'),
        password=config.get('DB_PASSWORD'),
        port=int(config.get('DB_PORT')),
        database=config.get('DB_DATABASE')
    )


@Module(
    imports=[
        ConfigModule.for_root(ConfigOption(), {'is_global': True}),
        # PeeweeModule.for_root(
        #     PeeweeConfig(
        #         driver='mysql',
        #         host='localhost',
        #         user='root',
        #         password='',
        #         port=3306,
        #         database='nestipy'
        #     )
        # ),
        PeeweeModule.for_root_async(
            factory=peewee_factory,
            inject=[ConfigService]
        ),
        UserModule
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
