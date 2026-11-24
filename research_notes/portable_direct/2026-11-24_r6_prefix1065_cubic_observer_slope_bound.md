# PREFIX-1065 — Cubic paired observer and a 347/53 asymptotic negative-order slope bound

2026-11-24. AUTHOR_CONDITIONAL_EXACT_PROOF / EXACT_INTEGER_AND_RATIONAL_CHECKED / NOT_REVIEWED. Independent portable continuation of EM-DIRECT-780BBE, TASK_RESEARCH. Own session recovery r6-20261124-2350-own-recovery verified original successful registration and no own run, execution_authorized=false. Current owner query r6-20261124-2350-owner-read was last RUNNING; no new formal Task CLAIM or state change.

Frozen scientific inputs: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Same Stage46 candidate X6 chart anchor O, incoming -e1, reversal signed weight -5 (positive phase cover 5q), other weight 1, next incoming -d; both orientations of Link {O,e1} blocked without renormalization; exactly two negative steps. Preserve full six-axis Cell, port, grade, phase, multiplicity and source relationships before the inherited exact paired observation. No new canonical native kernel execution or classical reference comparison.

Parents:
- PREFIX-1061 de68b2863b6c1839ea59113a5e617b8908f5bd1c:research_notes/portable_direct/2026-11-24_r6_prefix1061_grade2_rational_packet.md
- PREFIX-1062 d91f254e8f1fc36e8f974fd5452a91144e46f570:research_notes/portable_direct/2026-11-24_r6_prefix1062_no_finite_shift_complete_monotonicity.md
- PREFIX-1064 3edd02d6d6da12b74e6de8fb7126b8390f522f91:research_notes/portable_direct/2026-11-24_r6_prefix1064_localized_transport_slope.md (blob c38aab678eda0af947e7e8d604b01beaa1385d60).

## 1. Results
For p_n=Delta_n^(2)/36^n, D(n,k)=(-1)^k forward_difference^k p_n and k_min(n)=min{k:D(n,k)<0}, prove
    limsup_(n->infinity) k_min(n)/n <= 347/53.
More precisely, for all sufficiently large integer h,
    k_min(44+h) < 66+(347/53)h.
The earlier 79 and 10^35 bounds remain separately valid at their stated scopes. The explicit onset and a positive linear lower bound remain open.

The quartic paired-contrast term cancels identically. The inherited exact observer has order at most three, not four; this removes one derivative from localization. This is a cancellation after the full joint port-pair operation, not a state-space quotient.

## 2. Cubic observer and sharper contraction norms
As in PREFIX-1062, put x=SS*/36 and E=x d/dx. Write 2H_j(n)=h_{j,0}+n h_{j,1}+n^2 h_{j,2}; 4J_a is the coefficient of n^a in (2H_1)(2H_1)^*-(2H_2)(2H_2)^*. The terminal factor z_j cancels in each self-pair. The coefficient h_{j,2}=S^5 N_j(1/S,z) by the parent H construction. In the parent numerator, all j-dependent differences contain R=1-tS: C(h,j)=s(h,j)R+tL_h; at R=0 only tL_h remains; the extra first-hit correction terms containing R vanish. Thus h_{1,2}=h_{2,2} and J_4=0 identically. This is a formal polynomial argument (the temporary rational substitution is cleared by S^5).

Let C_{v,a} be the grouped coefficient of 4J_a at sorted absolute six-component difference v, from the exact multinomial identity in PREFIX-1062. For each nonzero class choose a balanced signed representative with the same absolute differences. All polynomial tests F(x) have the same CT[z^v F(Y/36)] for every signed representative in that class, by linearity and the parent moment identity. The discrete positive contraction norm of each representative is at most sup|F|. Thus with V_a=sum_v |C_{v,a}|,
    |L(F)| <= (4*36^8)^-1 sum_(a=0)^3 V_a sup|(E+8)^a F|.
