# Enterprise Math — Critical Multiplicity Orbit Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION ADDENDUM / MAIN-BACKED / INTEGER CRITICAL AUTOMATON`
Effective: `2026-09-03`
Parent: `ENTERPRISE_BRC_CRITICAL_DEGENERACY_FOUNDATION_20260903.md`
Theorem ledger: `ENTERPRISE_BRC_CRITICAL_ORBIT_THEOREM_LEDGER_20260903.json`

## 1. Purpose

This addendum freezes the main-backed consequences of PRs #1173 and #1174 for the integer critical-degeneracy matrix `K` produced by `WBRC-T39`.

Finite directed-multigraph word growth, Perron growth, shifts of finite type, dynamical zeta functions, primitive periodic-orbit Möbius inversion and Euler products are classical/general mathematics. No generic novelty claim is made.

The Enterprise/BRC content is the typed identification of those classical structures with **dominant branch multiplicity that survives the large-moment/tropical limit** of the explicit positive-rational histogram carrier.

## 2. Critical multiplicity automaton

For each tropical critical edge `i->j`, `K_ij` is the exact number of explicit branches tied at the dominant weight in that cell; noncritical entries are zero.

Expand `K_ij=d` into `d` parallel branch symbols. The resulting finite directed multigraph is the **critical multiplicity automaton**.

For every `n>=0`,

