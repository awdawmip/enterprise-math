# Research Return — A3 Recursive Shell Alignment Tomography Redispatch

Task: `RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY`  
Publication: `TP2-78C59019AE494DF41F65`  
Researcher-ID: `EM-A3SHELL-6F4B92`  
Claim-ID: `chatgpt-a3shell-20260828-1543-6f4b92`  
Execution branch: `research/a3-recursive-shell-alignment-tomography-em-a3shell-6f4b92`

## Terminal verdict

`PASS / FIXED_STABILIZER_RADIAL_RELATION_COHERENCE_CLOSED / EXACT_PAIR_GROUPOID_LIFT / DETERMINISTIC_DOUBLE_COSET_COMPOSITION_IFF_NORMAL`

This redispatch closes the precise coherence residue exposed by the first A3 shell-tomography package at fixed residual stabilizer.

## Main theorem package

Let \(G\) be any group and \(H\le G\).  On the double-coset set
\(\mathcal D=H\backslash G/H\), define

\[
A\star B=\{C\in\mathcal D:C\subseteq AB\}.
\]

Then:

1. \(AB\) is exactly an \(H\)-bi-invariant union of double cosets.
2. \(\star\) is associative as a set-valued operation.
3. \(H\) is a two-sided identity.
4. inversion \(HgH\mapsto Hg^{-1}H\) is an involution with
   \((A\star B)^*=B^*\star A^*\).
5. Every double-coset product is single-valued iff \(H\trianglelefteq G\).

Thus the earlier witness \(C_2C_2=\{C_0,C_2\}\) reflects nonnormality/loss of
determinism, not an associativity defect.

## Exact deterministic lift

Let \(\Omega=H\backslash G\).  The pair groupoid on \(\Omega\) has deterministic
composition

\[
(x,y)\circ(y,z)=(x,z).
\]

The defect projection

\[
\delta(Hg,Hk)=Hgk^{-1}H
\]

is well-defined and satisfies

\[
\delta(x,z)\in\delta(x,y)\star\delta(y,z).
\]

The converse is exact: every \(C\in A\star B\) is realized by some composable
triple \(x,y,z\) with adjacent defects \(A,B\) and endpoint defect \(C\).
Therefore the double-coset law is exactly the relation image of the pair
groupoid; it has neither missing nor spurious outputs.

## Frozen A3 \(S_4/H\) instance

For

\[
G=S_4,\qquad H=\{e,(12)\},
\]

the checker certifies:

- 12 left-coset alignment objects;
- 7 double-coset defect classes of sizes `2,2,4,4,4,4,4`;
- complete seven-by-seven support table;
- all `343/343` boolean associativity triples;
- all `1728/1728` pair-groupoid triples satisfy exact support projection;
- all `343/343` weighted orbital associativity triples;
- class involution `0,1,2,4,3,5,6`;
- orbital valencies `1,1,2,2,2,2,2`;
- `C2*C2={C0,C2}`;
- exactly 24 composable `C2,C2` triples end in `C0` and 24 end in `C2`;
- nonnormality witness `(23)(12)(23)=(13) notin H`.

The 48-triple split proves that no deterministic function of the two adjacent
defect labels alone can recover every exact endpoint.

## Integer orbital refinement

Writing \(R_i\) for the orbital relation of class \(C_i\) on the 12 alignment
cosets and \(M_i\) for its adjacency matrix,

\[
M_iM_j=\sum_k p_{ij}^kM_k
\]

with exact nonnegative integer structure constants.

Examples:

\[
M_2M_2=2M_0+M_2,
\qquad
M_2M_3=2M_1+M_3,
\qquad
M_6M_6=2M_0+2M_1.
\]

The positive supports are exactly the relation-valued defect products.

## Research implication

The correct fixed-stabilizer radial state hierarchy is

\[
g_n
\to Hg_n
\to (Hg_n,Hg_{n+1})
\to Hg_ng_{n+1}^{-1}H.
\]

The pair \((Hg_n,Hg_{n+1})\) is the minimal deterministic transport arrow.
Compressing it to a double coset erases the middle interface information and
forces relation-valued composition unless \(H\) is normal.

Therefore H7 is realized by composition of existing relation/BRC, quotient,
finite-symmetry and holonomy tools.  No new shared tool family or Foundation
primitive is justified.

## Exact files

Full theorem package:

`research_artifacts/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_REDISPATCH/RADIAL_RELATION_COHERENCE_RESULT_20260828.md`

Machine certificate:

`research_artifacts/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_REDISPATCH/s4_h_orbital_certificate.json`

Deterministic checker:

`scripts/check_a3_recursive_shell_alignment_tomography_redispatch.py`

Checker terminal verdict:

`A3_RADIAL_RELATION_COHERENCE_CHECK=PASS`

## Boundary / remaining residue

Closed:

`FIXED_STABILIZER_RADIAL_RELATION_COHERENCE`

Still open only beyond the fixed-subgroup hypothesis:

`SCALE_VARYING_STABILIZER_OR_PARTIAL_MOVE_GROUPOID_COHERENCE_OPEN`

A justified successor must therefore involve scale-dependent \(H_n\), partial
move domains/groupoids, non-conjugate target stabilizers, or restriction maps
that fail to transport interface symmetries coherently.  Enlarging the same
finite \(S_4/H\) census is not a successor.

## Tool verdict

`COMPOSE_EXISTING_TOOLS / NO FOUNDATION PROMOTION / NO NEW SHARED TOOL FAMILY`
