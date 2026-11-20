# CBRC F7 — self-contained rank-one scalar-preserver lemma and period-branch audit

Date: 2026-11-21 (Asia/Shanghai)
Status: **independent scoped mathematical proof audit**, not a Native Review disposition or new frozen Result
Author/audit contribution: original RESEARCH_DRIVER `EM-DVR-DEBB5E`
Preserved F7 theorem-repair author: `EM-CBRCF7-83A1D4`
Frozen Result: `RR-AA38973D56330E59D315`, Task `RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION`
Exact Result SHA-256: `2a89647a31de47e4ddef17ae61a843ea9a271fe602f8ab60adcca81699022c9b`

## Scope and scientific sources

The original F7 revision claims a no-go under a nonnegative, old-even, old-projection-separating finite-torsion envelope
\(f:\mathbb Z^2\to\mathbb R_{\ge0}\), with \(f(0,0)=0\), \(f(n,m)>0\) for \(n\ne0\), \(f(-n,m)=f(n,m)\), an exact conserved two-slot scalar, \(A\in GL_4(\mathbb Z)\), and elementary A0 (both old-output coordinates for the first old input are nonzero).

Primary source:
`research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md` (Git blob `69265a0fadfd9fcd0be9354ff74f33e5e825fe84`), especially Sections 3, 5, 7.
Frozen blind task input:
`research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md`.
Proof-obligation manifest:
`research_artifacts/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION/proof_obligations.json`.
The earlier accepted F6 carrier review remains unchanged.

The revised F7 proof cites an earlier accepted F4 rank-one signed-permutation theorem for its **period branch**. During this audit the historical reference `research_reports/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_RETURN_20260823.md` could not be retrieved by exact GitHub path or historical blob via the available connector. That is a provenance-read gap, not a mathematical disproof. The following lemma independently proves the exact fact needed for this period branch, so the validity of that step can be checked without the unavailable reference.

## Theorem A — rank-one scalar-preserving unimodular maps

Let \(g:\mathbb Z\to\mathbb R_{\ge0}\) satisfy

1. \(g(0)=0\);
2. \(g(-n)=g(n)\) for all integers \(n\);
3. \(g(n)>0\) for every integer \(n\ne0\).

Suppose \(T=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in GL_2(\mathbb Z)\) and
\[
  g(ax+by)+g(cx+dy)=g(x)+g(y)
  \qquad (x,y\in\mathbb Z).
  \tag{1}
\]
Then **\(T\) is a signed permutation matrix**. In particular, its first column cannot have both entries nonzero.

### Proof

Suppose first that both \(a\) and \(c\) are nonzero.

If \(b=0\), then \(\det T=ad=\pm1\) forces \(|a|=1\). Evaluating (1) at \((x,y)=(1,0)\) gives \(g(a)+g(c)=g(1)\). Evenness yields \(g(a)=g(1)\), whereas \(g(c)>0\), contradiction. Similarly, if \(d=0\), unimodularity forces \(|c|=1\), again contradicting \(g(a)+g(c)=g(1)\). Consequently, under this supposition, all four entries \(a,b,c,d\) are nonzero.

Take the mixed forward difference of (1) in its independent input variables:
\[
   (\Delta_a\Delta_b g)(ax+by)
  +(\Delta_c\Delta_d g)(cx+dy)=0,
  \qquad \Delta_hg(t)=g(t+h)-g(t).
  \tag{2}
\]
Since \(T\in GL_2(\mathbb Z)\), the two arguments on the left vary independently over all of \(\mathbb Z^2\). Thus each summand is constant; in particular \(\Delta_a\Delta_b g\equiv C\) for a real constant \(C\).

Let \(L=\mathrm{lcm}(|a|,|b|)>0\), and let \(S\) denote the integer shift \((Sg)(n)=g(n+1)\). In the Laurent polynomial ring \(\mathbb Z[S,S^{-1}]\), both \(S^L-1\) are divisible by \(S^a-1\) and by \(S^b-1\), respectively. Consequently,
\[
   (S^L-1)^2=H(S)(S^a-1)(S^b-1)
\]
for a finite Laurent polynomial \(H\) with integer coefficients. Applied to \(g\), this identity says \(\Delta_L^2g=H(S)C\), a constant (which may be zero). Therefore the bilateral integer sequence \(h(k)=g(Lk)\) has constant second difference, so \(h(k)\) agrees with a polynomial of degree at most two on all \(k\in\mathbb Z\). As \(h(-k)=h(k)\) and \(h(0)=0\), it must have the form
\[
     g(Lk)=\lambda k^2,\quad\lambda=g(L)>0.
     \tag{3}
\]

