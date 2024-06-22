from typing import Any, Type, TypeVar
from typing_extensions import TypeGuard as Guard

T = TypeVar('T', bound=Type)
def definitely(_: Any, __: T) -> Guard[T]:
  return True
