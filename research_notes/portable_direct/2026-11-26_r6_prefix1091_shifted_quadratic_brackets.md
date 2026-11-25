# PREFIX-1091 — Exact shifted quadratic tail and bounded-denominator ideal-floor brackets

2026-11-26 Asia/Shanghai. AUTHOR_CONDITIONAL_ALGEBRAIC_PROOF / FINITE_EXACT_COMPUTATION / NOT_REVIEWED. Independent continuation of PREFIX-1090. Own registration receipt r6-20261123-2358-session-start-own-v1 recovered SUCCEEDED: EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. Inventory r6-20261126-0150-owner-read last observed RUNNING, error=null; no new CLAIM or protected task mutation. This is independently preserved science, not a formal Task return.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Same Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Complete signed/phase-paired Cell/port/ordered multiplicity carrier retained. The radial reference measure and bounds below are auxiliary observers, not changes to native states. Native-to-CT correspondence inherited, not reverified.

Parents:
- af9a793687306321e359a07c77ff0c1fbffc9acc:research_notes/portable_direct/2026-11-26_r6_prefix1090_radial_weight_floor_matching.md
- 508dd49782d0203dbcf0e7891fa01484da5be5ef:research_notes/portable_direct/2026-11-25_r6_prefix1085_quadratic_orbit_tail_certificate.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md
- 4c7f400d0557b5ec344b7297b5354f49bfa1fc81:research_notes/portable_direct/2026-11-25_r6_prefix1089_signed_block_floor_certificate.md

## 1. Finite shifted second moment and actual upper bounds

Use parent notation m>=0,r>=1,k>=3,M=m+r,Q=k+u,c_u=binom(u+r-1,r-1),x=SB/36,y=1-x,w_Q=x^(M+2)y^(Q-3), c=1/(8*36^6), D_m(k)>0. Let F_Q be the four signed Newton terms of 1085 using exchange-symmetrized K2 (not the full S6 orbit average). For j=0,1 define b_u^j=c_u CT[x^j w_Q], B_j(U)=sum b_u^j, f_u=c_u D_M(Q)/D_m(k), S(U)=sum f_u, C_j(U)=sum c_u CT[x^(-j)w_Q F_Q^2]. Reference-weight changes preserve each f_u exactly. The finite 1085 formula for C_j substitutes M+2+d+e-j for its first index M+2+d+e; every remaining exponent is nonnegative. Apply positive-measure Cauchy-Schwarz:

  A_j(U)^2 = c^2 B_j(U) C_j(U)/D_m(k)^2,
  N_tail(U) <= (A_j(U)-S(U))/2.

The shifted C_1 and A_1 have now actually been evaluated, separately from the ideal floor. No full-orbit or Gram optimization was applied in this run.

## 2. Bounded-denominator certified summation

Ideal squared floor is E_j(U)^2=B_j(U) sum f_u^2/b_u^j. For integer P>=1, scale H=2^P, define t_u=f_u^2/b_u^j and a_u=floor(H t_u), computed by integer quotient of exact numerator and denominator. For V>U,

  L=H^(-1)sum_(U<=u<V) a_u,
  L <= sum_(U<=u<V) t_u <= L+(V-U)/H.

Therefore the following is an exact rational outward bracket, combining 1090 and directed rounding:

  B_j(U)[L+S(V)^2/B_j(V)] <= E_j(U)^2
  <= B_j(U)[L+(V-U)/H+c^2 C_j(V)/D_m(k)^2].

Proof: floor inequality term by term, plus the lower and upper tail Cauchy-Schwarz bounds of 1090. Rounding adds at most B_j(U)(V-U)/H to squared-bracket width. The sum accumulator uses integers of denominator H rather than an expanding common denominator. Exact f,b calculation still has its original cost; this is an accumulator-size improvement, not an end-to-end timing claim. A shared prefix sum of a_u answers any interval in the covered range by two integer reads. For a required squared rounding contribution <=epsilon>0 it suffices to choose H >= B_j(U)(V-U)/epsilon. If V varies unboundedly, increase P accordingly. All endpoint comparisons can use exact rationals; displayed roots are rounded for readability.

## 3. Adaptive reference scaling is exactly equivalent to blockwise Cauchy-Schwarz

For disjoint blocks I_i covering u>=U, let B_i>0 and C_i>=0 denote each block's reference mass and joint squared carrier moment, using either j=0 or j=1 and any previously certified local null control. Multiply the weight on I_i by positive scalar t_i and divide its carrier by t_i. Every bin's signed observer is unchanged. The squared global certificate (without common normalization c^2/D^2) becomes

  (sum t_i B_i)(sum C_i/t_i) >= (sum sqrt(B_i C_i))^2.

