from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )

    phone_number: Mapped[str] = mapped_column(
        String(20), unique=True, nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        String(150), nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(20), default="renter", nullable=False
    )

    verification_status: Mapped[str] = mapped_column(
        String(20), default="pending", nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
