from pydantic import BaseModel


class Bookings(BaseModel):
    firstName: str
    secondName: str
    carNumber: str
    parkingLot: int


class ParkingLots(BaseModel):
    id: int
    status: int


class EndingBooking(BaseModel):
    parking_lot: int


class AdminRequest(BaseModel):
    login: str
    password: str


class AdminBook(BaseModel):
    parkingLot: int
    carNumber: str
