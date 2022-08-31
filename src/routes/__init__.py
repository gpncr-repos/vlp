from fastapi import APIRouter
from models.models import VlpCalcRequest, VlpCalcResponse
from routes.queries import save_well_data, save_vlp_data, get_check_well_data_exists, get_check_vlp_exists
from .queries import save_well_data
from db import get_session
main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc",response_model=VlpCalcResponse )
def calc_vlp(vlp_in: VlpCalcRequest):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    # функция считающая VLP
    from src.calculations.vlp import calc_vlp as vlp_calculation # noqa
    res = vlp_calculation(dict(vlp_in.inclinometry), dict(vlp_in.casing), dict(vlp_in.tubing), dict(vlp_in.pvt),
                    vlp_in.p_wh, vlp_in.geo_grad, vlp_in. h_res)
    save_well_data(get_session(), vlp_in)
    save_vlp_data(get_session(),res)
    return res