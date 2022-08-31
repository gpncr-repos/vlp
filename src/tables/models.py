from src.db import Base
import sqlalchemy as sa


class WellData(Base):
    __tablename__ = "well_data"

    id = sa.Column('id', sa.String, primary_key=True, comment="Идентификатор набора входных данных")
    inclinometry = sa.Column('inclinometry', sa.String, nullable=False, comment="Инклинометрия")
    d_cas = sa.Column('d_cas', sa.Float, nullable=False, comment="Данные по ЭК")
    h_tub = sa.Column('h_tub', sa.Float, nullable=False, comment="Глубина спуска НКТ, м")
    d_tub = sa.Column('d_tub', sa.Float, nullable=False, comment="Данные по НКТ")
    wct = sa.Column("wct", sa.Float, nullable=False, comment="Обводненность, %")
    rp = sa.Column("rp", sa.Float, nullable=False, comment="Газовый фактор, м3/т")
    gamma_oil = sa.Column("gamma_oil", sa.Float, nullable=False, comment="Отн. плотность нефти")
    gamma_gas = sa.Column("gamma_gas", sa.Float, nullable=False, comment="Отн. плотность газа")
    gamma_wat = sa.Column("gamma_wat", sa.Float, nullable=False, comment="Отн. плотность воды")
    t_res = sa.Column("t_res", sa.Float, nullable=False, comment="Пластовая температура, C")
    p_wh = sa.Column("p_wh", sa.Float, nullable=False, comment="Буферное давление, атм")
    geo_grad = sa.Column("geo_grad", sa.Float, nullable=False, comment="Градиент температуры, C/100 м")
    h_res = sa.Column("h_res", sa.Float, nullable=False, comment="Глубина Верхних Дыр Перфорации, м")

class VLP(Base):
    __tablename__ = "vlp"

    well_id = sa.Column('well_id', sa.String, primary_key=True, comment="Дебиты жидкости, м3/сут")
    vlp = sa.Column('vlp', sa.String, nullable=False, comment="Забойное давление, атм")
