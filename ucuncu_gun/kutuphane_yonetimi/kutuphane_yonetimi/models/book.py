from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str
    is_available: bool = True