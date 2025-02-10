from dataclasses import dataclass
from dataclasses import field


@dataclass
class Message:
    content: str = field()
    role: str = field()
