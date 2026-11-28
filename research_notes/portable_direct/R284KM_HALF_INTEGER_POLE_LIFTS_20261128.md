# R284KM — Half-integer pole-fiber Hensel compression and exact degeneracy closure

2026-11-28. Author research, NOT_REVIEWED. Auxiliary R284 arithmetic, not native spatial transfer. Researcher EM-DIRECT-0C386E / TASK_RESEARCH / RA-B82240E8488EF5A1DA5186C4. Own session recovered by r1-20261128-1700-own-recovery-v2 (metadata only, no runs, no shared execution authority). Owner inventory r284kl-next-20261128-1700-owner-read SUCCEEDED at 09:02:31 UTC, as-of 09:01:14 UTC, 547 tasks, no LEASED entries. No Task/CLAIM/Result mutation. Global entry snapshot 401e5300954ba213d1aef66bee721da84ebb3535 (both entry blobs matched), P000 V4, Source startup projection, ACTIVE worldview, portable protocol and research method read.

Frozen source: R284KL @fb7dcfee4832d57603641d9f0af9137d6b441c00:research_notes/portable_direct/R284KL_ODD_BOUNDARY_AND_POLE_BAND_20261128.md; retain its KK/JR/KD pins. Integer carrier evaluator adapted from KG @8d6a334b0713e70e2267dbe0a71ba7bdfa853651:research_notes/portable_direct/R284KG_sextic_fiber_certificate.py and KL @87cbd27a2836e45f8d64523271eb5a1db4afa43b:research_notes/portable_direct/R284KL/root.py. No new independent review of dependencies.

## 1. Unbounded exact lift theorem
For odd d>=5 let h=2q+d+2 and g(h)=P_d((h-d-2)/2). Since P_d is an integer polynomial (JR), g belongs to Z[1/2][h], hence to Z_p[h] for every odd prime p. All denominators at the original pole are cleared BEFORE evaluation. For any odd p>2d+3, suppose p divides h and g(0)=0 mod p. Define b=g(0)/p mod p, a=g'(0) mod p. Then
g(pt)/p = b+a*t mod p.
If a=0 and b!=0 there are no lifts; if both vanish, no exclusion from this order. If a!=0, every zero must satisfy t=-b/a mod p.
For q in [ceil(4d^2/5),floor(4d^2/3)], 0<h<=8d^2/3+d+2<p^2 since p>2d+3. Therefore 0<t<p, and h is odd, requiring t odd. The simple case has at most one integer budget in the interval, specifically q=(p*t-d-2)/2, and none if the range or parity fails. KD proves this interval contains the unique legal root for d>=81; smaller d already excluded by JR. Higher mod p^k evaluation at that single candidate suffices to rule out the whole p-fiber if nonzero. This is an unbounded conditional theorem, not a claim of uniform derivative nonvanishing.

No symbolic derivative expansion is needed: if r=g(0) mod p^2 and s=g(p) mod p^2, then b=r/p and a=(s-r)/p mod p. The difference is a multiple of p by polynomial integrality. This retains the joint first correction of all signed terms, including the boundary contribution, even when the individual rational observations have poles.

## 2. Denominator-free observer
For v=u=q+d or n=2q+d, let D_v=product_{i=0}^{d-1}(v+i+3), U_v(k)=product_{i<k}(v-i) product_{k<=i<d}(v+i+3). Retain U=U_u, N=U_n. Their values are integer polynomials in q. Evaluate using prefix and suffix products, without division.
Set J=2u(2u+1), L=4n+2. In the code V,Q denote the unnormalized sums with a=(k+1)(l+1)U[k]N[l] and b=(k+1)l U[k]N[l-1] (zero for l=0), l=d-k. A=sum (u-k)(u+k+2)(a+b). The exact cleared observations are
W_n=L*A+u*U[d]*D_n*q*(2d+3)*(n+2),
Q_n=J*L*Q,
Z_n=L*(q*A+J*(V+Q)).
Each equals its original rational observer times D=J*L*D_u*D_n on the regular domain, hence their polynomial combination is P_d=3q(4q+3d+1)^2 W_n Q_n-32(3q+d+1) Z_n^2 identically. The extension to a pole is evaluation of this polynomial, not inversion of a zero denominator. All modular computations use only the inverse of 2 for the half-integer input. O(d) modular multiplications/additions per evaluation, with arithmetic cost depending on modulus bitlength. No assumption of independent sieve events.

## 3. Actual experiment
Recomputed all 10,340 prime/deficiency pairs for odd 5<=d<=301 and 2d+3<p<=5d. Counts exactly reproduce KL: 3,621 near, 6,719 far, 12 and 10 first-order degeneracies. All 22 have a!=0. Of them 20 yield no budget by parity/range, two yield one candidate each, both excluded modulo p^3. Independent direct Fraction evaluation of the original rational carrier verified the two final residues. For d=73 the interval test is a conditional interval experiment (JR already excludes that d). No new extension of the full integer exclusion range beyond 3200 is claimed. The exact output and executed Python 3 source follow; no floating-point decisions. The two files locally had SHA256 ff083390894b19ff186f08a33d3f3becc8496e7eb8be3135c9f1b701618fd8f0 (script), d2ae6649d335b1e8b82d65cf15e64bd7907a8d4e1d277f4272f0ca3c3c1201ef (stdout).

## 4. Next
The 22 tested first-order degeneracies are closed on the declared interval. Seek a uniform derivative formula or a resultant condition for the singular case a=b=0; the experiment does not imply it cannot occur. Extend to actual d>3200 root candidates and assess whether joint KG/KJ/KK/KL conditions can replace full interval scans. Preserve exact boundary terms. No need to redo KL finite root checks.

