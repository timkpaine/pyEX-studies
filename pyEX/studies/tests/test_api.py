# for Coverage
import time
from mock import patch, MagicMock
import pandas as pd

C = MagicMock()
S = 'AAPL'

C.chartDF.return_value = pd.DataFrame({'open': [1., 2., 3., 4.], 'close': [1., 2., 3., 4.], 'high': [1., 2., 3., 4.], 'low': [1., 2., 3., 4.]})


class TestAPI:
    def test_peercorrelation(self):
        from pyEX.studies import peerCorrelation
        peerCorrelation(C, S, '6m')

    def test_bollinger(self):
        from pyEX.studies import bollinger
        bollinger(C, S, '6m')

    def test_emasma(self):
        from pyEX.studies import ema, sma, dema
        ema(C, S)
        ema(C, S, periods=30)
        ema(C, S, periods=[30, 45])
        dema(C, S)
        dema(C, S, periods=30)
        dema(C, S, periods=[30, 45])
        sma(C, S)
        sma(C, S, periods=30)
        sma(C, S, periods=[30, 45])

    def test_sar(self):
        from pyEX.studies import sar
        sar(C, S)

    def test_rsi(self):
        from pyEX.studies import rsi
        rsi(C, S)