For C_i>0 equality at t_i=const sqrt(C_i/B_i); zero C_i blocks use the infimum t_i->0, with zero contribution to the signed/absolute observer. Proof is Cauchy-Schwarz, and equality follows directly from its proportionality criterion. Thus optimal scalar reweighting on a prescribed partition equals the blockwise envelope, including when each block chooses its own radial exponent. Positive rational t_i approximate the infimum, so no irrational coefficients are needed for arbitrarily close certificates. This does not make the underlying reference carrier pointwise constant, and requires no removal of original joint relations.

For two adjacent blocks, the squared excess from merging instead of optimizing their scales is exactly

  (sqrt(B_1 C_2)-sqrt(B_2 C_1))^2.

This measures **upper** certificate splitting benefit and complements 1089's signed-mean lower-floor increment. Equivalently the merge excess in the absolute envelope is this square divided by sqrt((B1+B2)(C1+C2))+sqrt(B1*C1)+sqrt(B2*C2). Use both diagnostics: if C_i/B_i differ substantially, splitting has measurable potential, even if the signed lower-floor diagnostic is small. If C_i/B_i are equal, splitting these fixed carriers gives no gain. In all cases original f_u remains unchanged. This is a finite partition result; no greedy optimality or uniform resource gain claimed.

## 4. Executed exact calculation

Fixed (m,r,k)=(0,1,115), V=400, H=2^100. Reused 66-term K, 84-term K2, exact paired CT occupation counts with 25 shift classes, no native re-enumeration. Nmax=530,Jmax=550. First eight A values matched frozen parent; all 393 signed differences and 786 radial differences passed; 12 sampled direct second moments checked nonnegative, Cauchy-Schwarz, and exact C_j(u)-C_j(u+1) difference. Ten ideal-floor brackets and six actual upper certificates computed. Displayed ideal-negative certificate intervals [(sqrt(lo)-S)/2,(sqrt(hi)-S)/2] refer to the infimum for the chosen measure, not directly to the true negative mass.

U | j | S(U) | lower | upper
7 | 0 | 1.07326231356434854 | .05886923180180723 | 14.0463097404488998
7 | 1 | 1.07326231356434854 | .123618705285289475 | 14.3132483190708468
20 | 0 | .991984088376968450 | .011073959976634840 | 12.0940404364114508
20 | 1 | .991984088376968450 | .041940084890797105 | 11.7124578634116485
120 | 0 | .204628340692588379 | .001538328684634533 | 5.5026845035330395
120 | 1 | .204628340692588379 | .000496207128498692 | 4.04635657886839529
200 | 0 | .0727977900795234721 | .0006454651973004065 | 3.61019757966538829
200 | 1 | .0727977900795234721 | .00007632438222834605 | 2.30099153385013425
300 | 0 | .0265522632392951556 | .00018404906038515675 | 2.41742286607198016
300 | 1 | .0265522632392951556 | .00001188723609996035 | 1.34685198763297784

Actual absolute tail certificates (no full orbit or Gram optimization):
U | A0 | A1
120 | 68.98606499383892 | 35.28300403809121
300 | 8.081335613371227 | 4.077970451487529
400 | 3.5361388023637623 | 1.7786100541330288

The new actual shifted envelope is nearly half the same-carrier unshifted envelope in these three tests. It is not a comparison with the five-direction optimized unshifted certificate. At U=300 the ideal negative-floor lower diagnostic is ~15.48x smaller, but intervals overlap: no finite-scale ordering of the ideal floors is certified. The large bracket widths come from joint squared tail bound, not from the 100-bit accumulator. The 1089/1090 prefix is rechecked as part of the calculation, not counted as novel science. No independent review or formal checker.

## 5. Reproduction

