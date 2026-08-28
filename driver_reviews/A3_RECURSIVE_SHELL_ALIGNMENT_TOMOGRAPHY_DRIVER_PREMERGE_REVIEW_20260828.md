# Driver Review — A3 Recursive Shell Alignment Tomography

Status: `DRIVER_FINAL / REJECTED_FULL_PACKAGE / PARTIAL_EXACT_RESULTS_PRESERVED / H4_REFUTED_AS_STATED / REVISION_PUBLISHED`

Date: `2026-08-28`

Driver-ID: `EM-DVR-7C31A8 / CONTROL_PLANE`

Task: `RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY`

Publication: `TP2-78C59019AE494DF41F65`

Primary result: `RR-FFB5FBD20103CC20A2A6`

Source evidence: merged PR #779 and exact current result artifacts.

Redispatch side evidence inspected: `RR-D1C4B1E36D02053560EA / PR #800`.

Revision task: `RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION / TP2-E6E8A3DC37930B4CF4AA`.

## Disposition

`DRIVER_DISPOSITION = REJECTED`.

`RESULT_CLASS = PARTIAL_EXACT_PACKAGE_WITH_DECISIVE_H4_COUNTEREXAMPLE`.

`DESTINATION = FOLLOWUP_TASK`.

`FOUNDATION_MUTATION = NONE`.

`METHOD_HARVEST = DOMAIN_OPERATOR / COMPOSE_EXISTING_TOOLS`.

The result is rejected **as a complete task-level PASS** because its H4 scale-coherence criterion is false for the task's own depth-2 prefix move semantics. Exact subresults below remain usable at their stated carrier/operational strength and are frozen as inputs to the revision task.

## Exact subresults preserved

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
   The alignment-set / stabilizer-orbit distinction remains valid and required for choice-safe interior observation.

4. Under the selected prefix-support semantics, depth-1 shell moves shield the next inner ball, while depth 2 is the first support depth capable of changing the immediately observed interior shell.

5. The redispatch theorem in PR #800 is accepted only as a **fixed-subgroup algebraic side result**: for fixed \(G,H\), double-coset support multiplication on \(H\backslash G/H\) is associative as a relation-valued law; its deterministic lift by the pair groupoid on \(H\backslash G\) is exact; and universal single-valuedness is equivalent to normality of \(H\). The `S4/H` seven-class table and `C2*C2={C0,C2}` witness may be retained as compressed frame-phase algebra. This side result does not satisfy the parent H4 state-level scale square.

## Decisive H4 counterexample

Let the task's depth-2 prefix action at scale \(n\) act by \(R_g\) on shells \(S_n\cup S_{n-1}\) and fix deeper shells. Compare scales 3 and 2. Choose the same nontrivial aligner

\[
g=(23)
\]

at both scales. Therefore the submitted double-coset defect is the identity class:

\[
\Delta_2=Hgg^{-1}H=H=C_0.
\]

Use outer pointer targets

\[
a_k=(k,-k,0,0),
\]

and choose shell markers \(p_k=R_g^{-1}a_k\) on \(S_k\), so the same \(g\) is a valid aligner at scales 3 and 2. Add the interior marker

\[
p=(1,-1,0,0)\in S_1.
\]

### Path A — align at scale 3, then restrict

The depth-2 scale-3 action has support on \(S_3\cup S_2\). It fixes \(p\in S_1\). After restriction to \(B_2\), the inner marker remains

\[
p=(1,-1,0,0).
\]

### Path B — restrict to scale 2, then align

The depth-2 scale-2 action has support on \(S_2\cup S_1\), so it acts on \(p\). With the sign-twisted action for \(g=(23)\),

\[
R_gp=(-1,0,1,0).
\]

The residual target stabilizer is \(H=\{e,(12)\}\). Under the same sign-twisted action, \((12)\) fixes \(p\), hence

\[
H\cdot p=\{p\}.
\]

Therefore

\[
R_gp\notin H\cdot p.
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
Hg_ng_{n+1}^{-1}H
\]

records only relative frame phase. It does not record that the support of the nominally same depth-2 operation shifts inward when the radius decreases:

\[
D_{n+1,2}(g)|_{B_n}\neq D_{n,2}(g).
\]

The parent checker verifies shell counts, the 24-frame group, stabilizers, double cosets and compressed class algebra, but it does not evaluate both sides of H4 as actual maps on nested states. The three-radius class sequence therefore cannot certify H4.

The PR #800 fixed-stabilizer pair-groupoid lift repairs the composition law of compressed frame-phase labels only. It explicitly leaves scale-varying stabilizer / partial-move groupoid coherence open, which contains this counterexample.

## Required revision

Do not restart H1-H3 and do not enlarge the finite census. The revision task begins at the smallest failed unit:

1. freeze actual partial/action maps \(D_{n,d}\), restrictions \(\rho_{n+1,n}\), alignment relations \(C_n\), and observed state language;
2. test the two H4 paths as relations/maps on states, not merely on \(S_4/H\) labels;
3. include the \(n=2,\ g=(23),\ p=(1,-1,0,0)\) counterexample as a mandatory regression;
4. derive the strongest correct support/domain-aware radial defect or exact no-go;
5. place the fixed-\(H\) pair-groupoid/double-coset algebra only as a quotient/special case of the corrected object;
6. re-evaluate H5/H6 statements depending on the false H4 iff criterion;
7. return a corrected theorem, exact impossibility theorem, or strictly smaller typed obstruction with a complete checker.

## Routing consequence

The original result `RR-FFB5FBD20103CC20A2A6` is rejected at task-PASS strength.

The original task generation is terminal at `REJECTED_WITH_PARTIAL_EXACT_RESULTS`; its verified subresults are preserved.

Continuation is routed to the already published registered revision:

`RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION / TP2-E6E8A3DC37930B4CF4AA`.

No Foundation promotion, larger finite census, or new shared tool family is authorized from the current evidence.