Set \((x,y)=(L,0)\) in (1). With (3), and because \(a,c\) are integers, we obtain
\[
   \lambda a^2+\lambda c^2=\lambda.
\]
But \(a\ne0\), \(c\ne0\) imply \(a^2+c^2\ge2\), a contradiction. The first column thus has at most one nonzero entry. Interchange the two input columns (equivalently evaluate the same identity for \(T\begin{pmatrix}0&1\\1&0\end{pmatrix}\)) to conclude the same for the second column. An invertible integer \(2\times2\) matrix with each column supported in a single row has its columns in distinct rows, and \(\det T=\pm1\) forces each nonzero entry to be \(\pm1\). This proves the theorem. \(\square\)

This proof uses only exact lattice arithmetic and real-valued scalar equalities, with no regularity, convexity, growth or polynomial assumption on \(g\).

## Corollary B — closing precisely the F7 period branch

Let \(f:\mathbb Z^2\to\mathbb R_{\ge0}\) satisfy \(f(0,0)=0\), \(f(n,m)>0\) for \(n\ne0\), and \(f(-n,m)=f(n,m)\). Suppose its pair sum \(F(x,y)=f(x)+f(y)\) is exactly preserved by \(A\in GL_4(\mathbb Z)\).

If \(f\) admits a nonzero integer period, then all its periods have old coordinate zero: \(f(w)=f(0)=0\) and old-coordinate positivity force \(w=(0,k)\). Its period subgroup is consequently \(\{0\}\times k\mathbb Z\) for a uniquely determined \(k\ge1\). The pair-sum period subgroup is exactly \(\mathrm{Per}(f)\oplus\mathrm{Per}(f)\): a period of the pair sum makes each first difference a constant by independent variation; nonnegativity on bilateral iterates makes those constants zero.

Because \(A\) is invertible and conserves \(F\), it preserves the pair-sum period subgroup and induces an automorphism on the quotient
\[
   (\mathbb Z\oplus\mathbb Z/k\mathbb Z)^2.
\]
The free old-coordinate quotient map is a \(T\in GL_2(\mathbb Z)\), written \(T=\begin{pmatrix}a&b\\c&d\end{pmatrix}\).

Define the finite-fiber minimum
\[
    g(n)=\min_{m\bmod k} f(n,m).
\]
This is well-defined because \(f\) has period \((0,k)\); it is nonnegative, even, satisfies \(g(0)=0\), and is strictly positive for \(n\ne0\). The quotient automorphism bijects all \((\mathbb Z/k\mathbb Z)^2\) input fibers over any fixed old input pair with output fibers over the old image \(T(x,y)\). Taking the minimum of exact pair conservation on each such finite fiber yields precisely
\[
   g(ax+by)+g(cx+dy)=g(x)+g(y).
\]
Theorem A therefore implies that \(T\) is signed permutation. But F7 elementary A0 requires \(a,c\ne0\) in its first column. Contradiction.

Thus the **nonzero-period branch of the corrected F7 no-go proof is closed by a stand-alone exact proof**, independently of the inaccessible F4 historical report. \(\square\)

## Review boundary and exact provenance

This audit removes one specific external-proof dependency from the revised F7 period case. The other F7 case arguments (rank-two/rank-one hub, rank-one block determinant and the other finite-difference cases) remain statements of the original researcher until independently checked at the strength required for a full Native Review. The original standalone period-or-quadratic Lemma 3.3 remains **retracted**: the counterexample \(f(n,m)=n^2+|m|\) under the cross-slot new-coordinate swap remains valid and fails A0.

The auditor has shared control/review context and does not assert clean blind discovery, formal independent Native Review acceptance, Result admission, Task DONE, mother-objective closure or P000 promotion. The original research author and every original Result byte remain unchanged.

### Control-note

Original bounded-queue request `dvr-20261120-2327-needs-dispatch-v1` was read back `SUCCEEDED/error=null`, without replay. Native frozen Result artifact read `dvr-20261121-0012-f7-result-exact-artifact-v1` succeeded with exact Result hash; `dvr-20261121-0020-f7-review-current-flow-v1` verified no operational reviews. A proposed reference-pass write `dvr-20261121-0022-f7-rank-one-proof-crosscheck-p1-v1` was **rejected** with `CANONICAL_REJECTED: review intake requires actual immutable review evidence`. That rejected request must not be replayed under a changed identity or alternate write transport. This GitHub scientific note is separate from Native Review state.
