from pydantic import BaseModel, Field
import requests

class Service(BaseModel):
    id: int
    title: str

    model_config = {"populate_by_name": True}

class Properties(BaseModel):
    device_name: str = Field(alias="deviceName")
    image: str
    imei: str
    meid: str
    imei2: str
    serial: str
    estimate_pruchase_date: int = Field(alias="estPurchaseDate")
    sim_lock: bool = Field(alias="simLock")
    replaced: bool
    apple_or_region: str = Field(alias="apple/region")
    loaner: bool

    model_config = {"populate_by_name": True}

class ImeiCheckRequest(BaseModel):
    device_id: str = Field(alias="deviceId")
    service_id: int = Field(alias="serviceId")

    model_config = {"populate_by_name": True}

class ImeiCheckResponse(BaseModel, extra="allow"):
    warning: str = Field(alias="!!! WARNING !!!")
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
    def __init__(self, base_url: str | None, token: str | None) -> None:
        if not base_url or not token:
            raise ValueError("either base_url or token missing")

        self.base_url = base_url
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-type": "application/json",
        }


    def check_device(self, device_id: str) -> ImeiCheckResponse:
        url = f"{self.base_url}/v1/checks"
        payload = ImeiCheckRequest.model_construct(device_id=device_id, service_id=12)

        response = requests.get(
            url,
            headers=self.headers,
            data=payload.model_dump_json(by_alias=True)
        )

        return ImeiCheckResponse.model_validate(response.json()[0])
