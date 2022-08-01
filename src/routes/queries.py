from src.tables.models import WellData, VLP


def save_init_data(session, init_data):
    well_data = WellData(
        inclinometry=init_data["inclinometry"],
        d_cas=init_data["casing"]["d"],
        d_tub=init_data["tubing"]["d"],
        h_tub=init_data["tubing"]["h_mes"],
        wct=init_data["pvt"]["wct"],
        rp=init_data["pvt"]["rp"],
        gamma_oil=init_data["pvt"]["gamma_oil"],
        gamma_gas=init_data["pvt"]["gamma_gas"],
        gamma_wat=init_data["pvt"]["gamma_wat"],
        t_res=init_data["pvt"]["t_res"],
        p_wh=init_data["p_wh"],
        geo_grad=init_data["geo_grad"],
        h_res=init_data["h_res"]
    )
    session.add(well_data)
    session.commit()
    return well_data.id


def save_vlp_data(session, vlp, init_data_id):
    vlp = VLP(
        vlp=vlp,
        data_id=init_data_id
    )
    session.add(vlp)
    session.commit()
    return vlp.id
