# BRC Weighted Multiplicity Tower — 2026-09-02

Status: `RESEARCH CANDIDATE / EXACT FINITE-PATH COMPARISON THEOREMS / NO TOOL PROMOTION`

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Parent result: `research_notes/BRC_WEIGHTED_LOG_SEMIRING_EXTENSION_20260902.md`

## 0. Main result

The weighted-BRC candidate admits three simultaneous semiring evaluations of the same supported path family:

```text
C = supported path count
M = strongest single-path mass
W = total path mass
```

or, in log coordinates,

```text
C = count-semiring result
T = ln(M) = max-plus result
L = ln(W) = log-sum-exp result.
```

For every reachable finite target,

```text
M <= W <= C*M
```

and therefore

```text
T <= L <= T + ln(C).
```

Define

```text
E = W/M
Delta = ln(E) = L-T.
```

Then

```text
1 <= E <= C
0 <= Delta <= ln(C).
```

This creates a precise bridge between:

- Boolean BRC: whether `C>0`;
- natural-count BRC: exact supported path multiplicity `C`;
- T12 max-plus path evaluation: dominant-path coordinate `T`;
- weighted/log BRC: total log mass `L`;
- BRC LN runtime: exact finite-scale materialization of `Delta=ln(E)` when masses are rational.

The comparison does **not** claim that max-plus is a quotient homomorphism of log-sum-exp. It is a separate idempotent evaluation of the same path family, related by an exact inequality and a tropical limit.

## 1. Finite path setup

Let `P(v)` be the finite set of supported source-to-target paths at a vertex `v`. Every path `p` has positive mass

```text
w_p > 0.
```

Define

```text
C(v) = |P(v)|
W(v) = sum_{p in P(v)} w_p
M(v) = max_{p in P(v)} w_p.
```

If `P(v)` is empty, Boolean support is false, `C(v)=0`, and both weighted and max-path masses are zero. The logarithmic coordinates are then typed as unreachable / `-infinity`, not as `LN(0)`.

## 2. WBT-1 — three-semiring sandwich theorem

For reachable `v`, every supported path satisfies

```text
0 < w_p <= M(v).
```

At least one path attains `M(v)`, so

```text
M(v) <= W(v).
```

There are exactly `C(v)` positive summands, each at most `M(v)`, so

```text
W(v) <= C(v) * M(v).
```

Hence

```text
M(v) <= W(v) <= C(v)M(v).
```

Taking natural logarithms gives

```text
ln M(v) <= ln W(v) <= ln M(v) + ln C(v).
```

Set

```text
T(v)=ln M(v)
L(v)=ln W(v).
```

Then

```text
T(v) <= L(v) <= T(v)+ln C(v).
```

**Status:** `PROVED / ELEMENTARY / ENTERPRISE BRC-T12 BRIDGE`.

## 3. Equality conditions

For reachable `v`:

```text
W(v)=M(v)
```

iff there is exactly one supported path. Because every supported path mass is strictly positive, any second path makes the sum strictly larger than the maximum.

Also

```text
W(v)=C(v)M(v)
```

iff every supported path has mass `M(v)`.

Therefore

```text
Delta(v)=0       iff C(v)=1,
Delta(v)=ln C(v) iff all supported paths have equal mass.
```

This sharpens the earlier equal-branch identity `Delta=ln(k)` from one local merge to the entire source-to-target path family.

## 4. Effective multiplicity

Define the exact rational/pre-log quantity

```text
E(v)=W(v)/M(v).
```

Then

```text
1 <= E(v) <= C(v).
```

`E(v)` is an effective path multiplicity measured relative to the strongest path. It is not required to be an integer.

Examples:

```text
path masses (1/6,1/6,1/6):
C=3, W=1/2, M=1/6, E=3, Delta=ln 3.

path masses (1/2,1/4):
C=2, W=3/4, M=1/2, E=3/2, Delta=ln(3/2).
```

For exact non-negative rational masses, `E` can be constructed as an unreduced `DIV` carrier by cross multiplication; no numerical division is needed. Only final `Delta` materialization needs the already-existing BRC `LN` runtime.

## 5. WBT-2 — local multiplicity transport law

Suppose target `v` has incoming supported edges `e:u->v` with edge mass `a_e>0`.

For each predecessor define

```text
W_u = total path mass to u
M_u = strongest path mass to u
E_u = W_u/M_u.
```

The strongest path reaching `v` through edge `e` has candidate mass

```text
m_e = M_u * a_e.
```

Let

```text
M_v = max_e m_e.
```

The total mass arriving through `e` is

```text
W_u*a_e = E_u*m_e.
```

Therefore

```text
W_v = sum_e E_u*m_e
```

and dividing by `M_v` gives the exact transport law

