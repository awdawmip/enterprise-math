# X6 V2 relative-observer / signed-frame compatibility, 2026-11-17

Task RS-X6-UPPER-STRUCTURE-INTEGRATION-V2; publication TP2-9AC22B43194DA7427684. Author-side exact lemma, not complete law, Result, independent review or Foundation.

## Verified inherited inputs

Source 2fbae65cdb46d16036fe49d74fbe861e400d75d8, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md: in a chosen Cell anchor chart the signed spatial carrier is Z^6, D=(1,1,1,1,1,1), Delta=Z*D, r(z)=can6(z)=z-min(z)D; all twenty 3-axis min-zero observations jointly identify z modulo Delta. The lossless chart is (r,h), h=min_i z_i.

Existing research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md: signed triadic frame group R=(C2)^6 semidirect A6, order 23040; Q_S^3=J_S flips the signs on exactly a selected triple. V1-V43 durable handoff @5d3162ed9986052e555a59077ba2dc7d123ab533 records earlier path, BRC, time and holonomy science and leaves V2 typed integration unfinished.

## Theorem 1: largest relative-compatible frame subgroup

For a signed permutation g in R, an induced observer map gbar on Z^6/Delta with [gz]=gbar([z]) for all z exists iff g Delta=Delta.

Necessity: since z and z+D lie in the same quotient class, gz and gz+gD must also. Since each component of gD is +1 or -1, gD in Delta forces all signs equal, so gD=+D or -D. Sufficiency: invariance of Delta makes gbar([z])=[gz] well-defined.

Because the permutation part is A6 (360 elements), compatible frame subgroup H={epsilon*sigma: epsilon in {+1,-1}, sigma in A6} has order 720. The other 22320 of 23040 signed triadic frame elements fail the global relative quotient criterion. H acts via r->can6(g r). For positive permutations this is just coordinate permutation; for a global negative permutation it is r->max(r)D-g_positive(r).

## Theorem 2: an exact existing triad witness

Take J=Q_{1,2,3}^3=diag(-1,-1,-1,+1,+1,+1). r(0)=r(D)=0, yet r(J 0)=0 and r(J D)=(0,0,0,2,2,2). Equality of all relative observations is not preserved by this existing signed triadic frame action. No new physical transition licensing was assumed.

## Theorem 3: no finite-fibre patch under the full frame group

Suppose the report is (r(z),f(z)), where f has only finitely many possible values on each fixed relative fibre r=r0, while r must remain readable after all signed-frame actions. On the infinite fibre r0+hD, two unequal h,h' must yield identical reports. Under the fixed J, however, their relative post-observations differ by the nonzero quotient class (h-h')[JD]. Contradiction. Hence every depth h must be distinguished on each relative fibre. In particular (r,h mod m) fails for every finite m>=1: 0 and mD collide before J, but r(J(mD))=(0,0,0,2m,2m,2m). The lossless (r,h) state is sufficient for signed spatial frames on a fixed anchor chart, by reconstruction and recanonicalization. This is no universal claim about optimal compression on bounded domains or restricted operation families.

## Projection safety matrix

- r under primitive native signed translations z->z+/-e_i: SAFE, r'=can6(r+/-e_i).
- r under the uniform-sign times A6 subgroup: SAFE by Theorem 1.
- r under all R, including Q_S^3: REFUTED by Theorem 2.
- (r,h) under signed spatial frame action: SAFE by exact recovery z=r+hD in the chosen chart.
- (r,h) alone under path/BRC provenance, non-Abelian cycle holonomy, triadic-field/network, channel and native causal-time future updates: NOT CERTIFIED, distinct typed components still needed.

## Interpretation / pending obligations

This supplies a precise spatial forgetful-map lease and noncollapse test, not the whole decorated-state integration hard target. The task requires the three sibling returns when available, typed separate law slots, composition/type closure and two downstream reuse demonstrations. No physical admissibility, P000 promotion, or independent mathematical acceptance follows. The local checker enumerates all 360 even permutations and 64 sign patterns, and checks the triadic witness; the symbolic arguments above establish the unbounded result.