from src.calculations.vlp import calc_vlp as vlp_calculation
from fastapi import APIRouter
from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import save_init_data, save_vlp_data, get_check_well_data_exists, get_check_vlp_exists
from src.db import get_session
from hashlib import sha256
import json

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
def calc_vlp(vlp_in: VlpCalcRequest):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    session = get_session()

    init_data = vlp_in.dict()
    well_data_hash = sha256(json.dumps(init_data).encode()).hexdigest()
    well_data_id = get_check_well_data_exists(session, well_data_hash)

    if not well_data_id:
        save_init_data(session, init_data, well_data_hash)
        well_data_id = well_data_hash

    vlp_result = get_check_vlp_exists(session, well_data_id)

    if not vlp_result:
        vlp_result = vlp_calculation(**init_data)
        save_vlp_data(session, vlp_result, well_data_id)

    return VlpCalcResponse.parse_obj(vlp_result)
