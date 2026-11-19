# OAI7 r358 — Exact 490-rank certificate and five-tree rigidity at critical uniform support

Date: 2026-11-19. Exact finite mathematical extension of the OAI7 minimax sampler line, in the existing shared RESEARCH_DRIVER context. This is author-side work and not an independent Native Result review.

## Model, precise conclusions

Use the pinned prime-29 OAI7 minimax model: five distinct ordered coordinates \(H=(H_1,\ldots,H_5)\in\mathbb F_{29}^5\); underlying unordered set \(C\); 350 strictly positive complete fixed-test loss-profile masses \(p_x=k_x/N\), \(N=28\cdot474893659=13,297,022,452\), \(\gcd(N,29)=1\). The profile of \(C\) is invariant under simultaneous translation. Each profile representative \(W_x\) is selected from a different translation class and has a fixed ascending ordering \(w_x=(w_{x,1},\ldots,w_{x,5})\).

An ordered sampler with exact uniform marginals has variables \(z_{x,t}\ge0\) for \(x=1,\ldots,350\) and \(t\in\mathbb F_{29}\), and constraints
\[
\sum_tz_{x,t}=p_x,\qquad
\sum_{x,t:\,w_{x,\ell}+t=a}z_{x,t}=1/29
\quad(\ell=1,\ldots,5;\ a\in\mathbb F_{29}).
\]
Every such sampler retains the exact r347 minimax failure vector by profile invariance.

**Theorem A (full linear rank).** With the canonical ascending-order representatives from r350, the above \(495\times10150\) rational constraint matrix has **rank exactly \(490\)**. Thus its strictly feasible affine solution set has dimension \(10150-490=9660\); the five omitted row dependencies are the only linear equation dependencies. The existing r353 support-\(\le490\) vertex bound is the actual matrix-rank bound, not an overestimate due to undetected row dependencies. This statement does *not* assert that all vertices require 490 atoms.

**Theorem B (critical-support five-tree condition).** For **any** exactly minimax ordered five-coordinate law with all five coordinates uniform and exactly \(350+29-1=378\) positive ordered atoms, construct five bipartite multigraphs \(B_\ell\) on the common 350 profile vertices \(x\) and 29 residue vertices \(a\). Each positive atom \(h\), labeled by its profile \(x(h)\), makes one edge \((x(h),h_\ell)\) of weight \(\Pr(H=h)\) in each \(B_\ell\). Then, for every \(\ell\), \(B_\ell\) is a **spanning tree**. In particular no two positive atoms from the same profile may share the same residue at any position.

For any edge \(e\) in any such tree, remove it and let one resulting component contain \(K\) units of integer fiber mass \(\sum_{x\in U}k_x=K\) and \(b\) residue vertices. Its weight is uniquely forced by
\[
\boxed{\Pr(e)=\frac{|29K-Nb|}{29N}.}
\]
Thus any 378-atom all-five-coordinate construction must carry **five simultaneous tree structures with a single consistent assignment of these cut-forced rational atom weights**. This supplies a finite arithmetic/combinatorial certification target for the unresolved 378–490 gap. Whether such a five-tree realization actually exists remains open.

## Proof of theorem A: Fourier rank and an exact small-field witness

Fourier transform the 29 translation variables \(z_{x,t}\) separately for each \(x\), with a primitive complex 29th root of unity \(\zeta\). The zero frequency gives the 350 independent profile equations. At every nonzero frequency \(k\), the remaining five marginal equations have coefficient matrix
\[
B(k)_{\ell,x}=\zeta^{k w_{x,\ell}},\qquad
1\le\ell\le5,\ 1\le x\le350.
\]
The full rank is therefore
\[
350+\sum_{k=1}^{28}\operatorname{rank}_{\mathbb Q(\zeta)}B(k).
\]
Galois conjugacy \(\zeta\mapsto\zeta^k\) makes all 28 ranks equal. It suffices to prove that \(B(1)\) contains a nonzero \(5\times5\) minor.

Among the 28 translation classes of the supported multiplicative-affine orbit numbered 7 by the pinned r347/r355 canonical enumeration, select the ascending five-sets at zero-based class indices \(1,2,3,4,5\):
\[
\begin{split}
&(0,1,4,5,6),\quad(0,1,6,7,12),\\
&(0,2,4,10,12),\quad(0,2,8,10,12),\\
&(0,5,6,11,12).
\end{split}
\]
In \(\mathbb F_{59}\), the element \(3\) has order 29. Evaluate the determinant polynomial of the corresponding 5-by-5 matrix of powers of \(\zeta\) at \(\zeta=3\bmod59\). Exact modular Gaussian elimination yields
\[
\det[3^{w_{j,\ell}}]_{\ell,j=1}^5=24\pmod{59}\ne0.
\]
If the complex cyclotomic determinant vanished, its integral polynomial would be divisible by \(\Phi_{29}(z)\), and would evaluate to zero at every nontrivial 29th root over \(\mathbb F_{59}\). The nonzero residue is a contradiction. Hence every \(B(k)\) has row rank 5, giving \(350+28\cdot5=490\). Rational and complex ranks agree for this integer matrix. Since \(z_{x,t}=p_x/29>0\) is feasible, the affine dimension is exactly \(10150-490=9660\).

