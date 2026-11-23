"""R139: uniform D-tube strict-near robustness, using R138 full-B certificate."""
from fractions import Fraction as Q
from x6_r138_all_B_fixed_D500_verify import CELLS, TARGET, all_directions, affine, nonnegative

def run():
    dirs=all_directions()
    assert len(dirs)==1935
    inchecks=outchecks=0
    for lo,hi,K,L0,L1,wit in CELLS:
        for a in TARGET:
            for j in range(6):
                assert nonnegative(affine(dirs[a],j,K,L0,L1,-7,-10),lo,hi),(a,lo,j)
                inchecks+=1
        for a,g in dirs.items():
            if a in TARGET:continue
            assert any(nonnegative(affine(g,j,K,L0,L1,5,8),lo,hi) for j in range(6)),(a,lo)
            outchecks+=1
    R=Q(500,41)
    # At the open outer boundary the inner ratio bound reaches 3/2 exactly.
    assert (Q(500)+R)/(Q(500)-R)==Q(21,20)
    assert Q(8,5)*((Q(500)-R)/(Q(500)+R)) > Q(3,2)
    print('R139 UNIFORM TUBE CERTIFICATE PASS')
    print('insider_upper_margin_checks',inchecks,'outsider_lower_margin_checks',outchecks)
    print('insider_F_over_eta_upper',Q(10,7),'outsider_F_over_eta_lower',Q(8,5))
    print('uniform_open_D_interval',str(Q(20000,41)),str(Q(21000,41)))
if __name__=='__main__':run()
