# P025 Supplement 42 — Effective Small Derivatives After Intrinsic Wronskian Normalization

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 34, 41  
Hard block: `NONE`
Novelty status: `NOVELTY_UNVERIFIED / PRIORITY SEARCH INCOMPLETE`

## 1. Prior-art boundary first

Hector Pasten's arithmetic-derivative program already asks for small relation-adapted derivations with nonzero arithmetic Wronskian. His Small Derivatives Conjecture bounds the `L_infinity` norm of such a derivation by a power of `c`, and his work proves precise exponent-dependent implications between sufficiently small derivatives and the `abc` conjecture.

Therefore the minimum nondegenerate witness radius

\[
\mu
=
\min\{\|\psi\|_\infty:
\psi\in\mathscr T(a,b),
W^\psi(a,b)\ne0\}
\]

is **ADOPTED PRIOR ART / REINTERPRETED AS A PRECISION HORIZON**. P025 does not claim the optimization problem itself.

The new question in this supplement is whether Stage 34's complete Wronskian-image index permits a weaker norm condition at the exact step where the Wronskian estimate feeds an `abc` bound.

## 2. Exact integer block capacity

For a positive integer `n`, define

\[
R_n=\operatorname{rad}(n)
\]

and

\[
\boxed{
C(n)
=
\sum_{p\mid n}
 v_p(n)\frac{R_n}{p}.
}
\]

For `n=1`, set `C(1)=0`.

If a derivation has prime-coordinate norm at most `r`, then

\[
|d^\psi(n)|
\le
r\,m(n)C(n),
\]

because the raw derivative coefficients are

\[
\frac{nv_p(n)}p
=m(n)\,v_p(n)\frac{R_n}p.
\]

For the pair `(a,b)` put

\[
\boxed{
K_{ab}
=R_aC(b)+R_bC(a).
}
\]

Then

\[
|W^\psi(a,b)|
\le
r\,m(a)m(b)K_{ab}.
\]

## 3. P025-T101 — intrinsic Wronskian image strengthens the capacity lower bound

Let

\[
M=m(a)m(b)m(c).
\]

Pasten's residual divisibility gives

\[
M\mid W^\psi(a,b).
\]

Stage 34 refines this by computing the complete Wronskian image:

\[
W(\Lambda)=D\mathbb Z,
\qquad
D=\eta_{\min}M.
\]

Take a minimum-norm nondegenerate derivation of radius `mu`. Its Wronskian need not equal `D`, but because it is a nonzero element of `D Z`,

\[
|W_\mu|\ge D=\eta_{\min}M.
\]

Combining with the block capacity bound gives

\[
\eta_{\min}m(a)m(b)m(c)
\le
\mu m(a)m(b)K_{ab}.
\]

Cancel the positive first two residuals:

\[
\boxed{
\eta_{\min}m(c)
\le
\mu K_{ab}.
}
\]

Equivalently,

\[
\boxed{
\eta_{\min}c
\le
\mu R_c K_{ab}.
}
\]

Since

\[
R_cK_{ab}
=
\operatorname{rad}(abc)
\left(
\sum_{p\mid a}\frac{v_p(a)}p
+
\sum_{p\mid b}\frac{v_p(b)}p
\right),
\]

this is the refined arithmetic-Wronskian capacity estimate

\[
\boxed{
\eta_{\min}c
\le
\mu\operatorname{rad}(abc)
\left(
\sum_{p\mid a}\frac{v_p(a)}p
+
\sum_{p\mid b}\frac{v_p(b)}p
\right).
}
\]

The ordinary residual-only estimate is the weaker specialization obtained by replacing `eta_min` with one.

## 4. P025-D26 — effective small-derivative norm

Define the rational quantity

\[
\boxed{
\mu_{\rm eff}
=
\frac{\mu}{\eta_{\min}}.
}
\]

Then P025-T101 becomes

\[
\boxed{
 c
\le
\mu_{\rm eff}
\operatorname{rad}(abc)
\left(
\sum_{p\mid a}\frac{v_p(a)}p
+
\sum_{p\mid b}\frac{v_p(b)}p
\right).
}
\]

Thus the Wronskian-to-radical implication sees the **effective norm** `mu/eta_min`, not only `mu`.

This does not mean Pasten's original Small Derivatives Conjecture was incorrectly formulated. His norm condition is stronger and is connected to broader derivative arguments. The claim here is narrower: for this specific Wronskian `abc` estimate, dividing by the intrinsic image index loses no strength in the displayed implication.

## 5. P025-C04 — Effective Small Derivatives candidate

For an exponent

\[
0<\alpha<1,
\]

consider the condition

\[
\boxed{
\mu_{\rm eff}<c^\alpha,
}
\]

i.e.

\[
\boxed{
\mu<\eta_{\min}c^\alpha.
}
\]

Call this the **Effective Small Derivatives (ESD) condition at exponent `alpha`**.

For a rational exponent

\[
\alpha=p/q,
\qquad
0<p<q,
\]

it is exactly the finite integer comparison

