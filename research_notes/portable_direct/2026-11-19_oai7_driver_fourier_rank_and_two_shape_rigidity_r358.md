# OAI7 r358 — Exact Fourier rank of the uniform-coordinate transport polytope and small-family rigidity

Date: 2026-11-19. New exact mathematical result continuing r353–r357 within the original OAI7/RESEARCH_DRIVER scientific line. This is author-side mathematics with shared prior scientific context, not an independent Native Result review.

## General prime-cyclic theorem

Let (p) be an odd prime, (d\ge1), and let (W_x=(w_{x,1},\ldots,w_{x,d})\in\mathbb F_p^d), (x=1,\ldots,m), be fixed ordered shapes. Let (p_x>0) be rational masses summing to 1. Choose nonnegative (z_{x,t}), (t\in\mathbb F_p), satisfying the fixed-profile and uniform-position equations

\[
\sum_t z_{x,t}=p_x,\qquad
\sum_x z_{x,a-w_{x,i}}=1/p
\quad(i=1,\ldots,d,\ a\in\mathbb F_p).
\tag{1}
\]

Define (\zeta=e^{2\pi i/p}), (M=(\zeta^{w_{x,i}})_{i,x}\in\mathbb Q(\zeta)^{d\times m}), and (r=\operatorname{rank}_{\mathbb Q(\zeta)}M). Let (A) denote the rational (0/1) coefficient matrix of all equations (1).

**Exact rank and dimension.**
\[
\boxed{\operatorname{rank}_{\mathbb Q}A=m+(p-1)r,\qquad
\dim_{\mathbb R}\mathcal P=(p-1)(m-r).}\tag{2}
\]
The dimension is the affine dimension of the nonnegative feasible polytope, because its strictly positive point (z_{x,t}=p_x/p) exists.

**Conditional translation rigidity.** The baseline law (z_{x,t}=p_x/p) is the **only** law satisfying (1) if and only if (r=m). In that case all (m p) atoms have positive weight. If the shapes are pairwise inequivalent under common translation, the ordered tuples are distinct across ((x,t)), and their joint Shannon entropy is exactly
\[
\boxed{H(H)=H((p_x)_x)+\log_2 p.}\tag{3}
\]

**Nonrigidity and rational entropy reduction.** If (r<m), the homogeneous constraint system has a nonzero *rational* vector. Starting from the strictly positive baseline and moving along this vector to a rational nonnegativity endpoint yields an exact feasible rational law with strictly fewer than (mp) positive cells and strictly smaller conditional-translation entropy. For translation-inequivalent shapes the same strict inequality holds for the entropy of the ordered sampler. A rational vertex has support at most (m+(p-1)r).

### Proof

For any real array (h_{x,t}), set (\widehat h_x(k)=\sum_t h_{x,t}\zeta^{kt}). Row-sum homogeneous constraints are (\widehat h_x(0)=0). The uniform-position homogeneous constraint in position (i) has Fourier transform
\[
\sum_x\zeta^{k w_{x,i}}\widehat h_x(k)=0
\qquad(k=1,\ldots,p-1).\tag{4}
\]
The Fourier transform is invertible over (\mathbb C). As (p) is prime, for each (k\ne0) the Galois automorphism (\zeta\mapsto\zeta^k) takes (M) to (M_k), so each (M_k) has complex rank (r). The complexification of the real homogeneous system therefore has dimension ((p-1)(m-r)). The original constraint matrix has rational entries, hence its rational, real and complex ranks coincide; rank-nullity gives (2).

If (r=m), every nonzero Fourier mode vanishes, fixing (z_{x,t}=p_x/p). Conversely if (r<m), the rational matrix has a nonzero rational null vector (h) with zero row totals and zero marginal changes. Since the baseline is positive and (h\ne0), taking either feasible nonzero scalar perturbation gives a different law; at the first nonnegativity endpoint all weights remain rational and at least one becomes zero. For fixed profile masses, conditional entropy satisfies (H(T\mid X)\le\log_2p), with equality precisely for uniform shifts in every positive fiber; hence any nonzero perturbation strictly lowers (H(X,T)=H(X)+H(T\mid X)). Translation-inequivalent shapes make ((X,T)\mapsto H) injective. Every rational vertex has at most \(\operatorname{rank}A\) positive variables by the standard dependent-column perturbation argument. This proves all claims.

## Two-profile obstruction for fully uniform positions

Take (m=2\), (d\ge2\), two shapes (W_1,W_2) with **different relative offsets** in some pair of coordinates, i.e.
\[
(w_{1,i}-w_{1,j})\ne(w_{2,i}-w_{2,j})\pmod p.
\]
The (2\times2) minor of (M_k) on rows (i,j) is nonzero for every (1\le k<p), since equality would imply (\zeta^{k[(w_{1,i}-w_{1,j})-(w_{2,i}-w_{2,j})]}=1). Therefore (r=2=m). With any prescribed positive profile masses, exact uniformity of *all* ordered-coordinate marginals forces each profile to use **every one of the (p) shifts uniformly**. If the profiles are translation-inequivalent, support is exactly (2p), with entropy (H(p_1,p_2)+\log_2 p). This excludes low-entropy conditional-shift compression in the two-shape model, without assuming equal profile masses or equal-probability individual codewords.

## OAI7 prime-29: exact rank 490 and kernel dimension 9,660