```text
E_v = sum_e E_u * (m_e/M_v).
```

Each coefficient satisfies

```text
0 < m_e/M_v <= 1.
```

In log form, with

```text
Delta_u = ln E_u
r_e = ln m_e - ln M_v <= 0,
```

we get

```text
Delta_v = logsumexp_e(Delta_u + r_e).
```

So multiplicity accumulated inside predecessor subgraphs is transported forward as an additive log bonus, then recoalesced by one further `log-sum-exp`.

**Status:** `PROVED / EXACT ALGEBRAIC REWRITE`.

## 6. WBT-3 — count bound by local induction

The supported path count obeys

```text
C_v = sum_e C_u
```

for incoming supported edges, because every path to `v` has a unique final edge.

Assume inductively

```text
E_u <= C_u.
```

Using WBT-2 and `m_e/M_v <= 1`,

```text
E_v
 = sum_e E_u*(m_e/M_v)
 <= sum_e E_u
 <= sum_e C_u
 = C_v.
```

Thus the global bound `E_v<=C_v` also has a purely local BRC/recoalescence proof.

## 7. WBT-4 — beta/tropical bridge to T12

Let each supported path have log weight

```text
ell_p = ln w_p.
```

For `beta>0`, define

```text
L_beta = (1/beta) * ln(sum_p exp(beta*ell_p)).
```

Let

```text
T = max_p ell_p
C = number of supported paths.
```

Factoring out the maximum gives

```text
L_beta
 = T + (1/beta) * ln(sum_p exp(beta*(ell_p-T))).
```

Every exponent in the remaining sum lies in `(0,1]`, with at least one equal to `1`. Hence

```text
1 <= sum_p exp(beta*(ell_p-T)) <= C,
```

so

```text
T <= L_beta <= T + ln(C)/beta.
```

Therefore

```text
lim_{beta->infinity} L_beta = T.
```

The `beta->infinity` limit is the max-plus/T12 dominant-path evaluation. At `beta=1` it is the ordinary weighted-log BRC total.

This establishes a controlled tropical bridge rather than an exact semiring quotient:

```text
log-sum weighted BRC --beta->infinity--> max-plus T12.
```

The approximation error is certified by

```text
0 <= L_beta-T <= ln(C)/beta.
```

## 8. Exact pre-log form of the beta bound

For positive integer `beta`, the same statement can be checked without any logarithm:

```text
M^beta <= sum_p w_p^beta <= C*M^beta.
```

This is suitable for exact rational regression. Natural logarithms are required only to express the final coordinate gap.

## 9. Information interpretation and boundary

Normalize supported path masses by

```text
q_p = w_p/W.
```

Then

```text
max_p q_p = M/W = 1/E,
```

so

```text
Delta = ln E = -ln(max_p q_p).
```

Thus `Delta` equals the min-entropy of the normalized path distribution.

This identity does **not** mean Boolean BRC stores entropy. Boolean BRC retains only whether `C>0`; the entire value of `Delta` is discarded by support projection.

It also does not make `Delta` monotone under arbitrary branch insertion. Example:

```text
weights (1,1):       E=2,       Delta=ln 2
weights (1,1,100):   E=102/100, Delta=ln(1.02).
```

Adding a new overwhelmingly dominant branch can reduce the surplus because the reference maximum changes. If a newly added branch does not exceed the existing maximum, then `M` stays fixed while `W` rises, so `Delta` strictly increases.

This is a required boundary for using `Delta` as a BRC diagnostic.

## 10. Operational consequence

A finite exact rational Weighted-BRC evaluator can compute the four coordinates

```text
B(v) = Boolean support
C(v) = supported path count
W(v) = total rational mass
M(v) = strongest rational path mass
```

using only integer arithmetic on unreduced rational carriers.

Then it derives

```text
E(v)=W(v)/M(v)
Delta(v)=LN(E(v)).
```

The current BRC logarithm runtime materializes `Delta` only when a finite-scale readout is requested.

This provides an exact operational bridge:

```text
T0 Boolean support
+ natural count
+ T12 max-product/max-plus path evaluator
+ non-idempotent weighted sum-product
+ existing BRC LN materialization
-> typed multiplicity-surplus trace.
```

No float `log-sum-exp` primitive is required.

## 11. Next falsification target

The next useful question is whether the tuple

```text
(B,C,W,M,E,Delta)
```

has a minimal closed local state under graph composition, or whether some components are redundant once exact rational masses and path counts are present.

In particular, test:

1. whether `(C,W,M)` is the minimal exact pre-log local carrier needed to recover all six quantities;
2. how quotienting/recoalescing graph states affects `M` when provenance is erased too early;
3. whether a safe weighted quotient criterion can be stated as a T6-style operation-safe quotient preserving `(W,M,C)` rather than only Boolean support.
