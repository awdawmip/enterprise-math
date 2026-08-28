<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "title": "Perfect Prime Table Route-A Critical Cofactor All-m Proof or Exact Counterexample",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The actual AP Route-A critical cofactor is exactly full rank through m=40 and has multiple all-m structural reductions, most recently to a signed factorial-Cauchy K_{m,m} Laplacian cofactor; the remaining all-m signed tree-sum nonvanishing is open.",
  "next_action": "Schur-complement the positive supersymmetric-Schur normalizers of the factorial-Cauchy boundary Laplacian and prove or refute nonvanishing of the resulting core determinant for every m, prioritizing the actual AP shifts a_l=1+l m^2.",
  "dependencies": [
    "research_runtime_state_machine.json@main",
    "research_task_publication_contract_v2.json@main",
    "research_objective_contract.json@main",
    "research_taskbook_policy.json@main"
  ],
  "source_refs": [
    "GLOBAL_KNOWLEDGE:1a85ca140cbb219709f1cf4850c260db8f713210",
    "GLOBAL_KNOWLEDGE:c2708e77e4eb3be506eb5da3866932c633dc8d09",
    "GLOBAL_KNOWLEDGE:f4609e6e64e00333078c581e61a874befc5b89ea",
    "GLOBAL_KNOWLEDGE:d3a28eea50c567c54cb0a5a0e81b80145c85e6fc",
    "GLOBAL_KNOWLEDGE:fa9c4dc5dd1a172bc50beea5bcc9381ec0906c33",
    "GLOBAL_KNOWLEDGE:b65fc6c396e5788c84f6c000d07d54de0d059b22",
    "GLOBAL_KNOWLEDGE:e048b1127df84b489670d5bc11216db6449d5e51",
    "GLOBAL_KNOWLEDGE:8ef6239d5a3c05d4612f94da1c2eb53edadce1b1"
  ],
  "evidence_status": "EXACT_ALL_M_REDUCTIONS_AVAILABLE / EXACT_FULL_RANK_THROUGH_M40 / TERMINAL_ALL_M_NONVANISHING_OR_COUNTEREXAMPLE_OPEN",
  "last_progress_ref": "GLOBAL_KNOWLEDGE:8ef6239d5a3c05d4612f94da1c2eb53edadce1b1",
  "last_progress_at": "2026-08-28T01:18:00+00:00",
  "hard_block": "No exact sign theorem is yet known for the signed factorial-Cauchy K_{m,m} spanning-tree cofactor produced by the actual AP reciprocal-product kernel.",
  "tags": [
    "perfect-prime-table",
    "Route-A",
    "critical-cofactor",
    "all-m",
    "factorial-Cauchy",
    "supersymmetric-Schur",
    "Bezoutian",
    "Loewner",
    "signed-Laplacian",
    "matrix-tree",
    "exact-proof"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "parent_objective_generation_id": "OG-9CD71978EC19A9D5B7FA",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTA",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime Table Route-A Critical Cofactor All-m Proof or Exact Counterexample

Status: `PUBLISHED_REGISTERED / NEW_DIRECTION / EXACT ALL-M CLOSURE TASK`

## Mother question

For every integer \(m\ge 2\), let

\[
A_{ij}
=
\prod_{k=0}^{m-1}
\left(1+i+mj+k m^2\right),
\qquad
0\le i,j<m.
\]

Does the critical bidegree-\((m-2,m-2)\) polynomial cofactor system have only the zero solution? Equivalently, is the actual arithmetic-progression Route-A critical determinant nonzero for every \(m\)?

The task is terminally two-sided:

\[
\boxed{
\texttt{CRITICAL\_COFACTOR\_ALL\_M\_NONVANISHING\_PROVED\_OR\_EXACT\_COUNTEREXAMPLE}
}
\]

A stronger generic-shift theorem is welcome only when it directly discharges this actual AP statement. It is not itself the target.

## Frozen inputs and scope

### A. Exact critical system

A cofactor matrix \(c_{ij}=c(i,j)\) is admissible in the critical polynomial family when \(c(i,j)\) has bidegree at most \(m-2\). Put

\[
D_{ij}=c_{ij}A_{ij}.
\]

The desired additive-rank collapse would require

\[
D_{ij}=s_i-t_j,
\]

equivalently all adjacent mixed differences vanish:

\[
D_{ij}-D_{i,j+1}-D_{i+1,j}+D_{i+1,j+1}=0.
\]

The critical coefficient matrix is square of dimension \((m-1)^2\). Exact modular certificates already show full rank for every checked case through \(m=40\), including a \(1521\times1521\) certificate. These checks are evidence only, not an all-\(m\) proof.

### B. Transfer formulation

Set \(n=m-1\). In the bivariate falling-factorial basis, let

\[
L=X\otimes I+mI\otimes X,
\]

with source and target index squares

\[
S=\{0,\ldots,n-1\}^2,
\qquad
T=\{1,\ldots,n\}^2.
\]

For the actual AP product

\[
P_m(z)=\prod_{\ell=0}^{m-1}(z+a_\ell),
\qquad
a_\ell=1+\ell m^2,
\]

critical nonvanishing is equivalent, up to explicit fixed nonzero triangular/basis factors, to

\[
\det P_m(L)[T,S]\ne0.
\]

All basis changes and gauge factors used by the final proof must be reproduced exactly rather than cited informally.

### C. Frozen all-\(m\) lemmas already available

The following are inputs, not goals to rediscover.

1. **Two-factor transfer.** For positive \(a,b\),

\[
\det\!\left(((L+aI)(L+bI))[T,S]\right)
=
m^{(m-1)^2+1}\big((m-1)!\big)^2>0.
\]

2. **Single-factor radical.** For \(\ell=x+my\),

\[
\operatorname{Rad}(\ell+a)
=
\left\{
\frac{F(x)-F(-my-a)}{x+my+a}:
\deg F\le m-1
\right\}/\mathbb R,
\]

of dimension \(m-1\).

3. **Affine-substitution boundary geometry.** With

\[
T_a f(y)=f(-my-a),
\qquad
W=\operatorname{diag}\!\left((-1)^i\binom ni\right),
\]

the dual boundary transform is

\[
M_a=W^{-1}T_a^{T}W,
\]

and

\[
\det M_a
=
(-1)^{m(m-1)/2}m^{m(m-1)/2}.
\]

Distinct-shift radical graphs intersect only in the constant gauge; after the fixed checkerboard gauge the affine-substitution curve is sign-regular/TN.

4. **Reciprocal-product full finite differences.** For

\[
h(q)=\frac1{\prod_{\alpha=1}^{m}(q+a_\alpha)},
\]

full one-sided finite differences are rectangular supersymmetric-Schur/resultant quotients. In particular the Route-A signed normalizers below are strictly positive.

5. **Factorial-Cauchy boundary reduction.** Define

\[
H_{ij}=h(i+mj),
\qquad
w_i=(-1)^i\binom ni,
\qquad
W=\operatorname{diag}(w_i),
\]

\[
e_i=\sum_{j=0}^{n}w_jH_{ij}>0,
\qquad
d_j=\sum_{i=0}^{n}w_iH_{ij}>0.
\]

Up to the explicit nonzero scalar \((-1)^n/n!\), the duplicated-boundary matrix is

\[
Q=
\begin{pmatrix}
\operatorname{diag}(e)&HW\\
H^TW&\operatorname{diag}(d)
\end{pmatrix}.
\]

After the known diagonal gauge/congruence it is the weighted complete-bipartite Laplacian of \(K_{m,m}\) with signed edge weights

\[
c_{ij}=w_iw_jh(i+mj).
\]

By Jacobi complementarity and the Matrix-Tree theorem, the critical determinant is nonzero exactly when the signed factorial-Cauchy tree sum

\[
\tau_c
=
\sum_{\mathcal T\text{ spanning tree of }K_{m,m}}
\prod_{(i,j)\in\mathcal T}c_{ij}
\]

is nonzero.

### D. Evidence that must remain evidence

The following may guide proof search but may not be promoted to theorem without proof:

- exact finite full-rank checks through \(m=40\);
- coefficientwise positivity observed for low \(m\);
- numerical left-half-plane root observations for AP-step specializations;
- spectral or stability patterns seen only numerically.

### E. Closed shortcuts — do not retry as if unresolved

The execution must not base success on any of the following already-falsified shortcuts:

- finite-\(m\) verification as a substitute for an all-\(m\) proof;
- raw Cauchy-Binet summands all having one sign;
- interpreting the signed barycentric map as ordinary convex averaging;
- ordinary Schur positivity of the full critical determinant;
- generic strict total positivity alone;
- an all-principal-minors-positive shortcut;
- requiring the compressed Christoffel operator to have all eigenvalues in the open right half-plane;
- direct use of separable multivariate multiplier-sequence classification on \(P(r+ms)\);
- support-parity or same-sign spanning-tree arguments without exact regrouping.

### F. Scope boundary

Do not broaden this task to:

- general integer factorization;
- a general arithmetic-circuit lower bound;
- the full Strong-Divisor conjecture;
- arbitrary positive-shift products when the actual AP target can be settled more narrowly.

The actual shifts

\[
a_\ell=1+\ell m^2
\]

have priority.

## Hard target and required outputs

### Hard target

Produce exactly one of the following terminal mathematical outcomes.

**Outcome PROOF**

A rigorous proof that for every \(m\ge2\),

\[
\det P_m(L)[T,S]\ne0,
\]

equivalently the critical bidegree-\((m-2,m-2)\) cofactor system has no nonzero solution, equivalently the signed factorial-Cauchy \(K_{m,m}\) tree sum above is nonzero.

**Outcome COUNTEREXAMPLE**

An exact integer \(m\ge2\) together with exact data proving that the determinant vanishes. A counterexample return must include either:

- a nonzero exact critical cofactor polynomial/kernel vector; or
- an exact zero determinant certificate with enough data to reconstruct a nontrivial kernel.

Floating-point near-zero evidence is not a counterexample.

### Required research artifact

Write the terminal return to:

`research_returns/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF_RETURN_20260828.md`

The return must contain:

1. the terminal verdict `PROOF`, `COUNTEREXAMPLE`, or `UNRESOLVED_EXACT_FRONTIER`;
2. a complete statement of the theorem or counterexample;
3. the exact equivalence chain back to the original \(D_{ij}=c_{ij}A_{ij}\) mixed-difference system;
4. every normalization, basis change and determinant sign needed for the argument;
5. exact computational certificates used for falsification or counterexample search;
6. a section `Previously closed shortcuts respected` confirming that the proof does not reuse a known-false shortcut;
7. if unresolved, one smallest explicit unproved lemma together with a proof that this lemma is sufficient for the actual AP mother question.

### Preferred next proof interfaces

Prioritize these exact interfaces before inventing a new route:

1. Schur-complement the positive \(e_i,d_j\) normalizers and identify the remaining core as a flagged/generalized-factorial Cauchy determinant.
2. Identify the core as a Bezoutian or Loewner divided-difference determinant with controlled sign.
3. Prove direct noncancellation of the signed factorial-Cauchy tree sum by an exact regrouping or determinant identity.
4. Exploit the AP alphabets \(a_\ell=1+\ell m^2\) and mixed-radix node alphabets before strengthening to arbitrary shifts.

## Research value to preserve

The canonical residue-class factorial construction already supplies a perfectly prime-loaded \(m^2\)-cell table. The unresolved mathematical resource is whether its critical cell correction can be compressed into the additive rank required by an \(O(m)\)-state endpoint representation.

A terminal negative result for the critical polynomial family is therefore valuable even without a factorization algorithm: it rigorously closes the entire sub-\(m\) polynomial cofactor repair mechanism for this prime-loaded Route-A construction.

A terminal counterexample is equally valuable: it identifies the first exact algebraic compression mechanism that escaped the observed \(m^2\)-parameter payback.

The task must preserve this distinction. It must not claim a general factoring lower bound.

## Success, kill, and return criteria

### Success

`PASS_PROOF` only if the actual AP all-\(m\) nonvanishing theorem is proved rigorously.

`PASS_COUNTEREXAMPLE` only if an exact zero witness is produced and independently reconstructible.

### Kill conditions for a proof route

Kill a local proof route immediately when one of the following is established:

- it requires a known-false positivity/convexity shortcut listed above;
- its key theorem applies only to a generic class that does not preserve the factorial-Cauchy/product-rooted structure actually used here;
- it proves only bounded-\(m\) cases;
- it proves a stronger conjecture numerically but does not prove the actual AP target;
- it silently assumes the determinant sign it is supposed to prove.

Killing a local route does not terminate the task while another exact proof interface remains executable.

### Unresolved return

Use `UNRESOLVED_EXACT_FRONTIER` only after the available exact interfaces have been seriously reduced and no executable proof or counterexample step remains in the current execution.

The unresolved return must isolate the smallest remaining lemma. The preferred form is an explicit \((m-1)\times(m-1)\) Schur-complement / Bezoutian / Loewner determinant whose nonvanishing is proved equivalent to the actual AP critical determinant.

Do not return merely because the problem is difficult.

### Provenance

The GLOBAL_KNOWLEDGE commits listed in task metadata are durable research evidence and derivation checkpoints. The source repository taskbook and immutable task publication record control execution authority for this task.

This is the first formal task publication for this pre-taskbook Route-A exploratory line; those earlier checkpoints are evidence, not a parent task publication.