In the pinned r353 OAI7 polytope, (p=29,d=5,m=350), with 350 pairwise translation-inequivalent complete-loss-profile representatives. It suffices to certify that (M) has row rank 5. Five specific classes from r355's affine-orbit-7 enumeration, in the indicated order, are
\[
\begin{aligned}
&(0,5,6,11,12),\quad (0,1,7,8,14),\quad
(0,3,12,15,18),\\
&(0,4,7,15,18),\quad (0,3,6,15,18).
\end{aligned}
\]
For the (5\times5) matrix (B_{i,j}=\zeta^{w_{j,i}}\), specialize (\zeta\mapsto3\pmod {59}). Since (3^{29}=1\pmod {59}) and (3\ne1\pmod {59}), this defines a valid homomorphism (\mathbb Z[\zeta]\to\mathbb F_{59}\). Direct modular elimination gives
\[
\boxed{\det(B)\bmod 59=47\ne0.}\tag{5}
\]
Consequently the cyclotomic determinant is nonzero, proving (r=5) exactly, without numerical rank tolerances or a full 10,150-variable LP.

The **precise** number of independent linear constraints in r353 is thus
\[
\boxed{350+28\cdot5=490};
\]
the affine feasible dimension is
\[
\boxed{10,150-490=9,660}.\tag{6}
\]
The r353 rational-vertex upper bound of 490 positive rows follows with an *exact* rank certificate; r356–r357's sharp lower support 378 for one uniform coordinate is unchanged. Whether all five coordinates can be uniform with only 378 rows remains open.

### Standalone exact modular certificate (Python 3)

~~~python
from itertools import combinations
P=29
full=(1<<P)-1
def rot(m,t):
    return (((m<<t)|(m>>(P-t)))&full) if t else m
def norm(m):
    return min(rot(m,t) for t in range(P))
def mul(m,a):
    return sum(1<<((a*x)%P) for x in range(P) if (m>>x)&1)
reps=sorted({norm(sum(1<<x for x in ss))
             for ss in combinations(range(P),5)})
assert len(reps)==4095
where={m:i for i,m in enumerate(reps)}
orbits=[];seen=set()
for m in reps:
    if m in seen:continue
    orbit=[reps[i] for i in sorted({where[norm(mul(m,a))]
                                    for a in range(1,P)})]
    assert not (set(orbit)&seen)
    orbits.append(orbit);seen.update(orbit)
assert len(orbits)==150 and len(orbits[7])==28
shapes=[tuple(i for i in range(P) if (mask>>i)&1)
        for mask in orbits[7]]
chosen=[shapes[j] for j in [5,6,17,16,15]]
assert chosen==[
    (0,5,6,11,12),(0,1,7,8,14),(0,3,12,15,18),
    (0,4,7,15,18),(0,3,6,15,18)]
q=59;z=3
assert pow(z,29,q)==1 and z!=1
mat=[[pow(z,chosen[j][i],q) for j in range(5)] for i in range(5)]
def det_mod(A,q):
    A=[row[:] for row in A];n=len(A);res=1
    for k in range(n):
        t=next((i for i in range(k,n) if A[i][k]%q),None)
        if t is None:return 0
        if t!=k:A[t],A[k]=A[k],A[t];res=-res
        pivot=A[k][k]%q;res=res*pivot%q
        inv=pow(pivot,-1,q)
        for i in range(k+1,n):
            fac=A[i][k]*inv%q
            for j in range(k+1,n):
                A[i][j]=(A[i][j]-fac*A[k][j])%q
            A[i][k]=0
    return res%q
assert det_mod(mat,q)==47
assert 350+28*5==490 and 350*29-490==9660
print("r358 PASS: exact cyclotomic rank 5; polytope rank 490; nullity 9660")
~~~

The source class enumeration matches the r355 fixed finite construction. The modular certificate only determines the linear rank; its use alongside r347–r352's primal/dual and 350-profile certificates retains those results' existing evidence and contribution dependencies.

## Sources, scope, and continuation

Original task RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19; original researcher EM-EMF6D046-5A2844. This work builds on [r353](https://github.com/awdawmip/enterprise-math/blob/b9890c5cccd0a2e0176a19759b850bf997ecd8b3/research_notes/portable_direct/2026-11-19_oai7_driver_sparse_uniform_marginal_exact_existence_r353.md), [r355](https://github.com/awdawmip/enterprise-math/blob/6f359bcf30bccb59a3bbf1a025772cddfe301995/research_notes/portable_direct/2026-11-19_oai7_driver_four_disjoint_determinantal_transport_r355.md), [r356](https://github.com/awdawmip/enterprise-math/blob/b8d5997425d3a86110f9e2463b3e87b3e24b601a/research_notes/portable_direct/2026-11-19_oai7_driver_modular_uniform_support_gap_r356.md), and [r357](https://github.com/awdawmip/enterprise-math/blob/22bd6c41175866bc05595faf26ec7745f84b3b54/research_notes/portable_direct/2026-11-19_oai7_driver_one_uniform_coordinate_support_378_r357.md).

This is an author-side theorem and independently reproducible modular certificate. It is not a native independent mathematical Review, a Source/Activity association, a formal Result admission, a CLAIM, an X6 carrier transfer, or closure of the original mother objective. Current native Driver authority and any formal admission are checked separately. The next scientific decision is to exploit exact linear rank and component/connectivity obstructions to seek or rule out 378-support five-marginal vertices.