Polynomial density in C^3 (approximate third derivative uniformly, integrate matching lower initial values) gives the same bound on C^3 tests. All 121 grouped classes are retained; no claim about arbitrary future blocked-Link evolution is made.

Executed exact BigInt construction of the parent numerator, H and pair coefficients gave
    H support: (2072,2072)
    number of nonzero classes: 121
    V=(1429950702816,604314716448,85648332624,4014839808,0).
The last zero agrees with the independent algebraic cancellation above. Compared to the separate-port norm estimate of PREFIX-1064, this uses cancellations only between coefficients whose complete free-suffix pair observer is equal for every degree.

## 3. Larger exact negative witness
Extend the already proved paired multinomial observer of PREFIX-1062 from n+k<=48 to n+k<=110. All 41 previously saved integer rows n=8..48 matched exactly. There are 5356 entries in the enlarged difference triangle, including 1842 strict negatives. First negative orders for n=22..44:
    29,30,32,34,35,37,39,40,42,43,45,47,48,50,51,53,55,56,58,59,61,62,64.
No assertion for rows whose first negative falls outside the triangle. Choose n0=44,k0=66,m=36. The exact negative numerator is
    W=471337890306553727568840587306401901662842510189340854529332095636983263850556564591744460633117850446823851889065972528947256828469194624
    D(44,66)=-W/36^110.
The larger witness suppresses the small-x cutoff contribution.

Reproduction: use the actual embedded JS check() in PREFIX-1062, changing maxN=48 to maxN=110. Immediately after deleting zero classes add:
```js
const V=Array(5).fill(0n);
for(const c of J.values())for(let i=0;i<5;i++)V[i]+=c[i]<0n?-c[i]:c[i];
```
The existing loops and exact integer operations otherwise suffice. Add V:V.map(String) to the returned object; inspect rows and violations and select [44,66] for the signed numerator -W. The actual run also compared all 41 old rows against the JSON actual second-run output in the immutable parent; all matched. The last row n=110 was
34718648628742616932206713629391583043911652525799786221122784212469880142364646048939115185089267059664039592076654737081914247665104631046639182015699664351499648.
These are exact computations of the inherited candidate BRC terminal observer, not a new canonical kernel run.

