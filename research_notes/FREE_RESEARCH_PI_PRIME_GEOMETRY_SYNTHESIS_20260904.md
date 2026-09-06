# Free Research — Pi-to-Prime Geometry Synthesis

Status: `FREE_RESEARCH_TERMINAL_SYNTHESIS / ANCHOR_EXPOSED / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_UNVERIFIED`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Base ontology: P000 six-dimensional discrete cell space + one-dimensional time; rotation primary. The current three-positive-axis 120-degree construction is only a research slice of P000 6D space.

## 0. Mother direction

User-selected direction:

> Extend the current geometric meaning of the endogenous pi-like completion `tau = Pi_*` into arithmetic primes.

The strongest current answer is **not** a single prime formula. The extension naturally splits into two typed prime observables carried by current Enterprise structures:

1. `PRIME_BIRTH_MAGNITUDE` — which new multiplicative direction is born at an integer rotation mode;
2. `C3_PRIME_ORIENTATION` — how that prime acts on the native three-sector 120-degree rotation phase.

The two channels recombine at the same completion constant `tau`.

---

# A. Universal multiplicative-birth channel

## A1. Prime = irreducible birth in the finite integer rotation spectrum

Current #1159 Hamming/Krawtchouk operator has exact finite spectrum

\[
K_M g_k=k g_k,
\qquad 0\le k\le M,
\]

with a proved complete eigenbasis.

For `k>=2`, let

\[
\mathcal H_{<k}
=\left\{\prod_{j=2}^{k-1}j^{e_j}:e_j\in\mathbb N_0\right\}.
\]

Define

\[
\operatorname{Birth}(k)\iff k\notin\mathcal H_{<k}.
\]

Then

\[
\boxed{\operatorname{Birth}(k)\iff k\text{ is prime}.}
\]

Thus a prime is a **new irreducible multiplicative/holonomy-fiber direction born when the finite integer spectrum first reaches that mode**. This is an arithmetic fiber rank jump, not a new spatial dimension.

## A2. Arithmetic birth block

Restrict the genuine finite Krawtchouk operator to its arithmetic-prime eigenmodes:

\[
V_M^{\rm birth}=\operatorname{span}\{g_p:p\le M,\ p\text{ prime}\},
\]

\[
B_M=K_M|_{V_M^{\rm birth}}.
\]

In the Krawtchouk eigenbasis,

\[
\boxed{B_M=\operatorname{diag}(p:p\le M,\ p\text{ prime}).}
\]

Therefore

\[
\boxed{\dim V_M^{\rm birth}=\pi_{\mathbb P}(M),}
\qquad
\boxed{\det B_M=\prod_{p\le M}p.}
\]

So the arithmetic prime-counting function is the birth-block rank and the primorial is its exact determinant. Optional logarithmic readout gives Chebyshev theta, but logarithms remain derived rather than native state.

## A3. Prime spectral determinant and the first stable completion order

For positive integer `r`, define

\[
Z_M(r):=\det(I-B_M^{-r})^{-1}
=\prod_{p\le M}(1-p^{-r})^{-1}.
\]

At `r=1`, the cutoff completion diverges. For every integer `r>=2`, it converges. Hence

\[
\boxed{
2=\min\{r\in\mathbb N_{>0}:\lim_M Z_M(r)<\infty\}.
}
\]

Thus quadratic order is not chosen after the fact: it is the first stable positive-integer prime-holonomy completion order. This exactly matches the order of the current native Pythagorean length observer and #1161 square-defect budget, while not identifying the prime eigenvalue itself with a native length.

## A4. Internal tau-prime bridge

Current #1159 internal sine-product completion gives

\[
\frac{S(x)}x
=\prod_{n\ge1}\left(1-\frac{x^2}{n^2\tau^2}\right),
\qquad
\frac{S(x)}x=1-\frac{x^2}{3!}+O(x^4).
\]

