# R284JC — Uniform growing-offset pole certificates
2026-11-27. Author proof and executed exact rational checks; NOT_REVIEWED. Auxiliary binary-tag joint-count observer, not a native spatial transfer. Frozen source R284JB at e92de4ef4680b68015e53c4c702fbf929dada0a0:research_notes/portable_direct/R284JB_FIXED_OFFSET_INTERIOR_POLE_FAMILY_20261127.md (blob 9ac16b9644637a8416a050c701568463acb70248). Uses its exact joint normalized residue and density input. P000 V5, ACTIVE worldview, joint-observer and portable research rules consulted. Own session recovery confirms existing researcher registration, no runs, no shared claim; owner inventory request r1-20261127-0500-owner RUNNING at prepublication observation. No formal Result or Review claimed.

## 1. Uniform theorem
Retain the full original V,Q,A,E,Z,W,C and Y defined in JB section 1. For integer d>=10, 1<=r<=floor(d/10), set j=d-r, q0=-2d+r-2, u0=-j-2, m0=-M=-3d+2r-4. The reduced fiber is exactly JB section 2: c_h=(-1)^h binom(2j+h+1,h), k=j+h, l=r-h; a_h=(k+1)(l+1)c_h R_m0(l), b_h=(k+1)l c_h R_m0(l-1) (zero at l=0), v_h=(u0-k)(u0+k+2)/(2u0(2u0+1)), V*=sum a, Q*=sum b, A*=sum v(a+b), Z*=q0 A*+Q*+V*. The bracket in E* simplifies exactly to (2d+3)u0, giving
E*=c_r (u0-d)(2d+3)(m0+2)/[2(2u0+1)(4m0+2)].
Let W*=A*+E*, G=3q0(4q0+3d+1)^2 W*Q*-32(3q0+d+1)(Z*)^2.
Then G>0 uniformly throughout the triangular range, not merely eventually for each fixed r. In fact G>=d^5 |c_r c_(r-1)|.
For every actual legal q>=64,d^2<=4q in this range and prime p|q+2d-r+2, p>20d+20, JB gives C/T^2 congruent to G modulo p, T=R_(q+d)(j). Hence p not dividing the numerator of G suffices for Y !=32/3, even if Z* vanishes.

## 2. Proof by joint tail dominance with explicit residual payment
Set theta=2/27. Since j>=9d/10, the reverse coefficient ratio |c_(h-1)/c_h|=h/(2j+h+1)<=1/18 for 1<=h<=r. Since M>=7r+5, every R_m0 ratio R_m0(l+1)/R_m0(l)=(M+l)/(M-l-3) is positive and <=4/3 for 0<=l<r. Thus |c_(r-l)| R_m0(l) <= |c_r| theta^l and likewise with R_m0(l-1) for l>=1 (the latter even has a spare factor 3/4).
Absolute mass bounds:
sum |a_h| <= (d+1)|c_r|/(1-theta)^2 < (6/5)(d+1)|c_r|;
sum |b_h| <= (d+1)|c_r| theta/(1-theta)^2 < (1/10)(d+1)|c_r|.
In Q* ordered by l=1,...,r the signs alternate starting with sign(c_(r-1)); successive magnitude ratios <=2theta=4/27 (the factor (l+1)/l<=2, the k+1 ratio <=1, and the two raw ratios just bounded). Consequently Q* has sign(c_(r-1)), and |Q*| >= (1-4/27)d|c_(r-1)| >= d|c_(r-1)|/2.
Also |v_h| = h(2j+h+2)/[2(j+2)(2j+3)] <= (r/(2j))(1+r/(2j)) <=19/324 <1/16.
Therefore |A*| <= (13/160)(d+1)|c_r|. The E* prefactor is positive and equals
(j+d+2)/(2j+3) * (2d+3)/2 * (M-2)/(4M-2).
The first factor lies in [1,2], the last in [1/5,1/4] (M>=8), and d <= (2d+3)/2 <=2d. So d|c_r|/5 <= |E*| <= d|c_r|. Thus W* has sign(c_r), and |W*|>=d|c_r|/10, since d/5-13(d+1)/160>=d/10 for d>=10. The two signed observations W* and Q* have opposite signs. Both q0 and 3q0+d+1 are negative, and |q0|>=d, |4q0+3d+1|>=4d. The first term in G is therefore at least 3*d*(4d)^2*(d|c_r|/10)*(d|c_(r-1)|/2) >= d^5 |c_r c_(r-1)|; the second is nonnegative. This proves the uniform theorem, without erasing the E residual or assuming that Z has a nonzero first residue. This is only a sign/height result for the normalized observer, not a real lower bound on F for positive q.

## 3. Uniform exceptional-prime budget
At integral d,r the c_h are already integers. Unlike JB's polynomial-in-d construction we do not need the extra r! in a numeric common denominator. Take
D=2u0(2u0+1)(4m0+2) prod_(i=0..r-1)(m0+i+3).
All D V*, D Q*, D A*, D E*, D Z*, D W* are integers (raw R denominator divides displayed product; observer denominators divide exterior product), so P=D^2 G is a nonzero positive integer. Every factor of D has absolute value <=20d and hence p>20d+20 is coprime to D. Also |c_r|<= (3d)^r. The mass bounds above give |V*|+|Q*| <= (20d)^(r+1); |W*|,|Z*| <= (20d)^(r+2), using |A*| <= sum absolute masses/16, |E*|<=d|c_r|, |q0|<=3d. Coefficients satisfy 3|q0||4q0+3d+1|^2 <=(20d)^3 and 32|3q0+d+1| <=(20d)^2. Therefore 0<G<(20d)^(2r+8), |D|<=(20d)^(r+3), 0<P<(20d)^(4r+14). There are at most 4r+13 distinct exceptional primes >20d+20, uniformly in d,r. This is a numeric height bound, not a claim about degrees of the symbolic reduced numerator.

