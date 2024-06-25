from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class RepositoryInterface(Generic[T]):
    
    def read(id:str) -> Optional[T]:
        pass
    
    def write(id:str, obj: T):
        pass