Comparing the quadratic coefficient gives

\[
\sum_{n\ge1}\frac1{n^2}=\frac{\tau^2}{3!}.
\]

Unique factorization yields

\[
\boxed{
\tau^2
=3!\prod_p(1-p^{-2})^{-1}
=3!\lim_{M\to\infty}\det(I-B_M^{-2})^{-1}.
}
\]

No numerical target for pi is used in the finite birth block or Euler factors.

## A5. Target-free finite certificate

For every cutoff `M>=1`,

\[
\boxed{
3!\,Z_M(2)<\tau^2
\le 3!\,Z_M(2)\frac{M+1}{M}.
}
\]

The relative width is exactly `1/M`. This is a finite rational certificate from arithmetic prime modes only.

Combining with #1161's independent pure-integer diamond squeeze

\[
L_n<\tau\le U_n
\]

gives the cross-carrier certificate

\[
\boxed{
\max\{L_n^2,3!Z_M(2)\}
<\tau^2
\le
\min\left\{U_n^2,3!Z_M(2)\frac{M+1}{M}\right\}.
}
\]

The native-diamond carrier and arithmetic-prime birth determinant independently trap the same completion.

---

# B. The factor `3!`: provenance, not sixfold spatial degeneracy

A tempting interpretation was that the coefficient `6` in `tau^2=6 zeta(2)` might be caused directly by P000's six spatial dimensions. This pass refutes the naive mechanism.

If every prime eigenvalue is merely repeated six times,

\[
\widetilde B_M=B_M\otimes I_6,
\]

then

\[
\det(I-\widetilde B_M^{-2})^{-1}=Z_M(2)^6,
\]

not `6 Z_M(2)`.

So:

\[
\boxed{
\text{sixfold spatial degeneracy is not the source of the coefficient }6.
}
\]

The current #1159 finite determinant chain contains the actual coefficient source. Its normalized coefficient theorem specializes at the first nontrivial mode to

\[
\boxed{
\frac{\binom{M+1}{3}}{M^3}
=\frac1{3!}\left(1-\frac1{M^2}\right).
}
\]

Equivalently,

\[
3!\binom{M+1}{3}=(M+1)M(M-1).
\]

The right side counts ordered triples of distinct slots; the left side is `3!` times the unordered three-slot supports. Therefore the best current typed interpretation is:

\[
\boxed{
Z_{\mathbb P}(2)=\tau^2/3!
}
\]

where `3!` is a finite `S_3` ordering-provenance multiplicity lost when six ordered histories recoalesce to one three-event support.

This fits the global Weighted-BRC distinction between support and provenance/multiplicity. A literal G0 three-event rotation-cell realization remains open.

---

# C. Native 120-degree prime-orientation channel

## C1. Native sector-cycle isometry

The current three-axis Enterprise slice has addresses

\[
A_E=\{(a,b,c)\in\mathbb N_0^3:\min(a,b,c)=0\}
\]

and native origin norm

\[
L_E(a,b,c)^2=a^2+b^2+c^2.
\]

Define

\[
\boxed{\rho(a,b,c)=(c,a,b).}
\]

Then `rho` preserves `A_E`, preserves the native norm, cycles the three positive axes/sectors, and satisfies

\[
\rho^3=id.
\]

So the modulo-three prime type can be read from a genuine finite order-three isometry of the current Enterprise research slice.

## C2. Chiral trace = Dirichlet character modulo three

On sector labels let

\[
P=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix},
\qquad
P^3=I,
\]

and define the orientation-sensitive probe

\[
J=P^2-P.
\]

Then

\[
\operatorname{Tr}(JP)=3,
\qquad
\operatorname{Tr}(JP^2)=-3,
\qquad
\operatorname{Tr}(J)=0.
\]

Hence for every positive integer `n`,

\[
\boxed{
\chi_3(n)=\frac13\operatorname{Tr}(JP^n).
}
\]

