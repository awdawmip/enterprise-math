"""PREFIX-430: exact rational consequences and illustrative numeric checks.

The strict continuous derivative bounds belong to PREFIX-424's author-side
interval certificate; this script does not rerun that full interval proof.
mpmath samples are not rigorous interval certificates.
"""
from fractions import Fraction as Q

LOW = Q(691 * 691, 7832)
HIGH = Q(708 * 708, 7649)
GAP_LOW = LOW / 2
GAP_HIGH = HIGH / 2
WEDGE_COEFF = Q(15664, 691)
UNIFORM_GAIN_COEFF = GAP_HIGH * WEDGE_COEFF**2
assert Q(60) < LOW < HIGH < Q(66)
assert Q(30) < GAP_LOW < GAP_HIGH < Q(33)
assert UNIFORM_GAIN_COEFF < 16838
assert Q(15298, 708) < WEDGE_COEFF
print("EXACT_JUMP_BOUNDS", str(LOW), str(HIGH))
print("EXACT_CORNER_GAIN_COEFFICIENTS", str(GAP_LOW), str(GAP_HIGH))
print("EXACT_UNIFORM_GAIN_BOUND", str(UNIFORM_GAIN_COEFF), "< 16838")
print("PASS_PREFIX430_RATIONAL_IMPLICATION_CHECK")

try:
    from mpmath import mp
except ImportError:
    print("NUMERIC_CROSSCHECK_SKIPPED_mpmath_unavailable")
else:
    mp.dps = 65
    beta = mp.mpf("0.000001")

    def V(r, s, eta):
        a = (s-r-1)/2
        b = -mp.sqrt(r-a*a)
        J = (53+29*r)/2 + 39*a - 4*b
        A = 36+28*a+12*b
        B = -20-12*a+28*b
        P = (245*(1+a)+123*b)/16
        Qv = (-123*(1+a)+245*b)/16
        c = mp.mpf(709)*(s-2)/64
        E = mp.mpf(53)/8
        N = P*P + Qv*Qv
        K = -eta-c-E*beta
        S = mp.sqrt(N*beta-K*K)
        L = (A*P+B*Qv)/N
        M = (A*Qv-B*P)/N
        return J+L*K+M*S+16*beta

    def vs(r,s,eta):
        return mp.diff(lambda x: V(r,x,eta),s)

    def vss(r,s,eta):
        return mp.diff(lambda x: V(r,x,eta),s,2)

    def vs_eta(r,s,eta):
        return mp.diff(lambda x,y: V(r,x,y),(s,eta),(1,1))

    for epsilon_text in ("0", "0.0000001", "0.000001"):
        epsilon=mp.mpf(epsilon_text)
        r=1+epsilon
        a=mp.findroot(lambda x: vs(r,2+epsilon,x), (mp.mpf("0.01951"),mp.mpf("0.01954")))
        b=mp.findroot(lambda x: vs(r,2-epsilon,x), (mp.mpf("0.01952"),mp.mpf("0.01955")))
        ja=vs_eta(r,2+epsilon,a)**2/vss(r,2+epsilon,a)
        jb=vs_eta(r,2-epsilon,b)**2/vss(r,2-epsilon,b)
        assert mp.mpf(LOW.numerator)/LOW.denominator < ja < mp.mpf(HIGH.numerator)/HIGH.denominator
        assert mp.mpf(LOW.numerator)/LOW.denominator < jb < mp.mpf(HIGH.numerator)/HIGH.denominator
        assert b>=a
        print("EPS",epsilon_text,"ETA_A",mp.nstr(a,26),"ETA_B",mp.nstr(b,26))
        print("JUMP_MAGNITUDES",mp.nstr(ja,23),mp.nstr(jb,23))
        if epsilon>0:
            eta=(a+b)/2
            sstar=mp.findroot(lambda x:vs(r,x,eta),(2-epsilon,2+epsilon))
            loss=V(r,2-epsilon,eta)-V(r,sstar,eta)
            delta=b-eta
            lo=mp.mpf(GAP_LOW.numerator)/GAP_LOW.denominator*delta**2
            hi=mp.mpf(GAP_HIGH.numerator)/GAP_HIGH.denominator*delta**2
            assert lo<loss<hi
            print("MIDPOINT_LOWER_CORNER_LOSS",mp.nstr(loss,25))
    print("PASS_PREFIX430_HIGH_PRECISION_NUMERIC_CROSSCHECK_ONLY")