\[
\boxed{(K^n)_{ij}=\#\{\text{length-n critical dominant branch words }i\to j\}.}
\]

Define

\[
B_n=\mathbf1^TK^n\mathbf1,
\qquad
T_n=\operatorname{tr}(K^n).
\]

Then `B_n` is the total length-`n` critical dominant-word count and `T_n` is the based closed-word count. Because `K` is finite nonnegative and recurrent,

\[
\boxed{\Gamma_{\rm crit}=\ln\rho(K)=\lim_{n\to\infty}\frac1n\ln B_n.}
\]

This unifies

\[
\boxed{\ln d\longrightarrow \frac1r\ln D\longrightarrow\ln\rho(K)}
\]

for one dominant tie, one critical circuit, and a general critical multigraph.

Canonical ID: `WBRC-T43`.

## 3. Exact rational gauge invariance

For a positive rational vertex gauge

\[
q'_{ij,\alpha}=q_{ij,\alpha}\frac{h_j}{h_i},
\]

all parallel branches in one cell receive the same factor, so the dominant tie set and `d_ij` are unchanged. Every cycle product telescopes, so tropical critical cycles and critical edges are unchanged. Therefore

\[
\boxed{K'=K}
\]

exactly, not merely up to similarity.

Hence every `K`-derived observable is already a rational-gauge quotient:

\[
B_n,\ T_n,\ p_K(z),\ z_c,\ \Gamma_{\rm crit}.
\]

The zero-correction law `WBRC-T42` becomes: `Gamma_crit=0` iff the critical multiplicity automaton is a disjoint union of unit-multiplicity directed cycles; equivalently `B_n` is bounded (constant for `n>=1` on the recurrent-state carrier).

## 4. Finite recurrence and critical multiplicity zeta

The integer polynomial

\[
p_K(z)=\det(I-zK)
\]

finitely encodes the infinite critical word-count sequences. Every matrix entry of `K^n`, `B_n`, and `T_n` satisfies the integer Cayley-Hamilton recurrence corresponding to

\[
\det(\lambda I-K)=\lambda^N p_K(1/\lambda).
\]

Define

\[
\boxed{Z_{\rm crit}(z)=\frac1{p_K(z)}}.
\]

Formally,

\[
\boxed{\ln Z_{\rm crit}(z)=\sum_{n\ge1}\frac{T_n}{n}z^n}
\]

and equivalently

\[
\boxed{-z\frac{p_K'(z)}{p_K(z)}=\sum_{n\ge1}T_nz^n.}
\]

The smallest positive root remains `z_c=1/rho(K)`, so `Gamma_crit=-ln z_c` as in `WBRC-T41`.

## 5. Primitive periodic critical branch orbits

A closed edge-labeled critical branch word is **primitive** if it is not a proper power of a shorter closed word. Cyclic shifts of one primitive word define one primitive periodic orbit.

Let

\[
P_n=\#\{\text{primitive periodic critical branch orbits of exact length }n\}.
\]

Each primitive orbit of length `d` contributes its `d` choices of base point to `T_n` whenever `d|n`, hence

\[
\boxed{T_n=\sum_{d\mid n}dP_d}
\]

and Möbius inversion gives

\[
\boxed{P_n=\frac1n\sum_{d\mid n}\mu(d)T_{n/d}\in\mathbf N_0.}
\]

The critical zeta has the exact formal Euler product

\[
\boxed{Z_{\rm crit}(z)=\prod_{n\ge1}(1-z^n)^{-P_n}.}
\]

Every coefficient through order `z^N` uses only `P_1,...,P_N`; the entire infinite inventory is finitely represented through `p_K`.

Canonical ID: `WBRC-T44`.

## 6. Zero and positive residual growth

If `Gamma_crit=0`, the critical automaton is a finite disjoint union of unit cycles. Then the primitive inventory has finite support: one primitive orbit for each component cycle at that component's length.

If `Gamma_crit>0`, then `rho(K)>1` and the critical automaton has exponentially proliferating dominant words; its primitive periodic-orbit inventory is infinite. The exact critical radius remains encoded by the smallest positive root of `p_K` rather than by enumerating the full inventory.

## 7. Semantic boundaries

Freeze:

```text
CRITICAL_MULTIPLICITY_AUTOMATON = INTEGER_K
CRITICAL_WORD_COUNT_n = SUM_ENTRIES(K^n)
CRITICAL_RESIDUAL_GROWTH = LN(RHO(K))
PRIMITIVE_PERIODIC_ORBIT_COUNT = P_n
T_n = SUM_{d|n} d P_d
Z_CRIT = PRODUCT_n (1-z^n)^(-P_n)
RATIONAL_VERTEX_GAUGE -> K_AND_P_n_INVARIANT_EXACTLY
PRIMITIVE_PERIODIC_ORBIT != WBRC_T29_SIMPLE_SUPPORT_CIRCUIT
CRITICAL_RESIDUAL_GROWTH != SHANNON_ENTROPY_CLAIM
P_n != ARITHMETIC_PRIME_COUNT
```

`WBRC-T29` concerns Möbius-primitive subsets of a finite declared feedback-event universe and produces simple support circuits. `WBRC-T44` concerns arbitrary-length primitive periodic edge-words in the already condensed critical automaton. They are distinct typed objects.

The Euler-product form is a classical dynamical-zeta structure; it is not an arithmetic-prime Euler product and does not claim a new generic zeta theorem.

Canonical negative IDs: `WBRC-N23`, `WBRC-N24`, `WBRC-N25`.

## 8. Tool routing

No new top-level family is created. A companion T0 subtool

`t0.weighted_brc_critical_orbits` -> `src/enterprise_math/brc_critical_orbits.py`

consumes the canonical integer `K` and provides exact finite-prefix total/closed word counts, primitive periodic-orbit counts, determinant-zeta coefficients and verified Euler-product coefficients. The parent `t0.weighted_brc_critical_degeneracy` remains responsible for constructing `K` and its critical-log selector.

## 9. Validation evidence

Main-backed PR #1173 exact checker:

- 11,626 critical-graph matrices;
- 139,512 Cayley-Hamilton scalar checks;
- 81,382 zeta-trace checks;
- 11,812 zero-structure checks;
- rational gauge `K'=K` checks.

Main-backed PR #1174 exact checker:

- 93,008 primitive-integrality checks;
- 93,008 Möbius inversion checks;
- 104,634 Euler-product coefficient checks;
- 36 direct edge-labeled periodic-orbit enumeration checks;
- rational-gauge primitive-inventory checks.
