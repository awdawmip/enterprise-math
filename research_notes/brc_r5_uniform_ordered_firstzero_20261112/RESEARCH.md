# R5 — Uniformly legal *ordered* first-zero witnesses at every fixed capacity

Date: 2026-11-12 (Asia/Shanghai). Status: exact finite author-side computation and proof for the frozen external 28-coordinate P/Q–BRC Blackwell auxiliary transport model. This does **not** assert a native X6 or physical interpretation, or formal Source acceptance.

## Scientific lineage and frozen input

The immutable original 15-operation fixture is Enterprise Math commit `435e77af0d180eac32bd1f9c4c464bc4010b7551`, path `research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`. The 1,144 fixed capacities and earlier aggregate-subset certificates are in Draft PR #2130 at `0bb04a83ddcaededda0e5970e9b5ea865dc5e194`; their exact all-parameter spectrum and 2,909-chamber event sweep are at Draft PR #2139 (`0db2aa81587b0ec7e70cfb7404cf016f70eeb8b5`) and #2143 (`337bf8771943a7ebe09b89b31667c79f9a851796`).

Science pins from the earlier R5 line: global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Those are original scientific inputs, not current behavioral-policy snapshots.

Write the 15 labeled operation vectors as `M_a`, define the integer vector `P_S=36*sum_(a in S) M_a`, and let `k0=(target0,source3)`. The fixed integer coordinate weights of the 15 operations are:

```
(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80).
```

Let `x=X[k0]=155682221/25142124560000000`, `X(r)=X+x*r*H`, `L=-427508577031693280/628800490619`, `U=1/23`, and `I=[L,U]`. For each of the 1,144 distinct values

```
N = {-P_S[k0] : S subset of {1,...,15}, P_S[k0] <= -3}
T_n = 36*x/n, n in N,
```

we consider the actual ordered-prefix legality condition

```
X(r) + eps * sum_(a in prefix) M_a >= 0 coordinatewise
```

for every prefix of a *single ordering*, every real `r in I`, and every `0 <= eps <= T_n`.

## Theorem — all 1,144 capacities have a single uniformly legal ordered prefix

For every `n in N` there exists a subset `S_n` and one ordering of its **distinct labeled operations** such that:

1. `1 <= |S_n| <= 9`;
2. every ordered intermediate prefix is nonnegative in all 28 coordinates, **simultaneously for all real** `r in I` and all `0 <= eps <= T_n`;
3. at `eps=T_n` the complete prefix has mass zero in coordinate `k0`.

The minimum possible operation count among such uniformly legal ordered witnesses, classified by `n`, is:

| Minimum steps | Number of n |
|---:|---:|
| 1 | 5 |
| 2 | 41 |
| 3 | 153 |
| 4 | 319 |
| 5 | 326 |
| 6 | 180 |
| 7 | 86 |
| 8 | 29 |
| 9 | 5 |
| **Total** | **1,144** |

The five requiring exactly nine operations are `n=818,1030,1046,1061,1178`. There is no 10-step requirement in this frozen fixture.

Across the 32,768 labeled masks, precisely **13,371** mask/capacity pairs have an aggregate endpoint-feasible subset at their associated `T_n`. Of these, precisely **12,672** admit an ordering uniformly legal on `I`. Thus **699** are endpoint-feasible *but not uniformly orderable*. Eighty `n` have exactly one orderable mask (which may have more than one valid ordering).

## Exact recurrence and complete finite certificate

For a mask `S`, let `P_S` denote its full 28-dimensional integral sum. Write `B_{e,k}=X[k]+x*e*H[k]` for `e in {L,U}`.

For each mask define a capped integer demand `c(S)`: the maximum of zero and the ceilings of all coordinatewise lower bounds on **positive** integers `n` needed to satisfy

```
B_{e,k} + (x/n) P_S[k] >= 0
for all e in {L,U}, k=0,...,27.
```

