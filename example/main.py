import uvicorn
from nestipy.core import NestipyFactory
from nestipy.openapi import DocumentBuilder, SwaggerModule

from app_module import AppModule

app = NestipyFactory.create(AppModule)
document = DocumentBuilder().set_title('Peewee API').set_description('Peewee database module for nestipy').set_version(
    '1.0').build()
SwaggerModule.setup('api', app, document)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
