# R749SUG — Divisor-layer anatomy of the maximal-Port unimodular feedback boundary

Date: 2026-11-18 (Asia/Shanghai); evidence status: AUTHOR_EXACT_NOT_REVIEWED.
Direct continuation of R749SUF (same Draft PR) and R749SUE. Freeze: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`, WBRC-T30–T32, positive-rational two labeled Port feedback. This paper concerns its integer-grid observation signature, not an admitted triadic X6 event.

## Exact boundary question
Let \(\mathcal U_M\) be all ordered 2×2 positive integer matrices \((a,u;v,d)\) with entries 1..M and \(ad-uv=1\). R749SUF proved that their thresholds \(\tau=\max(u,v)ad\) determine the entire late deficit \(D_M(K)\) when \(K>M,\ 2K>M^3\).

We now classify **every** such matrix whose largest off-diagonal Port-bin equals M, i.e. \(\max(u,v)=M\), by integer divisors of numbers congruent to 1 modulo M.

## Theorem 1 — Exact maximal-Port divisor layers

For integer M>=2, take matrices with u=M. Then automatically a,d<=M-1 and 1<=v<=M-1. Put r=M-a and s=M-d. All solutions arise **uniquely** from
\[
0\le q\le M-2,\qquad rs=qM+1,\qquad
1\le r,s\le M-1,\qquad
v=M-r-s+q\ge1.
\]
The associated tuple is
\[
(a,u,v,d)=(M-r,\ M,\ M-r-s+q,\ M-s),
\]
and its exact threshold is
\[
\boxed{\tau=M(M-r)(M-s).}
\]
Every qualifying ordered divisor pair (r,s) gives two labeled matrices at that threshold, the second by exchanging u and v; u=v=M cannot occur. In particular, for every integer threshold T, the boundary contribution to the histogram is exactly
\[
\boxed{
g_M^{\partial}(T)=
2\sum_{q=0}^{M-2}\ \
\sum_{\substack{r\mid(qM+1),\ s=(qM+1)/r\\
1\le r,s\le M-1,\ M-r-s+q\ge1}}
\mathbf1\{T=M(M-r)(M-s)\}.
}
\]
This counts the full **labeled maximal-Port** subpopulation, not all unimodular matrices. It refines the global R749SUF parity invariant by locating exact modular/divisor sources of even jumps.

**Proof.** u=M and det=1 give \(ad=Mv+1\). If a or d equals M, its product is divisible by M, contradiction; thus r,s>=1. Expanding \(ad=(M-r)(M-s)\) yields
\[
rs-1=M(v-M+r+s).
\]
Set q=(rs-1)/M. As rs lies between 1 and \((M-1)^2\), q is integral with 0<=q<=M-2. Then v=M-r-s+q. Conversely these conditions give ad-Mv=1. Bounds imply \(v=(ad-1)/M<M\); the lower bound is precisely the displayed v>=1 condition. Uniqueness is immediate from r=M-a, s=M-d, q=(rs-1)/M. Swapping u and v creates a distinct labeled matrix since v<M, and every matrix with max(u,v)=M occurs in exactly one such pair. QED.

## Corollary — The first two arithmetic layers

For q=0, rs=1 forces r=s=1, so \(v=M-2\) and \(\tau=M(M-1)^2\) for M>=3; exactly two labeled edge tuples occur at the saturation threshold. This rederives, but does not claim novelty over, the R749SUE terminal two-class step.

For q=1, one has rs=M+1, with a concrete family indexed by every admissible ordered factorization of M+1:
\[
u=M,\quad v=M-r-s+1,\quad a=M-r,\quad d=M-s,\quad
\tau=M(M-r)(M-s).
\]
Hence arithmetic factorization of M+1 determines an explicit, sometimes large, high-resolution boundary sub-spectrum.

## Theorem 2 — Infinite family outside the adjacent diagonal ladder

For each integer t>=4, choose
\[
M=t^2-1,\quad a=d=M-t,\quad u=M,\quad v=t(t-2).
\]
Then all entries are in [1,M], and \(ad-uv=1\). Its threshold is
\[
\boxed{\tau_t=M(M-t)^2},
\quad 2\tau_t>M^3,
\]
so this is a **genuine late-regime missing-signature breakpoint** for the relevant K. It strictly exceeds the adjacent-diagonal canonical threshold at the same k=M-t, namely \((k+1)k^2\), by
\[
\boxed{(t-1)(M-t)^2>0}.
\]

**Proof.** \(ad-uv=(M-t)^2-M(M-2t+1)=t^2-M=1\), and v=t(t-2) is positive and strictly below M. The condition \(2\tau_t>M^3\) reduces to \(2(M-t)^2>M^2\). Since t/(t²-1) decreases for t>=2 and at t=4 equals 4/15<1-1/sqrt(2), the latter inequality holds for t>=4. The threshold difference is the displayed algebraic identity. QED.

This infinite family proves that the single neighbor-bin choice u=k+1,v=k-1 at fixed a=d=k is **not exhaustive** even in the late regime. It does not prove that \(\tau_t\) differs from every other neighbor threshold at a different k, nor establish which matrix produces the globally second-largest breakpoint; those remain separate classification questions.

## Concrete exact witness

At M=20, the q=1 factor pair (r,s)=(3,7), rs=21=M+1, gives
\[
(a,u,v,d)=(17,20,11,13),\quad ad-uv=221-220=1,
\quad\tau=20\cdot17\cdot13=4420.
\]
The canonical nearest-neighbor threshold sequence begins 7220, 6156, 5202, 4352, ... . Thus 4420 is a noncanonical **intrusion between the third and fourth thresholds**. The two orders of r,s and two choices for which off-diagonal entry is M give four labeled tuples at this threshold.

At M=15 (t=4), \(a=d=11,\ u=15,\ v=8,\ \tau=1815\); the adjacent k=11 threshold is \(12\cdot121=1452\). Here \(2\cdot1815>15^3\), so this is already in the late-regime range.

## Validation and boundaries

The accompanying dependency-free JavaScript integer certificate independently compares the divisor-layer histogram against direct enumeration over a,d (solving v=(ad-1)/M) for each M=2..128. It tests the t²-1 infinite-family algebraic identities and strict late-boundary inequality for t=4..100. No floating-point tolerance or random sampling is involved; numerical values stay below the JS exact-integer bound in this finite test.

Theorem 1 and Theorem 2 hold for all integer parameters in their stated domains by the proofs; code is a regression/exact finite check, not independent review. No claim is made about the full X6 native triadic event or preservation of signed provenance through a BRC Port collapse.

Next: classify the *global* upper-tail intrusion order by comparing all divisor q-layers with the interior Farey-tree branches. Construct a rigorous upper envelope for the first few threshold ranks or a counterexample to a proposed uniform envelope, preserving port labels.
