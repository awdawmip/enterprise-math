# R284AS — Exact fibres and minimal directed interventions for three positive Port channels

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AQ (rank-one gauge and interventions), R284AR (minimal transpose ambiguity), R284AP (diagonal observer).
Frozen scientific input: carry forward R284AR's `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; predecessor scientific file fixed at `dad9d797a53bdfd9925f49cc90a2f5acbe2bc45f`. Current behavioural rules were separately read. Scope: strictly positive rational 3x3 *auxiliary Port-channel* matrices, independent named diagonal variables and directed entry edits. Neither native X6 dynamics nor P000 is being modified.

## AS1. The full diagonal observer has exactly one or two positive diagonal-gauge classes

Let `C=(c_ij) in Q_{>0}^{3x3}`, `D=diag(d_1,d_2,d_3)`, `F_C(d)=det(D-C)`. Write

- `alpha_i=c_ii`;
- `p_ij=c_ij*c_ji>0` (`i<j`);
- `a=c_12*c_23*c_31`, `b=c_13*c_32*c_21`;
- `s=a+b`, `P=p_12*p_23*p_13=ab`.

Leibniz expansion gives the exact identity

`F_C(d)=prod_i(d_i-alpha_i) - (d_1-alpha_1)*p_23 - (d_2-alpha_2)*p_13 - (d_3-alpha_3)*p_12 - (a+b).` (AS1)

Consequently `F_C` determines every `alpha_i,p_ij,s`; the two oriented cycle weights are the roots of `x^2-s*x+P=0`. Its discriminant is `Delta=s^2-4P=(a-b)^2`.

**Classification theorem.** For strictly positive rational matrices `C,C'`, `F_C=F_C'` if and only if `C'=SCS^{-1}` or `C'=SC^TS^{-1}` for a positive invertible diagonal matrix `S`. The fibre of `F_C`, modulo positive diagonal similarity, consists of exactly one class when `a=b`, and exactly two when `a!=b`.

**Proof.** Set `S_0=diag(1,c_12,c_12*c_23)`. A direct multiplication makes `S_0 C S_0^{-1}` equal to

`K(a)=[[alpha_1,1,p_13/a],[p_12,alpha_2,1],[a,p_23,alpha_3]].` (AS2)

The invariants in (AS1) determine `K` except for `a`, which must be one of `a,b`. Two matrices choosing the same root are positively diagonal-similar via (AS2). Transposition swaps `a` and `b` while preserving the diagonal observer, so it realizes the second root. When `a=b`, both choices coincide; otherwise they are distinguished by the diagonal-similarity invariant oriented cycle product `a`. This proves necessity, sufficiency, and the class count, including singular `C` (strict positivity alone was used). QED.

## AS2. A single full directed-edit response resolves the orientation branch

For distinct `u,v` let `w` denote the third index and define
`H_C^{uv}(d,z)=det(D-C-z*E_uv)`, with `E_uv` the single-entry matrix at row `u`, column `v`.

Cofactor expansion, exact in the formal variables, yields

`H_C^{uv}(d,z) = F_C(d) - z * [c_vu*(d_w-alpha_w) + c_vw*c_wu].` (AS3)

Thus the complete observer `(F_C,H_C^{uv})` reveals both `c_vu` and `q_vu=c_vw*c_wu` by coefficient extraction. Their ratio

`rho_uv = q_vu / c_vu`, and `p_uv*rho_uv = c_uv*c_vw*c_wu`, (AS4)

is invariant under every positive diagonal similarity and equals one of the two oriented triangle weights `a,b`. This identifies which root in (AS1) belongs to the system. Therefore **for every ordered pair `u!=v` one named directed intervention is sufficient to determine the positive diagonal-gauge equivalence class**, for all positive 3x3 rational matrices, even where `a=b`. In the latter case the diagonal observer already identifies that class.

In observer terms, `F` retains the unordered pair `{a,b}`, or `(a-b)^2`, but erases the orientation of the signed exact residual `delta=a-b`. A directed edit recovers the appropriate oriented cycle through its length-two path term `q_vu`. This is a precise scope-typed observer-loss and repair statement.

## AS3. Two directed interventions on different undirected edges are necessary and sufficient for exact entrywise recovery