Set `c(S)=1349` if no positive integer `n<=1348` satisfies the conditions. The value `c(S)=0` is a harmless no-negative-coordinate sentinel: for every positive `n`, the inequalities hold if and only if `n>=c(S)`. Explicitly, over every negative `P_S[k]`, take the ceiling of `-x*P_S[k]/B_{e,k}`; a zero base and negative change require the sentinel 1349. Positive coordinate changes pose no constraint. Set `c(empty)=0`.

For each mask define the minimum bottleneck demand among **all** labeled operation permutations:

```
b(empty)=0,
b(S)=max(c(S), min_(a in S) b(S \ {a})).
```

The recurrence is exact by partitioning possible permutations according to their last operation. The recorded minimizer yields an actual ordered prefix. A given mask `S` with `-P_S[k0]=n` admits an ordered uniform witness if and only if `b(S) <= n`. All masks are considered, so minimizing `|S|` within the feasible class is an exact finite optimum.

The verifier independently reconstructs the minimizing operation order for one optimal mask at each of the 1,144 `n`, then checks **all** its intermediate prefix vectors using exact rational inequalities at both parameter endpoints. Each coordinate condition is affine in `r`; it therefore holds on the entire real interval `I`. At any `eps` between zero and `T_n`, each intermediate prefix vector is the convex interpolation of the initial nonnegative vector and the verified vector at `T_n`. This proves the two universal parameter quantifiers.

The earlier aggregate witness lemma used subset endpoint legality. The new bottleneck recurrence resolves the additional order-realizability obligation: endpoint legality alone does not guarantee an ordered legal execution.

## Small explicit obstruction

For mask `1025=2^0+2^10` (atoms #1 and #11), `P_S[k0]=-84`. At `n=84`, the completed two-operation subset is nonnegative at both parameter endpoints: `c(1025)=84`. However, atom #1 on its own violates a required endpoint constraint (its `c=1349` sentinel), and atom #11 alone requires `c(1024)=420`. Hence `b(1025)=420>84`; neither order is uniformly legal at `T_84`. Other masks still furnish legal witnesses for `n=84`.

## Verification and evidence

The attached standalone verifier `VERIFY_R5_UNIFORM_ORDERED_WITNESSES.py` reconstructs the full frozen 28-vector `X`, 15 operations, observation-preserving `H`, and interval endpoints directly from exact integer and rational literals. It enumerates all `2^15` labeled masks, evaluates every required coordinate at `L,U`, executes the complete minimax-subset DP, constructs all 1,144 optimal witnesses, and rechecks their exact ordered prefix inequalities.

Author-side executable: Python 3 standard library, `fractions.Fraction`, no floating-point arithmetic and no external dependency. Exact observed output is in `EXACT_OUTPUT.txt`. No claim is made that another independent reviewer has already reproduced the remote GitHub bytes.

This is BRC residual-path work retaining the full 28-coordinate carrier and source/target labels. The `k0` weight supplies the target value, while all 28 coordinates constrain intermediate legality. In particular it is *not* a quotient to the integer subset-sum alone.

## Reusable method and next question

The threshold demand `c(S)` plus minimax recurrence `b(S)` is an exact finite-algorithm template for observer-preserving transport fibers with affine hidden-state uncertainty. For general `m` labeled operations and `d` coordinates, computing all subset vectors costs `O(d 2^m)` arithmetic operations, evaluating endpoint capacity demands costs `O(d 2^m)`, and the naive predecessor DP costs `O(m 2^m)`. These are arithmetic-operation bounds for exact rationals; actual bit complexity also depends on input numerator/denominator sizes and rational reductions. No general subexponential claim is made.

Next: attach the chosen ordered witness and its 28-coordinate endpoint-margin certificate to each of the 3,432 fixed/moving crossing pairs, audit at collision boundaries, and analyze whether a dominance/antichain compression can compute the bottleneck witnesses without all `2^m` masks on larger transport fibers. Formal Source Result intake and independent audit of both this derivation and its inherited two-coordinate reduction remain separate tasks.