## Executed Python 3 certificate

```python
from math import isqrt
from fractions import Fraction as F
from collections import Counter

def primes(n):
    a=[True]*(n+1); a[:2]=[False,False]
    for i in range(2,isqrt(n)+1):
        if a[i]: a[i*i::i]=[False]*((n-i*i)//i+1)
    return [i for i in range(n+1) if a[i]]

def carrier(d,q,M):
    # q is residue of the rational argument modulo the odd modulus M.
    def scaled(v):
        tail=[1]*(d+1)
        for k in range(d-1,-1,-1): tail[k]=tail[k+1]*(v+k+3)%M
        z=1; out=[]
        for k in range(d+1):
            out.append(z*tail[k]%M); z=z*(v-k)%M
        return tail[0],out
    u=q+d; n=2*q+d; J=2*u*(2*u+1)%M; L=(4*n+2)%M
    Du,U=scaled(u); Dn,N=scaled(n)
    V=Q=A=0
    for k in range(d+1):
        l=d-k; a=(k+1)*(l+1)*U[k]*N[l]; b=(k+1)*l*U[k]*N[l-1] if l else 0
        V=(V+a)%M;Q=(Q+b)%M; A=(A+(u-k)*(u+k+2)*(a+b))%M
    W=(L*A+u*U[d]*Dn*q*(2*d+3)*(n+2))%M
    Qn=J*L*Q%M; Z=L*(q*A+J*(V+Q))%M
    return (3*q*(4*q+3*d+1)**2*W*Qn-32*(3*q+d+1)*Z*Z)%M

def g(d,h,M): return carrier(d,(h-d-2)*pow(2,-1,M)%M,M)

def main():
    ps=primes(1505); counts=Counter(); rows=[]
    for d in range(5,302,2):
        lo=(4*d*d+4)//5; hi=4*d*d//3
        for p in ps:
            if not 2*d+3<p<=5*d:continue
            band='near' if p<=3*d+2 else 'far';counts[band]+=1
            if g(d,0,p):continue
            counts[band+'_degenerate']+=1
            M=p*p; r=g(d,0,M); s=g(d,p,M)
            assert r%p==s%p==0
            b=r//p; a=((s-r)//p)%p
            if a:
                counts['simple']+=1; t=-b*pow(a,-1,p)%p
                h=p*t; q=(h-d-2)//2
                if t==0 or (h-d-2)%2 or not lo<=q<=hi:
                    counts['range_or_parity']+=1; rows.append((d,p,band,a,b,t,'outside',q));continue
                residue=carrier(d,q,p**3);assert residue%M==0
                counts['inside']+=1
                if residue:counts['mod_p3_excluded']+=1
                else:counts['unresolved']+=1
                rows.append((d,p,band,a,b,t,'mod_p3',q,residue))
            elif b:
                counts['singular_no_lift']+=1;rows.append((d,p,band,a,b,'none'))
            else:
                counts['singular_all_lift']+=1;rows.append((d,p,band,a,b,'all'))
    for row in rows: print(*row)
    print(dict(counts))
if __name__=='__main__':main()

def rational_carrier(d,q):
    u=q+d;n=2*q+d;J=2*u*(2*u+1);L=4*n+2
    def pref(v):
        r=[F(1)];D=F(1)
        for i in range(d):
            D*=v+i+3;r.append(r[-1]*(v-i)/(v+i+3))
        return r,D
    U,Du=pref(u);N,Dn=pref(n);V=Q=A=F(0)
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*N[l];b=(k+1)*l*U[k]*N[l-1] if l else 0
        V+=a;Q+=b;A+=(u-k)*(u+k+2)*(a+b)/J
    E=U[d]*q*(2*d+3)*(n+2)/(2*(2*u+1)*L);Z=q*A+V+Q
    return (J*L*Du*Dn)**2*(3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2)

if __name__=='__main__':
    for d,p,q in [(73,269,5477),(147,347,18490)]:
        x=rational_carrier(d,F(q)); assert x.denominator==1
        assert x.numerator%(p**3)==carrier(d,q,p**3)
        print('independent rational verification',d,p,q,x.numerator%(p**3))
```

## Complete actual stdout

```
5 23 far 16 3 7 outside 77
21 59 near 53 36 6 outside 165
23 109 far 21 3 31 outside 1677
51 197 far 179 196 186 outside 18294
53 137 near 131 41 121 outside 8261
57 167 near 46 37 119 outside 9907
63 131 near 68 26 42 outside 2718
73 269 far 152 224 41 mod_p3 5477 5065270
91 401 far 183 346 226 outside 45266
93 367 far 276 274 124 outside 22706
103 353 far 163 47 95 outside 16715
111 229 near 117 182 202 outside 23072
147 347 near 295 12 107 mod_p3 18490 8789857
147 431 near 194 264 323 outside 69532
151 349 near 239 285 304 outside 52971
157 449 near 31 439 290 outside 65025
213 797 far 296 677 582 outside 231819
255 1039 far 574 712 6 outside 2988
261 743 near 501 35 562 outside 208651
271 1153 far 867 882 761 outside 438580
277 563 near 121 437 15 outside 4083
283 751 near 610 142 507 outside 190236
{'near': 3621, 'far': 6719, 'far_degenerate': 10, 'simple': 22, 'range_or_parity': 20, 'near_degenerate': 12, 'inside': 2, 'mod_p3_excluded': 2}
independent rational verification 73 269 5477 5065270
independent rational verification 147 347 18490 8789857
```