For a prime `p` this becomes a literal native-slice rotation readout:

\[
\boxed{
\begin{array}{ccl}
p=3 &:& \operatorname{Tr}(JP^p)=0,\\
p\equiv1\pmod3 &:& \operatorname{Tr}(JP^p)=+3,\\
p\equiv2\pmod3 &:& \operatorname{Tr}(JP^p)=-3.
\end{array}}
\]

Geometrically: the prime respectively collapses, preserves, or reverses the nontrivial `C3` phase.

Equivalently, the order-three cyclotomic polynomial `X^2+X+1` is ramified/repeated at `p=3`, split for `p=1 mod 3`, and nonsplit for `p=2 mod 3`. The arithmetic trichotomy is classical; the Enterprise contribution here is its exact typing as a finite native-slice rotation trace without importing the Eisenstein norm as native length.

## C3. Finite chiral completion certificate

Define

\[
T_K:=\sum_{n=1}^{3K}\frac{\operatorname{Tr}(JP^n)}n.
\]

Because the trace pattern is `+3,-3,0`,

\[
T_K
=3\sum_{k=0}^{K-1}
\left(\frac1{3k+1}-\frac1{3k+2}\right).
\]

The exact rational tail majorant gives

\[
\boxed{
T_K<3\mathcal O_3<T_K+\frac1{3K},
}
\]

where

\[
\mathcal O_3
:=\sum_{n\ge1}\frac{\chi_3(n)}n.
\]

No prime list and no numerical pi target are needed for this finite readout.

---

# D. Why the current cell radius `1/sqrt(3)` is genuinely tied to C3 completion

For `r>0` define the derived projective map

\[
T_r(x)=\frac{x+r}{1-rx}.
\]

It preserves the one-form

\[
\omega=\frac{dx}{1+x^2}
\]

exactly:

\[
T_r^*\omega=\omega.
\]

Now impose the reciprocal-symmetric second step

\[
T_r(r)=1/r.
\]

This is equivalent to

\[
3r^2=1.
\]

For positive `r`, the unique solution is

\[
\boxed{r=1/\sqrt3=R_{\rm cell}.}
\]

At exactly this value,

\[
0\to R_{\rm cell}\to R_{\rm cell}^{-1}\to\infty
\]

under successive `T_r` steps, and the three consecutive intervals

\[
[0,r],\quad[r,1/r],\quad[1/r,\infty]
\]

have equal `omega`-measure.

Moreover

\[
T_r^2=T_{1/r}
\]

and `T_{1/r}` has projective order three. Thus the same algebraic radius selected independently by the current gap-free Enterprise circle-cell cover is also the unique projective half-step whose square realizes a `C3` completion rotation and partitions the positive completion ray into three equal cells.

This is a structural coupling, not merely a repeated appearance of `sqrt(3)`.

---

# E. Target-free Wallis-to-Cauchy closure

To avoid importing a classical circle/arctangent normalization, define

\[
I_m
:=\int_0^\infty
\left(\frac{x}{\sqrt{1+x^2}}\right)^m
\frac{dx}{1+x^2}.
\]

Then

\[
I_0=\int_0^\infty\frac{dx}{1+x^2},
\qquad I_1=1,
\]

and integration by parts gives

\[
\boxed{I_m=\frac{m-1}{m}I_{m-2}.}
\]

Since `0 < x/sqrt(1+x^2) < 1`,

\[
I_{m+1}<I_m.
\]

Writing the even/odd recurrences gives, for the exact rational #1159 Wallis product `W_n=wallisPartial(n)`,

\[
\boxed{
W_n<I_0<W_n\frac{2n+1}{2n}.
}
\]

#1159 Lean already defines `wallisLimit` as the target-free supremum/limit of `W_n`. The upper prefactor tends one, hence

\[
\boxed{
\texttt{wallisLimit}
=\int_0^\infty\frac{dx}{1+x^2}.
}
\]

