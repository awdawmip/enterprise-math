# Two-Stage Witness Descent Across Precision

Status: `RESEARCH BRIDGE / NONCANONICAL`

Coefficient branch mixing and the profinite ghost separate two logically different descent problems:

1. **Does a local/unlabelled state carry a coherent witness label across precision?**
2. **Once one witness label is fixed, do its compatible finite states descend to an exact state?**

These require different hypotheses.

## 1. Labelled branch family

Let an exact world law be a union of labelled branches

`P(x) = OR_(lambda in Lambda) P_lambda(x)`.

For a declared precision level M define the branch-support set

`S_M = {lambda in Lambda : branch P_lambda has a local solution at precision M}`.

When N refines M and every N-solution reduces to an M-solution,

`S_N subseteq S_M`.

So increasing precision can remove witness labels but cannot create a label that was impossible at a coarser reduction.

## 2. Local branch reflection is the first guard

An unlabelled quotient law is **branch-reflecting** at precision M if local solvability of the quotient law implies

`S_M != empty`.

The strongest form says the quotient solution set is literally the union of the labelled branch solution sets.

This guard can fail before any inverse limit is considered.

For the ghost product polynomial at modulus15, the product equation has a solution, but all three labelled square branches are unsolvable mod15. Hence branch reflection already fails at one finite joint precision.

## 3. Directed precision is the second structural ingredient

Let the experiment family be ordered by refinement. Require it to be **finitely directed**:

> every finite collection of declared precisions has another declared precision refining all of them.

For ordinary modular precision this means the family contains, or can semantically evaluate at, a common multiple/lcm refinement.

Examples:

- all positive moduli: directed by lcm;
- one ladder `R,R^2,...`: directed by taking the larger exponent;
- all prime moduli once: **not** directed under lcm, because the joint refinement of two distinct primes is composite and leaves the family.

Prime-local branch safety therefore does not by itself imply cross-prime witness coherence.

## 4. Finite witness theorem

Assume:

1. Lambda is finite;
2. the precision family is finitely directed;
3. branch supports descend under refinement;
4. the unlabelled law is branch-reflecting at every declared joint precision;
5. the unlabelled law is locally solvable at every declared precision.

Then

`intersection_M S_M != empty`.

Hence one fixed label `lambda_*` is locally solvable at every precision.

### Blocker proof

Suppose no label survives all precisions. For every lambda choose one blocker precision `M_lambda` with `lambda notin S_(M_lambda)`.

Because Lambda is finite and precision is directed, choose one joint refinement L of all `M_lambda`.

Refinement monotonicity gives

`S_L subseteq intersection_lambda S_(M_lambda)`,

so every label is absent and `S_L=empty`.

But local solvability plus branch reflection requires `S_L!=empty`, contradiction.

For ordinary moduli, L is simply the lcm of the blocker moduli.

## 5. The ghost exposes the first guard at modulus15

For branches

`x^2=13`, `x^2=17`, `x^2=221`,

one blocker per label is

`13 -> mod5`,

`17 -> mod3`,

`221 -> mod3`.

Their lcm is15.

At mod15 every labelled branch is blocked, yet the unlabelled product polynomial has root `x=1`.

Thus the failure is not mysterious cross-limit incompatibility. The product encoding has already ceased to reflect the branch relation at the finite joint precision15.

This is an executable blocker-lcm diagnosis.

## 6. Witness compactness is the real general principle

Finiteness of Lambda is sufficient but not conceptually fundamental.

Let W be a compact witness space, and for each precision let

`S_M subseteq W`

be a nonempty closed set of admissible witnesses. If the precision family is finitely directed and supports shrink under refinement, then the `S_M` have the finite-intersection property. Compactness gives

`intersection_M S_M != empty`.

So the general witness-coherence resource is:

`compact witness space + directed precision + closed shrinking witness supports`.

A finite label alphabet is the discrete finite special case.

## 7. Infinite noncompact labels can escape

Take witness labels `k=1,2,3,...` and exact branch laws

`P_k : 0=k`.

Every exact branch is impossible.

Modulo M, branch k is locally solvable iff

`M|k`.

Thus

`S_M={k:M|k}`

is nonempty for every M and satisfies refinement monotonicity, but

`intersection_M S_M=empty`.

For every finite precision prefix there is a common large label (the lcm of that prefix), yet every fixed label is eventually blocked.

The witness escapes to infinity because the discrete witness space N is not compact.

Therefore an infinite witness alphabet is not automatically safe even when local branch reflection and directed precision both hold.

## 8. Fixed-label profinite descent is a separate second guard

The first-stage theorem only produces a label `lambda_*` that is locally solvable at every precision.

It does **not** yet produce one exact state satisfying branch `P_(lambda_*)`.

For that implication one still needs a route-specific descent theorem:

`branch locally solvable at every precision`

`=> branch has a profinite solution`

`=> exact branch solution`.

For fixed finite polynomial branches, compactness supplies the first arrow. The second is the branch's own **profinite exactness** condition.

Affine integer branches satisfy it. General nonlinear Diophantine branches need not.

## 9. Complete two-stage witness descent theorem

A safe sufficient architecture for exact descent of a finite labelled union is therefore:

### Stage A — witness coherence

- local branch reflection;
- a finitely directed precision family;
- finite/compact witness space with closed shrinking support.

This yields one fixed witness label surviving every precision.

### Stage B — state descent inside that witness

- compatible local solutions for the fixed branch;
- profinite exactness or another route-specific exact descent theorem.

This yields an exact state carrying that witness.

The two stages repair different precision losses and must not be merged.

## 10. A4/P023 routing consequence

This clarifies several earlier boundaries:

- support can forget path/witness identity;
- coefficient quotient can forget factor/branch identity;
- finite precision can produce a completion state without exact descent;
- witness label coherence and state realization are separate questions.

A future language that can read the witness must retain enough structure for **both** stages.

Finite-set compactness, directed inverse systems, lcm refinement and profinite descent are standard prior mathematics. The Enterprise Math value is the two-stage precision routing and the explicit identification of witness compactness as a resource.