**Theorem.** Given full `F_C` and the full formal response for two directed edits `H_C^{u_1 v_1}, H_C^{u_2 v_2}`, every entry of every strictly positive 3x3 matrix `C` is uniquely determined if and only if `{u_1,v_1}` and `{u_2,v_2}` are distinct unordered vertex pairs. A single directed intervention, or two directions on the same unordered pair, cannot give entrywise identification on the class of all such matrices.

**Proof of sufficiency.** By AS2, matching the first edit plus matching `F` puts two candidates `C,C'` in the same positive diagonal-gauge class: `C'=SCS^{-1}`. The linear-in-`d_w` coefficient of (AS3) makes the reverse entry `c_vu` equal in the two candidates for each edit. Because these entries are positive, the gauge ratios `s_v/s_u` equal 1 along the two distinct underlying edges. Those edges form a spanning tree of three vertices, forcing all `s_i` equal. Hence `C'=C`.

For constructive recovery choose `E_21,E_32`. Extract `c_12` and `q_12=c_13 c_32` from `H^{21}`, and `c_23` from `H^{32}`. Then calculate exactly:
`c_21=p_12/c_12; b=c_21*q_12; a=s-b; c_31=a/(c_12*c_23); c_32=p_23/c_23; c_13=p_13/c_31.`
Together with the three diagonals, this recovers `C` entrywise.

**Proof of necessity.** For any single queried unordered pair `{u,v}`, let `w` be the third vertex and `T=diag(t_1,t_2,t_3)` with `t_u=t_v=1`, `t_w=t>0` arbitrary. Then `C_t=TCT^{-1}` has identical `F`; both `c_vu` and `c_vw c_wu` are invariant, so (AS3) shows the entire queried response is identical. For `t!=1`, strict positivity makes `C_t!=C`. The same argument simultaneously preserves both opposite directed probes on `{u,v}`. Thus at least two distinct unordered edges are necessary. QED.

## AS4. Exact positive stable example and path provenance

Take `epsilon=1/100`, `A=[[1,2,1],[1,1,2],[2,1,1]]`, `C=epsilon*A`, `C'=C^T`. As in R284AR, `F_C=F_C'` while `a=8*epsilon^3`, `b=epsilon^3`. All row sums of both systems are `4/100<1`.

For the single edit `E_21` at `d=(1,1,1)`, `z=epsilon`, the difference is `H_C^{21}-H_C'^{21}=-3/31250` (exact, matching R284AR). This distinguishes the two gauge classes. In contrast, `T=diag(1,1,2)` gives `C_t=TCT^{-1}`, a different strictly positive row-substochastic matrix with the same `F` and *the entire same* `H^{21}`. The additional `E_32` response separates `C_t` from `C`, illustrating the two-edit reconstruction theorem.

The three named vertices are **auxiliary Port channels**. The exact directed path products are retained rather than collapsed into a positive total or a geometry claim. This reuses the R284AQ/AR observer distinction and the project's BRC provenance-preserving principle; no BRC numerical routine or native six-axis transfer was executed.

## Reproduction and evidence

Companion code: `R284AS_three_port_fibre_checker.py` (Python 3 standard-library `Fraction`, exact Leibniz determinant).
Evidence: `R284AS_exact_verification.json`.

The local executable checker enumerated all `3^9=19,683` strictly positive integer 3x3 matrices with entries 1,2,3, grouped their exact diagonal observer data into 9,558 fibres and checked the gauge-canonical classification. Across these finite fibres, the largest class count was 2; 7,938 fibres had two represented classes. It recovered all 19,683 matrices from two probes and checked the explicit cofactor identity on 39,366 ordered-probe instances. The transpose and non-identifiability witnesses were verified with exact fractions. All checks PASS.

The universal conclusions follow from AS1–AS3; enumeration is regression evidence, not the proof. Independent review: NOT_REVIEWED. Native X6 interpretation: NOT_ATTEMPTED. Formal Task/CLAIM/Result: not asserted by this portable note.

## Next scientific question

Investigate `n=4` and higher positive Port fibres. Determine whether the diagonal observer plus a bounded set of *directed* probes determines all matrices, when overlapping oriented cycles create nontrivial principal-minor equivalences. Seek a graph/holonomy certificate for sufficient probe sets and test cases with equal diagonal minors but inequivalent named path provenance. In any large-scale algorithmic claim account for rational bit growth, full observer costs and reconstruction, rather than extrapolating the three-channel constant-size result.
