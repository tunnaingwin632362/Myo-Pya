from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from models import ListingStatus

# Auth
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    is_admin: bool

# Listings
class ListingCreate(BaseModel):
    title: str
    description: Optional[str]
    price: float
    address: str
    city: str
    state: Optional[str]
    zip_code: Optional[str]
    bedrooms: Optional[int]
    bathrooms: Optional[float]
    sqft: Optional[int]
    lot_size: Optional[float]
    year_built: Optional[int]
    status: ListingStatus = ListingStatus.for_sale
    property_type: str = "house"
    images: Optional[str] = "[]"
    amenities: Optional[str] = "[]"
    agent_id: Optional[int]
    is_featured: bool = False

class ListingUpdate(ListingCreate):
    pass

class ListingOut(ListingCreate):
    id: int
    views: int
    created_at: datetime
    class Config:
        from_attributes = True

# Agents
class AgentCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str]
    title: Optional[str]
    bio: Optional[str]
    avatar_url: Optional[str]
    market: Optional[str]
    years_experience: Optional[int]

class AgentOut(AgentCreate):
    id: int
    properties_sold: int
    rating: float
    is_active: bool
    class Config:
        from_attributes = True

# Inquiries
class InquiryCreate(BaseModel):
    listing_id: Optional[int]
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str]
    interest: str
    message: str

class InquiryOut(InquiryCreate):
    id: int
    is_read: bool
    created_at: datetime
    class Config:
        from_attributes = True