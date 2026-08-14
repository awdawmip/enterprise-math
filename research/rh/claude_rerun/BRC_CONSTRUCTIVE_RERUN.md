# BRC_CONSTRUCTIVE_RERUN — RH constructive rerun with Branch-Recoalescence Collapse

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Driver: `EM-DVR-7Q4K2C`  
Phase: `CONSTRUCTIVE_RERUN_AFTER_FORENSICS`

## 0. Scope correction

The goal of this phase is not to stop at the first fatal error in an external RH proof. The external proof objects are now raw material. We reroute their load-bearing obligations through Enterprise Math tools, especially R021 Branch-Recoalescence Collapse (BRC), R015 result-support branch deferral, P023 future-signature quotients, P018 precision carriers, P021 correlation/witness retention, and R014 representation-resource accounting.

The main question is:

> can an invalid global deterministic compression be replaced by exact branch-preserving/on-demand refinement, yielding a correct weaker theorem, a new proof architecture, or a sharper irreducible RH core?

Status at this checkpoint:

`BRC_CONSTRUCTIVE_RERUN_ACTIVE / RECTANGULAR_DUALITY_REPAIR_FOUND / EVENTUAL_VERTICAL_POSITIVITY_DERIVED / RH_NOT_CLOSED`

No novelty claim is made for Jacobi–Trudi, residue asymptotics, Dodgson condensation, or standard PF theory. The research value here is their BRC typing and the repaired RH proof routing.

---

## 1. Why Candidate B is the natural BRC target

Candidate A (bounded square-difference spectral operator) is blocked by an asymptotic counting invariant. BRC cannot repair a pointwise target after the complete runtime encoding has already erased an invariant required by the target; this is exactly the R021 `NO_RESURRECTION` boundary.

Candidate C (spectral determinant) contains a circular divisor identification. BRC can preserve unresolved divisor branches, but cannot declare them real without a new bridge.

Candidate B / the Xi coefficient–Toeplitz–PF route has a different shape:

```text
many finite positivity obligations
        ↓
all Toeplitz minors nonnegative
        ↓
PF_infinity
        ↓
Laguerre–Pólya / all Xi zeros real
        ↓
RH
```

The failed external proof attempted to compress infinitely many future obligations into a single spectral-gap formula for the *original* Taylor coefficients. That compression is false. BRC suggests not collapsing those obligations prematurely.

---

## 2. Exact proof-obligation lattice

Normalize the positive Xi coefficient generating function by

\[
A(z)=\sum_{n\ge 0} a_n z^n,\qquad a_0=1,
\]

and define the consecutive Toeplitz minors

\[
D_{r,k}(a)=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\qquad a_n=0\quad(n<0).
\]

The RH/PF route becomes a two-dimensional proof-obligation lattice

\[
\Omega=\{(r,k):r\ge1,\ k\ge0\}.
\]

Each cell asks for the result-support observable

```text
SIGN_SUPPORT(D_{r,k}) ∈ {POSITIVE, ZERO, NEGATIVE, UNKNOWN}.
```

A global proof no longer needs one narrative lemma. It needs a certified cover of `Omega` by regions whose final support excludes `NEGATIVE`.

This is a BRC-compatible target because obligations can be split into disjoint/overlapping regions, certified independently, and unioned without changing the final set of unresolved or negative obligations.

Important typing boundary:

- once a branch is terminal and only its final sign matters, it may coalesce to a sign token;
- if it will still participate in Dodgson/ratio propagation, sign-only coalescence is unsafe because future operations need magnitudes/correlations.

That is R021 `NO_RESURRECTION` plus P021 correlation retention applied to determinant certificates.

---

## 3. Current safe BRC regions

### 3.1 Boundary branch

For `k=0`, the Toeplitz matrix is triangular with diagonal `a_0=1`, hence

\[
D_{r,0}=1
\]

for every `r`.

Certificate: `EXACT_ALGEBRA`.

### 3.2 Low-order branch from zero verification + Schoenberg sector control

The current external coefficient literature records that verified critical-line zeros through height `H = 3,000,175,332,800`, combined with Schoenberg's sector theorem, certify PF order up to approximately `pi H`; therefore all Toeplitz minors of order up to that bound are nonnegative.

Certificate type: `EXTERNAL_STANDARD_THEOREM + VERIFIED_ZERO_PREFIX`.

BRC use: the entire horizontal strip may coalesce to `NONNEGATIVE` because no later operation needs individual determinant values after the certificate is terminal.

### 3.3 Uniform cubic tail branch

A 2026 external theorem proves the strict consecutive-minor wedge

\[
D_{r,k}>0
\qquad
(k\ge 10^{18}r^3).
\]

