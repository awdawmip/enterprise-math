# R4-EC11 — Exact rank 14 of bit-resolved affine BRC, versus 13 for the aggregate sequence

**Status:** author-side theorem / exact computational certificates / unreviewed research draft. **Date:** 2026-10-25. **Parent:** R4-EC10, immutable commit `26e041da71e577bbfa476c76f9701b67397b48e7`. The object here is the ordered, positive-unit-mass binary affine BRC **auxiliary model**, not P000's native X6 dynamics.

## I. Precisely declared model and observational strength

An initial state `(q,r,e,k)=(0,0,+1,0)` receives a word over letters 0 and 1. Control `q∈{0,1,2}`; provenance `r=0` means no 00 and previous letter nonzero/empty, `r=1` means no 00 and previous letter 0, and `r=2` means 00 has occurred. Affine orientation `e∈{+1,-1}` and displacement k evolve by `(e',k')=(eta e,eta k+b)` with exactly these original positive-branch edges:

| q | letter 0: (q',eta,b) | letter 1: (q',eta,b) |
|:-:|:-:|:-:|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

For a letter 1, `r' = 0` unless previously dirty (`r=2`), and for letter 0, `r'=1` from 0, `r'=2` from 1 or 2. Put `t=e k` so `t'-t=e'b`. Work over the Laurent rational field `K=Q(z)`. Among the 14 reachable fine states `(q,r,e)`, let `T_0,T_1 ∈ Mat_14(K)` record each chosen letter by one monomial edge weight `z^(e'b)`. The initial fine-state column is `v` and the `12×14` readout `C` combines only clean r=0/1 into `c=0` while dirty r=2 goes to c=1, keeping q and e. For every **specified** word `w=a_1...a_n`, the word-resolved Laurent vector is `F(w)=C T_(a_n)...T_(a_1) v`, preserving all grades t and hence the full effect `(e,k=e t)`. Future operations are **arbitrary chosen binary suffixes**, not just the sum of all 2^n words.

## II. Theorem: exact minimum word-resolved linear dimension is 14

A K-linear bit-labelled realization has dimension d and fixed matrices `A_0,A_1`, input column b and observation matrix D with `D A_w b = F(w)` **for every finite binary word**, including empty. The original fine-state model gives d≤14. We now prove d≥14 by an explicit exact Hankel determinant, allowing arbitrary (even signed) K-matrix entries in the comparator.

Sort states `(q,r,e)` lexicographically, with e=-1 before +1. The 14 prefix words in this exact order reach the indicated state and Laurent grade t:

| (q,r,e) | prefix | t |
|---|---|---:|
| (0,0,-) | 0101 | 2 |
| (0,0,+) | empty | 0 |
| (0,2,-) | 001 | 1 |
| (0,2,+) | 000 | -1 |
| (1,1,-) | 010 | 1 |
| (1,1,+) | 10 | 0 |
| (1,2,-) | 00 | 0 |
| (1,2,+) | 00010 | -1 |
| (2,0,-) | 01 | 2 |
| (2,0,+) | 1 | -1 |
| (2,1,-) | 0 | 1 |
| (2,1,+) | 01010 | 1 |
| (2,2,-) | 0000 | 0 |
| (2,2,+) | 0001 | -2 |

Therefore the reachability columns `R=[T_w v]` are a monomial-permutation matrix, and direct inversion parity with the displayed order gives the **exact identity** `det R=z^3`.

Choose 14 suffix/output rows: the 12 empty-suffix observers `(q,c,e)` in lexicographic q,c,e order, and then two **one-letter suffix 0** observers of `(q'=1,c'=0,e'=-1)` and `(q'=1,c'=0,e'=+1)`. Their fine-state observation matrix is

`O=[ C ; (C T_0)_(1,clean,-) ; (C T_0)_(1,clean,+) ]`.

Only the two fine states `(q=2,r=0,e)` and `(q=2,r=1,e)` are identified by the 12-row C. A suffix 0 sends the former to `(q'=1,clean,e)` with weight `z^e`, while the latter becomes dirty. The 2×2 residual blocks therefore separate them. With the exact row and column ordering above, elementary elimination gives `det O=1`.

