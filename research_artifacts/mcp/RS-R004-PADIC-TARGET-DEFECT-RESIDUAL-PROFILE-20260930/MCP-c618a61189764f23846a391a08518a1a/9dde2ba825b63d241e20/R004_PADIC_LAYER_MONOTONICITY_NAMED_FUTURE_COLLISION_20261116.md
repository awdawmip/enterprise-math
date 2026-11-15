# R004 p-adic target-defect profile: monotone layers and named-future collision

Date: 2026-11-16. Author-side exact algebra; task RS-R004-PADIC-TARGET-DEFECT-RESIDUAL-PROFILE-20260930 / publication TP2-2F73D1BB1AAA29EF4FCD. Researcher EM-EMF6D046-5A2844; Activity RA-6B0C6701D225841FFCCECF3E. Frozen historical R004 input: D_H=(Row(A_H)+Row(B_H))/Row(A_H) over R=Z/p^KZ. Standard finite p-group structure is reused; no independent mathematical review or formal Result.

## Lemma: exact layer monotonicity

For H subset J, restricting coordinates sends Row(A_J) onto Row(A_H) and Row(B_J) onto Row(B_H), yielding a natural surjection f:D_J -> D_H. For each 1<=j<=K, restriction of f gives a surjective F_p-linear map p^(j-1)D_J/p^jD_J -> p^(j-1)D_H/p^jD_H: every p^(j-1)y has a lift p^(j-1)x, and the p^j-denominators respect f. Thus c_j(D_H)<=c_j(D_J), where c_j(D)=dim_Fp(p^(j-1)D/p^jD). If D is a sum of cyclic factors R/(p^e_i), c_j(D) counts e_i>=j. Accordingly the number of factors with exponent j is c_j-c_(j+1) (c_(K+1)=0) and the scalar Delta=log_p|D| equals sum_j c_j. This coordinatewise monotonicity neither proves submodularity nor a future-query sufficient statistic.

## Exact two-coordinate counterexample to abstract profile sufficiency

Fix p=2, K=2, R=Z/4Z, H={1,2}, and the SAME named target B=I_2. Compare two allowed initial source-observation histories A_1=[1 0], A_2=[0 1]. In each, D_H=R^2/Row(A_i) is abstractly R and has profile c=(1,1), Delta=2.

Allow one next named source-observation update: append q=[1 0] to A. For A_1 it is redundant, hence future D_1 remains R with c'=(1,1). For A_2 it raises the observation span to all R^2, hence future D_2=0 with c'=(0,0). Likewise the named query whether target row q is already determined has answers yes and no respectively. Both initial profiles and H, p, K, B coincide. Therefore c_j alone does not determine this declared named future update/query across differing admissible A histories. Relative embedding Row(A) inside the named target row space (or an equivalent query-compatible map) is relevant retained structure. The witness is a cross-input/observation-history claim; if a protocol retains the full A separately it can already distinguish the cases. K=1 also admits a similar collision; this K=2 example visibly exercises two p-adic layers.

## Verification and open frontier

A standard-library integer checker enumerated full row spans and p-filtrations in (Z/4Z)^2. Exact output: R004_P2_NAMED_FUTURE_PROFILE_COLLISION_PASS (1, 1) (1, 1) (1, 1) (0, 0). Companion file r004_padic_named_target_future_witness_20261116.py.

Research next: for a FIXED original A,B with explicitly chosen hide/refine/target query language, decide which quotient/embedding maps are necessary and sufficient; test named future profile collisions with same retained static source, and account for representation/update/query cost. Earlier R004 negative scalar sub/supermodularity is preserved unchanged. No P000/Foundation change.