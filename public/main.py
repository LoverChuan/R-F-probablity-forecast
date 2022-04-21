import numpy as np
import LinearRegression as lR
import LogisticRegression as LgR

filenames = ["ag_15m.txt", "al_15m.txt", "au_15m.txt", "bu_15m.txt",
             "cf_15m.txt", "cu_15m.txt", "dci_15m.txt", "dcp_15m.txt",
             "fg_15m.txt", "jm_15m.txt", "j_15m.txt", "ma_15m.txt",
             "ni_15m.txt", "pb_15m.txt", "rb_15m.txt", "sn_15m.txt",
             "sr_15m.txt", "zn_15m.txt"]


if __name__ == '__main__':
    for filename in filenames:
        lR.f(filename)
