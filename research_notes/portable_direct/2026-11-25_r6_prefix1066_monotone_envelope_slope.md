# PREFIX-1066 — Exact monotone envelope and a 81/19 negative-order slope bound

2026-11-25. AUTHOR_CONDITIONAL_EXACT_PROOF / EXACT_INTEGER_AND_RATIONAL_CHECKED / NOT_REVIEWED. Independent portable continuation of EM-DIRECT-780BBE, TASK_RESEARCH. Own session recovery r6-20261125-0050-own-recovery confirmed original registration SUCCEEDED, no own run, execution_authorized=false. Owner request r6-20261125-0050-owner-read last RUNNING when checked; no formal CLAIM or shared Task state change.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; same Stage46 candidate X6 chart anchor O, incoming -e1, reversal signed weight -5 (positive phase cover 5q), other weight 1, next incoming -d; both orientations of Link {O,e1} blocked without renormalization; exactly two negative steps. Reuse full six-axis Cell/port/grade/phase/branch/multiplicity pairing and its proved observer symmetry. No canonical native kernel rerun, classical comparison or new physical attribution.

Parents:
- PREFIX-1062 d91f254e8f1fc36e8f974fd5452a91144e46f570:research_notes/portable_direct/2026-11-24_r6_prefix1062_no_finite_shift_complete_monotonicity.md.
- PREFIX-1064 3edd02d6d6da12b74e6de8fb7126b8390f522f91:research_notes/portable_direct/2026-11-24_r6_prefix1064_localized_transport_slope.md.
- PREFIX-1065 e22d153b377149d9052d2395e9a4e288a74b8d8c:research_notes/portable_direct/2026-11-24_r6_prefix1065_cubic_observer_slope_bound.md (blob ffaf02c17c4183b0b5cf1d9f0f687c6afd1f0166).

## Result

For the inherited p_n, D(n,k)=(-1)^k forward_difference^k p_n and k_min(n), prove

    limsup k_min(n)/n <= 81/19 = 4.2631578947...
    k_min(84+h) < 130+(81/19)h for every sufficiently large integer h.

This improves the previous asymptotic 347/53. Explicit onset and positive linear lower bound remain open.

## Exact witness

Reexecute the exact paired BRC checker of PREFIX-1062 with maxN=220 instead of 48; the original H support construction and grouped moment recurrence are unchanged. Count negatives rather than printing all. Check the five historical rows n=8..12 as in parent, and row n=110 against PREFIX-1065. All six comparisons passed. The actual calculation gave H=(2072,2072), J=121, V=(1429950702816,604314716448,85648332624,4014839808,0), unchanged. The triangle n>=8, n+k<=220 has 22791 entries, 7446 strictly negative. The first negatives for n=70..88 were 104,105,107,108,110,111,113,114,116,117,119,120,122,123,125,126,128,129,131. No extrapolation from these data is used.

Choose n=84,k=130,m=76. The exact negative numerator W is
355315645446552216705332390290085192402637198606035491623879220025625779544570910695672664476956937555030219304653440633099807757872724306887013899125348875515675605486242663461412093265352652559715394778970089343451284241338628560768372529742527970394348621750505957120
so L(f)=D(84,130)=-W/36^214, f=x^76(1-x)^130. Reproduction in parent's JS difference loop: for i=84-8, k=130, inspect -dif[i]/36n**BigInt(220-84-130), converting to string. Compute V by summing absolute grouped coefficients after deleting zero classes. In the actual execution this row, the earlier 44,66 witness, H support and V were returned. The finite triangle is exact via inherited multinomial observer, not a direct trajectory rerun.

## Monotone-envelope certificate

Retain the cubic norm |L(F)| <= (4*36^8)^(-1) sum_{i=0}^3 V_i sup|(E+8)^i F|, E=x d/dx. Choose a=19/100, b=21/100 and chi as in PREFIX-1065: zero on [0,a], one on [b,1], 35u^4-84u^5+70u^6-20u^7 between them, u=(x-a)/(b-a). It is nonnegative C^3. Write Q=1-chi.

For j=0..3, (E+8)^j f = x^m(1-x)^(k-j) P_j(x), P_0=1 and P_(j+1)=[n(1-x)-(k-j)x]P_j+x(1-x)P'_j. The exact ascending coefficients are (1), (84,-214), (7056,-36082,45796), (592704,-4562842,11623922,-9800344).

