# R269 — Exact affine–time closure of 63 labelled modular source profiles

Date: 2026-11-18. Status: **AUTHOR_PROVED / EXACT_FINITE_RECURRENCE_CERTIFICATE / NOT_REVIEWED**. Model: **fixed auxiliary positive-rational seven-source scalar observer**, not native typed BRC. Scientific input **frozen at** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Provenance and precise problem

Continue R268 [`5ffd245c3d26e62b4584b16073002777b7b20b08:research_notes/portable_direct/R268_EXACT_RESIDUE_PROFILE_REFINEMENT_20261118.md`] without modifying its definitions. Let `q_m(n)=q(m,n+3) mod 13` for all 63 original labelled masks `0<=m<63` and `n>=0`, with the rational initialization, integer recurrence, and common verified period `L=2184` of R268. R268 has **25 distinct entire value profiles**, classified by the first two residues.

The 25-profile family is not necessarily closed under the following declared **auxiliary readout operations**:
- `T_t q(n)=q(n+t)` (time/event shift, with `t` modulo 2184);
- `A_c q(n)=q(n)+c mod 13` (`c` in `F_13`).

Find the smallest set of exact 2184-periodic value functions containing the original 25 and closed under both operations. Count it exactly, classify its orbits and quantify its flat-index information cost. Source label/port/branch data are **not** quotientable by this computation.

## Theorem 1 — Affine–time orbit classification

Let `F=` the set of 25 distinct original functions, `G=C_2184 x F_13` act by `(t,c).q(n)=q(n+t)+c`, and `Cl_G(F)` be the union of their orbits. Then

```
|F| = 25
|Cl_time(F)| = 522
|Cl_translation(F)| = 325
|Cl_G(F)| = 6474
number of G-orbits meeting F = 13.
```

The exact 13 orbits meeting the original source family are:

| least original mask | masks representing original profiles in this orbit | minimal derivative period d | full orbit size 13d |
|---:|---|---:|---:|
| 0 | 0 | 1 | 13 |
| 9 | 9,14,29,41,46,61 | 168 | 2184 |
| 10 | 10,25,30,42,57 | 6 | 78 |
| 12 | 12,44 | 21 | 273 |
| 13 | 13 | 12 | 156 |
| 15 | 15,47 | 28 | 364 |
| 24 | 24 | 12 | 156 |
| 26 | 26 | 26 | 338 |
| 27 | 27,59 | 168 | 2184 |
| 45 | 45 | 12 | 156 |
| 56 | 56 | 12 | 156 |
| 58 | 58 | 26 | 338 |
| 62 | 62 | 6 | 78 |
| **Total** | **25 distinct original profiles** | — | **6474** |

The 39 labels with identically zero profiles all represent the single original profile indexed by mask 0; they have not become 39 independent profiles in this table.

**Consequences for fixed-width indices.** An explicit flat code of all distinct observation functions needs `ceil(log2 N)` bits: 5 for the original 25, 10 for the shift-only 522, 9 for translation-only 325, and **13 for the full 6474 closure**. These are *full-function identifiers under this specified observer interface*, not costs of original mask identities, branch history, event counters, ports, transition tables, or BRC computation.

## Theorem 2 — First differences are a complete affine–time orbit invariant

For any `L`-periodic sequence `q:Z/LZ -> F_p` define

```
(Dq)(n) = q(n+1)-q(n) mod p.
```

Two periodic value sequences `u,v` lie in the same orbit under **time shifts and constant translations** iff the derivative sequences `Du,Dv` lie in the same cyclic time-shift orbit. In particular, if `d` is the smallest positive period of `Dq`, its affine–time orbit has **exactly `p d` elements**, including when a shift by `d` introduces a nonzero additive drift.

**Proof.** Both `D(A_c q)=Dq` and `D(T_t q)=T_t Dq`. Conversely, if `Dv=T_t Du`, then `D(v-T_t u)=0`; adjacent differences of that function vanish, so it is constant on the cyclic index set. Thus `v=T_t u+c`. The derivative of an affine orbit has exactly `d` shifted patterns, and above each pattern are exactly `p` functions differing by a constant; they are distinct. This proves the orbit formula and sufficiency. It uses no unproved classification of the specific R268 model.