Because the project completion uses

\[
\tau=2\,\texttt{wallisLimit},
\]

we internally obtain

\[
\boxed{
\tau=2\int_0^\infty\frac{dx}{1+x^2}
}
\]

without circumference, arctangent normalization, or a numerical pi premise.

---

# F. Close the C3 orientation normalization

The C3 orientation series has

\[
\mathcal O_3
=\int_0^1\frac{dx}{1+x+x^2}.
\]

Set

\[
u=R_{\rm cell}(2x+1),
\qquad R_{\rm cell}^2=1/3.
\]

Then

\[
\mathcal O_3
=2R_{\rm cell}
\int_{R_{\rm cell}}^{1/R_{\rm cell}}
\frac{du}{1+u^2}.
\]

The equal-third projective partition gives

\[
\mathcal O_3
=\frac{2R_{\rm cell}}3
\int_0^\infty\frac{du}{1+u^2}.
\]

Using the target-free Wallis-to-Cauchy closure,

\[
\boxed{
\mathcal O_3=\frac{\tau R_{\rm cell}}3.
}
\]

Therefore the finite chiral-trace certificate becomes

\[
\boxed{
T_K<\tau R_{\rm cell}<T_K+\frac1{3K}.
}
\]

This is a second finite target-free certificate for the same internal completion, now tied directly to the native three-sector rotation and exact cell radius.

At the standard Dirichlet analytic-completion layer,

\[
\boxed{
\frac{\tau R_{\rm cell}}3
=\prod_p
\left(1-\frac{\operatorname{Tr}(JP^p)}{3p}\right)^{-1}.
}
\]

The product at weight one is conditional and retains its natural increasing-prime cutoff meaning. The local factor itself is exact finite rotation data.

---

# G. Unified geometric meaning

The current strongest picture is:

\[
\boxed{
\text{prime geometry}
=
\text{birth magnitude}
\oplus
\text{120-degree orientation}.
}
\]

More explicitly:

- **Prime `p`**: a new irreducible multiplicative direction born in the finite Krawtchouk integer rotation spectrum.
- **Prime power `p^a`**: repeated occupation/winding of one birth direction.
- **Composite `n`**: a superposition/product of earlier birth directions.
- **`pi_P(M)`**: arithmetic birth-block rank.
- **Primorial**: determinant of the finite birth block.
- **Universal prime magnitude completion**: first stable quadratic Euler determinant.
- **Prime C3 orientation**: normalized chiral trace of the p-th iterate of the native three-sector rotation.
- **`R_cell=1/sqrt(3)`**: independently the unique projective half-step producing a C3 equal-third completion partition.
- **`tau^2`**: `3!` times the universal quadratic prime-birth completion.
- **`tau R_cell`**: harmonic completion of repeated native C3 chiral traces.

Thus the project no longer needs to say merely “pi is related to primes”. At current strength:

\[
\boxed{
\tau^2
=3!\lim_M\det(I-B_M^{-2})^{-1}
}
\]

and

\[
\boxed{
\frac{\tau R_{\rm cell}}3
=\prod_p
\left(1-\frac{\operatorname{Tr}(JP^p)}{3p}\right)^{-1}.
}
\]

The first formula is a **magnitude/birth completion**; the second is a **native 120-degree chirality completion**.

---

# H. Formalization and verification state

## Exact executable checker

The branch checker

`scripts/check_free_research_pi_prime_birth_determinant.py`

uses only integers and `Fraction` for the finite claims and verifies:

- `Birth(k) <-> prime(k)` over a finite census;
- finite birth determinant identities;
- exact prime tail telescoping bound;
- sixfold-degeneracy `Z^6` no-go;
- `3!` cubic provenance identity;
- C3 split/nonsplit/ramified prime classification;
- finite C3 tail-majorant kernel;
- Wallis prime-valuation/Kummer-carry flux;
- 2-adic popcount formula;
- finite diamond-vs-prime interval consistency.