New useful bound: instead of bounding x^m and (1-x)^(k-3) independently (which combines incompatible endpoints), preserve their common product B(x). It is increasing on [0,b], because B'(x)=x^(m-1)(1-x)^(k-4)[m-(m+k-3)x] and b<m/(m+k-3)=76/203. Hence on each [l,h] its exact upper bound is B(h)=h^76(1-h)^127. This controls a correlated scalar envelope without losing the negative branch information of the inherited observer.

For each i, factor B(x) out of Leibniz expansion (E+8)^i(fQ), enclose the signed remaining polynomial terms on each interval using exact rational arithmetic, then take that derivative's maximum; sum the four weighted maxima. This proves

    |L(fQ)| / (W/36^214) < 87/200 = 0.435.

The actual diagnostic was 0.4344611669934793, so at least 56.5% of the original negative witness magnitude is retained. Apply PREFIX-1064 localized finite-order transport lemma with q=3, m=76>3, and chi. All its hypotheses hold. L(f chi)<0 and the resulting positive binomial-weighted sum of D(84+h,130+j) is strictly negative for sufficiently large h, with j<h(1/a-1)=(81/19)h. At least one term is negative, proving the theorem.

## Executed exact cutoff reproducer

```python
from fractions import Fraction as Q
from math import comb
W=355315645446552216705332390290085192402637198606035491623879220025625779544570910695672664476956937555030219304653440633099807757872724306887013899125348875515675605486242663461412093265352652559715394778970089343451284241338628560768372529742527970394348621750505957120
V=[1429950702816,604314716448,85648332624,4014839808]
n,k=84,130
m=n-8
P=[[1],[84,-214],[7056,-36082,45796],[592704,-4562842,11623922,-9800344]]
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    z=[a*b for a in x for b in y];return min(z),max(z)
def sc(x,c):return mul(x,(Q(c),Q(c)))
def poly(c,x):
    y=(Q(0),Q(0))
    for cc in c[::-1]:y=add(mul(y,x),(Q(cc),Q(cc)))
    return y
def mag(x):return max(abs(x[0]),abs(x[1]))
def qval(u):return (1-u)**4*(1+4*u+10*u*u+20*u**3)
def fine(a,b,N=200):
    mx=[Q(0)]*4
    assert b<Q(m,m+k-3)
    for seg,(left,right) in enumerate([(Q(0),a),(a,b)]):
        for j in range(N):
            l=left+(right-left)*j/N;h=left+(right-left)*(j+1)/N
            F=[mul(poly(P[i],(l,h)),((1-h)**(3-i),(1-l)**(3-i))) for i in range(4)]
            if seg==0:C=[(Q(1),Q(1))]+[(Q(0),Q(0))]*3
            else:
                u=(l-a)/(b-a);v=(h-a)/(b-a);r=(l/(b-a),h/(b-a))
                c0=(qval(v),qval(u))
                d1=(-140*v**3*(1-u)**3,-140*u**3*(1-v)**3)
                d2=sc(mul((u**2*(1-v)**2,v**2*(1-u)**2),(1-2*v,1-2*u)),-420)
                d3=sc(mul((u*(1-v),v*(1-u)),poly([1,-5,5],(u,v))),-840)
                c1=mul(r,d1);c2=mul(mul(r,r),d2);c3=mul(mul(mul(r,r),r),d3)
                C=[c0,c1,add(c1,c2),add(add(c1,sc(c2,3)),c3)]
            for i in range(4):
                s=(Q(0),Q(0))
                for j1 in range(i+1):
                    s=add(s,sc(mul(F[j1],C[i-j1]),comb(i,j1)))
                ratio=V[i]*mag(s)*h**m*(1-h)**(k-3)*36**(n+k-8)/(4*W)
                mx[i]=max(mx[i],ratio)
    return sum(mx)
v=fine(Q(19,100),Q(21,100))
assert v<Q(87,200)
print('PREFIX1066_CUTOFF_CHECK_PASSED',float(v),P)
```

Actual output: PREFIX1066_CUTOFF_CHECK_PASSED 0.4344611669934793 [[1], [84, -214], [7056, -36082, 45796], [592704, -4562842, 11623922, -9800344]].

Exploration with a=1/5,b=11/50 returned bound 3.439777501673156, not a certificate; the same witness with a=9/50,b=1/5 returned 0.04498143757195125. These are bounds, not assertions of sign failure at the larger cutoff.

Next: derive sign-sensitive local observer representations (especially near x=1), obtain a positive linear lower bound or fixed-k eventual sign, and improve localization without unbounded growth of exact moment computations. Preserve candidate qualification, unresolved canonical native revalidation and independent review.
