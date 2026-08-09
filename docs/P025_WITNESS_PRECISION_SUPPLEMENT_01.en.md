# P025 Supplement 01 — Relation-Conditioned Witness Precision

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P023 future-safe quotient; Pasten arithmetic-derivative prior art  
Novelty status: `ARCHITECTURE NOVELTY_UNVERIFIED`

## 1. From arithmetic derivatives to finite coordinates

Fix a primitive abc triple

\[
a+b=c,\qquad \gcd(a,b)=1,
\]

and let

\[
S=\operatorname{supp}(abc).
\]

Pasten's universal Leibniz map uses one coordinate `xi_p` for each `p in S`; on this finite support a derivation `psi` is an integer vector

\[
x=(x_p)_{p\in S},\qquad x_p=\psi(\xi_p).
\]

For an integer `n`,

\[
d^\psi(n)=n\sum_{p\mid n}\frac{v_p(n)}p x_p.
\]

These formulas and the lattice structures below are Pasten's prior work [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]. P025 only proposes a finite-precision reinterpretation.

## 2. P025-T05 — the additive witness lattice is an integer hyperplane kernel

The condition

\[
d^\psi(a)+d^\psi(b)=d^\psi(c)
\]

is equivalent to

\[
\sum_{p\in S}\alpha_p x_p=0,
\]

where pairwise coprimality gives

\[
\alpha_p=
\begin{cases}
 a\,v_p(a)/p,&p\mid a,\\
 b\,v_p(b)/p,&p\mid b,\\
 -c\,v_p(c)/p,&p\mid c.
\end{cases}
\]

Every coefficient is integral. Divide the coordinate gcd and fix the global sign to obtain a primitive normal

\[
\widehat\alpha(a,b,c).
\]

Then Pasten's additive witness module is

\[
\boxed{
T(a,b)=\ker_{\mathbb Z}\widehat\alpha
=\{x\in\mathbb Z^S:\widehat\alpha\cdot x=0\}.
}
\]

Pasten proves in the relevant `c>2` range that this is a saturated free abelian subgroup of rank

\[
|S|-1=\omega(abc)-1.
\]

### Architectural interpretation

The active relation need not retain all valuation data directly in the coarse state. It first turns the fine state into a **prime-labelled primitive normal**, and that normal generates the admissible witness lattice.

We therefore provisionally write the relation signature as

\[
\boxed{\Sigma_{\rm add}(a,b,c)=(S,\widehat\alpha).}
\]

The lattice theory is elementary/prior mathematics; `relation signature` is P025 architecture terminology.

## 3. P025-T06 — the primitive normal is a complete signature of the additive witness lattice

Let `S` be a fixed finite labelled set and let `alpha,beta in Z^S` be primitive nonzero vectors. Define

\[
L_\alpha=\ker_{\mathbb Z}\alpha,
\qquad
L_\beta=\ker_{\mathbb Z}\beta.
\]

Then

\[
\boxed{
L_\alpha=L_\beta
\iff
\beta=\pm\alpha.
}
\]

### Proof

The reverse implication is immediate.

If the two integer kernels agree, then their rational spans agree as well: every rational vector in `ker_Q(alpha)` can be cleared of denominators to produce an integer vector in `ker_Z(alpha)`, and conversely. Hence

\[
\ker_{\mathbb Q}\alpha
=
\ker_{\mathbb Q}\beta.
\]

Two nonzero linear functionals with the same codimension-one kernel are rational scalar multiples, so `beta=lambda alpha` for nonzero `lambda in Q`. Since both vectors are primitive integer vectors, necessarily

\[
\lambda=\pm1.
\]

This proves the claim.

### P023 minimal-repair interpretation

If the future observable is the whole witness lattice

\[
h(a,b,c)=T(a,b),
\]

then normalized `Sigma_add` is a complete encoding of `h`.

Consequently every quotient through which the complete additive witness lattice descends exactly must distinguish different `Sigma_add`. Starting from the radical coarse state `q_rad`, the refinement

