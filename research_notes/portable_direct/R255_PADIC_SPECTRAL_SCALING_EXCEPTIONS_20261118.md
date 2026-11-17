# R255 — Two prime-adic exception laws for the 63-mask integral spectral scale

Scientific date: 2026-11-18 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_COMPUTATION / NOT_REVIEWED.

Frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Immediate predecessors R254 and R254A: d97f5cb6d3cae6fc35107b605da809a2eb12e5dc. This is the 63-labelled-mask positive scalar auxiliary observer, not a signed/native BRC port or a Heartbeat X6 state quotient. All 63 source labels remain explicit.

## Definition

For rational 39/100 < s < 41/100, put t=(1691s-2615)/(2615s-3539), a=(1/5,1/4,3/10,9/20,s,2/3,t), b_0=13/60, and b_i=(5/18)|1/2-a_i| for i=1,...,6. Each mask m=0,...,62 corresponds to D_m={0} union {i+1: bit_i(m)=1}. Define its exact monic characteristic polynomial

c_m(x) = product_{i in D_m}(x-a_i) - sum_{i in D_m} b_i product_{j in D_m, j!=i}(x-a_j).

Let T_min(s) be the least positive integer T such that T^d c_m(y/T) belongs to Z[y] for every mask of size d. Let E(s) be the lcm of the reduced denominators of the fourteen rational inputs a_i,b_i. Always T_min(s) divides E(s), because E clears the entries in the displayed characteristic formula and admissible scales are characterized by independent integer p-adic lower bounds.

## Theorem (two exact p-adic exception laws)

Using v_p for the normalized p-adic valuation:

1. If v_13(s)=-r, r>=1, then v_13(t)=0 and

   v_13(E(s))=r,  v_13(T_min(s))=max(1,r-1).

2. If v_23(t)=-r, r>=1, then v_23(s)=0 and

   v_23(E(s))=r,  v_23(T_min(s))=max(1,r-1).

For every r>=2, this gives one factor of 13 or 23 saved in the characteristic-polynomial scale relative to E. Both exceptional families have infinitely many rational parameters in the open interval.

## Proof, p=13

Write t=(1691-2615/s)/(2615-3539/s). Because 1691 is congruent to 1 and 2615 to 2 modulo 13, v_13(s)<0 implies v_13(t)=0. Hence only a_4=s and b_4=5/36-(5/18)s can have a 13-adic pole; all other a_i,b_i are 13-integral.

The first nonleading coefficient of any mask containing 4 is minus the trace, -sum(a_i+b_i). Its nonintegral part comes from u_4=a_4+b_4=(13/18)s+5/36. For r>=2 this has valuation 1-r, forcing v_13(T)>=r-1.

Each coefficient of c_m is at most LINEAR in s: every term of the characteristic formula involves either a_4 or b_4, never their product, and all remaining factors are 13-integral. Hence every coefficient has valuation at least -r. Under scaling with v_13(T)=r-1, the j-th nonleading coefficient, j>=2, acquires valuation at least j(r-1)-r>=0; the first coefficient is integral by the trace calculation. Thus v_13(T_min)=r-1 for r>=2.

For r=1, one power of 13 suffices by the same linearity. To establish necessity, use mask 9 with states {0,1,4}:

c_9(x)=x^3-(13s/18+7/8)x^2+(11s/18+13/72)x-(5s/48+1/144).

Its x-coefficient has valuation -1, since 11/18 is a 13-unit. This is the j=2 integrality obstruction and forces v_13(T_min)=1.

Finally a_4=s and b_4 have denominator exponent r at 13, while all other inputs are integral there. Thus v_13(E)=r.

## Proof, p=23

Invert the fractional-linear map:

s=(3539t-2615)/(2615t-1691).

Since 3539=20 and 2615=16 modulo 23, v_23(t)<0 implies v_23(s)=0. Only a_6=t and b_6=(5/18)t-5/36 can have 23-adic poles. Their trace contribution is u_6=(23/18)t-5/36, with valuation 1-r for r>=2.

The identical trace/linearity argument gives v_23(T_min)=r-1 for r>=2 and an upper bound of 1 for r=1. For r=1, mask 32 with states {0,6} has

c_32(x)=x^2-(23t/18+5/18)x+(17t/36-1/36).

Its constant coefficient has valuation -1, forcing v_23(T_min)>=1. As a_6=t and b_6 have denominator exponent r, and other inputs are 23-integral, v_23(E)=r. QED.

## Infinite parameter families

For every r>=2 there exist numerators p not divisible by 13 with p/13^r in (39/100,41/100); for example s=67/169 when r=2. For the 23 family, the nonconstant Mobius map t(s) has determinant 853776 and maps the open interval bijectively to an open real interval. That interval contains rationals q/23^r with 23 not dividing q for arbitrarily large r; inverse images are admissible rational s.

## Exact finite computation

R255_padics.py uses only Python Fraction and integer arithmetic. For each parameter it constructs all 63 characteristic polynomials and checks all 249 nonleading coefficient positions, starts with E, and divides out prime factors exactly when all integral-scale conditions remain true. The resulting T is minimal by the primewise coefficient criterion. Independent witness checks include the explicit c_9 and c_32 coefficients above.

| Parameter s | E(s) | T_min(s) | E/T_min |
| --- | ---: | ---: | ---: |
| 2/5 | 299160 | 299160 | 1 |
| 46/117 | 12373718760 | 12373718760 | 1 |
| 67/169 | 12864192120 | 989553240 | 13 |
| 857/2197 | 820697347080 | 63130565160 | 13 |
| 770/1973 | 3529308161160 | 153448180920 | 23 |
| 767/1966 | 477928033560 | 20779479720 | 23 |

The exact verification JSON has seven rational witnesses (including 66/169) and an independently recalculated 21-point grid s=j/1000, 390<=j<=410. Every grid point satisfies E=T_min, so the 13/23 exceptions were invisible on R254A's grid. The script returned PASS for all these finite checks. The unlimited-r theorems follow from the displayed p-adic proof, rather than extrapolation from the grid.

## Interpretation and next problem

T_min here is the minimal integral characteristic scaling, not the sharp common reduced denominator of all 63 future scalar outputs. R254 separately established an all-event sharp denominator at s=2/5. Saving a factor p in the spectral scale may reduce a common denominator *upper bound* by about log2(p) bits per event; the source-specific numerator cancellations and initial moments must still be accounted for.

Next investigate whether for all rational s in this interval E(s)/T_min(s) always divides 13*23, and then lift R254's modular nonvanishing witnesses to general s. The separate continuous-parameter 270/403 two-mode thresholds remain open. Preserve source labels and stated future-observer scope.