# C266 — Eight new four-variable continuous positive hulls (author-level exact proof)

**Scope:** C195/H168 79-node positive-rational auxiliary interpolation function only. This is author evidence, NOT an original GF(2)-BRC/Cell-space theorem and NOT an admitted canonical Source Result.

## Immutable evidence sources

- GLOBAL_KNOWLEDGE_V1 main 2d3d634a004979f7263e09a54eba5db2bc3eed80; P000 and ACTIVE worldview unchanged.
- Enterprise Math main f08938461d73792f626c949c20044cbdac50dc8a; current portable research protocol applied.
- Historical C265 full author research package (unchanged bytes) with SHA256 dcf541ec1158d872eec5559548296197908e496da209a539f172955cbc73ff31.
- Original 79 rational nodes SHA256 173f6071a27c255f17178ff345e61002406f9a4958f852c9642cf7996f814529.

## Exact statement

Let I=(5,50,55,56), J={0,...,78}\I, Q=2^128, H=2^166, Z=141421356237309504880/10^20, A=(6912 * 50000^2)/17^2. The ordered rational nodes u_0,...,u_78 are embedded in C266_STANDALONE_REPLAY.py.

For j in J let B_j=floor[(Q*A / (H*((2-u_j^2)*(3-u_j^2))^3)) * product_{r != j} (Z-u_r)/|u_j-u_r|], a strictly positive integer. Define F(v) as the sum of: (i) the 75 fixed branches B_j * product_{p in I} [(Z-v_p)/(Z-u_p)]*[|u_j-u_p|/|u_j-v_p|]; (ii) the four moving branches [Q*A / (H*((2-v_k^2)*(3-v_k^2))^3)] * product_{j in J} [(Z-u_j)/|v_k-u_j|] * product_{p in I, p!=k} [(Z-v_p)/|v_k-v_p|].

**Theorem (C266).** Every legal real tuple v in ANY of the three fully continuous closed 4-coordinate boxes below satisfies:

    F(v) >= 2^128 + 536512712981048045481613993763132 > 2^128.

Coordinates are ordered (v_5,v_50,v_55,v_56). All parent box labels are zero-based.

| Parent hull | Lower endpoints | Upper endpoints | Exact leaves | Splits | Strict minimum floor(LB)-Q | Newly covered legal pairs |
|---|---|---|---:|---:|---:|---|
| (4,16) | (2/271, 7/10, 60/77, 4/5) | (6/409, 42/59, 11/14, 9/11) | 581 | 580 | 5158902987695659637439900477932651 | (4,16), (4,26), (4,30) |
| (16,22) | (1/119, 12/17, 18/23, 13/16) | (3/205, 42/59, 21/26, 9/11) | 698 | 697 | 536512712981048045481613993763132 | (16,22), (17,22), (22,31) |
| (13,28) | (1/123, 34/49, 18/23, 4/5) | (2/137, 7/10, 59/74, 9/11) | 755 | 754 | 3046191377545063607211587604835111 | (13,28), (23,28) |

Total: **2034 exact positive leaves; 2031 dyadic splits; 8 newly positive pairs**. The 363 legal parent-pair hulls are now partitioned into 213 previously witnessed F<Q, 111 fully proved F>Q (including C266's 8), and 39 unresolved. No claim about the 232 method-ineligible parent pairs.

## Why the bound proves a statement over the entire continuum

The compact standalone proof file stores three *complete preorder binary trees* using zlib/base85 only as lossless encoding. Each internal node splits one rational interval at its exact midpoint, making closed child boxes whose union equals the parent box. Each leaf is associated with the proved BASE or SHARED_k positive-rational bound. The executable reconstructs all 79 rational nodes and 75 strictly positive integer masses, then checks every leaf inequality with Python Fraction: floor(LB_leaf) - Q > 0 and checks the exact minimum for each root.

The fixed-branch factor (Z-t)/|u_j-t| is positive and convex on its ordered pole-free interval. Moving branches are positive and have log-second-derivative (as functions of their own active variable t): 6(2+t^2)/(2-t^2)^2 + 6(3+t^2)/(3-t^2)^2 + sum_{j in J} 1/(t-u_j)^2 + sum_{p != k} 1/(t-e_p)^2 > 0. BASE takes valid monotone end-point bounds on other positive factors and convex tangent bounds on moving terms. SHARED_k retains the SAME variable in the fixed branches and kth moving branch before applying a common exact tangent, while treating other moving terms via their own exact tangent bounds. Thus each leaf bound is globally valid on that leaf box, and the binary cover proves the claim on each full root. Exact rational parent-box inclusion transmits the positivity to the eight newly classified pairs.

## Reproduction / mathematical acceptance status

Run Python 3 standard library only: python research_handoffs/C266_STANDALONE_REPLAY.py . Expected final marker: C266_REMOTE_STANDALONE_EXACT_PASS 2034 2031 eight-new-pairs . The independently implemented same-author Fraction dual-number audit reconstructed all 75 fixed masses and all 2034 inequalities, and checked 2031 exact splits and the eight parent inclusions. Full expanded leaf JSON, auditor source and audit results are in the C266 local portable bundle; the GitHub standalone embeds all tree/leaf instructions needed to recompute each inequality without that bundle.

**Boundaries:** no 15685-candidate original enumeration rerun; no shrinkage of the 35 foundational box certificates; no independent Research Driver, formal task CLAIM, Source Result, or mathematical admission. No native six-axis GF(2)-BRC phase/port/future-operation/residual transfer theorem.

Native task list returned CONTROL_QUOTA; native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Therefore canonical owner is UNKNOWN; this GitHub branch is an author evidence handoff, not a control-plane claim. Google Drive was not used to work around access refusal.

**Next C267:** target the still-unresolved full four-active-coordinate (0,16) parent hull. Derive a two-shared-coordinate certified rational Hessian/convex support or an exact counterexample, and compare leaf complexity with single-coordinate bounds.