# ADDMUL Valuation–Tropical Collapse Geometry — Research Return

Task: `RS-ADDMUL-VALUATION-TROPICAL-COLLAPSE-GEOMETRY`  
Publication: `TP2-74B996CDCB92B54E82B8`  
Researcher-ID: `EM-AMTROP-A5-5D91C4`  
Claim: `chatgpt-amtrop-a5-20260830-5d91c4`  
Status: `SUCCESS / RETURN_FROZEN_FOR_DRIVER_REVIEW`  
Hard target: `VALUATION_PLUS_CANCELLATION_GEOMETRY_CLASSIFIED / UNIT_DATA_REQUIRED_FOR_OPERATION_SAFETY`

No Working Truth, Foundation, canonical-promotion, or novelty claim is made.

## 1. Exact single-prime classification

Use `v_p(0)=∞`. For `(x,y)!=(0,0)`, define `kappa_p(x,y)=∞` when `x+y=0`, and otherwise

`kappa_p(x,y) = v_p(x+y) - min(v_p(x),v_p(y))`.

For `(0,0)`, `∞-∞` is undefined and remains a separate `ZERO_ZERO / BASELINE_INFINITY` type.

For nonzero `x=p^a u`, `y=p^b w` with p-units `u,w`:

1. If `a!=b`, then `v_p(x+y)=min(a,b)` and `kappa_p=0`.
2. If `a=b=m` and `u!=-w`, then `kappa_p=v_p(u+w)`.
3. Finite `kappa_p=k>=1` iff `u == -w (mod p^k)` but not modulo `p^(k+1)`.
4. `kappa_p=0` iff `u+w` is nonzero modulo p.
5. If `u=-w`, then `x+y=0` and `kappa_p=∞`.
6. One zero input plus one nonzero input has `kappa_p=0`.
7. For p=2, tied nonzero units are odd, so finite tied cancellation always has `kappa_2>=1`. For odd p, tied depth zero is possible.
8. Depth is unbounded at fixed input valuations: `x=1`, `y=p^k-1` has `v_p(x)=v_p(y)=0` and `kappa_p=k`; `y=-1` gives exact cancellation.

Thus positive cancellation depth lives exactly on the tied-valuation wall, but its height is controlled by normalized unit/residue data rather than valuation alone.

## 2. Valuation-vector geometry and information loss

For nonzero integer n, let `V(n)=(v_p(n))_{p prime}`. It has finite support.

- On positive integers, full `V` is injective by unique factorization.
- On signed nonzero integers, `V` loses exactly sign.
- Zero must be typed separately.
- Multiplication is exact vector addition: `V(xy)=V(x)+V(y)`.

For `x+y!=0`, define `M_p=min(v_p(x),v_p(y))` and `K_p=kappa_p(x,y)`. Then

`V(x+y)=M(x,y)+K(x,y)`.

`M` is the tropical/min skeleton; `K` is the deterministic excess. Positive K can be created at a prime dividing neither input: `1+2=3` has tied 3-adic baseline zero and output excess one.

Information loss:

| State | Multiplication | Ordinary addition | Lost data |
|---|---|---|---|
| one `v_p` | exact additive | min plus unresolved tie | normalized p-unit/residue |
| full `V`, positive integers | exact and injective | globally reconstructible, not coordinate-local | none globally |
| full `V`, signed integers | exact additive | sign-sensitive | sign |
| finite prime window | exact coordinate addition | not single-valued | sign, outside-window cofactor, unit residue |

The structural distinction is `GLOBAL_RECONSTRUCTIBILITY != LOCAL_OPERATION_SAFETY`.

## 3. Finite-window no-descent theorem

For finite prime set S, define `pi_S(n)=(v_p(n))_{p in S}`. Multiplication descends exactly:

`pi_S(xy)=pi_S(x)+pi_S(y)`.

Ordinary addition does not descend to a deterministic operation on this window.

For any prescribed finite depths `k_p` (with the tied 2-adic restriction `k_2>=1`), CRT constructs a unit y such that every input coordinate is zero,

`v_p(1)=v_p(y)=0` for all `p in S`,

while independently forcing `kappa_p(1,y)=k_p`.

For `k_p>=1`, impose `y = p^k_p - 1 (mod p^(k_p+1))`; for odd p with `k_p=0`, impose `y=1 (mod p)`. The prime-power moduli are pairwise coprime.

Exact witnesses:

- `y=649`: `(kappa_2,kappa_3,kappa_5)=(1,0,2)`;
- `y=791`: `(3,2,0)`;
- `y=261659999`: `(kappa_2,kappa_3,kappa_5,kappa_7)=(5,1,4,2)`.

Therefore finite valuation windows do not determine K. Operation-safe finite addition must add residue/leading-unit information or accept set-valued output.

## 4. Finite residue precision law