For the R268 fixed instance, one complete finite residue period and all divisors of 2184 determine each derivative period `d`. The 13 different cyclic derivative orbits give the table in Theorem 1 and the sum 6474.

## Two explicit all-future relations

The exact modular recurrence certifies, for **every integer `n>=0`**:

```
q_14(n) = q_9(n+56)                 (mod 13)
q_57(n) = q_10(n+1) + 4             (mod 13).
```

These clarify why *distinct source profiles* may belong to the same enlarged affine–time orbit. They do not identify the underlying source labels, history, or ports.

The same original profile is also shared by masks 0 and 1: `q_0(n)=q_1(n)=0` for all `n`. If an enriched typed interface later admits an operation depending on an original label bit, these two states must be retained as distinct unless the operation is shown fiber-constant. No claim is made that such a label-bit operation is an already admitted native BRC operator.

## Theorem 3 — Minimality and typed descent boundary

For the *closed value-function population* `Cl_G(F)`, permit all shifted translated zero tests `Q_{t,c}(q)=[q(t)+c=0]`. Any two different functions are distinguished: choose an event `t` where their values differ and let `c` cancel only the first. Hence equality of exact value functions is the **coarsest** quotient preserving all these tests: the 6474-state count and its 13-bit flat code lower bound are sharp for this declared closed population.

For a richer typed carrier `S=(label,port,branch_history,value_profile,...)`, write `h:S->Cl_G(F)`. A deterministic typed operator `U:S->S` descends to a value-only operator iff

```
h(x)=h(y)  =>  h(U(x))=h(U(y))
```

for every pair in the actual population. This fiber-congruence condition for every admitted generator, along with observer factorization, is necessary and sufficient for all finite compositions, by induction on the operator word. Thus **13 bits is not a native typed state lower bound or an upper bound on a provenance-preserving implementation**; it applies to the auxiliary closed value interface only. The original label, path and port stay separately typed until the relevant BRC descent certificate is supplied, respecting P000 and the joint-relation observer preservation rule.

## Exact reproducible evidence and independent finite coverage

Reproduction file: `R269_affine_time_closure_certificate.py`. It embeds the exact R268 model and reconstructs all 63 sequences using `Fraction` rational initialization followed by monic integer recurrences. It checks the R268 recurrence period using **all d_m initial shifted positions**, with `sum_m d_m=249`, hence every 2184-position comparison extends to all future events. It then partitions the 25 original profiles by cyclic derivatives, determines minimal periods by exhaustive divisors, and separately **enumerates actual transformed 2184-byte vectors**, verifying each orbit is disjoint and has exactly `13d` members. Two additional direct enumerations independently verify 522 time-only and 325 translation-only functions; both displayed all-future identities are checked on a complete period and inherited by recurrence.

A separate local implementation of the same integer recurrence and direct closure returned `PASS`: 13 orbits, 6474 functions; 17 shift-only classes, 522 functions; 25 translation-only classes, 325 functions. Its exact JSON SHA-256 is `fc0749138a1fbb10f09bf577b629163f9bab2a4e5be95ab79eee2396180311f2`. This local digest identifies **that local output**, not the byte-identical content of the alternative published reproduction script's output.

All arithmetic here is rational-exact or modular-integer; no floating tolerance, probabilistic test or native dynamics simulation is used. Mathematical independent review and native BRC semantic transfer remain **NOT_REVIEWED / NOT_ESTABLISHED**.

## Next executable questions

1. Extend the operator language by an **actual defined** source-typed port/branch update from the existing recurrent BRC foundation, then compute or prove its `h`-fiber congruence (or give a concrete native counterexample). Do not assume the auxiliary affine translations are native operations.
2. For a costed implementation, compare a flat 13-bit class ID and a factored orbit+phase+offset representation, counting the original label, branch/port fields, event phase, lookup tables and decoding. A class-count reduction alone is not a speedup.
3. Revisit the `13^2` modulus: the R260A example demonstrates lost mod13 sufficiency at higher precision, so perform a separately scoped prime-power descent check rather than extrapolating R269.

Preserve existing R268/R267 provenance, P000, immutable scientific pin, independent review, and Source CLAIM/owner boundaries. No shared-task Result or native CLAIM is asserted by this research note.
