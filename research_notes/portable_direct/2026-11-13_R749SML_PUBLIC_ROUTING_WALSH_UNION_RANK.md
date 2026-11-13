# R749SML — Exact Walsh-union rank under publicly observable random routing

Date: 2026-11-13 (Asia/Shanghai). Continuation of R749SMG–R749SMK, with predecessor R749SMK at `c237ff17bf36b7ea7434ec6ad62922ad06039768`. Frozen scientific input remains `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Author-side abstract signed-source observer theorem, not an admitted native V29/V39 Cell/Link/Port event or a Foundation result. Independent review pending.

## Finite observer model and exact result

Let source `x in (F_2)^d`; each `a in (F_2)^d` names the Walsh source relation `chi_a(x)=(-1)^(a·x)`. A source-independent routing coin publicly reveals `B=b` from a finite nonempty set with `q_b>0`, `sum_b q_b=1`. Conditional on `B=b`, the controller queries the fixed finite list of named source parity indices `a_{b,1},...,a_{b,m_b}`. It emits binary outputs `Y_j in {-1,+1}` through conditionally independent sign channels:
```
P(Y_j=y | x,B=b) = (1 + lambda_{b,j} y chi_{a_{b,j}}(x))/2,
lambda_{b,j} in [-1,1].
```
The complete public observation is `(B,Y_1,...,Y_{m_B})`. Let `W_b=span_F2{a_{b,j}:lambda_{b,j} != 0}`, including the zero vector, and let `K` be the full finite likelihood matrix with rows indexed by complete public outcomes and columns by `x`.

**Theorem (public-route Walsh-union rank).** For every finite choice of parameters above,
```
rank_R(K) = | union_{b:q_b>0} W_b |,
c_min = | union_b W_b | - 1.
```
Here `c_min` is the smallest number of independent affine expectation coordinates sufficient to recover the full public-observation probability distribution for **every** source prior on `(F_2)^d`. It is a full-prior, specified-one-experiment sufficiency statement, not unrestricted future controller sufficiency. For two branches, with `r_i=dim W_i` and `r_12=dim(W_1 intersection W_2)`,
```
rank(K)=2^r1+2^r2-2^r12.
```
For arbitrary finite routing sets inclusion-exclusion gives
```
rank(K) = sum_{empty != J subset routes} (-1)^(|J|+1) 2^(dim intersection_{b in J} W_b).
```
The rank is therefore piecewise constant in the channel parameters: the only local rank change occurs when an informative channel crosses `lambda=0` (subject to fixed route support and query indices). A deterministic sign reversal `lambda=-1` retains the parity mode.

## Proof

For each fixed public branch `b` and subset `S subset {1,...,m_b}`, conditional independence yields
```
E[product_{j in S} Y_j | x,B=b]
 = (product_{j in S} lambda_{b,j}) chi_{xor_{j in S} a_{b,j}}(x).
```
The Walsh transform on the **reported output list** `Y` is invertible, even for deterministic or fully random coordinates. Thus the real span of rows `K(b,y|x)=q_b P(y|x,b)`, as functions of `x`, equals the span of exactly the Walsh characters `chi_a` with `a in W_b`: every output moment with a zero bias is identically zero, and every `a in W_b` is obtained by multiplying a subset of nonzero-bias output coordinates. Positive `q_b` changes only nonzero scalings. Taking the span over observed public branches produces the union of their Walsh character lists. Distinct Walsh characters on the full source population are orthogonal and linearly independent, establishing the first formula. The constant character `chi_0=1` is in the row span because `sum_{b,y} K(b,y|x)=1`. On the full simplex of source priors, the resulting affine image has dimension `rank(K)-1`; any affine-statistic reconstruction must retain at least this many independent coordinates, while the expectations of the nonconstant characters in the union attain the bound. The intersection and inclusion-exclusion identities follow by finite-set cardinality. QED.

## Concrete examples and a scope-sensitive information-loss witness

(1) Two equiprobable *public* branches respectively query only `chi_e1` and `chi_e2`, both with `lambda=1/2`. Then `W_1={0,e1}`, `W_2={0,e2}` and `rank(K)=3` (two independent source moments). This extends the non-power-of-two rank-three phenomenon in R749SMG, without claiming identical native update semantics.

(2) With three source bits, branch 1 queries `e1,e2` and branch 2 queries `e2,e3`, all nonzero biases. Then `W_1={0,e1,e2,e1+e2}` and `W_2={0,e2,e3,e2+e3}`, so `rank(K)=4+4-2=6` and `c_min=5`. Erasing the branch-1 `e2` channel lowers the rank to `2+4-1=5`.

(3) If the branch from example (1) is **not observed**, its two one-bit output distributions are mixed; the row span is only `span{1,chi_e1+chi_e2}`, of rank 2. Public routing information is a provenance coordinate even though the route coin itself is source-independent.

(4) Let `d=2`, and define two strictly positive source priors with `eta=1/2`: `mu_plus=eta*Uniform+(1-eta)*Uniform({00,11})` and `mu_minus=eta*Uniform+(1-eta)*Uniform({01,10})`. Both have zero marginal means for `chi_e1,chi_e2`, but `E_plus[chi_(e1+e2)]=1/2` and `E_minus[chi_(e1+e2)]=-1/2`. Hence public routing of the single-bit queries (1) is identical under these priors. If the allowed future experiment instead makes **both** parity queries in one run with independent nonzero biases `lambda_1=lambda_2=1/2`, the rank rises to 4 and the total-variation distance between the two complete output laws is exactly `1/8`. This is an explicit scope-typed residual: the joint source mode `chi_(e1+e2)` may be dropped for experiment (1), but must be retained for the expanded future language.

## Exact validation, reuse, and next scientific dependency

Companion Python `Fraction` checker builds the full source-column likelihood matrices, computes exact rational rank by Gauss–Jordan elimination, compares it with the GF(2) Walsh-subspace union, checks column normalization, and computes the strict-positive-prior witness. It actually returned **PASS** on 248 cases (five targeted cases and all 243 combinations of two coordinate-parity queries, three rational noise biases per branch, and three positive route probabilities). The hidden/public rank pair was 2/3, and the two-query strict-positive-prior total variation was 1/8. The arbitrary-finite theorem follows from the proof, not the grid. Files: `R749SML_PUBLIC_ROUTING_WALSH_UNION_EXACT_CHECK.py`, `R749SML_PUBLIC_ROUTING_WALSH_UNION_RESULTS.json`.

Scientific status: new abstract observer lemma, exact author-side proof and finite exact regression; independent scientific review pending. Preserves P000, native 6D basis, named signed provenance, and joint-relation observer-fidelity rule. The Walsh mode union is **not** the linear span of all queried GF(2) masks: two independent branch-local one-bit queries have union size 3, but their algebraic generated subspace has size 4, with the missing joint mode exposed by example (4).

Next: compute the minimal Walsh carrier for a controller whose *later routing decisions depend on noisy earlier public signals*, rather than one initial independent public route, and test a separately permitted actual V29/V39 signed-Port event with its named provenance. Do not infer an actual native event correspondence from this abstract probability model.
