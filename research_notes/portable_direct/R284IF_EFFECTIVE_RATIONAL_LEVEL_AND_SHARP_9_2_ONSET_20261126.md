# R284IF — Effective rational-level inversion and sharp 9/2 onset

2026-11-26. Author proof and exact symbolic certificates; NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer K, no native physical attribution. Frozen science: IE @ 38d4de01b4a2aa512767d33c258b6d2cbf64911b:research_notes/portable_direct/R284IE_RATIONAL_LEVEL_INVERSE_AND_RESONANCE_20261126.md; HW @ 8c3bad026fc69c3a685218fc4677433a48310256:research_notes/portable_direct/R284HW_UNIFORM_WEDGE_RESIDUAL_PAYMENT_20261125.md; ID @ 000fb8cf43bf42509bcb2b90e65fdbb5edc95ca8 through IE (minimum-budget implication conditional on ID author monotonicity, not independently reviewed). Current global main 898c7959e85eb263544d5bcdf4070911caae6977 entry blobs verified; P000 V5, ACTIVE worldview, joint and residual preservation, portable research and current method context read. Own registration recovery r1-20261126-0605-own-recovery: original registration SUCCEEDED, session open, no run; RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. LEASED inventory request r1-20261126-0606-owner-read last observed RUNNING, no completed owner inventory asserted at time of this note. Independent unclaimed continuation of own IE line only; no shared CLAIM, formal Result, Review or other owner mutation.

## Theorem 1: explicit effective onset for every positive rational level
Let c=a/b>0 (positive coprime integers), P=Aq²+Bq+C, where A=c/36, B=8c/27+17/6, C=(128c²-1431c-45360)/(162c). Let H=324ab; then HP has integer coefficients. Define
R=1+|A|+|B|+|C|, gamma=c^8/2176782336,
M=(966628+491752c)R^9, J=491752 R^8,
beta=gamma/(2HJ), Z=1200(144/A)^3.
Any integer q satisfying
q>max(1,2(|B|+|C|+1)/A,24/A,sqrt(1280/A),2HM/gamma,(4cZ/beta)^(1/3))
has K(q,floor(P))<c<K(q,floor(P)+1). Thus this is a fully explicit sufficient onset in (a,b), not intended sharp. One can use 1+ceil(max(...)) as the onset or check the squared/cubed inequalities by rational arithmetic. The minimum budget is floor(P)+1 conditional on ID. No residue enumeration needed for this universal bound.

Proof: reuse HW's positive paid rational K0=N/D. Recompute the expanded coefficient l1 norms: N=966628 (degree_u=9), D=491752 (degree_u=8); both weighted degree <=18 for wt(u)=2, wt(q)=1. D>0 in the HW wedge. For any fixed s in [-1,1], F(q)=N(P+s,q)-cD(P+s,q) has coefficient l1 norm <=M by submultiplicativity, and D(P+s,q) has norm <=J. From IE's weighted leading terms (independently replayed below), F has degree <=16, coefficient at 16 = gamma*s, and for s=0 coefficient at 15 = -gamma*T, T=2(68c²+6991c+81180)/(3c²)>1/H. For nonzero lattice offsets, |s|>=1/H. At q>2HM/gamma the sum of lower terms has absolute value <=M q^15 < gamma q^16/(2H) in the nonzero case. At resonance it is <=M q^14 < gamma T q^15/2. Therefore signs are sign(s) if s!=0, negative at s=0, and the absolute signed baseline gap exceeds beta/q³ after division by D<=Jq^18. Use s=floor(P)-P or s+1. The onset ensures U=P+s>=Aq²/2>=640 and U>=2q+10 for both integer endpoints (q>=1 and q>24/A implies Aq²/2>12q>=2q+10). Thus U-1>=Aq²/4. HW gives delta=200 exp(-(U-1)/36)<=Z/q^6 by exp(x)>=x³/6; delta<0.1 from HW. Since 4c delta<beta/q³, the HW sandwich (1+delta)^-2<=K/K0<=(1+2delta)(1+delta) transfers both signs: upper factor <=1+4delta and inverse denominator <=1+3delta. All omitted joint mass and E remain paid; no true-count real extension asserted.

## Theorem 2: exact minimal eventual onset at c=9/2
P=q²/8+25q/6-135/2. The bracket is true for every integer q>=22449, and fails at q=22448. Hence 22449 is the least integer onset for the bracket, improving IE's sufficient 100000. Conditional on ID it is also the least eventual onset of the proposed minimum-budget formula. At q=22448, floor(P)=63082553; K at u=63082553 and 63082554 is strictly below 9/2; at 63082555 strictly above. The actual minimal reading budget there (conditional on ID) is 63082555, one greater than IE's eventual formula.

For each residue r mod 24, the least eventual onset *within that residue class*, with last failure exactly 24 earlier, is:
r: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
onset: 7464 17977 5570 4227 4444 6869 3702 17959 22472 4233 11218 6875 7452 17965 5582 4239 4456 6881 3714 17971 22460 4245 11206 6887.
No claim about all earlier individual q; just eventual onset with preceding failure.