\[
\boxed{
q_1=(q_{\rm rad},\Sigma_{\rm add})
}
\]

is therefore the P023-style coarsest one-step repair for the specific future observable “retain the complete additive witness lattice.”

This does not say that `Sigma_add` is the minimum information required for abc, nor that it is safe for all future operations; it answers only this witness-lattice observation.

## 4. Wronskian degeneracy gives a second hyperplane

Pasten defines

\[
W^\psi(a,b)=a\,d^\psi(b)-b\,d^\psi(a).
\]

This is another integer linear form in the `x_p`:

\[
W^\psi(a,b)=\sum_{p\in S}\beta_p x_p.
\]

Define the degenerate sublattice

\[
T^\circ(a,b)
=
T(a,b)\cap\ker_{\mathbb Z}\beta.
\]

Pasten proves in the corresponding primitive nontrivial range that

\[
\operatorname{rk}T^\circ
=\operatorname{rk}T-1.
\]

Thus one obtains a strict lattice flag

\[
\boxed{
T^\circ(a,b)\subsetneq T(a,b)\subset\mathbb Z^S.
}
\]

The witnesses usable in a Mason-type argument are

\[
x\in T(a,b)\setminus T^\circ(a,b).
\]

## 5. P025-D01 — witness precision

Equip the ambient lattice with Pasten's sup norm

\[
\|x\|_\infty=\max_{p\in S}|x_p|.
\]

For every integer radius `k>=0`, define

\[
\mathcal W_k(a,b)
=
\{x\in T(a,b)\setminus T^\circ(a,b):
\|x\|_\infty\le k\}.
\]

Then

\[
\mathcal W_0\subseteq
\mathcal W_1\subseteq
\mathcal W_2\subseteq\cdots.
\]

Define the first usable witness radius

\[
\boxed{
\mu(a,b,c)
=\min\{k\in\mathbb N:\mathcal W_k(a,b)\neq\varnothing\}.
}
\]

Because `T^circ` is a proper sublattice of `T`, a non-degenerate integer witness exists and `mu` is finite.

### Precision interpretation

`mu` is neither measurement error nor floating-point tolerance. It records:

> **After a coarse collapse such as radical has forgotten fine detail, how large a discrete witness-coordinate radius must be opened before the active relation admits a non-degenerate cross-language certificate?**

This gives a task-relative, relation-conditioned finite integer precision coordinate.

## 6. P025-N02 — witness precision does not descend through radical state

Compare

\[
1+2=3,
\qquad
1+8=9.
\]

The complete radical triple state is identical:

\[
\boxed{
(\operatorname{rad}a,\operatorname{rad}b,\operatorname{rad}c)
=(1,2,3).
}
\]

Both witness spaces use prime coordinates `(2,3)`.

### State A: `1+2=3`

The additive condition is

\[
x_2-x_3=0,
\]

so

\[
T_A=\{(t,t):t\in\mathbb Z\}.
\]

The Wronskian is non-degenerate for `t neq 0`, hence

\[
\boxed{\mu_A=1.}
\]

### State B: `1+8=9`

The raw additive equation is

\[
12x_2-6x_3=0,
\]

whose primitive form is

\[
2x_2-x_3=0.
\]

Thus

\[
T_B=\{(t,2t):t\in\mathbb Z\},
\]

and the smallest non-degenerate vector has sup norm `2`:

\[
\boxed{\mu_B=2.}
\]

Therefore

\[
q_{\rm rad}(A)=q_{\rm rad}(B)
\quad\text{but}\quad
T_A\ne T_B,
\qquad
\mu_A\ne\mu_B.
\]

Hence

\[
\boxed{
\text{neither witness family nor witness precision is determined by the radical coarse state alone.}
}
\]

This is stronger than the earlier failure of radical to be an addition congruence: even when the future goal is weakened to “obtain a small certificate,” the minimum certificate cost still detects multiplicity forgotten by radical.

## 7. What this feeds back into P023

