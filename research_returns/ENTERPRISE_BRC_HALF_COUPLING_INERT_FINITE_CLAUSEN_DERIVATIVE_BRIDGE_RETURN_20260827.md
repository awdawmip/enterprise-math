# Enterprise BRC Half-Coupling Inert Finite Clausen Derivative Bridge — Research Return

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-FINITE-CLAUSEN-DERIVATIVE-BRIDGE`  
Publication: `TP2-E0FCCE50CD7EE0FF0759`  
Claim: `chatgpt-ebp3-20260827-1104`  
Researcher-ID: `EM-EBP3-F870C3`  
Execution record: `ER-FBE23DC9E1C9D93DAD49`

## Frozen verdict

`PROOF_NOT_CLOSED`

Hard target `INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_PROVED_REFUTED_OR_EXACTLY_OBSTRUCTED` is not fully closed. No inert counterexample was found. The exact all-inert congruence remains unproved here.

This execution does, however, close the finite-truncation bookkeeping substantially and proves a sharp **2+2 inert-class split** that was not present in the parent return:

- for `p ≡ 13,19 (mod 24)` (`p=6m+1`, target sign `+p`), the derivative-weighted finite Clausen tail is automatically divisible by `p^2`, and modulo `p^3` collapses to one explicit reflected low×top triangle;
- for `p ≡ 17,23 (mod 24)` (`p=6m+5`, target sign `-p`), the finite Clausen tail contains a genuine valuation-zero triangle. Hence no proof based only on termwise tail valuation can work in these two classes; nontrivial cancellation is load-bearing.

The smallest remaining bridge is therefore class-dependent, not one uniform “inert tail” lemma.

## 1. Exact finite Clausen identity

Put

\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}\,2^{-k},
\qquad
G_p=\sum_{k=0}^{p-1}B_k,
\qquad
H_p=\sum_{k=0}^{p-1}(12k+1)B_k.
\]

Let

\[
T_p=
\sum_{\substack{0\le i,j\le p-1\\ i+j\ge p}}
(1+6(i+j))B_iB_j.
\]

The formal Clausen identity is

\[
{}_2F_1(1/6,1/3;1;z)^2
=
{}_3F_2(1/3,1/2,2/3;1,1;z).
\]

For every degree `n<p`, truncating each `_2F_1` factor at `p-1` does not alter the coefficient of `z^n`. Therefore the only discrepancy between the square of the finite truncation and the `_3F_2` truncation occurs in convolution degrees `p,...,2p-2`. Applying `1+6\theta` and setting `z=1/2` gives the **exact rational identity**

\[
\boxed{S_p=G_pH_p-T_p.}
\tag{1}
\]

No infinite-series limit or p-adic approximation is used in (1).

This completely localizes the degree-at-least-`p` correction.

## 2. Exact p-adic valuation of the Clausen factor

From

\[
B_k=
\frac{\prod_{r=0}^{k-1}(6r+1)(3r+1)}
{36^k(k!)^2},
\qquad k<p,
\]

the denominator is a p-adic unit. The numerator gives an exact three-block theorem.

### 2.1 Case `p=6m+1`

The only p-multiples in the two numerator progressions before `k=p` occur at

\[
6m+1=p,\qquad 3(2m)+1=p.
\]

Hence

\[
v_p(B_k)=
\begin{cases}
0,&0\le k\le m,\\
1,&m+1\le k\le 2m,\\
2,&2m+1\le k\le p-1.
\end{cases}
\tag{2+}
\]

### 2.2 Case `p=6m+5`

Now the first p-multiples are

\[
3(4m+3)+1=2p,\qquad 6(5m+4)+1=5p.
\]

Hence

\[
v_p(B_k)=
\begin{cases}
0,&0\le k\le 4m+3,\\
1,&4m+4\le k\le 5m+4,\\
2,&5m+5\le k\le p-1.
\end{cases}
\tag{2-}
\]

This is the source of the 2+2 split.

## 3. `p ≡ 13,19 (mod 24)`: exact reflected-tail collapse

Assume `p=6m+1`. In the tail condition `i+j>=p`, the valuation-zero and valuation-one blocks cannot reach degree `p` when paired among themselves. Modulo `p^3`, all pairs involving valuation sums at least three vanish.

Consequently the only surviving tail terms are valuation `0×2` and `2×0`. More precisely, every surviving pair is uniquely

\[
1\le i\le m,\qquad j=p-r,\qquad 1\le r\le i,
\]

or its transpose. Therefore

\[
\boxed{
T_p\equiv
2\sum_{i=1}^{m}\sum_{r=1}^{i}
(1+6(i-r))B_iB_{p-r}
\pmod{p^3}.
}
\tag{3}
\]

In particular,

\[
\boxed{p^2\mid T_p.}
\tag{4}
\]

The top coefficient can be reflected explicitly. For `1<=r<=m`,

\[
\boxed{
\frac{B_{p-r}}{p^2}
\equiv
C_r:=
\frac{2^{r-1}(r-1)!^2}
{18(5/6)_r(2/3)_r}
\pmod p.
}
\tag{5}
\]

Proof of (5): use
\[
(1/6)_p/p\equiv-1/6,\qquad (1/3)_p/p\equiv-1/3\pmod p,
\]
which follow from Wilson after removing the unique p-factor in each progression; then
\[
(a)_{p-r}=(a)_p/(a+p-r)_r,\quad
(a+p-r)_r\equiv(-1)^r(1-a)_r\pmod p,
\]
\[
(p-r)!\equiv(-1)^r/(r-1)!\pmod p,
\qquad
2^{-(p-r)}\equiv2^{r-1}\pmod p.
\]
The signs cancel.

Combining (3) and (5), define

\[
R_p=
2\sum_{i=1}^{m}B_i
\sum_{r=1}^{i}(1+6(i-r))C_r
\pmod p.
\]

Then

\[
\boxed{T_p\equiv p^2R_p\pmod{p^3}.}
\tag{6}
\]

Thus for the two positive-sign inert classes `13,19 mod 24`, the original target is exactly reduced to

\[
\boxed{
G_pH_p\equiv p+p^2R_p\pmod{p^3}.
}
\tag{L+}
\]

This is strictly smaller than the parent finite-Clausen bridge: every degree-at-least-`p` term has been eliminated except one explicit one-dimensional reflected correction nested under the low block.

## 4. `p ≡ 17,23 (mod 24)`: exact valuation obstruction

Assume `p=6m+5` and split the indices according to (2-) into `I_0,I_1,I_2`.

Modulo `p^3`, the tail support is exactly

\[
I_0I_0,\quad
I_0I_1+I_1I_0,\quad
I_0I_2+I_2I_0,\quad
I_1I_1.
\tag{7}
\]

The blocks `I_1I_2+I_2I_1` and `I_2I_2` vanish termwise modulo `p^3`.

Crucially, `I_0I_0` intersects `i+j>=p`. Hence the tail contains terms that are individually p-adic units. This yields an exact no-go:

> **Finite-Clausen valuation-only no-go.** For `p ≡ 17,23 (mod 24)`, no argument that tries to discard the degree-at-least-`p` finite Clausen correction purely from termwise p-adic order can establish the target modulo `p^3`.

Any successful proof in these classes must prove cancellation inside the unit/valuation-one tail.

The checker exhibits a stronger bounded pattern: for every tested inert `p=6m+5<=250`, the aggregate `I_0I_0` and two-sided `I_0I_1` blocks are each divisible by `p`, while the two-sided `I_0I_2` and `I_1I_1` blocks are divisible by `p^2`. This is **regression only**, not promoted to an all-prime theorem.

For example:

- `p=17`: `T00=3009=17*177`, `T01(two-sided)=1241=17*73`, `T02(two-sided)=867=17^2*3`, and `T_p=204=17*12 (mod 17^3)`;
- `p=23`: `T00=6371=23*277`, `T01(two-sided)=6141=23*267`, `T02(two-sided)=2645=23^2*5`, `T11=1587=23^2*3`, and `T_p=4577=23*199 (mod 23^3)`.

The smallest unresolved negative-sign lemma is therefore a **block-cancellation theorem** upgrading (7), not a valuation theorem.

## 5. Original `A_n` middle blocks remain load-bearing

The parent result proved

\[
v_p\!\left(\binom{2n}{n}^2\binom{3n}{n}\right)
=
\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{3n}{p}\right\rfloor,
\quad 0\le n<p.
\]

Thus the original `_3F_2` summand has valuation-one and valuation-two middle blocks on

\[
p/3<n<p/2,\qquad p/2<n<2p/3.
\]

Nothing in the present Clausen reduction discards them. Identity (1) instead repackages their interaction into `G_pH_p-T_p`. The new result is therefore compatible with, and sharper than, the parent bookkeeping rather than a replacement for it.

## 6. Second proof lane: p-adic transformation / WZ audit

A second, structurally distinct lane was tested.

### 6.1 p-adic hypergeometric transformations

Mao–Pan, *p-adic analogues of hypergeometric identities* (arXiv:1703.01215), prove polynomial truncated analogues of classical quadratic/Clausen transformations modulo `p^2` and develop the corresponding p-adic Gamma first-order deformation machinery.

That precision is not enough to close the present derivative-weighted target:

- the target is modulo `p^3`;
- the operator `1+6\theta` forces control of a derivative-weighted finite correction;
- in the `p=6m+5` classes, the tail begins at valuation zero and its cancellation is not supplied by a mod-`p^2` unweighted Clausen congruence.

No Gamma evaluation from that source is therefore imported as a proof of the target. In particular, the target character
\[
(p/3)=
\begin{cases}
+1,&p\equiv13,19\pmod{24},\\
-1,&p\equiv17,23\pmod{24}
\end{cases}
\]
is never inserted into a transformation whose purpose is to produce it.

The 2026 Shvets mixed-CM theorem is also not the target: it concerns coefficients of a cubic power of the same `(1/6,1/3;1)` backbone, with a split-prime theorem and an inert Cartier obstruction. It supports the existence of a genuine Frobenius-class split but does not evaluate `S_p`.

### 6.2 Direct Gosper/WZ subroute

The weighted summand
\[
t_n=(6n+1)
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}2^{-n}
\]
is hypergeometric. A complete Gosper test for a one-dimensional hypergeometric antidifference returns no certificate. Equivalently, no direct hypergeometric `U_n` of the Gosper class was found with `U_{n+1}-U_n=t_n`.

This rejects only the **naive one-term telescoper** route. It does not rule out a p-deformed terminating identity with an auxiliary parameter or a higher-dimensional WZ pair, so it is not used as a theorem-level no-go for the hard target.

## 7. Deterministic checker

Retained checker:

`scripts/check_enterprise_brc_half_coupling_inert_finite_clausen_derivative_bridge.py`

Frozen regression:

- all `616` inert primes `5<=p<=9973`: target congruence passes;
- all `25` inert primes `p<=250`: exact finite Clausen identity (1), the `B_k` valuation blocks, class-specific support decomposition, and vanishing high blocks pass;
- for every tested `p=6m+1`, the reflected formula (5) and reduced-tail formula (6) pass;
- failures: `0`.

Artifact:

`research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE/regression_10000.json`

Status: `FINITE_REGRESSION_ONLY_NOT_A_PROOF`.

## 8. Dependency map

### Formal algebra, proved here

- exact finite identity `S_p=G_pH_p-T_p`;
- exact valuation blocks (2+) and (2-);
- exact `p=6m+1` support collapse (3)-(4);
- exact reflected coefficient congruence (5);
- exact reduced tail (6);
- exact `p=6m+5` support decomposition (7);
- valuation-only no-go for `17,23 mod 24`.

### Imported arithmetic

- Wilson's theorem and Fermat's little theorem in the proof of (5);
- the parent `A_n` valuation theorem;
- Mao–Pan's mod-`p^2` p-adic transformation framework, used only to audit attainable precision;
- Shvets 2026, used only as related structural literature, not as a proof of this sequence.

### Not proved / not assumed

- the target itself for any infinite inert residue class;
- the bounded `p=6m+5` aggregate block-divisibility pattern;
- a p-adic Gamma formula producing the target sign at derivative precision;
- any p-deformed higher-dimensional WZ identity.

## 9. Smallest unresolved lemmas

The former single inert bridge should be split mathematically into two typed lemmas.

### Positive-sign inert half: `p ≡ 13,19 (mod 24)`

Prove `(L+)`:

\[
G_pH_p\equiv p+p^2R_p\pmod{p^3},
\]

with the now-explicit `R_p`. The high-degree finite convolution is no longer an independent unknown.

### Negative-sign inert half: `p ≡ 17,23 (mod 24)`

Prove an exact cancellation law for the four surviving blocks in (7), beginning with the experimentally stable divisibilities

\[
p\mid T_{00},\quad p\mid T_{01}^{\mathrm{two-sided}},
\quad
p^2\mid T_{02}^{\mathrm{two-sided}},\quad p^2\mid T_{11},
\]

and then identify the first two p-adic digits needed in

\[
G_pH_p-T_p\equiv -p\pmod{p^3}.
\]

The divisibility display is a **candidate lemma**, not a frozen theorem.

## 10. Control-plane recommendation

Research execution stops at `PROOF_NOT_CLOSED` with a strictly smaller, class-split frontier.

Recommended Driver disposition: `FOLLOWUP_TASK` or `SPLIT_TO_TYPED_TASKS`:

1. `INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE` for `p ≡ 13,19 mod 24`;
2. `INERT_MINUS_UNIT_TAIL_BLOCK_CANCELLATION_BRIDGE` for `p ≡ 17,23 mod 24`.

Do not reissue the former undifferentiated inert finite-Clausen task unchanged. The present exact support theorem shows that the two halves require different proof mechanisms.

Research state after result freeze: `AWAITING_DRIVER_REVIEW`. The researcher does not self-issue `DONE`.
