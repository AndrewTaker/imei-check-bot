from pydantic import BaseModel, Field

class Service(BaseModel):
    id: int
    title: str

class Properties(BaseModel):
    device_name: str = Field(alias="deviceName")
    image: str
    imei: str
    estimate_pruchase_date: int = Field(alias="estPurchaseDate")
    sim_lock: bool = Field(alias="simLock")
    warranty_status: str = Field(alias="warrantyStatus")
    repair_coverage: str = Field(alias="repairCoverage")
    technical_support: str = Field(alias="technicalSupport")
    model_description: str = Field(alias="modelDesc")
    demo_unit: bool = Field(alias="demoUnit")
    refurbished: bool
    purchase_country: str = Field(alias="purchaseCountry")
    apple_or_region: str = Field(alias="apple/region")
    fmi_on: bool = Field(alias="fmi_on")
    lost_mode: str = Field(alias="lostMode")
    usa_block_status: str = Field(alias="usaBlockStatus")
    network: str


class ImeiCheckRequest(BaseModel):
    device_id: str = Field(alias="deviceId")
    service_id: int = Field(alias="serviceId")

class ImeiCheckResponse(BaseModel):
    id: str
    _type: str = Field(alias="type")
    status: str
    order_id: str = Field(alias="orderId")
    service: Service
    amount: str
    device_id: str = Field(alias="deviceId")
    processed_at: int = Field(alias="processedAt")
    properties: Properties

class ImeiService:
    def __init__(self, base_url: str | None, token: str | None) -> None:
        if not base_url or not token:
            raise ValueError("not base url or token")

        self.base_url = base_url
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}


    def ch
    def __repr__(self) -> str:
        return f"base_url = {self.base_url}, token = {self.token}"