P023's exact-repair route is

\[
\text{coarse quotient}
\to
\text{restore information required by the future}
\to
\text{exact operation descent}.
\]

P025 now supplies a second route:

\[
\text{coarse quotient}
\to
\text{relation signature}
\to
\text{multivalued witness lattice/flag}
\to
\text{first usable witness radius }\mu.
\]

They are not the same object:

- `q_1=(q_rad,Sigma_add)` makes the **complete witness lattice** descend exactly;
- abc may need only the existence of a sufficiently small non-degenerate witness, not reconstruction of the whole lattice;
- therefore a new minimization problem remains: to decide only `mu<=K` or the existence of a selected certificate class, can one use a repair strictly coarser than `Sigma_add`?

This is the next exact intersection between P025 and P023.

## 8. What this feeds back into A4

A4 already treats admissible support as a multivalued relation instead of forcing a single-valued map. P025's

\[
\mathcal W_k(a,b)
\]

is likewise a finite admissible witness family growing monotonically with radius.

But no A4 composition law may be imported automatically. At present we only have:

1. finite witness families at fixed `k`;
2. monotone growth in `k`;
3. `mu` as the first nonempty critical radius;
4. changing the relation changes the lattice itself, not merely the radius.

A reusable witness-composition or transport law remains open and must be tested counterexample-first.

## 9. A more precise foundation candidate

The first-stage sketch was

`coarse state -> witness family -> witness cost`.

P025-N02 shows that this is underspecified because the witness family is not determined by the coarse radical state. The more accurate candidate is

\[
\boxed{
\text{fine relation-state}
\xrightarrow{q}
\text{coarse state}
\quad+\quad
\text{relation signature}
\longrightarrow
\text{normed witness flag}
\longrightarrow
\mu.
}
\]

The certificate layer is therefore not an ordinary property of the coarse state; it is an attached object generated jointly by the **task relation and fine structure that has not been safely erased**.

This agrees with the boundary intuition in Foundation `FQ-20260809-004`: functional state, relation-state, and multivalued support should not be merged prematurely.

## 10. Current executable assets

New assets:

- `src/enterprise_math/abc_witness_precision.py`
  - primitive integer normal for Pasten's additive relation;
  - Wronskian-degeneracy normal;
  - normed witness flag;
  - bounded exact witness enumeration;
  - minimal witness cost;
  - same-radical / different-witness-precision counterexample;
  - primitive-kernel signature normalization.
- `tests/test_abc_witness_precision.py`
  - `1+2=3`: `mu=1`;
  - `1+8=9`: `mu=2`;
  - the stronger same-radical counterexample;
  - monotonicity of witness balls;
  - a three-coordinate sample `5+27=32`;
  - primitive-normal scaling invariance;
  - exact-enumeration state-cap guard.

These tools are exact small-support oracles only; they do not replace Pasten's Geometry-of-Numbers asymptotics.

## 11. Next questions

The most valuable next step is not more abc-triple enumeration, but two general questions.

### Q1 — coarsest repair for certificate decisions

If the future asks only

\[
\mu(x)\le K?
\]

rather than reconstructing all of `T(x)`, then `Sigma_add` is likely too fine.

The task is to derive the true P023-minimal repair for this binary/graded future observation and compare its information content as `K` changes.

### Q2 — canonical signature of a normed flag

The full non-degenerate witness structure is determined by

\[
T^\circ\subset T\subset\mathbb Z^S
\]

and the norm. `T` alone is completely encoded by primitive `alpha`; but `T^circ` depends only on the restriction of the second functional to `T`, so replacing `beta` by `beta + k alpha` can represent the same degenerate sublattice.

Thus the minimal canonical signature of the full flag is not simply the pair `(alpha,beta)`; a quotient / row-module / exterior invariant should be investigated. This sits exactly at the intersection of P023 quotient semantics and A4 relation-support semantics.

Current status: `OPEN / HIGH VALUE / HARD_BLOCK=NONE`.
