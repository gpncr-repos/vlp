from src.db import Base
from typing import List
import sqlalchemy as sa

class WellData(Base):
    __tablename__ = "well_data"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    MD = sa.Column(sa.String,  comment="")
    TVD = sa.Column(sa.String)
    d_casing = sa.Column(sa.Float)
    d_tubing = sa.Column(sa.Float)
    h_mes_tubing = sa.Column(sa.Float)
    wct = sa.Column(sa.Integer)
    rp = sa.Column(sa.Integer)
    gamma_oil = sa.Column(sa.Float)
    gamma_gas = sa.Column(sa.Float)
    gamma_wat = sa.Column(sa.Float)
    t_res = sa.Column(sa.Integer)
    p_wh = sa.Column(sa.Integer)
    geo_grad = sa.Column(sa.Integer)
    h_res = sa.Column(sa.Integer)


class VLP(Base):
    __tablename__ = "vlp"
    id = sa.Column(sa.Integer,primary_key=True, comment="id", autoincrement=True)
    q_liq = sa.Column(sa.String,comment="Дебиты жидкости, м3/сут")
    p_wf = sa.Column(sa.String, comment=' Забойное давление, атм')
