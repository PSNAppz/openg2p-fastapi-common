"""Module from initializing base middlewares"""


from .component import BaseComponent
from .config import Settings
from .context import app_registry

_config = Settings.get_config(strict=False)


class BaseMiddleware(BaseComponent):
    def __init__(self, name="", **kwargs):
        super().__init__(name=name)
        self.middleware = None

    def post_init(self):
        app_registry.get().add_middleware(self.__class__)
        return self
