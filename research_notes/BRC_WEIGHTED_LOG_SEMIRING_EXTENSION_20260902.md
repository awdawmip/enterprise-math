# BRC Weighted / Log-Semiring Extension — 2026-09-02

Status: `RESEARCH CANDIDATE / FINITE-DAG THEOREM LAYER PROVED / NO R023 MUTATION / NO TOOL PROMOTION`

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Baseline: `main@2fc50ba0823a02bd213bba4fe89d7446957dc34a`

## 0. Executive result

The logarithm runtime opened a stronger structural route than merely evaluating `LN` and `LOG`.

For weighted branching, propagation along one path is multiplicative while recoalescence of alternative paths is additive. Therefore the natural carrier is a semiring. In logarithmic coordinates these two operations become

```text
path propagation:      ell1 tensor ell2 = ell1 + ell2
branch recoalescence:  ell1 oplus ell2 = log(exp(ell1) + exp(ell2))
```

with additive zero `-infinity` and multiplicative identity `0`.

The main result of this note is that ordinary Boolean-support BRC is an exact projection of this weighted layer precisely when the weight semiring has two zero-structure properties:

1. no additive cancellation to zero (`zerosumfree`);
2. no multiplicative zero divisors.

This gives an exact mathematical reason why non-negative probability/weight semantics can refine Boolean BRC while signed/amplitude cancellation cannot be smuggled into the same support projection.

A second exact result is that for `k` equal positive incoming branches of log weight `ell`, recoalescence produces

```text
LSE(ell, ..., ell) = ell + ln(k).
```

Thus `ln(k)` is the exact multiplicity surplus erased when Boolean BRC idempotently identifies all positive incoming support with one support bit.

## 1. Scope and hard boundary

This note does **not** modify the canonical R023 Boolean-support theorem family. It defines a candidate weighted lift above it.

The finite theorem surface here is restricted to:

- finite directed acyclic branch graphs;
- explicitly declared edge weights;
- semiring-valued propagation and recoalescence;
- exact Booleanization conditions;
- the non-negative and logarithmic specializations.

Cycles, infinite path sums, signed amplitudes, complex phases, destructive interference, normalization by hidden measures, and continuum limits require separate typing.

## 2. Tool-reuse resolution

Relevant current Enterprise tools were checked before constructing the candidate calculus.

### T0_BRC

- coverage verdict: `EXTEND_EXISTING_TOOL`
- reuse state: `EXTEND_EXISTING_TOOL`
- applied content: support/result branch semantics and the hard rule that erased provenance/weight may not be inferred from Boolean support.
- exact gap: T0 deliberately has no multiplicity or weight carrier.

### T12_IDEMPOTENT_PATH_CLOSURE_BELLMAN

- coverage verdict: `REUSE_EXISTING_TOOL + EXACT_SCOPE_GAP`
- reuse state: `REUSE_APPLIED`
- applied content: semiring-valued path composition and the fixed-length path expansion law.
- exact gap: T12 is explicitly idempotent and computes path envelopes. Weighted BRC needs non-idempotent additive recoalescence because `a oplus a != a` is exactly where multiplicity survives.

### T8_RELATION_OBSERVABLE_SPECTRUM / weighted_relation_field

- coverage verdict: `NOT_SAME_SEMANTIC_CARRIER`
- reuse state: `REUSE_APPLIED_FOR_BOUNDARY_ONLY`
- boundary: the existing weighted relation field is a capacity-weighted antisymmetric relation-state construction `Z_ij=m_j*c_i-m_i*c_j`. It is not a path-sum/recoalescence weight algebra.

Conclusion: the residue is a narrow extension of BRC/path algebra, not a new unrelated global tool family.

## 3. Weighted BRC carrier

Let

```text
K = (K, oplus, tensor, 0_K, 1_K)
```

be a nontrivial semiring. Addition is commutative and associative; multiplication is associative; multiplication distributes over addition; `0_K` is additive identity and multiplicatively absorbing; `1_K` is multiplicative identity.

Let `G=(V,E)` be a finite DAG with source `s`, and let every edge carry an explicit weight

```text
w : E -> K.
```

For a path

```text
p = e1 ... em
```

define its path weight

```text
W(p) = w(e1) tensor ... tensor w(em).
```

For a vertex `v`, define the total branch weight

```text
B(v) = oplus_{p:s->v} W(p).
```

This is the candidate `WEIGHTED_BRC` state at `v`.

## 4. WBR-1 — finite-DAG path-sum / recoalescence theorem

**Claim.** The local recurrence

```text
B(s) = 1_K
B(v) = oplus_{e:u->v} B(u) tensor w(e)
```

is equal to the explicit sum of all source-to-`v` path weights.

