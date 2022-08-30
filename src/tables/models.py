from src.db import Base
import sqlalchemy as sa


class WellData(Base):
    __tablename__ = "well_data"

    id = sa.Column(sa.String, primary_key=True, comment="Идентификатор записи")
    inclinometry = sa.Column(sa.String, comment="Инклинометрия скважины в формате MD, TVD")
    casing = sa.Column(sa.Float, comment="Данные по Эксплуатационной Колонне")
    tubing = sa.Column(sa.String, comment="Данные по Колонне Насосно-Компрессорных Труб")
    pvt = sa.Column(sa.String, comment="Данные по флюидам")
    p_wh = sa.Column(sa.Integer, comment="Буферное давление, атм")
    geo_grad = sa.Column(sa.Integer, comment="Геотермический градиент, C/100 м")
    h_res = sa.Column(sa.Integer, comment="Глубина верхних дыр перфорации, м")


class VLP(Base):
    __tablename__ = "vlp"

    id = sa.Column(sa.String, primary_key=True, comment="Идентификатор записи")
    q_list = sa.Column(sa.ARRAY(sa.Float), comment="Массив дебитов жидкости")
    p_wf = sa.Column(sa.ARRAY(sa.Float), comment="Массив забойных давлений")