Certificate type: `EXTERNAL_UNIFORM_ANALYTIC_CERTIFICATE`.

This is exactly a BRC safe-recoalescence region: infinitely many `(r,k)` obligations are replaced by one region token with the same remaining suffix result-support `{POSITIVE}`.

After 3.1–3.3, the unresolved set is confined to an infinite central/low-shift region rather than the full quadrant.

---

## 4. Repair of the false spectral-gap lemma: rectangular Toeplitz duality

The previous adversarial rerun showed that the external Lemma 10 incorrectly placed a fixed-base exponential expansion on the original Taylor coefficients `a_n` of an entire function. Cauchy–Hadamard forbids such a nonzero exponential leading term.

The correct location for a pole/residue exponential expansion is the reciprocal generating function.

Define

\[
E(z)=\frac{1}{A(-z)}=\sum_{n\ge0}e_nz^n.
\]

### Theorem 4.1 — rectangular Jacobi–Trudi duality

For all `r,k >= 1`,

\[
\boxed{
D_{r,k}(a)
=
\det[e_{r+j-i}]_{i,j=0}^{k-1}.
}
\]

Equivalently,

\[
\boxed{D_{r,k}(a)=D_{k,r}(e).}
\]

#### Proof

Treat `a_n` as the complete homogeneous specialization `h_n` determined by

\[
H(z)=\sum h_nz^n=A(z),
\]

and define elementary coefficients by

\[
\sum e_nz^n=1/H(-z).
\]

The matrix `[h_{k+j-i}]` is the Jacobi–Trudi matrix for the rectangular partition

\[
\lambda=(k^r).
\]

Hence its determinant is `s_lambda`. The conjugate partition is

\[
\lambda'=(r^k),
\]

and the dual Jacobi–Trudi identity gives

\[
s_\lambda=\det[e_{r+j-i}]_{i,j=0}^{k-1}.
\]

This proves the identity. `QED`.

### Consequence

An `r x r` determinant at small shift `k` can be retyped as a `k x k` determinant at large reciprocal index `r` without loss of information.

This is an exact deterministic equivalence, not a heuristic collapse.

R014 consequence: evaluation/formalization dimension can be reduced from `r` to `k` in the regime `k << r`, with the cost of generating reciprocal coefficients `e_n`. No semantic information is hidden in a free token.

---

## 5. Correct spectral expansion on the reciprocal side

Let `A` be real entire with `A(0)=1`, and write `E(z)=1/A(-z)`.

Assume the first `k` poles of `E` in increasing modulus are distinct simple positive reals

\[
0<t_1<t_2<\cdots<t_k<R,
\]

with no other pole in `|z|<R`.

Choose any contour radius `R_*` with

\[
t_k<R_*<R.
\]

By residues/Cauchy coefficient extraction,

\[
e_n
=
\sum_{m=1}^k c_m t_m^{-n}
+O(R_*^{-n}),
\]

where