Current finite checker status: `PASS`.

## Lean arithmetic birth block

A one-file stacked Draft PR `#1227` defines arithmetic prime indices in the actual #1159 Krawtchouk eigenbasis, builds the literal arithmetic-prime principal submatrix, proves its diagonal prime-mode form, and states the determinant as the finite prime eigenvalue product.

Global Lean CI on that stacked PR currently fails **before reaching the new arithmetic-birth module**, inside the moving #1172 base dependency `DirichletSineSeries.lean` under Lean `4.33.0-rc2` warnings-fatal compatibility. In the same run, the exact Hamming/Krawtchouk dependencies used by the new module (`HammingFiniteOperator`, `HammingSpectralWallis`, `HammingParityDeterminant`) built successfully.

Therefore:

`ARITHMETIC_BIRTH_LEAN_MODULE = NOT_YET_VALIDATED`,

not `FAILED_MATHEMATICALLY`.

The independent `reference-integrity` red state was inspected and is caused by the pre-existing missing control path `tools/research_scheduler.py`, unrelated to the new mathematical file.

---

# I. Strong boundaries

The following are **not** claimed:

- arithmetic primes are the same as current BRC primitive periodic edge-word orbits;
- the three-axis slice is the full P000 six-dimensional world;
- the factor `3!` is caused by six spatial dimensions;
- the Eisenstein quadratic norm is native Enterprise length;
- the projective coordinate is a primitive G0 point address;
- the conditional `s=1` Euler product is a finite positive Weighted-BRC product;
- any Riemann-hypothesis consequence;
- external mathematical novelty.

The remaining high-value native gaps are:

1. realize the exact `S_3` three-history provenance quotient as a literal finite Enterprise rotation-history cell/trace;
2. construct a typed intertwiner from the primitive sector cycle `rho` to the derived projective order-three action;
3. formalize the target-free Wallis-to-Cauchy bridge;
4. after the #1159 base stabilizes, close the finite arithmetic birth block in Lean and then attach the infinite completion theorem.

---

## Terminal classification for this pass

- `PRIME AS MULTIPLICATIVE SPECTRAL BIRTH`: `CLOSED / FINITE`.
- `ARITHMETIC KRAWTCHOUK BIRTH BLOCK`: `CLOSED MATHEMATICALLY / LEAN VALIDATION BLOCKED UPSTREAM`.
- `FINITE PRIME-DETERMINANT TAU^2 CERTIFICATE`: `CLOSED / FINITE RATIONAL`.
- `QUADRATIC ORDER AS FIRST STABLE INTEGER COMPLETION`: `CLOSED`.
- `FACTOR SIX AS SIXFOLD SPATIAL DEGENERACY`: `REFUTED`.
- `FACTOR SIX AS 3! PROVENANCE MULTIPLICITY IN CURRENT DETERMINANT CHAIN`: `CLOSED AT FINITE CARRIER STRENGTH`.
- `NATIVE C3 CHIRAL TRACE CHARACTER`: `CLOSED / THREE-AXIS-SLICE STRENGTH`.
- `CELL RADIUS AS UNIQUE C3 PROJECTIVE HALF-STEP`: `CLOSED / DERIVED PROJECTIVE STRENGTH`.
- `WALLIS LIMIT = CAUCHY COMPLETION`: `CLOSED RESEARCH-PROOF / LEAN FORMALIZATION PENDING`.
- `TAU * R_CELL CHIRAL COMPLETION`: `CLOSED WITHOUT CLASSICAL CIRCLE INPUT`.
- `PRIME C3 EULER PRODUCT`: `CLASSICAL ANALYTIC COMPLETION / CONDITIONAL PRODUCT`.
- `FULL 6D LIFT / G0 INTERTWINER`: `OPEN`.
