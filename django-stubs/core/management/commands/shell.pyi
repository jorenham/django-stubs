from typing import Any

from django.core.management import BaseCommand

class Command(BaseCommand):
    shells: list[str]

    def handle(self, **options: Any) -> None: ...
    def ipython(self, options: Any) -> None: ...
    def bpython(self, options: Any) -> None: ...
    def python(self, options: Any) -> None: ...
    def get_auto_imports(self) -> list[str]: ...
    def get_namespace(self, **options: Any) -> dict[str, Any]: ...