Proof: For each of nine possible lower offsets s, form g=sign*(N(P+offset,q)-cD(P+offset,q)), with (offset,sign)=(s,-1),(s+1,+1), B0=D(P+offset,q). For each polynomial q^5*g-B0, shift by U listed below; exact rational coefficient checks give nonnegative coefficients and positive constant. Hence signed baseline gap exceeds 1/q^5 for all real q>=U, using D>0 on wedge. The lower U is 15 in every case; the upper U in offset order [-5/6,-19/24,-2/3,-1/2,-11/24,-1/3,-1/6,-1/8,0] is [22459,17955,11198,7445,6867,5568,4442,4227,3691]. For each residue take the first q>=upper U; for the preceding q (>=3600), exact rational evaluation gives g/B0<-1/q^5 for the upper sign, proving failure after payment. For q>=3600 all endpoints >=q²/8 and (U_budget-1)/36>=q²/300, and the wedge hypotheses hold. The sixth-term bound exp(x)>=x^6/720 yields delta<=144000*300^6/q^12, and 18 delta<1/q^5, delta<1/2 by the two integer inequalities checked in replay. HW factors therefore transfer all positive and negative signs. Maximum last failing residue point is 22448. All 24 residue classes are covered, not sampled asymptotics.

## Exact replay
Executed with Python/SymPy (integer/rational arithmetic). Polynomial coefficient shifts and all sign comparisons exact; displayed decimal gaps illustrative only. Compact replay of the actual calculation (fixed shifts in place of discovery search, same certificate and preceding-point checks):
```python
import sympy as s
u,q,c,z=s.symbols('u q c z')
S=4*u+2*q+4;j=u+2*q+1;d=u-q
f=lambda S,g:(4*(g+2)**2-S)/(S*(S-1))
Q=f(S,d-1);V=j/(S-j+1)*f(S,d)
A=j*(j-1)/(S*(S-1))*f(S-2,d)+j*(S-j)/(S*(S-1))*f(S-2,d-1)
N,D=s.fraction(s.factor(A*Q*(3*u+q+1)**2/((Q+V+q*A)**2*(u+2*q+1))))
for e,du,norm in [(N,9,966628),(D,8,491752)]:
    p=s.Poly(e,u,q)
    assert p.degree(u)==du and max(2*i+j for (i,j),v in p.terms())==18
    assert sum(abs(v) for v in p.coeffs())==norm
a,b,t=s.symbols('a b t');F=s.Poly(N-c*D,u,q)
def coef(deg):
    result=0
    for (i,j),v in F.terms():
        need=2*i+j-deg
        if need<0:continue
        for ib in range(min(i,need//2)+1):
            for it in range(min(i-ib,need//3)+1):
                ia=need-2*ib-3*it;ic=i-ia-ib-it
                if ia<0 or ic<0:continue
                result+=v*s.factorial(i)/s.prod(s.factorial(k) for k in [ia,ib,it,ic])*(c/36)**ic*a**ia*b**ib*t**it
    return s.factor(result)
a0=8*c/27+s.Rational(17,6);b0=(128*c*c-1431*c-45360)/(162*c)
T=2*(68*c*c+6991*c+81180)/(3*c*c);G=c**8/2176782336
assert coef(18)==0
assert s.factor(coef(17).subs(a,a0))==0
assert s.factor(coef(16).subs({a:a0,b:b0+z})-G*z)==0
assert s.factor(coef(15).subs({a:a0,b:b0,t:0})+G*T)==0
C=s.Rational(9,2);P=q*q/8+25*q/6-s.Rational(135,2)
res={i:s.floor(P.subs(q,i))-P.subs(q,i) for i in range(24)}
first={}
for off0,U in zip(sorted(set(res.values())),[22459,17955,11198,7445,6867,5568,4442,4227,3691]):
    for off,sign,shift in [(off0,-1,15),(off0+1,1,U)]:
        B0=s.Poly(D.subs(u,P+off),q)
        g=sign*(s.Poly(N.subs(u,P+off),q)-C*B0)
        poly=(g*s.Poly(q**5,q)-B0).shift(shift)
        assert poly.TC()>0 and all(v>=0 for v in poly.all_coeffs())
        if sign==1:
            for r,v in res.items():
                if v!=off0:continue
                y=U+(r-U)%24;first[r]=y;x=y-24
                assert x>=3600 and g.eval(x)/B0.eval(x)<-s.Rational(1,x**5)
assert 3600**7>18*144000*300**6
assert 3600**12>2*144000*300**6
assert max(first.values())-24+1==22449
x=22448;v=int(s.floor(P.subs(q,x)))
assert v==63082553
for uu,sign in [(v,-1),(v+1,-1),(v+2,1)]:
    k=N.subs({q:x,u:uu})/D.subs({q:x,u:uu})
    assert sign*(k-C)>s.Rational(1,x**5)
print(sorted(first.items()))
```
Actual output: weighted identities PASS; N,D terms 51,59, l1 norms 966628,491752; 18 shifted positive polynomials; 24 preceding residue failures all exact; sharp global onset 22449. At q=22448 the three baseline gaps are approximately -7.141255111073066e-8, -5.6105008759374425e-12, +7.140133010898102e-8, each separated from zero by more than 1/q^5, so paid true signs hold. No giant true combinatorial counts generated. Source review status NOT_REVIEWED; current result author evidence plus inherited HW residual lemma, not independent review of ID.

## Next
Use the actual residue-gap spectrum (rather than 1/H alone) to derive efficient sharp onsets for other rational levels or a height-sensitive bound much smaller than the coarse coefficient norm. Explore levels varying with q, where fixed-level lattice gap and expansion need new proof. Preserve ID independent review as separate work; do not repeat finite closure.
