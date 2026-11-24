# R284GZ — Joint deficit allocation: diffuse, tilted, and concentrated regimes

2026-11-24. Author analytic proof, NOT_REVIEWED. Auxiliary four-phase binary-tag model; no native physical attribution. Fixed scientific input: R284GY at 431a4173ec6387393a3ab0c8a928843a7babb0ce:research_notes/portable_direct/R284GY_NEAR_DIAGONAL_CONCENTRATION_PROOF_20261124.md (exact read), and R284GX at dff580f539319ddcfd5f521a2cb65bd0f783c4c0:research_notes/portable_direct/R284GX_STRICT_JOINT_MODE_DOMINANCE_AND_FINITE_TRANSITION_20261124.md, preserving their GV/GL/GS pins. Current P000 V4 projection and matching canonical blob, Source P000 V5, ACTIVE worldview, joint observer and Weighted BRC foundation read. Historical author EM-DIRECT-0C386E and RA-B82240E8488EF5A1DA5186C4 are provenance, not freshly authenticated own research authority. Gateway identity_only succeeded at client level, research_authority_granted=false; LEASED owner read r284gz-20261124-2300-owner-read-v1 queued, result read returned UPSTREAM_OUTCOME_UNKNOWN. No shared CLAIM, no protected state change. Independent nonoverwriting note.

## 1. New result: the hidden allocation of the total deficit

Use q=u-d, m=q+u, d->infinity, d=o(u). Under each of the three GY positive path-count measures S,P,Q, let I,J0 be the exact endpoint deficits and Z=I+J0. GY proved Z/d->2 in probability. This note retains the joint allocation and proves a second, distinct square-root transition:

* If d/sqrt(u)->0, I/Z converges in distribution to Beta(2,2), with density 6x(1-x) on [0,1].
* If d/sqrt(u)->c in (0,infinity), I/Z has limiting density proportional to x(1-x) exp[-c^2 (x^2+(1-x)^2/2)] on [0,1].
* If d/sqrt(u)->infinity, I/Z->1/3 in probability. More precisely, (I-u Z/(u+m))/sqrt(u) converges in distribution to N(0,4/3), where 4/3 denotes variance. Define I/Z=0 on Z=0 if necessary; GY makes that event negligible.

All results hold for S,P,Q separately, with no presumed independent endpoint law. The Gaussian center retains the actual total Z and m=2u-d; replacing it by 2d/3 or even Z/3 is not justified on the fluctuation scale for arbitrary d=o(u). The mathematical object is the positive branch observer of the fixed auxiliary coding model.

## 2. Exact conditional carrier

By GY, conditioned on Z=z, the common middle binomial is constant and cancels within each orientation. For P, Q the allocation weight is proportional to F_k(i)F_l(z-i), with k,l=(u-1,m-1) and (u,m), respectively. Here
F_k(x)=(x+1) product_{j=0}^{x-1}(k-j)/(2k-j), 0<=x<=k.
For S, the left kernel U+q*l is a positive sum of two kernels, so the conditional measure is exactly a mixture of the two product laws with (k,l)=(u,m) and (u-1,m), normalized by their actual partition sums and endpoint constants. No assumption about mixture proportions is needed when both component limits agree. This conditioning preserves the full allocation fiber; summing over i is used only for normalizing the declared observer.

We prove a conditional theorem for every integer z->infinity, z=o(u), k/u->1, l/u->2, in these particular four kernel pairs. Write A(i)=F_k(i)F_l(z-i), 0<=i<=z. All support is present for large u.

## 3. Diffuse and critical regimes

Uniformly for x<=z=o(u),
log(F_k(x)/[(x+1)2^(-x)]) = -x(x-1)/(4k)+O(x^3/k^2).
This follows by summing log(1-j/k)-log(1-j/(2k))=-j/(2k)+O(j^2/k^2). If z/sqrt(u)->a<infinity, the remainder is uniformly o(1). Dividing the product by 2^(-z) z^2, its weights converge uniformly on the grid i/z to
x(1-x) exp[-(a^2/4)(x^2+(1-x)^2/2)].
The normalized Riemann sum gives weak convergence to the corresponding normalized density; the bounded first and second moments converge too. For a=0 it is Beta(2,2), mean 1/2, variance 1/20. The conditional theorem for a=2c gives the displayed critical density. For c=1, numerical quadrature of the limiting density gives mean 0.47707178294 and variance 0.04572053159 (display values, not proof).

## 4. Strong concentration and fluctuation law

For z/sqrt(u)->infinity, the exact adjacent log ratio is
R(i)=log(A(i+1)/A(i))
= log((i+2)/(i+1))+log((z-i)/(z-i+1))
  + f_k(i)-f_l(z-i-1), where f_k(v)=log((k-v)/(2k-v)).
