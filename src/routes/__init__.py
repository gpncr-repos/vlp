from src.calculations.vlp import calc_vlp
from fastapi import APIRouter, Depends
from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import save_init_data, save_vlp_data
from src.db import get_session

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
def my_profile(vlp_in: VlpCalcRequest, session=Depends(get_session)):
    init_data_id = save_init_data(session, vlp_in.dict())

    vlp_result = calc_vlp(**vlp_in.dict())

    save_vlp_data(session, vlp_result, init_data_id)

    return VlpCalcResponse.parse_obj(vlp_result)
