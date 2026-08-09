# P024 — Adjoint Stabilization Duality, Supplement 03

Status: `ACTIVE RESEARCH NOTE`  
Parent: `docs/P024_ADJOINT_BOUNDARY_PULLBACK_SUPPLEMENT_02.en.md`  
Bridges: P008 order-adjoint semantics, P019 collapse-word stabilization, P020 well-founded stabilization  
Discipline: Galois connections, closure/interior operators, adjoint composition, and fixed-point selection are established order theory. This note isolates the Enterprise Math future-precision consequence and the exact collapse-word bridge.

## 1. Motivation

Supplement 02 identifies the left adjoint of a forward right-adjoint action as the exact reverse transport law for principal future boundaries.

P020 independently proves that a monotone reductive endomap on a `WellFoundedLT` partial order finitely stabilizes to the greatest original fixed point below the input.

The natural dual question is therefore:

> if the forward action is reductive and has a left adjoint, what does repeated boundary pullback stabilize to, and does the stabilized boundary map remain adjoint to the stabilized forward map?

The answer is exact, but one termination subtlety matters:

- a **global** upward stabilization theorem needs an upward well-foundedness condition such as `WellFoundedGT`;
- `N_0` does not satisfy that global condition;
- the collapse-word specialization on `N_0` instead terminates because every individual upward orbit is trapped below an explicit common fixed-point upper bound.

Those two mechanisms are kept separate below.

## 2. Setup

Let `X` be a partial order and let

\[
\lambda \dashv F
\]

mean

\[
\boxed{
\lambda(a)\le b
\iff
a\le F(b).
}
\]

Assume the forward action is reductive:

\[
\boxed{F(x)\le x.}
\]

Because adjoints are monotone, both maps are monotone.

## 3. P024-S3-T01 — A reductive right adjoint forces an extensive left adjoint

Status: `LEAN-CHECKED` in `EnterpriseMath/Order/AdjointReductiveDuality.lean`.

For every `x`, adjunction applied to the reflexive inequality

\[
\lambda(x)\le\lambda(x)
\]

gives

\[
x\le F(\lambda(x)).
\]

Reductivity gives

\[
F(\lambda(x))\le\lambda(x).
\]

Therefore

\[
\boxed{x\le\lambda(x).}
\]

So a reductive forward/right-adjoint action has an extensive boundary/left-adjoint action.

This is the abstract form of the direction reversal seen in Supplement 02.

## 4. P024-S3-T02 — The two adjoints have exactly the same fixed points

Status: `LEAN-CHECKED`.

Under the same assumptions,

\[
\boxed{
\lambda(x)=x
\iff
F(x)=x.
}
\]

### Proof

If `lambda(x)=x`, adjunction gives

\[
x\le F(x).
\]

Together with `F(x)<=x`, antisymmetry gives `F(x)=x`.

Conversely, if `F(x)=x`, adjunction gives `lambda(x)<=x`; T01 gives `x<=lambda(x)`, so `lambda(x)=x`. ∎

Thus the upward boundary dynamics and downward forward dynamics move in opposite order directions but target the **same fixed-state set**.

## 5. P024-S3-T03 — Upward finite stabilization on an upward-well-founded order

Status: `LEAN-CHECKED`.

Let `L:X->X` be monotone and extensive:

\[
x\le L(x).
\]

If `X` has `WellFoundedGT`, then ordinary iteration of `L` reaches after finitely many steps the least original fixed point above the initial state.

Define the selected map

\[
\operatorname{coStab}_L(x).
\]

Then:

\[
\boxed{x\le\operatorname{coStab}_L(x),}
\]

\[
\boxed{L(\operatorname{coStab}_L(x))=\operatorname{coStab}_L(x),}
\]

and for every fixed point `y` with `x<=y`,

\[
\boxed{
\operatorname{coStab}_L(x)\le y.
}
\]

The selected map is monotone and idempotent.

This is the exact order dual of the P020 downward stabilization theorem.

## 6. P024-S3-T04 — Stabilization preserves the adjunction

Status: `LEAN-CHECKED`.

Assume both `WellFoundedLT X` and `WellFoundedGT X`, and let

\[
\lambda\dashv F,
\qquad
F\le id.
\]

Let

\[
S_\uparrow=\operatorname{coStab}_\lambda,
\qquad
S_\downarrow=\operatorname{stab}_F.
\]

Then

\[
\boxed{
S_\uparrow\dashv S_\downarrow.
}
\]

Equivalently,

\[
\boxed{
S_\uparrow(a)\le b
\iff
a\le S_\downarrow(b).
}
\]

### Proof idea

T02 says the original left and right adjoints have the same fixed points.

`S_up(a)` is the least such fixed point above `a`; `S_down(b)` is the greatest such fixed point below `b`.

If `S_up(a)<=b`, then it is a fixed point below `b`, hence lies below `S_down(b)`, and therefore `a<=S_down(b)`.

Conversely, if `a<=S_down(b)`, then `S_down(b)` is a fixed point above `a`, so minimality gives `S_up(a)<=S_down(b)<=b`. ∎