Now take the 14×14 Hankel submatrix `H[(suffix, output), prefix]=[F(prefix·suffix)]_(output)`. Its exact factorization `H=OR` yields

**`det H = det(O) det(R) = z^3 ≠ 0 ∈ Q(z)`.**

Any d-state labelled realization must factor this H through dimension d, so d≥14. Combined with the original 14-state construction:

**`d_min(bit-labelled full-effect linear realizations) = 14.`**

This is a theorem for every word, proved by an exact finite symbolic determinant, not extrapolation from a finite search.

## III. Aggregate Krylov restriction is not bit-invariant

R4-EC10 proved that, for `T=T_0+T_1`, the **aggregate** vector time series `C T^n v` has minimum dimension 13 over Q(z), via an invariant Krylov space `V=span_K(v,Tv,...,T^12v)`. This subspace is T-invariant, but it is **not** T_0-invariant. Indeed, set

`B=[v, Tv, ..., T^12v, T_0 v]`, a 14×14 Laurent-polynomial matrix. At `z=2` modulo prime `1000003` exact elimination returns

**`det B(2) ≡ 520642 (mod 1000003) ≠ 0.`**

Because Laurent evaluation at z=2 is legal over this field, the original determinant cannot vanish identically over Q(z). Hence `T_0v∉V`. The incompatibility is already visible after the first selected input letter, and directly excludes interpreting the particular R4-EC10 13-dimensional *aggregate Krylov compression* as a per-bit invariant positive BRC path representation.

This is strictly stronger than merely noting that the aggregate and word-resolved models have different readouts: it locates a concrete edge-splitting failure and supplies an exact prime-field certificate.

## IV. Arithmetic, reuse, and limitations

The reproducible author-side `R4_EC11_verify.py` performs breadth-first exact fine-state reachability, verifies the two symbolic determinants `det O=1`, `det R=z^3`, checks `H=OR` from actual word transitions, and verifies the independent 14×14 finite-field obstruction `520642`. Python 3 + SymPy run: **PASS**. No floating point, π, classical trigonometric propagation, or untyped replacement for original BRC branch semantics.

BRC reuse: **COMPOSE_APPLIED** to R4-EC9/10's original positive ordered path carrier, full affine effect and provenance channel. K-linear elimination is an *analysis tool*; intermediate signed coefficients do not stand for negative underlying path masses.

**Important non-implication:** The 14-state lower bound requires preserving *every chosen input word*. It **does not** solve the separate effect-blind **positive, time-homogeneous aggregated** six-versus-seven control-state problem when only `Σ_(|w|=n)F(w)` and an effect-aware terminal decoder are required. That stricter aggregate question remains at `6 ≤ d_min ≤ 7`. Nor is this a statement about P000's six-dimensional discrete spatial axes, the three-dimensional research slice, native heartbeat time, or physical residuals: no X6 embedding, native transfer map, or R193 source-port/time correspondence was established.

## V. Authority and next research unit

Global Knowledge frozen source `main@51635e308eef1fb67e834c580595fa880f4fd45d`, P000 `ACTIVE_LOCKED` original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matching startup projection, ACTIVE worldview; Enterprise Math source `main@5ee544fdddd7817716721c67f3faec42ebff4151`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, and immutable parent R4-EC10 commit `26e041da71e577bbfa476c76f9701b67397b48e7`.

GitHub authenticated user: `awdawmip`. Native dispatch returned `CONTROL_QUOTA`; native `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. Active Owner and winning CLAIM could not be verified. This is **author-side research on a draft branch**, not a Source-signed Result or independent Driver review.

**Next smallest genuinely open unit (R4-EC12 candidate):** derive a constraint that applies to **effect-fiber-aggregated**, fixed-effect-blind six-state positive homogeneous transitions *without* presuming bit-labelled word preservation. Either construct such a six-state representation or produce an invariant/counterexample that truly rules out arbitrary six-state internal recodings. Preserve R193/native X6 source-port and time calibration as separate pending tasks.