## 4. Growing-coordinate consequences
Let d(q)=s sqrt(q)+O(1), 0<s<2, eventually nondecreasing integer, and 0<beta<1 fixed. For large d choose r(d)=floor(d^beta). Eventually 1<=r<=d/10. As d grows, r is nondecreasing with increments at most those of d (floor of x^beta on positive integers); q -> N=q+2d-r(d)+2 is strictly increasing, N=q+O(sqrt q), omitting O(sqrt X) values up to X+O(sqrt X). The reciprocal-prime/floor counting argument of frozen JB section 4 then shows that P^+(N)>20d+20 has natural density log 2, by restricting to [epsilon X,X], constant-factor threshold squeeze and epsilon->0. For each fixed d, the candidate q lie in an interval of length O(d), even if the bound's constant is large. Each exceptional prime >20d+20 can divide N for only O(1) such q. The number of discarded q up to X is O(sum_(d<=O(sqrt X)) (r(d)+1))=O(X^((1+beta)/2))=o(X). Thus the *valid* certificate event for the unbounded offset r=floor(d^beta) has density log 2. The same argument works for eventually nondecreasing integer r(d)=o(d) with increments at most those of d. No independence assumed.

For simultaneous exception control, for any integer R=R(X)>=1, R=o(X^1/4), consider all r<=min(R,floor(d/10)). For each (d,r), O(r+1) exceptional primes with O(1) q per prime, so at most O(sqrt X R^2)=o(X) budgets have ANY exceptional prime in this entire family (small d outside the declared range are irrelevant). For all remaining budgets every qualifying large prime in those coordinates is a valid JB non-equality certificate. This does not assert existence of a qualifying prime in a short interval, nor a larger union density. Factor discovery is separate; residue computation remains O(r) modular operations with the recurrence, not uniformly polynomial in log q for polynomially growing r.

## 5. Executed exact checks
Python Fraction; checked all (d,r), d=10..300, 1<=r<=floor(d/10) (4380 cases), plus (1000,100), (10000,1000), (100000,100), (10^30,40), (10^60,60). All final assertions passed. Early trial of |v_h|<1/30 was false and corrected before the final proof and full rerun; the retained bound 1/16 is justified above. The five larger G numerator/denominator bit lengths respectively were 2208/1035, 21296/9936, 4775/2226, 15291/7149, 46077/21776. This validates the reduced fiber inequalities, not a new full-domain primal observer experiment; the normalized mod-p bridge is JB.
```python
from fractions import Fraction as F
from math import comb
def reduced(d,r):
    j=d-r; q=-2*d+r-2; u=q+d; m=2*q+d
    R=[F(1)]
    for l in range(r): R.append(R[-1]*F(m-l,m+l+3))
    V=Q=A=av=aq=F(0)
    for h in range(r+1):
        k=j+h;l=r-h;c=(-1)**h*comb(2*j+h+1,h)
        a=(k+1)*(l+1)*c*R[l]
        b=(k+1)*l*c*R[l-1] if l else F(0)
        v=F((u-k)*(u+k+2),2*u*(2*u+1))
        assert abs(v)<F(1,16)
        V+=a;Q+=b;A+=v*(a+b);av+=abs(a);aq+=abs(b)
    c=(-1)**r*comb(2*j+r+1,r)
    E=c*F((u-d)*(2*d+3)*(m+2),2*(2*u+1)*(4*m+2))
    E0=c*F((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2))
    assert E==E0
    Z=q*A+Q+V;W=A+E
    G=3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2
    D=2*u*(2*u+1)*(4*m+2)
    for i in range(r):D*=m+i+3
    assert all((D*x).denominator==1 for x in [V,Q,A,E,Z,W])
    assert av<=F(6,5)*(d+1)*abs(c) and aq<=F(1,10)*(d+1)*abs(c)
    assert abs(A)<=F(13,160)*(d+1)*abs(c)
    assert F(d,5)*abs(c)<=abs(E)<=d*abs(c)
    assert c*W>0 and c*Q<0 and G>0
    P=D*D*G
    assert P.denominator==1 and 0<P<(20*d)**(4*r+14)
    return G
n=0
for d in range(10,301):
    for r in range(1,d//10+1):reduced(d,r);n+=1
print('exhaustive',n)
for d,r in [(1000,100),(10000,1000),(100000,100),(10**30,40),(10**60,60)]:
    g=reduced(d,r)
    print('sample',d,r,g.numerator.bit_length(),g.denominator.bit_length())
```
Next: extend the uniform sign theorem beyond r<=d/10 using sharper alternating moments; seek large-prime existence in the resulting consecutive coordinates and distinguish it from the exceptional-prime loss already bounded. Second-branch pole classification and all-budget equality exclusion remain open.
