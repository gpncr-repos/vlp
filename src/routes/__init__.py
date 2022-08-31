from fastapi import APIRouter, Depends
import json

from src import db
from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import save_init_data, save_vlp_data, get_check_well_data_exists, get_check_vlp_exists

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
def calc_vlp(vlp_in: VlpCalcRequest):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    # функция считающая VLP
    from src.calculations.vlp import calc_vlp as vlp_calculation  # noqa
    jsonData = json.dumps(vlp_in.dict())
    hashData = str(hash(jsonData))

    guid = queries.get_check_well_data_exists(db.get_session(), hashData)

    if not guid:
        result = vlp_calculation(vlp_in.inclinometry.dict(), vlp_in.casing.dict(), vlp_in.tubing.dict(),
                                 vlp_in.pvt.dict(), vlp_in.p_wh, vlp_in.geo_grad, vlp_in.h_res)
        save_init_data(db.get_session(), vlp_in, hashData)
        save_vlp_data(db.get_session(), json.dumps(result), hashData)
        return result
    else:
        vlpstr = get_check_vlp_exists(db.get_session(), hashData)
        result = json.loads(vlpstr)
        return result