**Status:** `PROVED / CLASSICAL SEMIRING PATH EXPANSION / BRC SPECIALIZATION`.

**Proof.** Topologically order the DAG. For the source the empty path has weight `1_K`. Assume the claim for all predecessors of `v`. Substitution gives

```text
B(v)
 = oplus_{e:u->v} (oplus_{p:s->u} W(p)) tensor w(e)
 = oplus_{e:u->v} oplus_{p:s->u} (W(p) tensor w(e)),
```

by distributivity. Every path to `v` has a unique last edge, so these terms are exactly all source-to-`v` paths once each.

Consequences:

- branch regrouping is harmless;
- recoalescence may occur locally or only at the terminal result;
- parenthesization/order of alternative-branch merging does not change the value;
- no idempotence assumption is needed for the finite path-sum theorem.

## 5. WBR-2 — exact characterization of Booleanizable weight semirings

Let the Boolean semiring be

```text
B = ({0,1}, OR, AND, 0, 1).
```

For nontrivial `K`, define the support map

```text
sigma(a) = 0  iff a = 0_K,
sigma(a) = 1  otherwise.
```

Definitions:

- `K` is **zerosumfree** if `a oplus b = 0_K` implies `a=b=0_K`.
- `K` has **no zero divisors** if `a tensor b = 0_K` implies `a=0_K` or `b=0_K`.

**Theorem.** `sigma : K -> B` is a semiring homomorphism **iff** `K` is zerosumfree and has no zero divisors.

**Proof, sufficiency.**

For addition, if both inputs are zero then the sum is zero. If at least one is nonzero, zerosumfreeness says the sum cannot be zero. Hence

```text
sigma(a oplus b) = sigma(a) OR sigma(b).
```

For multiplication, absorbing zero handles the case where either factor is zero, while absence of zero divisors handles the case where both are nonzero. Hence

```text
sigma(a tensor b) = sigma(a) AND sigma(b).
```

**Proof, necessity.**

If `sigma` preserves addition and `a oplus b=0_K`, then

```text
0 = sigma(a oplus b) = sigma(a) OR sigma(b),
```

so `a=b=0_K`. If `sigma` preserves multiplication and `a tensor b=0_K`, then

```text
0 = sigma(a tensor b) = sigma(a) AND sigma(b),
```

so at least one factor is zero.

Thus the two zero-structure conditions are necessary and sufficient.

## 6. WBR-3 — Boolean BRC as an exact homomorphic image

Assume the hypotheses of WBR-2.

Apply `sigma` to every edge weight and evaluate the same DAG in the Boolean semiring. Then for every vertex `v`,

```text
sigma(B_K(v)) = B_Boolean(v).
```

**Status:** `PROVED`.

Reason: WBR-1 expresses `B_K(v)` as a finite sum of finite products; a semiring homomorphism commutes with every such expression.

Therefore Boolean-support BRC can be viewed as a genuine forgetful projection of weighted BRC on this admissible class. It does not reconstruct the discarded weights; it only commutes with evaluation in the forward direction.

## 7. Admissible and inadmissible specializations

### 7.1 Natural counts

`K = N` with ordinary `+` and `*` is zerosumfree and has no zero divisors.

Here `B(v)` literally counts weighted path multiplicity when all edge weights are `1`. Booleanization remembers only whether that count is zero.

### 7.2 Non-negative rational/real weights

`Q_{>=0}` and `R_{>=0}` satisfy the two conditions. Probability weights therefore admit the Boolean support projection as long as all probability semantics are explicitly declared and no signed cancellation is introduced.

### 7.3 Signed weights fail

Over integers,

```text
1 + (-1) = 0.
```

Two supported incoming branches can cancel to zero. Therefore support does not preserve recoalescence:

```text
sigma(1 + (-1)) = 0
but
sigma(1) OR sigma(-1) = 1.
```

This is exactly why signed/amplitude cancellation cannot be represented by the current Boolean BRC projection.

### 7.4 Zero divisors fail

In `Z/6Z`,

```text
2 * 3 = 0 mod 6
```

although both factors are nonzero. Support therefore fails to preserve path propagation.

## 8. WBR-4 — logarithmic semiring lift

Let

```text
L = R union {-infinity}.
```

Define

```text
a oplus_L b = log(exp(a)+exp(b))
a tensor_L b = a+b
0_L = -infinity
1_L = 0.
```

Extend exponential by `Exp(-infinity)=0`.

Then

```text
Exp : L -> R_{>=0}
```

is a semiring isomorphism:

```text
Exp(a oplus_L b) = Exp(a)+Exp(b)
Exp(a tensor_L b) = Exp(a)Exp(b).
```