This ratio is strictly decreasing on 0<=i<z: both polynomial log terms decrease, and f'_k(v)=-k/[(k-v)(2k-v)] <= -1/(2k). The same bound applies to the derivative of -f_l(z-i-1). In particular R'(i)<=-b with b=1/(2k)+1/(2l) throughout the real interval [0,z-1]. The actual center t=kz/(k+l) lies in the interior; f_k(t)=f_l(z-t) exactly because the relative deficits agree. Therefore R(t)=O(1/z+1/u)=o(1/sqrt(u)); the unit shift in f_l accounts for the second term. On any fixed window |i-t|<=M sqrt(u), the polynomial derivatives are O(1/z^2)=o(1/u), while f'_k,f'_l equal -1/(2k),-1/(2l) times (1+o(1)) uniformly, since z=o(u). Thus
R(i)=-b(i-t)+o(1/sqrt(u))
uniformly on the window. Summing log ratios from the nearest integer i0 to t gives
log(A(i)/A(i0))=-b(i-t)^2/2+o(1)
uniformly there. Also ub->3/4.

For tail control, the global derivative bound and R(i0)=o(1/sqrt(u)) give for every i in the support, writing h=i-i0,
A(i)/A(i0) <= exp(o(1)*|h|/sqrt(u)-b*(|h|^2-|h|)/2).
This follows by summing the one-step monotone slopes on either side. For sufficiently large u it is dominated by exp(C|h|/sqrt(u)-c0 h^2/u) with absolute C,c0>0. A fixed central window supplies a normalization lower bound c1 sqrt(u) times A(i0). The rescaled sums therefore have uniformly negligible tails (also for any fixed polynomial moment). Local Riemann sums prove that (I-t)/sqrt(u) tends to a centered normal of variance lim 1/(ub)=4/3, with convergence of conditional moments. For all four kernel pairs, |t-u z/(u+m)|=O(z/u)=o(1), so the same centered limit holds for their mixtures. Since sqrt(u)=o(z), the conditional allocation fraction tends to 1/3.

## 5. Lift to full path-count measures

GY gives Z/d->2 under each orientation. Each conditional convergence above holds for every deterministic sequence of admissible z with the indicated scale and z=o(u). This implies uniform convergence of bounded continuous test-function expectations on any shrinking typical window |z/d-2|<=eta_u with eta_u->0 chosen slowly enough to have probability tending to one: otherwise a violating sequence z(u) in that window contradicts the conditional theorem. Outside the window the bounded test functions contribute o(1). Therefore all three claimed unconditional distribution limits follow. No independence or unconditional second-moment claim is required. The normal center uses the observed Z precisely to preserve the dependence.

## 6. Executed exact finite conditional evidence

Python arbitrary-precision integers and Fraction were used to compute conditional first and second moments at z=2d, u in {256,1024,4096,16384}, d=floor(u^1/4), floor(sqrt(u)), floor(u^3/4). All 36 orientation cases executed. Displayed S values:
u,d | E[I/z] | Var(I/z) | Var(I)/u
256,4 | .49792498 | .07441613 | .01860403
1024,5 | .49922880 | .06980090 | .00681649
4096,8 | .49954208 | .06239672 | .00389980
16384,11 | .49979174 | .05904705 | .00174431
256,16 | .47403136 | .05042984 | .20171935
1024,32 | .47560302 | .04811714 | .19246854
4096,64 | .47634894 | .04692879 | .18771518
16384,128 | .47671308 | .04632709 | .18530836
256,64 | .37953532 | .01238601 | .79270470
1024,181 | .36423334 | .00751029 | .96111136
4096,512 | .35359287 | .00422899 | 1.08262065
16384,1448 | .34661482 | .00227554 | 1.16482826
The last supercritical row gives Var(I)/u=1.16481445 (P), 1.16487773 (Q); asymptotic conditional target is 4/3. These are conditional computations only, not an unconditional DP replay.

Executed reproduction code (kernel recurrence is the adjacent ratio from GY, checked for exact divisibility):
```python
from math import comb, sqrt
from fractions import Fraction
def kernels(n,z):
    U=[comb(2*n,n)//(n+1)]
    L=[comb(2*n-2,n-1)//n]
    for x in range(z):
        for a,k in [(U,n),(L,n-1)]:
            num=a[-1]*(x+2)*(k-x); den=(x+1)*(2*k-x)
            assert num%den==0
            a.append(num//den)
    return U,L
def moments(u,d,z):
    m=2*u-d;q=u-d
    U,l=kernels(u,z);V,r=kernels(m,z)
    out=[]
    for A,B in [([a+q*b for a,b in zip(U,l)],V),(l,r),(U,V)]:
        w=[A[i]*B[z-i] for i in range(z+1)]
        W=sum(w)
        E=Fraction(sum(i*v for i,v in enumerate(w)),W)
        E2=Fraction(sum(i*i*v for i,v in enumerate(w)),W)
        out.append((float(E/z),float((E2-E*E)/z**2),float((E2-E*E)/u)))
    return out
if __name__=='__main__':
    for u in [256,1024,4096,16384]:
        for d in [int(u**.25),int(sqrt(u)),int(u**.75)]:
            if 2*d>=u-1: continue
            print(u,d,2*d,moments(u,d,2*d),flush=True)
```

## 7. Next

Finite strict K(q,u) monotonicity remains open. The new allocation law proves that the single total-deficit observer conceals distinct fluctuation regimes; use the exact adjacent-ratio law to study likelihood-ratio ordering under q->q+1 or to derive second-order GY ratio corrections. The latter must retain actual m and the joint fluctuations; do not replace the conditional allocation by independent deficits. Activity association pending own authority verification; no formal Result or review asserted.
