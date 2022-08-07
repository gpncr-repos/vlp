import random
from mock import patch
import numpy as np
import src.routes.queries as q
from src.tables.models import VLP, WellData


def generate_data_for_tests():
    return {
        "inclinometry": {
            "MD": [0, 1000, 1500],
            "TVD": [0, 1000, 1100]
        },
        "casing": {
            "d": np.random.uniform(0.062, 0.2)
        },
        "tubing": {
            "d": np.random.uniform(0.04, 0.06),
            "h_mes": np.random.uniform(100, 1000)
        },
        "pvt": {
            "wct": np.random.uniform(0, 100),
            "rp": np.random.uniform(0, 500),
            "gamma_oil": np.random.uniform(0.7, 0.9),
            "gamma_gas": np.random.uniform(0.6, 0.8),
            "gamma_wat": np.random.uniform(1, 1.1),
            "t_res": np.random.uniform(30, 100),
        },
        "p_wh": np.random.uniform(20, 40),
        "geo_grad": np.random.uniform(0.1, 2),
        "h_res": np.random.uniform(1100, 2000),
    }


def fill_tables(session, n=60):
    for _ in range(n):
        init_data = generate_data_for_tests()
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
        vlp = VLP(data=well_data, vlp={"q_liq": [np.random.uniform(100, 1000), np.random.uniform(100, 1000)],
                                       "p_wf": [np.random.uniform(100, 1000), np.random.uniform(100, 1000)]})
        session.add_all([well_data, vlp])
    session.flush()


def test_calc_model_success(api_client, sa_session):
    response = api_client.post("vlp/calc",
                               json=generate_data_for_tests())
    assert response.status_code == 200
    result = response.json()
    assert result
    assert result["p_wf"]
    assert result["q_liq"]


def test_get_vlp_id_by_depth(api_client, sa_session):
    fill_tables(sa_session)
    depth = 1500
    vlp_ids = q.get_vlp_ids(sa_session, depth)

    with patch("src.db.get_session") as get_session_test:
        get_session_test.return_value = sa_session
        response = api_client.get(f"vlp/get-vlp/depth/up-{depth}")
        assert response.status_code == 200
        result = response.json()

        for true_val, resp_val in zip(vlp_ids, result):
            assert resp_val["id"] == str(true_val[0])


def test_get_vlp_by_id(api_client, sa_session):
    fill_tables(sa_session)
    vlp = sa_session.query(VLP.id, VLP.vlp).first()

    with patch("src.routes.get_session") as get_session_test:
        get_session_test.return_value = sa_session
        response = api_client.get(f"vlp/get-vlp/depth/{vlp[0]}")
        assert response.status_code == 200
        result = response.json()
        assert result["vlp"] == vlp.vlp
