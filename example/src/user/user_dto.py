from dataclasses import dataclass


@dataclass
class CreateUserDto:
    name: str
    city: str
    age: int


@dataclass
class UpdateUserDto(CreateUserDto):
    id: int
