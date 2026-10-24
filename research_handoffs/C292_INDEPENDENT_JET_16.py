#!/usr/bin/env python3
"""Independent 16-center 2nd-order automatic differentiation cross-check for C292 (16 fixed centers).

This is a pointwise software cross-check, not a substitute for the C292
continuous-box rational enclosures.
"""
from fractions import Fraction as F
import C291_INDEPENDENT_SECOND_JET as jet
import C292_VERIFY as theorem


def run():
    paths,_=jet.c288.build_paths()
    W,_=jet.s.floor_fixed_masses()
    assert len(paths)==125
    n=0
    min_point_gap=None
    for idx in range(0,len(paths),8):
        p=paths[idx]
        B=tuple((lo-jet.c290.PAD,hi+jet.c290.PAD) for lo,hi in p['box'])
        mid=tuple((lo+hi)/2 for lo,hi in B)
        J=jet.direct_jet(mid,W)
        assert J.v==jet.s.original_F(mid,W)
        for i in range(4):
            assert J.h[i][i]/jet.s.Q>theorem.D[i]
            for j in range(4):
                t=J.h[i][j]/jet.s.Q
                assert J.h[i][j]==J.h[j][i]
                assert abs(t)<theorem.C[i][j]
                n+=1
            gap=J.h[i][i]/jet.s.Q-sum(abs(J.h[i][j]/jet.s.Q) for j in range(4) if j!=i)
            assert gap>312
            if min_point_gap is None or gap<min_point_gap:min_point_gap=gap
        print(f'CHECKPOINT index {idx}/124 independent direct second-jet',flush=True)
    print('C292_INDEPENDENT_PRODUCT_JET_16_PASS',n//16,'centers',n,'ordered Hessian entries')
    print('all pointwise Gershgorin gaps >312; these are checks, not full box proofs')
    return min_point_gap

if __name__=='__main__':run()
