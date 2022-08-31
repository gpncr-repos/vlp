from src.db import Base
import sqlalchemy as sa


class WellData(Base):
    __tablename__ = "well_data"

    id = sa.Column(sa.String, primary_key=True, comment="Идентификатор записи")
    inclinometry = sa.Column(sa.String, comment="Инклинометрия скважины в формате MD, TVD")
    d_cas = sa.Column(sa.Float, comment="Диаметр ЭК, м")
    d_tub = sa.Column(sa.Float, comment="Диаметр НКТ, м")
    h_tub = sa.Column(sa.Float, comment="Глубина спуска НКТ, м")
    wct = sa.Column(sa.Integer, comment="Обводнённость, %")
    rp = sa.Column(sa.Float, comment="Газовый фактор, м3/т")
    gamma_oil = sa.Column(sa.Float, comment="Относительная плотность нефти")
    gamma_gas = sa.Column(sa.Float, comment="Относительная плотность газа")
    gamma_wat = sa.Column(sa.Float, comment="Относительная плотность воды")
    t_res = sa.Column(sa.Float, comment="Температура пласта, С")
    p_wh = sa.Column(sa.Integer, comment="Буферное давление, атм")
    geo_grad = sa.Column(sa.Integer, comment="Геотермический градиент, C/100 м")
    h_res = sa.Column(sa.Integer, comment="Глубина верхних дыр перфорации, м")


class VLP(Base):
    __tablename__ = "vlp"

    id = sa.Column(sa.String, primary_key=True, comment="Идентификатор записи")
    well_id = sa.Column(sa.String, comment="Идентификатор скважины")
    vlp = sa.Column(sa.String, comment="Массив дебитов жидкости")
