from typing import Annotated
from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy.ioc import Inject, Body, Param
from nestipy.openapi import ApiOkResponse, ApiCreatedResponse, ApiBody
from .user_dto import CreateUserDto, UpdateUserDto
from .user_service import UserService


@ApiOkResponse()
@ApiCreatedResponse()
@Controller('users')
class UserController:
    user_service: Annotated[UserService, Inject()]

    @Get()
    async def list(self) -> str:
        return await self.user_service.list()

    @ApiBody(CreateUserDto)
    @Post()
    async def create(self, data: Annotated[CreateUserDto, Body()]) -> str:
        return await self.user_service.create(data)

    @ApiBody(CreateUserDto)
    @Put('/{user_id}')
    async def update(self, user_id: Annotated[int, Param('user_id')], data: Annotated[CreateUserDto, Body()]) -> str:
        return await self.user_service.update(user_id, data)

    @Delete('/{user_id}')
    async def delete(self, user_id: Annotated[int, Param('user_id')]) -> None:
        return await self.user_service.delete(user_id)
