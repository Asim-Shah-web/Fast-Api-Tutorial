from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


# Inherit SQLModel and set table = True
# to make a table in database
class Shipment(SQLModel, table = True):
    # Optional table name
    __tablename__ = "shipment"

    # Primary key with default value will be
    # assigned and incremented automatically
    id: int = Field(default=None, primary_key=True)
    
    content: str
    weight: float = Field(le=25)
    destination: int
    status: ShipmentStatus
    estimated_delivery: datetime