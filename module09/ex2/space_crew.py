from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"

rank.cadet

class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        high_ranks = {Rank.captain, Rank.commander}
        if not any(m.rank in high_ranks for m in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions require at least 50% experienced crew "
                    "(5+ years)"
                )

        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(
                f"All crew members must be active. Inactive: {inactive}"
            )

        return self


def main() -> None:
    """Demonstrate SpaceMission model validation."""
    print("Space Mission Crew Validation")
    print("========================================")

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-06-01T09:00:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=42,
                specialization="Mission Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=28,
                specialization="Engineering",
                years_experience=5,
            ),
        ],
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"  - {member.name} ({member.rank.value}) - {member.specialization}")

    print("========================================")

    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Doomed Mission",
            destination="Venus",
            launch_date="2024-07-01T09:00:00",
            duration_days=30,
            budget_millions=500.0,
            crew=[
                CrewMember(
                    member_id="CM010",
                    name="Bob Nobody",
                    rank=Rank.cadet,
                    age=22,
                    specialization="Maintenance",
                    years_experience=1,
                ),
            ],
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
