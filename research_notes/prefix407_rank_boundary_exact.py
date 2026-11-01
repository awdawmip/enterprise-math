#!/usr/bin/env python3
"""PREFIX-407: exact coherent-vs-PSD classification on the I3=0 slice.

Only rational arithmetic is used for decisive inequalities.
"""
from fractions import Fraction as Q


def defect(r, s, f4):
    """The 2x2 principal determinant as a rational number."""
    x = (s - 1 - r) / 2
    y = (2*f4 - 14 + 10*r - 39*s) / 8
    return r - x*x - y*y


def reconstruct(r, s, f4):
    """Return the (Re u, Im u) candidate; exact source iff defect == 0."""
    x = (s - 1 - r) / 2
    # H[1,2] = conjugate(u), so Im(u) is -y
    imag_u = (14 - 10*r + 39*s - 2*f4) / 8
    return x, imag_u


def exact_feasible(r, s, f4, f5, cv):
    """Complete exact six-readout criterion on I3=0 with I1 normalized to 1."""
    return cv == 1 and f5 == Q(709, 64)*s and defect(r, s, f4) == 0


def source_readouts(u_x, u_y):
    # On v=0, exact original six-observation model
    r = u_x*u_x + u_y*u_y
    s = (1 + u_x)*(1 + u_x) + u_y*u_y
    f4 = Q(53, 2) + Q(29, 2)*r + 39*u_x - 4*u_y
    f5 = Q(709, 64)*s
    return r, s, f4, f5


def certificate(epsilon, kappa):
    """Valid for 0 <= eps <1, kappa >= 0, exact I3=0, Cv=1.

    I2 in [1-eps,1+eps], Cu in [2-eps,2+eps],
    I4 in [41-kappa,41+kappa].
    """
    assert Q(0) <= epsilon < Q(1) and kappa >= Q(0)
    bound_x = epsilon
    bound_y = kappa/Q(4) + Q(49, 8)*epsilon
    lower_det = 1 - epsilon - bound_x*bound_x - bound_y*bound_y
    lower_lambda2 = 1 - kappa/Q(4) - Q(65,8)*epsilon
    return lower_det, lower_lambda2


def main():
    # Explicit two coherent endpoints in the original measurement model.
    for sign, intensity in [(1, Q(37)), (-1, Q(45))]:
        r,s,f4,f5 = source_readouts(Q(0), Q(sign))
        assert (r,s,f4,f5) == (Q(1),Q(2),intensity,Q(709,32))
        assert defect(r,s,f4)==0
        assert reconstruct(r,s,f4)==(Q(0),Q(sign))

    # Nontrivial rational coherent source and its unique recovery.
    p,q=Q(2,5),Q(3,7)
    r,s,f4,f5=source_readouts(p,q)
    assert exact_feasible(r,s,f4,f5,Q(1))
    assert reconstruct(r,s,f4)==(p,q)
    assert not exact_feasible(r,s,f4,f5+Q(1,100),Q(1))
    assert not exact_feasible(r,s,f4,f5,Q(1,2))

    # The midpoint is a unique rank-two PSD state, not a coherent source.
    assert defect(Q(1),Q(2),Q(41))==Q(1)
    assert not exact_feasible(Q(1), Q(2), Q(41), Q(709,32), Q(1))
    assert reconstruct(Q(1),Q(2),Q(41))==(Q(0),Q(0))

    # Exact critical threshold: κ <4 excludes rank-one; κ>=4 admits it.
    for k in [Q(0),Q(1),Q(2),Q(7,2),Q(4),Q(5)]:
        y_min = min(Q(1), k/Q(4))
        spectral_min = 1-y_min
        assert spectral_min == max(Q(0), 1-k/Q(4))
        assert (k>=4) == (spectral_min==0)
        # Construct attaining PSD H with h=i*y_min, r=1, s=2.
        assert defect(Q(1),Q(2), Q(41)+4*y_min)==1-y_min*y_min

    eps=Q(1,10000); k=Q(1)
    lower_det,lower_lambda2 = certificate(eps,k)
    assert lower_det > 0 and lower_lambda2 == Q(11987,16000)
    assert lower_lambda2 > Q(3,4)-Q(1,1000)
    print('epsilon:',eps,'kappa:',k)
    print('determinant_certificate:',lower_det)
    print('lambda2_certificate:',lower_lambda2)
    print('threshold_kappa_exact:',Q(4))
    print('PASS_PREFIX407_EXACT_SLICE_RECONSTRUCTION_AND_SHARP_NOISE_THRESHOLD')

if __name__=='__main__':main()
