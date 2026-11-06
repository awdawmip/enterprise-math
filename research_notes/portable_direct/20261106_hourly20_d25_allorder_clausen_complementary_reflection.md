# D25 — All-order Clausen defect and complementary-index finite-field identity

Date: 2026-11-06. Lane: TASK_RESEARCH, author-side portable science. Status: **AUTHOR-PROVED EXACT ALGEBRA / 81-PRIME FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.

Mother Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; original frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. The preceding four-shell theorem and second/third-jet Clausen corrections are reused without recrediting.

## Theorem 1. Universal all-order defect generator

Let (j\ge0). Work initially over (\mathbb Q[[t]]). For any integers (a,b,c\) define the D25 signed coefficient jets

\[
M_j(t)=(-1/2)^j\frac{j!}{(1-3t)_j}\prod_{s\in\{a,b,c\}}\binom{s+t}{j},
\quad
C_j(t)=(-1/2)^j\frac{\prod_{s\in\{a,b,c\}}\prod_{r=0}^{j-1}(s+t-r)}
{j!(1-t)_j(1-2t)_j}.
\]

The ratio is a universal unit independent of (a,b,c), even when their numerator vanishes at (t=0):

\[
\boxed{ M_j(t)=R_j(t)C_j(t),\quad
R_j(t)=\prod_{h=1}^{j}\frac{(h-t)(h-2t)}{h(h-3t)}.}
\]

Put (H_j^{(n)}=\sum_{h=1}^j h^{-n}) (and (H_0^{(n)}=0)). Then

\[
\boxed{\log R_j(t)=\sum_{n=2}^{\infty}
\frac{3^n-1-2^n}{n}H_j^{(n)}t^n.}
\]

Writing (R_j(t)=\sum_{n\ge0}E_{j,n}t^n), (E_{j,0}=1), (E_{j,1}=0), there is a universal triangular recurrence

\[
\boxed{n E_{j,n}=\sum_{k=2}^{n}(3^k-1-2^k)H_j^{(k)}E_{j,n-k}.}
\]

In particular

\[
E_{j,2}=2H_j^{(2)},\qquad E_{j,3}=6H_j^{(3)},\qquad
E_{j,4}=16H_j^{(4)}+2(H_j^{(2)})^2.
\]

Therefore the **new fourth-jet defect** is exactly

\[
\boxed{[t^4](M_j-C_j)=
2H_j^{(2)}[t^2]C_j+
6H_j^{(3)}[t]C_j+
\big(16H_j^{(4)}+2(H_j^{(2)})^2\big)C_j(0).}
\]

The identity and recurrence also hold over (\mathbb F_p) through all degrees (n<p), provided (p\ge5), (j<p). They do not assert a division by (p) in characteristic (p).

**Proof.** The displayed ratio follows by cancelling the common numerator, without ever dividing by that numerator. For each (h),
(log((1-t/h)(1-2t/h)/(1-3t/h))=\sum_{n\ge1}(3^n-1-2^n)t^n/(nh^n)).
The (n=1) coefficient is zero. Sum over (h) and differentiate (R=\exp(\log R)), giving the recurrence and fourth coefficient. Reduction modulo (p) is valid in orders below (p), since every (h\le j<p) and (n<p) is a unit.

## Theorem 2. Exact complementary-index reflection

For **every prime (p\ge5)** and every (0\le j<p), as rational functions over (\mathbb F_p(t)),

\[
\boxed{R_j(t)R_{p-1-j}(-t)=1-t^{p-1}.}
\]

The identity is exact, not an asymptotic congruence or finite computation. Consequently every Taylor coefficient below degree (p-1) of the complementary product vanishes, while the first possible residual is the canonical (-t^{p-1}). This supplies a source-respecting involution (j\leftrightarrow p-1-j, t\leftrightarrow-t) on the universal Clausen defect.

**Proof.** Reindex (h\in\{j+1,\dots,p-1\}) by (h=-k\pmod p), (1\le k\le p-1-j), to identify the missing factors of (R_j(t)) with those of (R_{p-1-j}(-t)). Thus the product equals (R_{p-1}(t)). In (\mathbb F_p[t]), for (u\in\{1,2,3\}),
(prod_{h=1}^{p-1}(h-ut)=(ut)^{p-1}-1=t^{p-1}-1), whereas
(prod_{h=1}^{p-1}h=-1). Substitution gives
(R_{p-1}(t)=(t^{p-1}-1)^2/[-(t^{p-1}-1)]=1-t^{p-1}).

As a harmonic-number corollary, for (2\le n<p-1),
\[
H_{p-1-j}^{(n)}=(-1)^{n+1}H_j^{(n)}\pmod p;
\]
the critical degree (p-1) must be retained as the explicit nonzero residual, not discarded.

## D25/BRC application and exact scope

In the frozen target class (p\equiv13,19\pmod{24}), (p=6m+1) and the weighted (1+6z\partial_z) observer erases exactly the source coordinate (j_*=m) modulo (p). The new reflection pairs the defect of that coordinate with the complementary index (p-1-m), but **does not itself prove weighted-sum cancellation, \\(\Theta_p=0\\), or the native LIFT**. Preserve the individual signed four-shell jets and the missing coordinate before scalar aggregation; the paired (R)-identity may now be used as a candidate factor in a source-preserving finite telescope.

For examples (p=13,19,373), the exceptional ((j_*,M_{j_*}(0),H_{j_*}^{(2)},[t^2](M_{j_*}-C_{j_*}))) modulo (p) is respectively
((2,6,11,2)), ((3,8,4,7)), ((62,122,124,43)).
Their labelled unweighted residuals need not vanish merely because the scalar weight is (p).

## Independent exact finite-field checks

A Python exact finite-field verifier uses **two independent coefficient recurrences** for (M_j,C_j), and a third recurrence for the complementary (R) jets. It checked all (0\le j<p) for the **81 distinct primes (5\le p\le421) together with (p=1009)** (all 80 primes from 5 through 421 plus 1009), through degree (t^4), including the (p=5) exceptional boundary. Result **81/81 PASS**; mathematical validity for all primes follows from the two algebraic proofs, not from this finite check.

## Next precise scientific action

Construct a paired, source-labelled candidate telescope for the original (\Theta_p=W_p/p-Z+S/6) using (j\leftrightarrow p-1-j), and test at (p=13,19,373) without assuming source weights or Gauss branches match after reflection. Reject pairings that do not respect the four-shell/support and (j_*) repair. If no such telescope exists, localize its exact residual and return to native (H0/B0, [X]U\bmod p^2,\eta,\kappa) obligations. Frozen mother objective remains \\(\Delta_p-R_p\equiv0\pmod p\\), (p\equiv13,19\pmod{24}).

This is **portable author-side evidence only**: no new service-issued Researcher identity, CLAIM, authorized run, native Source checkpoint, Result or review is claimed.
