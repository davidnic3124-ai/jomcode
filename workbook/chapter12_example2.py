from dataclasses import dataclass

@dataclass
class Workshop:
    title: str
    capacity: int

workshop = Workshop("Python",20)
print(workshop.title,workshop.capacity)