Use the polynomial definitions from PREFIX-1082 section 4 through K=... . Then use the definitions and setup from PREFIX-1085 section 5 with ORBIT=False, params=[(0,1,115)], Nmax=530, Jmax=Nmax+20, through definitions of get, D, rad, nb, and prodrows for this parameter. The executed version compressed products by shift and radial degree before CT; linearity gives identical integer moments. Its code for compression of a polynomial key (u,v,a,b) is:
```python
from collections import defaultdict
def compress(p):
    out=defaultdict(int)
    for (u,v,a,b),val in p.items():
        ds=(-a,b,0,0,0,0)
        assert u-v==sum(ds)
        out[(u-sum(max(x,0) for x in ds),canonical(ds))]+=val
    return {key:v for key,v in out.items() if v}
def ct_compressed(i,pol):
    return sum(p*tables[d][i+j] for (j,d),p in pol.items() if i+j>=0)
```
Run the following exact suffix with the 1085 rows (or the equivalent compressed rows). F is fractions.Fraction, k=115, den=D(0,k), c0=F(1,8*36**6). The 1085 nb includes all radial shift and multiplicity factors. The original execution used Nmax=530 and imax=16 for radial and product rows, imax=2 for Drows (more columns do not change these results).
```python
from fractions import Fraction as F
from decimal import Decimal,localcontext
import hashlib,json
k=115; den=D(0,k); c0=F(1,8*36**6); assert den>0
def Ctail(U,j):
    cc=F(0)
    for (d,e),rows in prodrows.items():
        l=d+e; fac=(-1)**l*(1 if d==e else 2)
        for h in range(max(d,e),l+1):
            for v in range(h+1):
                cc+=fac*comb(h,d)*comb(d,d+e-h)*comb(k,h-v)*nb(rows,3+l-j,k+v+3-l,1+v,U-v)
    return cc
bt=lambda u,j:get(rad,2+j,k+u-3)
b=lambda u,j:get(rad,3+j,k+u-3)
s=lambda u:D(0,k+u)/den
f=lambda u:D(1,k+u)/den
def direct(u,j):
    Q=k+u
    return sum((-1)**(d+e)*(1 if d==e else 2)*comb(Q,d)*comb(Q,e)*get(rows,3+d+e-j,Q+3-d-e) for (d,e),rows in prodrows.items())
V=400; scale=2**100
pref={j:[0] for j in (0,1)}
for u in range(7,V):
    assert s(u)-s(u+1)==f(u)
    for j in (0,1):
        assert bt(u,j)-bt(u+1,j)==b(u,j)>0
        t=f(u)**2/b(u,j)
        pref[j].append(pref[j][-1]+(t.numerator*scale)//t.denominator)
for j in (0,1):
    for u in (7,20,120,200,300,399):
        cc=direct(u,j)
        assert cc>=0 and f(u)**2<=c0*c0*b(u,j)*cc/den**2
        assert Ctail(u,j)-Ctail(u+1,j)==cc
C={j:Ctail(V,j) for j in (0,1)}; assert all(v>0 for v in C.values())
records=[]
for U in (7,20,120,200,300):
    for j in (0,1):
        low=F(pref[j][-1]-pref[j][U-7],scale)
        high=low+F(V-U,scale)
        lo=bt(U,j)*(low+s(V)**2/bt(V,j))
        hi=bt(U,j)*(high+c0*c0*C[j]/den**2)
        assert hi>=lo>=s(U)**2
        with localcontext() as ctx:
            ctx.prec=18
            dec=lambda x:Decimal(x.numerator)/Decimal(x.denominator)
            l,h=dec(lo).sqrt(),dec(hi).sqrt(); ss=dec(s(U))
            print(U,j,ss,(l-ss)/2,(h-ss)/2)
        records.append([U,j,str(lo),str(hi),str(s(U))])
for U in (120,300,400):
    for j in (0,1):
        sq=c0*c0*bt(U,j)*Ctail(U,j)/den**2
        assert sq>=s(U)**2
        print('actual',U,j,float(sq)**.5)
digest=hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest()
assert digest=='7c18f6491cfdd58dc83381f51f2298ba890e6c0ed76ca7f9a81bab51c57dd7e8'
with open('prefix1091_evidence.json','w') as fh:
    json.dump({'scale':scale,'V':V,'records':records,'C':{str(j):str(v) for j,v in C.items()}},fh,separators=(',',':'))
```
Actual execution produced the digest above. The parent-prefix plus suffix reproduces the evidence; the equivalent compressed implementation was the one executed.

## 6. Next

The bottleneck is now explicit: shifted weighting helps even the actual unoptimized Cauchy envelope, but the ideal-floor bracket still pays excessive unobserved joint variance. Use the shifted orbit or low-order null controls on the final block and the two-block upper-benefit formula; a separate promising route is explicit positive tail certification (1075 currently non-effective threshold). Keep the mother objective B_fix,odd(32), p,d and explicit uniform positivity open. No claim of speedup, independent review, Foundation promotion, or formal Task closure.