\[
\boxed{
\mu^q
<
\eta_{\min}^q c^p.
}
\]

No logarithms or floating-point powers are required.

## 6. P025-T102 — ESD gives the same capacity-type `abc` consequence

Assume

\[
\mu/\eta_{\min}<c^{p/q}.
\]

P025-T101 gives

\[
c
<
c^{p/q}R_cK_{ab}.
\]

Raise to the `q`th power and cancel `c^p`:

\[
\boxed{
 c^{q-p}
<
(R_cK_{ab})^q.
}
\]

Equivalently,

\[
\boxed{
 c^{1-p/q}
<
\operatorname{rad}(abc)
\left(
\sum_{p\mid a}\frac{v_p(a)}p
+
\sum_{p\mid b}\frac{v_p(b)}p
\right).
}
\]

This is exactly the capacity/radical inequality produced by imposing the same exponent on the unnormalized norm, but ESD is pointwise weaker because

\[
\eta_{\min}\ge1.
\]

Therefore, at the Wronskian implication step,

\[
\boxed{
\mathrm{SD}_\alpha
\Longrightarrow
\mathrm{ESD}_\alpha
\Longrightarrow
\text{same capacity-type abc estimate}.
}
\]

## 7. Strict pointwise relaxation exists

### `1+242=243`

The exact P025 values are

\[
\mu=27,
\qquad
\eta_{\min}=5,
\qquad
\mu_{\rm eff}=27/5.
\]

At exponent

\[
\alpha=1/3,
\]

the ordinary bound fails:

\[
27^3>243,
\]

but ESD holds:

\[
27^3
<
5^3\cdot243.
\]

So the normalization is not a notational restatement at fixed exponent.

Moreover the refined capacity inequality is sharp here:

\[
\eta_{\min}m(c)
=5\cdot81
=405
=
27\cdot15
=
\mu K_{ab}.
\]

### `1+512=513`

\[
\mu=13,
\qquad
\eta_{\min}=3,
\qquad
\mu_{\rm eff}=13/3.
\]

At exponent `1/4`, the ordinary norm bound fails while ESD holds.

## 8. Negative boundary: intrinsic normalization does not solve the whole route

If

\[
\eta_{\min}=1,
\]

then

\[
\mu_{\rm eff}=\mu.
\]

All squarefree primitive triples have `eta_min=1` by Supplement 05, and other nonsquarefree triples may also have saturated normalized Wronskian image.

Therefore ESD leaves a substantial hard subfamily completely unchanged.

A small computational scan also finds high-quality examples with `eta_min=1`; no claim is made that intrinsic normalization alone approaches a proof of `abc`.

## 9. Relation to Pasten's theorem

Pasten's published work already proves that sufficiently small arithmetic derivatives are tightly linked to `abc`, with precise exponent dependence. Thus:

- Pasten's `abc -> small derivatives` results automatically imply the corresponding **weaker** effective bound whenever their hypotheses/exponent choices apply;
- P025-T102 shows that an effective bound is already sufficient for the Wronskian-capacity implication back toward an `abc`-type radical estimate.

However this supplement does **not** assert a new published-equivalence theorem with all of Pasten's exceptional families and exponent bookkeeping already transferred. That full comparison remains a prior-art/theorem-scope audit item.

## 10. Why this is a serious next route

P025 has moved the problem from

\[
\text{make a high-dimensional arithmetic derivative small}
\]

to the weaker target

\[
\boxed{
\text{make its minimum norm small relative to the intrinsic Wronskian-image index}.
}
\]

The two quantities arise from different layers:

- `mu` — geometric access to a nondegenerate relation witness;
- `eta_min` — integral congruence coarseness of the complete normalized certificate image.

The ratio tests whether arithmetic congruence obstruction can compensate geometric access cost.

This is the first P025 candidate in the current route that potentially weakens the **sufficient derivative hypothesis itself**, rather than only repackaging its state.

## 11. Prior-art / novelty discipline

A focused search found Pasten's small-derivative / Wronskian framework but did not locate this explicit `mu/eta_min` normalization by the complete Wronskian image generator. This absence is **not evidence of originality**.

Status remains

\[
\boxed{\texttt{NOVELTY_UNVERIFIED}.}
\]

No priority language is permitted before broader literature review and independent mathematical checking.

## 12. Executable assets

Added:

- `src/enterprise_math/abc_effective_small_derivative.py`;
- `tests/test_abc_effective_small_derivative.py`.

The implementation uses exact integer powers for rational exponents and exact fractions for `mu_eff`.

## 13. Next frontier

No hard block exists. Continue with:

1. classify / count the hard saturated subfamily `eta_min=1`;
2. seek upper bounds on `mu/eta_min` directly, rather than bounding `mu` then dividing;
3. study whether the block-value / Apéry access compiler exposes such direct ratio bounds;
4. audit Pasten Section 4 carefully enough to transfer exact exponent/exception statements;
5. pressure-test ESD on known high-quality abc triples and structured prime-power families;
6. do not promote ESD to a claimed equivalent conjecture until those audits are complete.