Therefore logarithmic weighted BRC is not an approximation. It is the same non-negative weighted BRC written in multiplicative-to-additive coordinates.

The Booleanization map is simply

```text
sigma_L(ell)=0 iff ell=-infinity,
sigma_L(ell)=1 otherwise.
```

and WBR-3 applies.

## 9. Exact rational operational subcarrier

For the current Enterprise runtime, the strongest exact implementation route does **not** repeatedly evaluate `exp` and `log`.

Carry a non-negative rational mass symbolically as the existing unreduced `DIV(n,d)` state.

For masses `a,b`:

```text
propagate: MASS(a) tensor MASS(b) = MASS(a*b)
recoalesce: MASS(a) oplus MASS(b) = MASS(a+b)
Booleanize: support(MASS(a)) = (a != 0)
```

Only when a log-coordinate readout is actually requested:

```text
MASS(a), a>0 -> LN(a)
MASS(0)       -> -infinity / unreachable marker
```

and the existing BRC logarithm interval runtime can materialize the finite-scale `LN` readout.

This means weighted-log BRC can remain exact over rational masses without evaluating a transcendental function at every branch or merge.

## 10. WBR-5 — equal-branch multiplicity surplus is exactly ln(k)

Suppose `k>=1` incoming branches all have the same positive linear weight `a`, hence common log weight

```text
ell = ln(a).
```

Recoalescence gives total mass `ka`, therefore

```text
LSE(ell,...,ell)
 = ln(ka)
 = ell + ln(k).
```

Define the local recoalescence surplus relative to the strongest incoming branch as

```text
Delta = LSE(ell_1,...,ell_k) - max_i ell_i.
```

For equal branches,

```text
Delta = ln(k).
```

Thus `ln(k)` is an exact branch-multiplicity coordinate.

Boolean BRC sends every positive incoming collection to the same support value `1`; it necessarily erases this surplus.

## 11. WBR-6 — general surplus bounds and effective branch count

For positive incoming weights `w_1,...,w_k`, let

```text
W = sum_i w_i
M = max_i w_i
ell_i = ln(w_i).
```

Then

```text
Delta = ln(W) - ln(M) = ln(W/M).
```

Since

```text
M <= W <= kM,
```

we obtain

```text
0 <= Delta <= ln(k).
```

Moreover:

- `Delta=ln(k)` iff all `k` positive weights equal `M`;
- `Delta=0` iff exactly one incoming branch has positive weight.

Define

```text
N_eff = exp(Delta) = W/M.
```

Then

```text
1 <= N_eff <= k.
```

`N_eff` is an exact effective branch count relative to the strongest branch.

If incoming shares are normalized as `p_i=w_i/W`, then

```text
Delta = -ln(max_i p_i).
```

So the recoalescence surplus is exactly the local min-entropy of the normalized incoming branch distribution. This is an identity, not a claim that Boolean BRC itself stores entropy.

## 12. Exact checker evidence

The companion checker `experiments/brc_weighted_log_semiring_check.py` performs exact integer/rational arithmetic only.

On the complete 4-vertex DAG with the six forward edges, it exhausts all

```text
{0, 1/2, 1, 2}^6
```

edge-weight assignments: `4096` cases.

For every case it verifies:

1. local recoalescence recurrence equals explicit source-to-target path sum;
2. non-negative rational weighted support equals Boolean reachability support.

It also contains explicit witnesses for:

- signed additive cancellation;
- multiplicative zero-divisor failure modulo 6;
- equal-branch mass multiplication and surplus bounds at the pre-log exact-rational level.

## 13. What this changes about the log/ln direction

The previous runtime result said:

```text
LN/LOG may be materialized through a BRC exact interval certificate.
```

The present result is stronger structurally:

```text
BRC branch multiplication
    -> log turns propagation into addition
BRC branch recoalescence
    -> log turns addition into LSE
Boolean support
    -> exact homomorphic quotient when zero cancellation and zero divisors are absent
multiplicity of equal branches
    -> exact additive surplus ln(k).
```

So `ln` is not merely another arithmetic readout. It is a coordinate in which weighted branch propagation becomes additive while recoalescence retains multiplicity through `log-sum-exp`.

## 14. Next research frontier

The next justified stage is not to mutate R023. It is to test a separately typed finite `WEIGHTED_BRC` carrier with:

1. exact non-negative rational mass states;
2. local path propagation and recoalescence traces;
3. Boolean projection certificate;
4. optional `LN` readout through the already-merged BRC logarithm runtime;
5. explicit refusal of signed/cancelling carriers.

Only after that operational layer survives regression and dedup should a Driver decide whether the weighted lift deserves a stable Enterprise interface or remains a research-only domain facade.
