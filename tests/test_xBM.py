from __future__ import division

import numpy as np
import biggles

from traveling_waves import run_middle_ear_filter, _tw, S_ST, bm_pars

def main():
    fs = 48000                  # Hz

    forward = np.loadtxt('forward.txt') * S_ST
    t = np.arange(len(forward)) / fs * 1000

    ref = np.loadtxt('xBM_70.txt')


    xBM = _tw.bm_wave(fs=48000,
                      signal=forward)
    xBM = xBM[:,70]


    sec = range(400, 1000)
    t = t[sec]
    xBM = xBM[sec]
    ref = ref[sec]
    p = biggles.FramedPlot()
    p.add( biggles.Curve(t, ref, color='red', width=3))
    p.add( biggles.Curve(t, xBM))
    p.show()




if __name__ == "__main__":
    main()
