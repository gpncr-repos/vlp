from src.calculations.vlp import calc_vlp as vlp_calculation
from fastapi import APIRouter, Depends
from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import save_init_data, save_vlp_data
from src.db import get_session

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
def calc_vlp(vlp_in: VlpCalcRequest, session=Depends(get_session)):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    init_data_id = save_init_data(session, vlp_in.dict())

    vlp_result = vlp_calculation(**vlp_in.dict())

    save_vlp_data(session, vlp_result, init_data_id)

    return VlpCalcResponse.parse_obj(vlp_result)


@main_router.get('/get-vlp-id-by-depth')
def get_vlp():
    """Вернуть все VLP ID больше глубины скважины по возрастанию глубины"""
    pass


@main_router.get('/get-vlp-by-id')
def get_vlp():
    """Вернуть VLP по ID"""
    pass