## Proof of theorem B: coprimality turns critical support into trees

For a fixed position \(\ell\), its profile-to-residue bipartite multigraph has 350+29 vertices and 378 weighted edges. Every vertex is incident to an edge because all 350 profile masses are positive and all 29 residue marginals are \(1/29\).

Any graph connected component contains whole profile vertices and whole residue vertices, so conservation of its edge weights gives
\[
\frac{K}{N}=\frac{b}{29}
\quad\Longrightarrow\quad 29K=Nb.
\]
By \(\gcd(N,29)=1\), a nonempty component must have \(29\mid b\), hence \(b=29\); it contains *all* residue vertices and therefore all profile vertices. Thus the graph is connected. It has exactly \(350+29-1\) edges, so it is a tree, including as a multigraph (parallel edges would form a cycle).

For an edge \(e\), take one component after deletion. Conservation of internal masses cancels all other internal edges, leaving an unmatched source-minus-target total, equal in absolute value to the edge weight. This gives \(|K/N-b/29|\), the claimed cut formula. The same weighted atoms must satisfy that formula in each of the five different coordinate trees.

## Standalone finite exact certificate for theorem A

Python 3 standard library only. This independently regenerates all 4095 translation classes, all 150 multiplicative-affine orbits, the five named supported shapes, and the nonzero determinant modulo 59. Gaussian elimination is exact modular arithmetic.

~~~python
from itertools import combinations

P, Q = 29, 59
full = (1 << P) - 1
def rot(m,t):
    t %= P
    return (((m << t) | (m >> (P-t))) & full) if t else m
def norm(m):
    return min(rot(m,t) for t in range(P))
def mul(m,a):
    return sum(1 << ((a*i) % P) for i in range(P) if (m >> i)&1)

reps = sorted({norm(sum(1 << i for i in A))
               for A in combinations(range(P),5)})
assert len(reps) == 4095
seen, orbits = set(), []
for c in reps:
    if c in seen: continue
    orbit = sorted({norm(mul(c,a)) for a in range(1,P)})
    assert not (set(orbit) & seen)
    seen.update(orbit)
    orbits.append(orbit)
assert len(orbits)==150 and len(orbits[7])==28
shapes = [tuple(i for i in range(P) if (c >> i)&1)
          for c in orbits[7][1:6]]
assert shapes == [(0,1,4,5,6),(0,1,6,7,12),
                  (0,2,4,10,12),(0,2,8,10,12),
                  (0,5,6,11,12)]
assert pow(3,29,Q)==1 and 3 != 1
mat = [[pow(3,shapes[j][i],Q) for j in range(5)]
       for i in range(5)]
def det_mod(a,q):
    a=[r[:] for r in a]
    ans=1
    for j in range(len(a)):
        ix=next(i for i in range(j,len(a)) if a[i][j] % q)
        if ix!=j:
            a[j],a[ix]=a[ix],a[j]
            ans=-ans
        v=a[j][j]%q
        ans=ans*v%q
        inv=pow(v,-1,q)
        for i in range(j+1,len(a)):
            factor=a[i][j]*inv%q
            for k in range(j,len(a)):
                a[i][k]=(a[i][k]-factor*a[j][k])%q
    return ans%q
assert det_mod(mat,Q)==24
assert 350+5*(29-1)==490
print("PASS: supported 5-shape 29th-root minor = 24 mod 59; rank 490")
~~~

## Dependency and next action

The full-rank statement uses the r347/r355 canonical positive orbit-7 shape enumeration and r350/r353 ascending representative convention. The tree statement relies on the r351/r352 exact fixed 350 positive profile masses and the r356 denominator/coprimality fact, but its proof is independent of linear optimization. Pinned parent evidence: [r353](https://github.com/awdawmip/enterprise-math/blob/b9890c5cccd0a2e0176a19759b850bf997ecd8b3/research_notes/portable_direct/2026-11-19_oai7_driver_sparse_uniform_marginal_exact_existence_r353.md), [r356](https://github.com/awdawmip/enterprise-math/blob/b8d5997425d3a86110f9e2463b3e87b3e24b601a/research_notes/portable_direct/2026-11-19_oai7_driver_modular_uniform_support_gap_r356.md), [r357](https://github.com/awdawmip/enterprise-math/blob/22bd6c41175866bc05595faf26ec7745f84b3b54/research_notes/portable_direct/2026-11-19_oai7_driver_one_uniform_coordinate_support_378_r357.md).

For exact support 378 in all five positions, search for an admissible five-tree hypergraph with cut-consistent weights; alternatively extract a sparse vertex and verify all 350 fiber totals and all 145 positional sums in rational arithmetic. This document neither changes native ownership nor supplies an independent Driver pass.

Original Task RS-OAI7-028-C-20261007-6F2A81, immutable publication TP2-96FAC49786245691AE19, original researcher EM-EMF6D046-5A2844; author-side Driver continuation preserves those contributions. Native Result admission, formal Task completion and mother-objective closure are unchanged.
