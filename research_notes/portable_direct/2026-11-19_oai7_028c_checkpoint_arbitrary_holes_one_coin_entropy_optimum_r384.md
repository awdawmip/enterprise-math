# OAI7 r384 — Arbitrary checkpoint-dependent missing sets: one common coin is globally optimal

Date: 2026-11-19. Mathematical continuation and adversarial strengthening of r383, with the original researcher's missing-residue example preserved. This is an **author-side proof with shared-context exposure**, not an independent Native Result review, a frozen Result, or Task completion.

## Exact proposition (conditional shared shift, arbitrary holes)

Let \(G=\mathbb Z/p\mathbb Z\) for an integer \(p\ge3\), let \(k\ge1\), \(0<\beta<1\), and put \(L=p^{1-\beta}\), \(m=\lceil L\rceil\) with \(1\le m\le p/2\). Fix \(0<\tau\le3/8\), and set
\[
 a=\frac{\tau(p-m)}p,\qquad 0<a<1/2.
\]
Let \(C\) be a finite-valued checkpoint with \(\Pr(C=c)>0\) for each reported state. For each \(c\) and coordinate \(j\), choose **an arbitrary** set \(B_{j,c}\subset G\) of size \(m\). Conditional on \(C=c\), the coordinate \(Y_j\) is uniform on \(G\setminus B_{j,c}\). Different coordinates of \(Y\) may be dependent; no common interval or common hole is required.

A single joint displacement \(U\in G^k\) may have a law depending on \(C\), and may correlate its \(k\) coordinates arbitrarily, but assume the essential conditional-independence premise \(U\perp Y\mid C\). Write \(Z=Y+U\), and retain the original **strict-cardinality** signed-coverage criterion at every checkpoint and coordinate:
\[
 \#\{u\in G:\Pr(\pm Z_j=u\mid C=c)<\tau/p\}<L.
\]

**Theorem.** Every such displacement satisfying conditional coverage obeys
\[
 \boxed{ H(U\mid C)\ge h_2(a),\qquad H(U)\ge h_2(a). }
\]
Both lower bounds are attained **simultaneously for all checkpoint states and all coordinates**, by a *single binary coin independent of \(C,Y\)*:
\[
 \boxed{D\sim{\rm Bernoulli}(a),\quad U=D(1,\ldots,1)\pmod p.}
\]
Thus the minimum conditional and unconditional displacement entropy is \(h_2(a)\) nats even for arbitrary checkpoint-varying missing sets and arbitrary cross-coordinate dependence in \(Y\).

More precisely, this attaining construction has exactly
\[
 \boxed{\#\{u:\Pr(Z_j=u\mid C=c)<\tau/p\}
       =|B_{j,c}\cap(B_{j,c}+1)|\le m-1<L}
\]
exceptional residues at checkpoint \(c\), in each signed coordinate (with relabeled exceptional residues for the minus sign). The construction **need not repair every missing residue**. The strict permitted-exception budget, together with the absence of nontrivial periods under the generator \(1\), makes the one-coin optimum possible.

This theorem concerns entropy of the shared displacement variable. It does not assert full joint-vector coverage, satisfaction of an external coverage-transfer theorem's sample-size/Chernoff hypotheses, or a native X6/BRC transfer.

## Proof

Fix a checkpoint state \(c\) and coordinate \(j\). Denote the conditional law of \(U_j\) by \(\mu(v)\) and the hole by \(B\). Conditional independence and uniformity on \(G\setminus B\) give the exact convolution identity
\[
 \Pr(Z_j=u\mid C=c)
  =\frac{1-\mu(u-B)}{p-m},\qquad
 \mu(u-B)=\sum_{b\in B}\mu(u-b).
\]
Choose a modal value \(v\) with \(t=\mu(v)=\max_w\mu(w)\). If \(t>1-a\), then for all \(m\) **distinct** \(u\in v+B\), one has \(\mu(u-B)\ge t>1-a\), whence
\[
 \Pr(Z_j=u\mid C=c)<a/(p-m)=\tau/p.
\]
Since \(m=\lceil L\rceil\ge L\), this contradicts strict coverage. Therefore \(\max\mu\le 1-a\). Because \(0<a<1/2\), the binary probability vector \((1-a,a)\) majorizes \(\mu\). Shannon entropy is Schur-concave, so
\[
 H(U\mid C=c)\ge H(U_j\mid C=c)\ge h_2(a).
\]
Average over \(c\) to obtain the first bound. The elementary inequality \(H(U)\ge H(U\mid C)\) gives the second; nothing here assumes independent coordinates of \(Y\).

