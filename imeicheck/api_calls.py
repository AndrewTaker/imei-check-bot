from pydantic import BaseModel, Field
import requests
import datetime

class Service(BaseModel):
    """Model representing 'service' entity at imeicheck.net"""
    id: int
    title: str

    model_config = {"populate_by_name": True}

class Properties(BaseModel):
    """Model representing 'properties' nested entity at imeicheck.net"""
    device_name: str = Field(alias="deviceName", default="")
    image: str = Field(default="")
    imei: str = Field(default="")
    meid: str = Field(default="")
    imei2: str = Field(default="")
    serial: str = Field(default="")
    estimate_pruchase_date: int = Field(alias="estPurchaseDate", default=0)
    sim_lock: bool | None = Field(alias="simLock", default=None)
    replaced: bool | None = Field(default=None)
    apple_or_region: str = Field(alias="apple/region", default="")
    loaner: bool | None = Field(default=None)

    model_config = {"populate_by_name": True}

class ImeiCheckRequest(BaseModel):
    """Model representing request payload for imeicheck.net."""
    device_id: str = Field(alias="deviceId")
    service_id: int = Field(alias="serviceId")

    model_config = {"populate_by_name": True}

class ImeiCheckResponse(BaseModel):
    """Model representing imei response at api/checks."""
    id: str
    type: str = Field(alias="type")
    status: str
    order_id: str | None = Field(alias="orderId", default=None)
    service: Service
    amount: str
    device_id: str = Field(alias="deviceId")
    processed_at: int = Field(alias="processedAt")
    properties: Properties

    model_config = {"populate_by_name": True}

class ImeiService:
    """Simple wrapper to communicate with imeicheck.net api."""
    def __init__(self, base_url: str | None, token: str | None) -> None:
        if not base_url or not token:
            raise ValueError("either base_url or token missing")

        self.base_url = base_url
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-type": "application/json",
        }

    def time(self) -> str:
        return datetime.datetime.now().strftime("%H:%M:%S")

    def check_device(self, device_id: str) -> ImeiCheckResponse:
        """POST request to retrieve IMEI data."""
        url = f"{self.base_url}/v1/checks"
        payload = ImeiCheckRequest.model_construct(device_id=device_id, service_id=12)

        response = requests.get(
            url=url,
            headers=self.headers,
            data=payload.model_dump_json(by_alias=True)
        )

        return ImeiCheckResponse.model_validate(response.json()[0])