## 4. Localization at a=53/400
Let f=x^36(1-x)^66, a=53/400 and b=61/400. Set chi=0 for x<=a, chi=1 for x>=b. In between u=(x-a)/(b-a), use chi=35u^4-84u^5+70u^6-20u^7. It is nonnegative C^3 since chi'=140u^3(1-u)^3 and its first three derivatives vanish at the joins. Let Q=1-chi. Its transition derivatives are
    Q=(1-u)^4(1+4u+10u^2+20u^3)
    Q'=-140u^3(1-u)^3
    Q''=-420u^2(1-u)^2(1-2u)
    Q'''=-840u(1-u)(1-5u+5u^2).
For j=0..3,
    (E+8)^j f=x^36(1-x)^(66-j) P_j(x).
P_0=1 and P_(j+1)=[44(1-x)-(66-j)x]P_j+x(1-x)P'_j. In ascending coefficient order:
    P_0=(1)
    P_1=(44,-110)
    P_2=(1936,-9746,12100)
    P_3=(85184,-647658,1618914,-1331000).
On each subinterval of [0,b], factor out x^36(1-x)^63 and retain signed intervals for all remaining Leibniz terms. In the transition, E=(x/(b-a))d/du; use the exact Stirling expansion for E^j Q. Since the common factor is nonnegative, bound each derivative separately over the whole interval and sum its weighted supremum. The checker proves
    |L(fQ)| / (W/36^110) < 93/100.
The four separately maximized contributions, displayed approximately, are
    0.002927854688, 0.027331409856, 0.200354427375, 0.697554103375
with sum 0.928167795294. Their exact rational sum is less than 93/100. Each of the two segments has 400 equal intervals. Using a maximum of the pointwise sum instead of a sum of individual suprema would not follow from the norm bound; the initial exploratory test at a=2/15 had this defect and was discarded. Corrected tests at a=2/15,b=23/150 with 400 and 1200 intervals did not certify (1.08082 and 1.01779). No impossibility claim for that cutoff. A=1/8,b=7/50 with 400 intervals gives a separate robust certificate (ratio <0.218).

Apply the general finite-order localized transport lemma of PREFIX-1064 with q=3, f as above (m>q), and the new chi. Since L(f chi)=L(f)-L(fQ)<0, the lemma yields a negative sum of D(44+h,66+j) with nonnegative binomial weights supported in j<h(1/a-1)=(347/53)h for every sufficiently large h. At least one summand is negative. Divide by 44+h and pass to limsup. No numerical onset claimed.

## 5. Exact rational reproduction of cutoff certificate
The following is the executed interval method (Fraction arithmetic); the diagnostic ratios were displayed only after the exact comparison. No native state calculation is replaced by this auxiliary proof inequality.
```python
from fractions import Fraction as Q
from math import comb
W=471337890306553727568840587306401901662842510189340854529332095636983263850556564591744460633117850446823851889065972528947256828469194624
V=[1429950702816,604314716448,85648332624,4014839808]
P=[[1],[44,-110],[1936,-9746,12100],[85184,-647658,1618914,-1331000]]
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    z=[a*b for a in x for b in y]
    return min(z),max(z)
def sc(x,c): return mul(x,(Q(c),Q(c)))
def poly(c,x):
    y=(Q(0),Q(0))
    for cc in c[::-1]: y=add(mul(y,x),(Q(cc),Q(cc)))
    return y
def mag(x): return max(abs(x[0]),abs(x[1]))
def qval(u): return (1-u)**4*(1+4*u+10*u*u+20*u**3)
def cert(a,b,N=400):
    mx=[Q(0)]*4
    for seg,(left,right) in enumerate([(Q(0),a),(a,b)]):
        for j in range(N):
            l=left+(right-left)*j/N; h=left+(right-left)*(j+1)/N
            F=[mul(poly(P[i],(l,h)),((1-h)**(3-i),(1-l)**(3-i))) for i in range(4)]
            if seg==0:
                C=[(Q(1),Q(1))]+[(Q(0),Q(0))]*3
            else:
                u=(l-a)/(b-a); v=(h-a)/(b-a)
                r=(l/(b-a),h/(b-a))
                c0=(qval(v),qval(u))
                d1=(-140*v**3*(1-u)**3,-140*u**3*(1-v)**3)
                d2=sc(mul((u**2*(1-v)**2,v**2*(1-u)**2),(1-2*v,1-2*u)),-420)
                d3=sc(mul((u*(1-v),v*(1-u)),poly([1,-5,5],(u,v))),-840)
                c1=mul(r,d1); c2=mul(mul(r,r),d2); c3=mul(mul(mul(r,r),r),d3)
                C=[c0,c1,add(c1,c2),add(add(c1,sc(c2,3)),c3)]
            for i in range(4):
                s=(Q(0),Q(0))
                for j1 in range(i+1):
                    s=add(s,sc(mul(F[j1],C[i-j1]),comb(i,j1)))
                ratio=V[i]*mag(s)*h**36*(1-l)**63*36**102/(4*W)
                mx[i]=max(mx[i],ratio)
    return sum(mx),mx
v,parts=cert(Q(53,400),Q(61,400))
assert v<Q(93,100)
print([float(x) for x in parts],float(v))
```
Actual diagnostic: [0.002927854688044279, 0.027331409855604047, 0.20035442737469294, 0.6975541033752177], 0.9281677952935591; exact rational comparison v<1 passed; stronger v<93/100 is checked separately before publication.

## 6. Next
Determine whether the leading negative-support endpoint can be localized more sharply by a sign-sensitive distribution analysis rather than global contraction norm. Study positive linear lower bound and fixed-k eventual signs. Preserve the candidate model qualification and independent review status.
