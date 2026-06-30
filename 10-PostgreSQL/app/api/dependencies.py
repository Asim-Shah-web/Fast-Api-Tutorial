from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.services.shipment import ShipmentService


# Asynchronous database session dep annotation
SessionDep = Annotated[AsyncSession, Depends(get_session)]


# Shipment service dep
def get_shipment_service(session: SessionDep):
    return ShipmentService(session)


# Shipment service dep annotation
ServiceDep = Annotated[
    ShipmentService,
    Depends(get_shipment_service),
]
