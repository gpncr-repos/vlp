from src.db import Base
from typing import List
import sqlalchemy as sa

class WellData(Base):
    __tablename__ = "well_data"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, comment="")
    MD = sa.Column(sa.String,  comment="Измеренная по стволу глубина,м")
    TVD = sa.Column(sa.String, comment="Вертикальная глубина,м")
    d_casing = sa.Column(sa.Float, comment="Данные по ЭК")
    d_tubing = sa.Column(sa.Float, comment="Данные по МКТ")
    h_mes_tubing = sa.Column(sa.Float,comment="Глубина спуска МКТ, м")
    wct = sa.Column(sa.Integer,comment="Обводненность, %")
    rp = sa.Column(sa.Integer,comment="Газовый фактор,м3/т")
    gamma_oil = sa.Column(sa.Float,comment="Относительная плотность нефти")
    gamma_gas = sa.Column(sa.Float,comment="Относительная плотность газа ")
    gamma_wat = sa.Column(sa.Float,comment="Относительная плотность воды")
    t_res = sa.Column(sa.Integer,comment="Пластовая температура, С")
    p_wh = sa.Column(sa.Integer,comment="Буферное давление, атм")
    geo_grad = sa.Column(sa.Integer,comment="Градиент температуры, C/100 м")
    h_res = sa.Column(sa.Integer,comment="Глубина Верхних Дыр Перфорации, м")


class VLP(Base):
    __tablename__ = "vlp"
    id = sa.Column(sa.Integer,primary_key=True, comment="id", autoincrement=True)
    q_liq = sa.Column(sa.String,comment="Дебиты жидкости, м3/сут")
    p_wf = sa.Column(sa.String, comment=' Забойное давление, атм')