For attainment, take one Bernoulli coin \(D\) independent of \(Y,C\) and let every displacement coordinate equal \(D\cdot1\pmod p\). For a given \(B=B_{j,c}\),
\[
 \Pr(Z_j=u\mid C=c)
 =\frac{(1-a)\mathbf1_{u\notin B}
       +a\mathbf1_{u-1\notin B}}{p-m}.
\]
If \(u\notin B\cap(B+1)\), at least one numerator indicator is 1, and the probability is at least \(a/(p-m)=\tau/p\). At \(u\in B\cap(B+1)\), the probability is 0 and is exceptional.

Because \(1\) generates the full cyclic group and \(B\) is a nonempty proper subset, \(B+1\ne B\). Hence \(|B\cap(B+1)|\le m-1<L\). This holds for **every** set \(B_{j,c}\), so the same coin handles all \(c,j\), even when the holes are unrelated. Negation is a residue bijection, preserving the cardinality of the exceptional set. Since the map \(D\mapsto D(1,\ldots,1)\) is injective and \(D\perp C\),
\[
 H(U\mid C)=H(U)=H(D)=h_2(a).
\]
QED.

## Exact finite checks

The following finite check exhausts every missing set of size \(m=\lceil\sqrt p\rceil\) at \(p=7,11,13,17\), with \(\beta=1/2,\tau=3/8\). All arithmetic in the coverage test is rational. It separately verifies the precise intersection formula and the strict exception budget.

~~~python
from fractions import Fraction
from itertools import combinations
from math import isqrt, comb

for p in (7,11,13,17):
    m=isqrt(p) + (isqrt(p)**2 < p)
    assert m<=p//2
    tau=Fraction(3,8)
    a=tau*Fraction(p-m,p)
    count=0
    max_exception=0
    for subset in combinations(range(p),m):
        B=set(subset)
        Bshift={(v+1)%p for v in B}
        exceptions=[]
        for u in range(p):
            prob=((1-a)*int(u not in B)
                  +a*int((u-1)%p not in B))/(p-m)
            if prob < tau/p:
                exceptions.append(u)
        assert set(exceptions)==B.intersection(Bshift)
        assert len(exceptions)<=m-1
        max_exception=max(max_exception,len(exceptions))
        count+=1
    assert count==comb(p,m)
    print(p,m,count,max_exception,a)
# Expected: (7,3,35,2,3/14), (11,4,330,3,21/88),
#           (13,4,715,3,27/104), (17,5,6188,4,9/34).
~~~

These checks establish the stated finite exhaustions only. The general proof uses modal-mass majorization and the cyclic generator, not extrapolation from the finite tests.

## Distinction from r383 and task routing

- r383 optimized the independent shift for a **fixed consecutive missing interval**, constructing a zero-exception displacement \(g=m\).
- r384 permits **arbitrary missing sets changing with the exact shared checkpoint** and proves that the generator \(g=1\) always attains the same optimum with fewer than \(L\) exceptional residues. It also shows the lower bound persists when \(U\) depends on \(C\) subject to \(U\perp Y\mid C\).
- These checkpoint-conditional statements operate on the exact finite missing-residue model. The pinned external coverage-transfer lemma has additional stronger hypotheses, and no counterexample to that complete external theorem is claimed.

Formal Task: \`RS-OAI7-028-C-20261007-6F2A81\`, publication \`TP2-96FAC49786245691AE19\`. Original contributor \`EM-EMF6D046-5A2844\` retains authorship of the missing-residue finite counterexample and initial two-shift bound. Related author-side work: [r383](https://github.com/awdawmip/enterprise-math/blob/8421e1f27818aa736b0249119f467ea3418d0280/research_notes/portable_direct/2026-11-19_oai7_028c_independent_common_shift_global_entropy_optimum_r383.md), and original [Source checkpoint](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/_checkpoint.json).

Evidence status: author-side complete argument, exact finite audit above, *NOT* independent Native Review, *NOT* newly frozen Result or Task DONE. Next useful review is to compare the full external lemma's **conditional-time sample-size assumptions** and exact quantifier order against this sharp finite checkpoint family. Current Task owner and publication must be freshly checked before operational writes.
