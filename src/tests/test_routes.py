import pytest


@pytest.fixture
def generate_data_for_tests():
    data = {
            "inclinometry": {
                "MD": [0, 1000, 1500],
                "TVD": [0, 1000, 1100]
            },
            "casing": {
                "d": 0.1
            },
            "tubing": {
                "d": 0.062,
                "h_mes": 1000
            },
            "pvt": {
                "wct": 50,
                "rp": 100,
                "gamma_oil": 0.8,
                "gamma_gas": 0.7,
                "gamma_wat": 1,
                "t_res": 90
            },
            "p_wh": 10,
            "geo_grad": 3,
            "h_res": 1500
    }
    return data


def test_calc_model_success(api_client, generate_data_for_tests):
    response = api_client.post('http://127.0.0.1:8001/vlp/calc', json=generate_data_for_tests)
    assert response.status_code == 200
    assert response.json


