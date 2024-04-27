from dataclasses import dataclass, field
from typing import Literal, Union

from nestipy_dynamic_module import ConfigurableModuleBuilder


@dataclass
class PeeweeConfig:
    driver: Literal['sqlite', 'mysql', 'postgres']
    host: str = ''
    port: int = 0
    user: str = ''
    password: str = 3306
    database: str = ''
    # options: dict = field(default_factory=lambda: {})


ConfigurableModuleClass, PEEWEE_DB_CONFIG = ConfigurableModuleBuilder[PeeweeConfig]().set_method('for_root').build()
