# R5 — Exact eleven-edge low-ratio Blackwell lift (2026-11-08)

**Status:** AUTHOR_PROVED / LOCAL_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Scientific context: frozen seven-node P/Q-BRC observer. Original scientific pins stay Global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Direct predecessor: [PR #1800 immutable theorem and definitions](https://github.com/awdawmip/enterprise-math/blob/58f1444c42d487ac8d2c9a1801f3c3adfade003f/research_notes/brc_r5_complement_b_gt_a_wedge_20261108/RESEARCH.md). P000 and ACTIVE worldview unchanged. This concerns the statistical observer, not a native X6 dynamic operation.

## Exact result

Let r=(1/10,1/2,3/4,1,5/4,3/2,19/10) and let M(f) be the seven Q-terminal masses and T_P(f),T_Q(f) the two stopping times *defined in the predecessor* and fully reproduced in VERIFY.py. A lawful flow f=(g,a,b,u,v,w,z) is seedless iff 9bz=4a(v-z).

Define alpha=(sqrt(3385758529)-55477)/68458, the unique positive root of 34229 t² + 55477 t - 2250. In fact 1/26 < alpha < 1/25.

**Theorem.** For every real 0 <= t <= alpha, the legal FULL_HIST flow

    x(t)=(1,t,1,0,t/10,3t/40+21/80,t/10)

has the legal seedless target

    y(t)=(1, t/[4(t+2)], 1, 7t(4t+7)/[160(t+2)],
          t(5t+9)/[10(t+2)], 3(15t+28)/[160(t+2)],
          t²/[20(t+2)])

and a nonnegative declaration-independent 7×7 kernel Q(t), with precisely the following potentially nonzero entries (target row, source column):

| Entry | Exact rational function |
|---|---|
| Q00 | (1934t+189)/72000 |
| Q01 | 19t(257t+466)/[18000(t+2)] |
| Q11 | (2250-55477t-34229t²)/[90000(t+2)] |
| Q12 | t(18479t+36352)/[90000(t+2)] |
| Q21 | 19t(257t+466)/[11250(t+2)] |
| Q22 | (45000-58852t-40979t²)/[45000(t+2)] |
| Q23 | t(2383t+4479)/[5000(t+2)] |
| Q32 | t(18479t+36352)/[90000(t+2)] |
| Q33 | (121110-116819t-95288t²)/[180000(t+2)] |
| Q63 | t(2383t+4479)/[18000(t+2)] |
| Q66 | (4934t+10689)/72000 |

All unlisted entries equal zero. For all i,j:

    sum_j Q[i,j]=M_i(y);
    sum_i Q[i,j]=M_j(x);
    sum_i r_i*Q[i,j]=r_j*M_j(x);
    T_P(y)=T_P(x), T_Q(y)=T_Q(x).

For any terminal declaration d in [0,1]^7, put d'_i=sum_j Q[i,j]*d_j/M_i(y) if M_i(y)>0 (otherwise zero). Both errors and both stopping times are preserved exactly. The same holds for x_h=(1-h)x+h*y for any real h in [0,1], replacing Q by Q_h=(1-h)Q+h*diag(M(y)).

The original historical residual 9bz-4a(v-z)=9t/10 is **strictly positive whenever t>0**: these are non-seedless inputs. Therefore this extends the previous author-side b/5<=a<b wedge to a new positive-residual **continuous one-parameter** low-ratio family. It does not resolve the full low-ratio prism or the mother question.

## Proof of all-real legality and kernel signs

For y, write a'=t/[4(t+2)], b'=g'=1. Then w'=3a'/40+21b'/80, z'=t²/[20(t+2)], and v'-z'=9t/20. Consequently:

    9*b'*z' = 9t²/[20(t+2)] = 4*a'*(v'-z')
    a'/10-z'=t(1-2t)/[40(t+2)] >=0
    9b'/40-(v'-z')=9(1-2t)/40 >=0
    (13a'/40+b'/80)-u'=(4-34t-28t²)/[160(t+2)] >0.

The last numerator is decreasing and positive at 1/25; the other inequalities follow from t<=alpha<1/25. x itself satisfies all physical capacities, with g=b=1, u=0, w saturated and z=v=t/10.

All displayed Q numerators are manifestly nonnegative for t>=0 except three decreasing quadratics:

    N1=2250-55477t-34229t²
    N2=45000-58852t-40979t²
    N3=121110-116819t-95288t².

N1>=0 exactly to t=alpha, whereas N2(1/25)>0 and N3(1/25)>0. All denominators are positive. At t=alpha the entry Q11=0. Beyond alpha **this particular eleven-edge formula** has Q11<0; there is no impossibility claim for other formulas.

## Proof of all-real calibration and experiment scope

Direct substitution of the eleven entries into the 7 row-mass equations, 7 column-mass equations, 7 likelihood-weighted column equations and 2 stopping-time equations yields identities. Here is an independent exact finite *polynomial-identity certificate*: every term in these equations is affine in the source x or rational with denominator a constant multiple of (t+2) and polynomial numerator of degree <=2. Hence multiplying each difference by (t+2) gives a polynomial of degree at most 2. Exact Fraction substitution at the three **distinct** rational values t=0,1/52,1/26 yields zero for all these differences. Therefore each polynomial is identically zero, including for irrational t=alpha and every t in between. The same three-point check covers probability mass normalization and the nonlinear seedless identity because the displayed seedless products reduce to expressions with the same degree bound. The explicit algebra above separately proves nonnegativity throughout the interval. This is a valid all-real polynomial identity argument, not a finite-grid extrapolation.

The checked standard-library source VERIFY.py prints PASS_ALL_7x7_CALIBRATION_IDENTITIES_BY_THREE_POINT_DEGREE_TWO_CERTIFICATE, PASS_ALL_REAL_NONNEGATIVITY_TO_EXACT_QUADRATIC_ROOT, and 101 additional exact rational implementation checks. Exact output is stored in EXACT_OUTPUT.txt. Scientific status remains author proof / independent review pending; no native CLAIM/Result/Driver approval was assumed.

## Next unit

Seek a second exact kernel for this same difficult corner with overlapping ratio interval extending above alpha toward 1/5, then test other four-parameter corners. Possible route: fixed-tau seedless affine face z'=tau a'/10, v'-z'=9tau b'/40, with tau held constant during interpolation. A numerical LP proposal alone is not an exact certificate. Preserve the immutably frozen inputs; new source proof does not imply mathematical admission.
