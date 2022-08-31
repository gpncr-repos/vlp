from fastapi import APIRouter
import json
from src.db import get_session
from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import save_init_data, save_vlp_data, get_check_well_data_exists, get_check_vlp_exists

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
def calc_vlp(vlp_in: VlpCalcRequest):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    # функция считающая VLP
    from src.calculations.vlp import calc_vlp as vlp_calculation  # noqa

    session = get_session()
    if get_check_well_data_exists(session, str(hash(str(vlp_in)))):
        vlp = get_check_vlp_exists(session, str(hash(str(vlp_in))))
        return VlpCalcResponse.parse_raw(vlp)

    print(vlp_in.dict()["casing"]["d"])
    save_init_data(session, vlp_in.dict(), str(hash(str(vlp_in))))
    result = vlp_calculation(vlp_in.inclinometry.dict(),
                    vlp_in.casing.dict(),
                    vlp_in.tubing.dict(),
                    vlp_in.pvt.dict(),
                    vlp_in.p_wh,
                    vlp_in.geo_grad,
                    vlp_in.h_res)

    save_vlp_data(session, result, str(hash(str(result))), str(hash(str(vlp_in))))
    return VlpCalcResponse.parse_obj(result)