\[
c_m=\frac{1}{t_mA'(-t_m)}.
\]

Because `A(-t)` is real, begins positive at `t=0`, and crosses the first `k` simple real zeros in order,

\[
\operatorname{sgn}(c_m)=(-1)^{m-1}.
\]

This is the correct version of the spectral-gap/exponential mechanism: it belongs to the reciprocal coefficients `e_n`, not the entire coefficients `a_n`.

---

## 6. New surviving theorem — finite real-pole prefix gives an infinite vertical positivity ray

### Theorem 6.1

Under the assumptions of Section 5, for this fixed `k` there exists `R_k` such that

\[
\boxed{
D_{r,k}(a)>0
\qquad\text{for every }r\ge R_k.
}
\]

Thus finitely many certified real poles plus one separating contour close infinitely many Toeplitz obligations in the vertical `r` direction.

### Proof

Put

\[
x_m=t_m^{-1},
\qquad
x_1>x_2>\cdots>x_k>R_*^{-1}.
\]

By Theorem 4.1,

\[
D_{r,k}(a)=\det[e_{r+j-i}]_{i,j=0}^{k-1}.
\]

Ignore the exponentially smaller `O(R_*^{-n})` remainder first. The `k`-pole leading matrix factors as

\[
M^{(0)}_{ij}
=
\sum_{m=1}^k c_m x_m^{r+j-i}
=
U\,\operatorname{diag}(c_mx_m^r)\,V^T,
\]

where

\[
U_{im}=x_m^{-i},
\qquad
V_{jm}=x_m^j.
\]

Therefore

\[
\det M^{(0)}
=
\left(\prod_{m=1}^kc_mx_m^r\right)
\det[x_m^{-i}]
\det[x_m^j].
\]

For the descending positive sequence `x_1>...>x_k`,

\[
\operatorname{sgn}\det[x_m^j]
=(-1)^{k(k-1)/2},
\]

while

\[
\det[x_m^{-i}]>0.
\]

Also

\[
\operatorname{sgn}\prod_{m=1}^kc_m
=(-1)^{0+1+\cdots+(k-1)}
=(-1)^{k(k-1)/2}.
\]

The signs cancel, so

\[
\det M^{(0)}>0.
\]

Every determinant term containing at least one remainder column/row carries an extra exponential factor bounded by a fixed multiple of

\[
(R_*^{-1}/x_k)^r
=(t_k/R_*)^r
\to0.
\]

Hence the full determinant has the same positive sign as `M^(0)` for all sufficiently large `r`. `QED`.

### Status

`PROVED_CLASSICALLY_IN_THIS_RERUN / PRIOR_ART_NOVELTY_UNCHECKED`.

This is not RH. It is a reusable weaker theorem and a direct constructive repair of the failed spectral-gap placement.

---

## 7. Xi corollary and what it actually buys

For the normalized Xi coefficient function

\[
A(z)=G(z)/G(0),
\]

critical-line zeros of Xi correspond to negative real zeros of `A`, hence positive real poles of `E(z)=1/A(-z)`.

Therefore:

> any finite prefix of Xi zeros that is rigorously certified to be simple, critical-line, and separated in modulus yields — after an effective contour/residue bound — eventual positivity of `D_{r,k}` in the entire vertical ray for each fixed `k` covered by that prefix.

This converts finite spectral information into an infinite proof region.

BRC interpretation:

```text
branch: fixed shift k
    ↓ verify first k reciprocal poles + contour gap
certificate token
    ↓
all sufficiently large r recoalesce to POSITIVE
```

This is precisely the kind of sparse-reachability / low-reuse regime in which R021 says branching/on-demand refinement can beat a global deterministic table.

It still does not cover arbitrary `k`, so RH remains open.

---

## 8. Exact local future dynamics: Dodgson condensation

Define `D_{0,k}=1`. Desnanot–Jacobi gives

\[
\boxed{
D_{r,k}D_{r-2,k}
=
D_{r-1,k}^2-D_{r-1,k-1}D_{r-1,k+1}.
}
\]

Whenever the relevant lower minors are positive, define

\[
q_{r,k}
=
\frac{D_{r,k-1}D_{r,k+1}}{D_{r,k}^2}.
\]

Then

\[
D_{r+1,k}
=
\frac{D_{r,k}^2}{D_{r-1,k}}
(1-q_{r,k}),
\]

so the next-order positivity obligation is exactly

\[
q_{r,k}<1.
\]

A direct substitution yields the local ratio dynamics

\[
\boxed{
q_{r+1,k}
=
\frac{q_{r,k}^2}{q_{r-1,k}}
\frac{(1-q_{r,k-1})(1-q_{r,k+1})}{(1-q_{r,k})^2}.
}
\]

This is the exact local state transition that the external proof was trying to control by a global unitarity estimate.

### BRC consequence

The state at `(r,k)` is not merely `sign(D_{r,k})`. A future Dodgson step needs the correlated tuple

```text
(q_{r-1,k}, q_{r,k-1}, q_{r,k}, q_{r,k+1})
```

or an exact interval/certificate object from which it can be recovered.

Therefore:

- terminal positive branches may coalesce;
- active propagation branches may coalesce only when their remaining ratio/future signatures coincide;
- current-sign-only coalescence is invalid by R021 `NO_RESURRECTION`.

This identifies the correct carrier for the repaired route.

---

## 9. Finite propagation / on-demand refinement

`D_{r,k}` only reads the finite coefficient window

\[
a_{k-r+1},\ldots,a_{k+r-1}
\]

(with negative indices interpreted as zero).

So every fixed proof obligation has a finite information light cone.

This matters operationally:

- no global Xi coefficient table is needed to verify a single branch;
- BRC may generate/refine only coefficient cells reachable from the currently unresolved `(r,k)` region;
- once a region is certified by a uniform theorem, its interior coefficient data need never be materialized;
- R014 should charge coefficient-window generation, interval precision, active branch count, and ratio correlation data, not the size of an imaginary global exact table.

---

## 10. Proof-by-region-cover compiler

A sound BRC proof compiler can use the following branch types.

### `K0_EXACT`
Predicate: `k=0`.  
Certificate: `D_{r,0}=1`.  
Final support: `{POSITIVE}`.

### `LOW_ORDER_SECTOR`
Predicate: `r <= R_verified`.  
Certificate: zero verification + Schoenberg sector theorem.  
Final support: `{NONNEGATIVE}`.

### `CUBIC_TAIL`
Predicate: `k >= C r^3`, currently `C=10^18` from external theorem.  
Certificate: uniform saddle/q-Pascal/Banach-algebra theorem.  
Final support: `{POSITIVE}`.

### `DUAL_VERTICAL_k`
Predicate: fixed certified `k`, `r >= R_k`.  
Transition: exact duality `D_{r,k}(a) -> D_{k,r}(e)`.  
Certificate: first `k` reciprocal poles real/simple/separated + residue remainder bound.  
Final support: `{POSITIVE}`.

### `DODGSON_ACTIVE`
Predicate: not terminal.  
Payload: interval/exact ratio stencil and provenance.  
Transition: split/refine by the local `q` recurrence.  
Recoalescence: only on equality of remaining future certificate signature.

### `CRITICAL_UNRESOLVED`
The remaining branch family. This is the actual RH core after current certificates are removed.

---

## 11. Shape of the remaining RH core

Using only the boundary, low-order strip and cubic tail, an RH counterexample minor must lie in a region of the form

\[
r>R_{\mathrm{verified}},
\qquad
1\le k<10^{18}r^3.
\]

Adding the vertical theorem for every certified shift `k <= K` changes the unresolved set to

\[
\mathcal U(K)
\subseteq
\{r>R_{\mathrm{verified}},\ k>K,\ k<10^{18}r^3\}
\cup
\bigcup_{1\le k\le K}\{R_{\mathrm{verified}}<r<R_k\}.
\]

The second term is finite for each finite `K`.

This is a concrete BRC gain:

> a finite verified spectral prefix can delete infinitely many future Toeplitz obligations without pretending to know the unverified zero set.

---

## 12. The next four constructive targets

### Target T1 — clustered reciprocal-pole BRC

Theorem 6.1 assumes individually simple/separated poles. Close zero pairs make pointwise pole separation expensive. Replace individual poles by contour clusters and preserve the cluster's full finite-rank residue subspace as branch metadata.

Goal:

```text
point-pole splitting
→ cluster branch
→ exact determinant subspace
→ split only if future sign needs internal resolution
```

This is a direct application of BRC safe deferred refinement.

### Target T2 — uniform vertical threshold

Derive an explicit `R_k` bound, preferably uniform over large ranges of `k`, from zero-free/sector information plus cluster separation rather than individual-zero spacing.

A useful result need not prove RH; even a polynomial/exponential vertical wedge would shrink the critical region sharply.

### Target T3 — critical-regime comparison carrier

The cubic tail theorem collapses `log a_{k+s}` to a quadratic local model and pays a remainder of scale roughly `r^3/k`. When that collapse becomes unsafe, BRC says retain the missing local jet/shape information instead of discarding it.

Research a hierarchy:

```text
quadratic q-Pascal carrier
→ cubic/relative-window carrier
→ saddle-profile carrier
```

and ask whether an exact/positive comparison model survives down toward `k ~ r`.

### Target T4 — Dodgson first-failure back-propagation

Assume a first negative minor exists. Then at the previous order there is a local log-concavity failure

\[
q_{r-1,k}\ge1.
\]

Use the exact local `q` dynamics to branch backwards through the finite dependency cone.

Goal theorem shape:

> every first-failure branch must back-propagate to either a base-layer violation or an already certified boundary/tail region.

If this theorem were proved with no hidden global assumption, it would close the PF/RH route. At present it is a research target, not a result.

---

## 13. Relation to precision-first mathematics

For a coefficient/determinant precision state, store

```text
(value interval, precision, index window, certificate provenance, future language)
```

rather than a fictitious exact floating point.

A determinant branch is terminal when its interval/certificate excludes zero with the needed sign. If it straddles zero, refine only the coefficients/ratios in its finite dependency cone.

The `delta -> 0` limit is therefore not the proof engine. The proof engine is a uniform certificate showing that every branch eventually becomes terminal positive/nonnegative at finite precision.

This cleanly separates:

- finite numerical evidence;
- rigorous finite interval certificates;
- region-uniform theorems;
- the remaining global cover problem.

---

## 14. Current verdict

The BRC rerun does **not** prove RH at this checkpoint.

It does produce three substantive changes to the proof architecture:

1. **the false exponential-coefficient lemma has a correct dual replacement:** reciprocal coefficients, not the original entire coefficients, carry pole/residue exponentials;
2. **finite verified spectral data can close infinite vertical Toeplitz rays** through exact rectangular duality plus residue dominance;
3. **RH is retyped as a BRC region-cover / local-Dodgson propagation problem** with exact safe-coalescence rules, instead of one fragile global asymptotic identity.

The highest-leverage next route is `T1 + T4`: cluster-preserving reciprocal branches plus first-failure Dodgson back-propagation.

Hard block: `NONE`.

CI: `CI_NOT_REQUIRED_FOR_RESEARCH`.
