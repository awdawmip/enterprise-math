from fractions import Fraction as F
import unittest

from enterprise_math.brc_transport import (
    Affine, EffectHistogram, MomentState, eye, matrix, point_moment,
    euclidean_digits, recompose, mm, inv,
)
from enterprise_math.brc_histogram import histogram_serial

class BRCAffineTransportTests(unittest.TestCase):
    def test_joint_weight_action_correlation(self):
        plus=Affine(eye(1),(F(1),)); minus=Affine(eye(1),(F(-1),))
        a=EffectHistogram.from_terms(1,[(1,plus,1),(2,minus,1)])
        b=EffectHistogram.from_terms(1,[(2,plus,1),(1,minus,1)])
        self.assertEqual(a.forget_effects(), b.forget_effects())
        ma=a.moment_action(point_moment((0,))); mb=b.moment_action(point_moment((0,)))
        self.assertEqual(ma[0][1]/ma[1][1], F(-1,3))
        self.assertEqual(mb[0][1]/mb[1][1], F(1,3))

    def test_serial_projection_and_moment_composition(self):
        p=EffectHistogram.from_terms(1,[(F(2,3),Affine(eye(1),(F(1),)),2)])
        q=EffectHistogram.from_terms(1,[(F(3,5),Affine(eye(1),(F(-2),)),1)])
        self.assertEqual(p.then(q).forget_effects(), histogram_serial(p.forget_effects(),q.forget_effects()))
        m=point_moment((3,))
        self.assertEqual(p.then(q).moment_action(m), q.moment_action(p.moment_action(m)))

    def test_moment_state_six_axis_path_compression(self):
        dim=6
        rot=matrix([[int(i==(j+1)%dim) for j in range(dim)] for i in range(dim)])
        step=EffectHistogram.from_terms(dim,[(1,Affine(rot,(F(1),)+(F(0),)*5),1),(1,Affine(rot,(F(-1),)+(F(0),)*5),1)])
        state=MomentState.from_point((0,)*dim)
        for _ in range(32): state=state.then(step)
        m=state.to_matrix(); mass=2**32
        self.assertEqual(m[-1][-1], mass)
        cov=tuple(tuple(m[i][j]/mass for j in range(dim)) for i in range(dim))
        self.assertEqual(cov, matrix([[([6,6,5,5,5,5][i] if i==j else 0) for j in range(dim)] for i in range(dim)]))

    def test_5_7_relative_defect(self):
        a5=matrix(((1,-1),(2,3))); a7=matrix(((1,-2),(2,3)))
        h=mm(mm(a7,a5),inv(mm(a5,a7)))
        self.assertEqual(h,matrix(((F(41,35),F(-8,35)),(F(-16,35),F(33,35)))))

    def test_mixed_radix_roundtrip_negative(self):
        for x in range(-100,101):
            q,r=euclidean_digits(x,(5,7))
            self.assertEqual(recompose(q,r,(5,7)),x)

if __name__=='__main__': unittest.main()
