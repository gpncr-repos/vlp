import uuid

from sqlalchemy import Column, ForeignKey, JSON, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from src.db import Base


class WellData(Base):
    __tablename__ = "well_data"

    id = Column(String, primary_key=True)
    inclinometry = Column(JSON, comment="Инклинометрия")
    d_cas = Column(Float, comment="Диаметр ЭК, м")
    d_tub = Column(Float, comment="Диаметр НКТ, м")
    h_tub = Column(Float, comment="Глубина спуска НКТ, м")
    wct = Column(Float, comment="Обводненность, %")
    rp = Column(Float, comment="Газовый фактор, м3/т")
    gamma_oil = Column(Float, comment="Плотность нефти")
    gamma_gas = Column(Float, comment="Плотность газа")
    gamma_wat = Column(Float, comment="Плотность воды")
    t_res = Column(Float, comment="Температура пласта, С")
    p_wh = Column(Float, comment="Буферное давление, атм")
    geo_grad = Column(Float, comment="Температурный градиент, С/100 м")
    h_res = Column(Float, comment="Глубина верхних дыр перфорации, м")

    vlp = relationship("VLP", back_populates="data")


class VLP(Base):
    __tablename__ = "vlp"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    vlp = Column(JSON, comment="VLP")
    well_id = Column(String, ForeignKey("well_data.id"))

    data = relationship("WellData", back_populates="vlp")
