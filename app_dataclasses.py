from dataclasses import dataclass


@dataclass(frozen=True)
class MoveChoice:

    description: str
    next_location_id: str
    next_level_id: str


@dataclass(frozen=True)
class Location:

    id: str
    name: str
    description: str
    move_choices: tuple[MoveChoice, ...]
    pictures: list[str]  # MUST be more than 4


@dataclass(frozen=True)
class Level:

    id: str
    name: str
    locations: tuple[Location, ...]

    def get_location_by_id(self, location_id: str) -> Location | None:
        for location in self.locations:
            if location.id == location_id:
                return location
