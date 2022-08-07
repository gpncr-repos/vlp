from src.calculations.vlp import calc_vlp as vlp_calculation
from fastapi import APIRouter, Depends
from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import save_init_data, save_vlp_data
from src.db import get_session

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
def calc_vlp(vlp_in: VlpCalcRequest):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    session = get_session()

    init_data_id = save_init_data(session, vlp_in.dict())

    vlp_result = vlp_calculation(**vlp_in.dict())

    save_vlp_data(session, vlp_result, init_data_id)

    return VlpCalcResponse.parse_obj(vlp_result)


@main_router.get('/get-vlp/depth/up-{depth}')
def get_vlp_id_by_depth(depth: float):
    """Вернуть все VLP ID больше глубины скважины по возрастанию глубины"""
    session = get_session()
    vlp_ids = queries.get_vlp_ids(session, depth)
    return vlp_ids


@main_router.get('/get-vlp/depth/{vlp_id}')
def get_vlp_by_id(vlp_id):
    """Вернуть VLP по ID"""
    session = get_session()
    vlp = queries.get_vlp_by_id(session, vlp_id)
    return vlp