Suppose tied normalized p-units u,w are known modulo `p^D`, and set `k=v_p(u+w)`.

- If `k<D`, D-digit residue data determines k exactly.
- After dividing the sum by `p^k`, the normalized output unit is determined only modulo `p^(D-k)`.
- If `u+w=0 (mod p^D)`, the finite state knows only `kappa_p>=D` (or exact cancellation) and must refine.

Hence, when `kappa_p<D`:

`remaining_unit_precision = D - kappa_p`.

A depth-k cancellation consumes exactly k digits of normalized unit precision. A fixed-depth valuation+residue state is not closed under unrestricted tied addition at fixed precision; an operation-safe version needs dynamic refinement or an explicit `OVERFLOW / DEPTH_AT_LEAST_D` state.

## 5. Multi-term sums: coherence and path dependence

For a block A of leaves, define

- `S_A = sum_{i in A} x_i`,
- `mu_A = min_{i in A} v_p(x_i)`,
- `E_A = v_p(S_A)-mu_A` when `S_A!=0`,
- `E_A=∞` when `S_A=0` and `mu_A` is finite.

At a merge `A|B`, put `h_A=mu_A+E_A`, `h_B=mu_B+E_B`, and `kappa_AB=kappa_p(S_A,S_B)`.

For a nonzero parent:

`E_(A union B) = tau(A,B) + kappa_AB`

with

`tau(A,B) = min(h_A,h_B) - min(mu_A,mu_B)`.

Thus `tau` transports/survives inherited cancellation height, while `kappa` generates new cancellation at the current tie.

If `mu_A<mu_B` and `d=mu_B-mu_A`, then `tau=min(E_A,d+E_B)`. If `mu_A=mu_B`, then `tau=min(E_A,E_B)`.

The root invariant

`E_root = v_p(sum_i x_i) - min_i v_p(x_i)`

is bracketing-independent. The local kappa ledger is not:

- at p=2, `(1,1,1,3)` has root excess 1, but different bracketings give finite-local-kappa totals 2 or 3;
- `(1,-1,2)` has one bracketing passing through exact zero and another avoiding it, while both end at total 2 with root excess 1.

Therefore `SUM_LOCAL_KAPPA != GENUINE_HOLONOMY`. With full transport state and residue data, the `tau+kappa` recurrence is coherent by associativity. Apparent path defects are projection/presentation artifacts.

## 6. Tool reuse and prior-art boundary

`src/enterprise_math/precision_holonomy.py` is reused conceptually: it already enforces the pattern

`direct_defect = lower_defect + transported_upper_defect`

and staged/direct coherence. The valuation recurrence deliberately follows the same generation-versus-transport separation. Reuse resolution: `COMPOSE_APPLIED`.

The executable is not sufficient unchanged because this task needs typed infinity, min-gated transport, tie walls, normalized p-unit residues, exact-cancellation branches, and residue-depth overflow. `weighted_relation_field.py` is `NOT_APPLICABLE` to the nonlinear min/tie/unit mechanism. No new global tool family is claimed; method harvest is `RESULT_ONLY`.

External-theory boundary: generalized tropical hyperfields already formalize valuation addition as multivalued (unequal valuations select the minimum; equal valuations allow higher values), and enriched/fine valuations already retain sign/leading/residue information. Sources consulted were *Valuations on Structures More General Than Fields* and *Geometry of tropical extensions of hyperfields*. This return claims neither construction as new.

Task-local value is the exact integer kappa selection calculus, CRT finite-window no-descent witness, finite-depth precision-consumption law, and the separation of root coherence from local-ledger path dependence.

## 7. Exact regression

Checker: `research_checks/ADDMUL_VALUATION_TROPICAL_COLLAPSE_GEOMETRY_CHECK_20260830.py`  
Certificate: `research_artifacts/ADDMUL_VALUATION_TROPICAL_COLLAPSE_GEOMETRY/exact_regression_certificate.json`

`PASS / 476360 exact checks`

- single-p classification: `186240`
- vector/product and min+K laws: `164480`
- finite-residue precision budget: `125520`
- tree/root coherence: `66`
- arbitrary-depth + CRT witnesses: `54`

No floating point, random sampling, or p-adic completion is used.

## 8. Final disposition

Closed: single-p kappa classification including zero/infinity; exact multiplication translation; information-loss classification; tropical skeleton+excess; finite-window addition no-descent; finite-depth precision law; multi-sum transport/generation recurrence; root coherence versus presentation dependence; precision-holonomy reuse boundary.

Unresolved only as a possible successor: carry a residue-depth budget at each active prime and test whether dynamic refinement composes across long operation sequences without reconstructing the whole integer.

Terminal recommendation: `Driver review as VALUATION_PLUS_CANCELLATION_GEOMETRY_CLASSIFIED, with UNIT_DATA_REQUIRED_FOR_OPERATION_SAFETY retained as an explicit boundary.`
