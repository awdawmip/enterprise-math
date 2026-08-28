# Driver Pre-Merge Review — A3 Recursive Shell Alignment Tomography

Status: `DRIVER_PREMERGE / REQUEST_CHANGES / PARTIAL_EXACT_RESULTS_PRESERVED / H4_REFUTED_AS_STATED`

Date: `2026-08-28`

Driver-ID: `EM-DVR-7C31A8 / CONTROL_PLANE`

Task: `RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY`

Publication: `TP2-78C59019AE494DF41F65`

Primary result under review: `RR-FFB5FBD20103CC20A2A6 / Draft PR #779`

Redispatch result inspected: `RR-D1C4B1E36D02053560EA / Draft PR #800`

## Disposition

`PREMERGE_DISPOSITION = REQUEST_CHANGES`.

`TASK_TERMINAL = FALSE`.

`RESULT_CLASS = PARTIAL_EXACT_PACKAGE_WITH_DECISIVE_H4_COUNTEREXAMPLE`.

`FOUNDATION_MUTATION = NONE`.

`METHOD_HARVEST = DOMAIN_OPERATOR / COMPOSE_EXISTING_TOOLS`.

The finite shell package contains several exact reusable results, but the submitted H4 scale-coherence theorem is false for the task's own depth-2 prefix move semantics. The task cannot be accepted or closed until the actual cross-scale action/restriction square is repaired and checked on states rather than only on frame/double-coset labels.

## Exact subresults preserved

The following parts are accepted as mathematically usable at their stated carrier/operational strength, subject to ordinary source typing:

1. For
   \[
   \Lambda_3=\{x\in\mathbb Z^4:\sum_i x_i=0\},\qquad r(x)=\max_i|x_i|,
   \]
   the finite balls/shells satisfy
   \[
   |B_n|=\frac{16n^3+24n^2+14n+3}{3},\qquad |S_n|=16n^2+2.
   \]

2. The sign-twisted coordinate-permutation action
   \[
   R_\sigma=\operatorname{sgn}(\sigma)P_\sigma|_{\Lambda_3}
   \]
   gives the faithful orientation-preserving 24-frame action and preserves the chosen shell radius.

3. For the pointer target used by the finite prototype, the residual stabilizer is
   \[
   H=\{e,(12)\}.
   \]
   The alignment-set / stabilizer-orbit distinction is valid and remains required for choice-safe interior observation.

4. Under the selected prefix-support semantics, depth-1 shell moves shield the next inner ball, while depth 2 is the first support depth capable of changing the immediately observed interior shell.

5. The redispatch theorem in PR #800 is accepted as a **fixed-subgroup algebraic subtheorem**: for fixed \(G,H\), double-coset support multiplication on \(H\backslash G/H\) is associative as a relation-valued law; its deterministic lift by the pair groupoid on \(H\backslash G\) is exact; and universal single-valuedness is equivalent to normality of \(H\). The `S4/H` seven-class table and `C2*C2={C0,C2}` witness may be retained as compressed frame-phase algebra.

None of these points proves the task's full cross-scale commutation claim.

## Decisive H4 counterexample

Let the task's depth-2 prefix action at scale \(n\) act by \(R_g\) on shells \(S_n\cup S_{n-1}\) and fix deeper shells. Compare scales 3 and 2. Choose the same nontrivial aligner

\[
g=(23)
\]

at both scales. Therefore the submitted double-coset defect is the identity class:

\[
\Delta_2=H g g^{-1}H=H=C_0.
\]

Use outer pointer targets

\[
a_k=(k,-k,0,0),
\]

and choose shell markers \(p_k=R_g^{-1}a_k\) on \(S_k\), so the same \(g\) is a valid aligner at scales 3 and 2. Add the interior marker

\[
p=(1,-1,0,0)\in S_1.
\]

Now compare the two paths from the scale-3 state to aligned scale-2 interior data.

### Path A — align at scale 3, then restrict

The depth-2 scale-3 action has support on \(S_3\cup S_2\). It aligns the outer data, but fixes \(p\in S_1\). After restriction to \(B_2\), the inner marker remains

\[
p=(1,-1,0,0).
\]

### Path B — restrict to scale 2, then align

After restriction, the depth-2 scale-2 action has support on \(S_2\cup S_1\), so it acts on the same interior marker. With the sign-twisted action for \(g=(23)\),

\[
R_g p=(-1,0,1,0).
\]

The residual target stabilizer is \(H=\{e,(12)\}\). Under the same sign-twisted action, \((12)\) fixes \(p\), hence

\[
H\cdot p=\{p\}.
\]

Therefore

\[
R_g p\notin H\cdot p.
\]

So the two paths are not equal even after the declared residual-\(H\) quotient, despite

\[
\Delta_2=C_0.
\]

This refutes the submitted implication

\[
\Delta_n=H\Longrightarrow
\widehat\rho_{n+1,n}\circ C_{n+1}=C_n\circ\rho_{n+1,n}
\]

for the stated scale-dependent prefix move model.

## Root cause

The compressed label

\[
H g_n g_{n+1}^{-1}H
\]

records only relative **frame phase**. It does not record the fact that the support of the nominally same depth-2 operation shifts inward when the radius decreases:

\[
D_{n+1,2}(g)|_{B_n}
\neq
D_{n,2}(g).
\]

The checker in PR #779 verifies shell counts, the 24-frame group, stabilizers, double cosets and compressed class algebra, but it does not evaluate both sides of the H4 square as actual maps on nested states. The three-radius class sequence therefore cannot certify H4.

The PR #800 fixed-stabilizer pair-groupoid lift repairs the **composition law of the compressed frame-phase labels**, but it does not repair this scale-dependent support mismatch. PR #800 itself correctly leaves `SCALE_VARYING_STABILIZER_OR_PARTIAL_MOVE_GROUPOID_COHERENCE_OPEN`; that open residue includes the counterexample above.

## Required revision — smallest unfinished unit

Do not restart H1-H3 and do not enlarge the finite census. Resume at H4 only.

1. Freeze the actual partial/action maps \(D_{n,d}\), restrictions \(\rho_{n+1,n}\), alignment relations \(C_n\), and observed state language on the same finite prototype.
2. Test
   \[
   \widehat\rho_{n+1,n}\circ C_{n+1}
   \quad\text{versus}\quad
   C_n\circ\rho_{n+1,n}
   \]
   as relations/maps on states, not merely on \(S_4/H\) labels.
3. Add the explicit \(n=2\), \(g=(23)\), \(p=(1,-1,0,0)\) counterexample above as a mandatory regression.
4. Derive the strongest correct radial defect object. It must retain enough support/domain/interface data to distinguish the two paths. A scale-dependent action groupoid, typed support-transition profile, or another operation-safe relation is admissible; no particular repair is preselected by this review.
5. Reinterpret the fixed-\(H\) pair-groupoid/double-coset algebra as a quotient or special case of the corrected cross-scale object, not as the full H4 invariant.
6. Re-evaluate every H5/H6 statement whose correctness depended on the false H4 iff criterion, and update the deterministic checker to cover the actual commuting square.
7. Return a corrected result only after the revised H4 is proved, exactly falsified with the strongest replacement classification, or reduced to a strictly smaller explicit obstruction.

## Routing consequence

`RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY` remains open.

The current redispatch owner may continue on the same task; no additional task publication is needed for this repair. The correct next frontier is

`PARTIAL_MOVE_SCALE_COMMUTATION_AND_RADIAL_DEFECT_REPAIR`.

No Foundation promotion, larger finite census, or new shared tool family is authorized from the current evidence.