The Lean proof uses exactly these extremal fixed-point characterizations; it does not assume that the two pointwise stabilization times are equal.

## 7. P024-S3-T05 — Fixed words inherit the same dual structure

Status: `PROVED`.

Let

\[
\lambda_i\dashv F_i,
\qquad
F_i\le id,
\qquad i=1,\ldots,m.
\]

For the forward word

\[
W=F_m\circ\cdots\circ F_1,
\]

the left adjoint is the reverse-side boundary word

\[
\Lambda=\lambda_1\circ\cdots\circ\lambda_m.
\]

Because compositions of reductive maps are reductive and compositions of extensive maps are extensive,

\[
W\le id,
\qquad
id\le\Lambda.
\]

Moreover,

\[
\boxed{
\operatorname{Fix}(W)
=
\bigcap_i\operatorname{Fix}(F_i)
=
\bigcap_i\operatorname{Fix}(\lambda_i)
=
\operatorname{Fix}(\Lambda).
}
\]

The reductive-word equality is the same descending-chain mechanism already used in P019/P023; the extensive-word side is its ascending dual. No new fixed-word theory is claimed here.

Whenever the two word iterations satisfy the termination hypotheses of T03/P020, their stabilized maps select the least common fixed point above and greatest common fixed point below respectively, and T04 applies to the composite adjunction.

## 8. Why T04 does not directly apply to `N_0` upward collapse dynamics

The natural numbers have

\[
0<1<2<3<\cdots,
\]

so `WellFoundedGT N_0` is false.

Therefore one must **not** cite T04 as if it globally proved upward collapse-word termination on `N_0`.

The correct collapse proof uses a weaker local mechanism:

> the upward orbit from a particular boundary is monotone and bounded above by an explicit common fixed point; the corresponding finite integer interval contains no infinite strictly increasing chain.

This local bounded-termination principle is enough for the collapse specialization and is strictly weaker than global upward well-foundedness.

The distinction is important because other adjoint actions need not have such a bound. Supplement 02's repeated floor division provides the opposite example: its pulled boundary orbit `1,d,d^2,...` is genuinely infinite.

## 9. Collapse boundary operator

For `p>=1`, recall the power collapse

\[
C_p(n)=R_p(n)^p.
\]

Define the upward perfect-power selector

\[
\boxed{
N_p(b)
=
\min\{k^p:k^p\ge b\}.
}
\]

Supplement 02 proves

\[
\boxed{N_p\dashv C_p.}
\]

Both maps have exactly the perfect `p`-th powers as fixed points.

`C_p` is reductive and idempotent; `N_p` is extensive and idempotent.

## 10. P024-S3-T06 — Collapse-word boundary stabilization is the least perfect `L`-th power above

Status: `PROVED`.

Take a nonempty exponent word

\[
p_1,\ldots,p_m
\]

and set

\[
L=\operatorname{lcm}(p_1,\ldots,p_m).
\]

Let the forward word be

\[
W=C_{p_m}\circ\cdots\circ C_{p_1}
\]

and its left-adjoint boundary word be

\[
\Lambda=N_{p_1}\circ\cdots\circ N_{p_m}.
\]

P019 proves

\[
\boxed{
W^\infty(n)=C_L(n),
}
\]

the greatest perfect `L`-th power below `n`.

On the boundary side,

\[
\boxed{
\Lambda^\infty(b)=N_L(b),
}
\]

the least perfect `L`-th power above `b`.

### Proof

Every `N_p` is monotone and extensive, so the orbit

\[
b\le\Lambda(b)\le\Lambda^2(b)\le\cdots
\]

is ascending.

`N_L(b)` is a perfect `L`-th power and therefore a fixed point of every `N_(p_i)`. Hence it is a fixed point of `Lambda`.

Because `b<=N_L(b)` and `Lambda` is monotone,

\[
\Lambda^k(b)\le N_L(b)
\]

for every `k`.

The orbit is thus trapped in the finite integer interval

\[
[b,N_L(b)].
\]

It must stabilize after finitely many strict increases. The terminal state is a common fixed point of all `N_(p_i)`, hence a perfect `L`-th power. Since it lies above `b`, minimality of `N_L(b)` forces equality. ∎

No global `WellFoundedGT N_0` assumption is used.

## 11. P024-S3-T07 — Stable collapse and stable boundary maps form one adjoint pair

Status: `PROVED`.

For every `L>=1`,

\[
\boxed{
N_L(b)\le n
\iff
b\le C_L(n).
}
\]

Therefore

\[
\boxed{N_L\dashv C_L.}
\]

The stable forward and boundary dynamics are not merely symmetric descriptions. They are the two sides of one Galois connection selecting the nearest common fixed state above/below.

For the exponent word of T06,

\[
\boxed{
\operatorname{stab}(W)=C_L,
\qquad
\operatorname{coStab}(\Lambda)=N_L.
}
\]

This is the exact P019/P024 bridge.

## 12. P024-S3-T08 — Transient boundary-word order can differ while the stable map agrees

Status: `PROVED BY EXPLICIT WITNESS`.

