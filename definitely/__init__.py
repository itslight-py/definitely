from typing import Any, Type, TypeVar
from typing_extensions import TypeGuard as Guard

T = TypeVar('T')
def definitely(_: Any, __: Type[T]) -> Guard[T]:
  return True
