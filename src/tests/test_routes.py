import pytest
import requests
import json

@pytest.fixture
def generate_data_for_tests():
    return {
  "inclinometry": {
    "MD": [
      0,
      1000,
      1500
    ],
    "TVD": [
      0,
      1000,
      1100
    ]
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


def test_calc_model_success(api_client, generate_data_for_tests):
    response = requests.post(url="http://localhost:8001/vlp/calc",
                             json=generate_data_for_tests)
    answer = {
  "q_liq": [
    0,
    66.67,
    133.33,
    200,
    266.67,
    333.33,
    400
  ],
  "p_wf": [
    41.13,
    17.75,
    20.4,
    27.31,
    36.94,
    48.67,
    62.29
  ]
}
    text = response.text
    print()
    text = json.loads(text)
   # assert response.status_code == 200
    print()
    assert dict(text) == answer