Take exponents `2` and `3`, initial boundary `b=2`, and compare the two repeated boundary words.

One order gives

\[
2\to9\to36\to64,
\]

while the other gives

\[
2\to8\to27\to64.
\]

So transient boundary dynamics are genuinely order-sensitive.

Yet

\[
L=\operatorname{lcm}(2,3)=6
\]

and both stabilize to

\[
\boxed{N_6(2)=64.}
\]

This is the upward counterpart of P019's distinction between transient word action and stable lcm-controlled behavior.

## 13. P024-S3-T09 — Stable boundary-word equivalence is the same lcm join structure

Status: `PROVED`.

For every nonempty collapse-boundary exponent word, T06 shows that its stabilized boundary map is exactly `N_L`, where `L` is the lcm of the exponents appearing in the word.

If two words have the same `L`, their stable boundary maps are identical.

Conversely, if `L!=K`, then

\[
N_L(2)=2^L
\]

and

\[
N_K(2)=2^K,
\]

which are distinct. Hence

\[
\boxed{
N_L=N_K
\iff
L=K.
}
\]

Therefore collapse-boundary words modulo stable equivalence are indexed by the same positive-integer lcm classes as P019 forward collapse words.

Concatenating words unions their exponent requirements, so the stable class combines by

\[
\boxed{L\vee K=\operatorname{lcm}(L,K).}
\]

Thus the forward and boundary stable-equivalence semigroups have the same lcm join-semilattice invariant, with representatives `C_L` and `N_L` forming an adjoint pair.

This does not claim that lcm semilattices or closure/interior duality are new mathematics.

## 14. P024-S3-T10 — Stable pair is an interior/closure pair on the same fixed skeleton

Status: `PROVED`.

For every `L>=1`:

- `C_L` is monotone, reductive and idempotent;
- `N_L` is monotone, extensive and idempotent;
- both have exactly the perfect `L`-th powers as fixed points;
- `N_L ⊣ C_L`.

So the same finite-information skeleton of perfect `L`-th-power states supports two canonical selectors:

\[
\boxed{
\text{nearest fixed state above}
\quad\dashv\quad
\text{nearest fixed state below}.
}
\]

P024 interprets the upper selector as stable future-boundary pullback and P019 interprets the lower selector as stable forward collapse.

The closure/interior language itself is established order theory and remains prior art.

## 15. Executable and formal audit

Formalization:

- `EnterpriseMath/Order/AdjointReductiveDuality.lean`

Lean checks:

- reductive right adjoint -> extensive left adjoint;
- equality of fixed-point sets;
- finite upward stabilization under `WellFoundedGT`;
- `coStabilize` fixed-point selection, monotonicity and idempotence;
- stabilized Galois connection `coStabilize(l) ⊣ stabilize(u)` when both order directions satisfy the corresponding well-founded hypotheses.

Executable regression:

- `tests/test_p024_adjoint_stabilization_dual.py`

Independent pre-document pressure tests included:

1. all monotone reductive right-adjoint maps on finite chains of sizes 1 through 5;
2. thousands of fixed words of length up to three on those chains;
3. all tested non-chain finite posets with a fixed topological labelling through four elements, including every available reductive right-adjoint pair and short word family;
4. collapse exponent families `(2,3)`, `(3,2)`, `(2,4)`, `(4,6)`, `(2,3,5)`, `(3,4,6)` and others over hundreds of boundaries;
5. direct bounded verification of `N_L(b)<=n iff b<=C_L(n)`.

No counterexample was found in those audit domains. The abstract T01–T04 statements are additionally Lean-checked; the `N_0` local-bounded specialization T06–T10 uses the ordinary proofs above rather than pretending that `N_0` satisfies `WellFoundedGT`.

## 16. Prior-art and novelty boundary

The following are established mathematics and are not claimed as Enterprise Math inventions:

- Galois connections and composition of adjoints;
- closure/interior operators and fixed-point characterizations;
- well-founded finite stabilization patterns;
- lcm classification of common perfect-power fixed points;
- order duality.

P008, P019, P020, and the existing source records already cover the relevant structural neighbors.

The project-specific result under test is the integrated interpretation

\[
\boxed{
\text{forward reductive right-adjoint dynamics}
\longleftrightarrow
\text{extensive future-boundary pullback}
\longrightarrow
\text{nearest-fixed stable adjoint pair},
}
\]

and the exact identification of P019's stable collapse map `C_L` with P024's stable boundary partner `N_L`.

Historical novelty remains `NOVELTY_UNVERIFIED`.

## 17. Next questions

1. replace the global `WellFoundedGT` sufficient condition by a reusable local bounded-orbit theorem general enough to cover `N_0` without specializing to perfect powers;
2. formalize the collapse-specific `N_L ⊣ C_L` and local bounded stabilization in Lean;
3. combine Supplement 01's score-lattice guard geometry with Supplement 02/03's nonlinear adjoint score evolution;
4. study boundary-orbit merger counts as action-language compression without conflating them with historical irreversibility `M_t`;
5. determine when stable adjoint pairs commute with precision projection across P018's divisibility lattice.
