# R336 — portable research handoff

**Scientific increment:** In the untruncated signed 12-step BRC auxiliary K/J model, conditional on R330 author-side rational extraction and `deg H_r <= r`, prove for every integer r>=4:

`c[r,r-4] = 6**r*(39366*r**4-185652*r**3+89864*r**2+126192*r+170815)/455625 >= (55/81)*6**r >0`.

Proof uses newly derived `E5=-z**3*(123*z**3-20*z**2-480*z+240)/64`, `N4=-z**2*(67*z**2-156*z+32)/16`, and universal normalized fourth jet for all j>=4: `w_j=3*(7555707*j**4-73290834*j**3+48387073*j**2-224798666*j-566198120)/40960000`; induction at j>=9 with exact bases 4..8 and separate j0..3 Euler moments. See full proof and exact code.

**Actual checks:** `python R336_symbolic.py` -> PASS; `python R336_independent_integer.py --max-r 64` -> PASS. 61 fifth coefficients, 61 x 4 prior coefficients and 61 extra-degree nodes agree; signed B_s from 0..194, triangle 19110 >0, 8031 exterior negatives preserved; SHA256 fifth sequence `f8ef3594c08893f48bdec7fc4d8cc3f432a50be79543ca83210c53c0aa53233b`. Python 3 and SymPy 1.14 were actually run locally (no native EM simulation). Explicit proof condition: R330 author formula remains unreviewed; numerical range only r<=64.

**Source pins:** GLOBAL_KNOWLEDGE_V1 main@7dd3a2481543bc82bd83e9993c6646a06738f304; EM main@4f9653b3b03cd94f69c6a914a02cf757ea06720f; GLOBAL P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; R330 7c73f56263c3f0515aa28e55ced2d4c703b8e086; R335 b411ee4e6c9c47fdacb7f51b9fdcf154c609ca13. P000/ACTIVE worldview are unchanged. Current R336 contribution identity EM-R336-B7BF04, local author-side, not service issued or independent review.

**Permission/owner:** GitHub identity awdawmip push/admin. Native em_control_tasks -> CONTROL_QUOTA, current active Owner not verified. No native CLAIM, Source Result, mathematical admission or independent Driver review. Scientific artifact preservation, not role-bound task execution.

**Next:** independently review R330 key extraction/degree before any promotion; derive E6,N5 and j>=5 fifth normalized pole jet for candidate universal c[r,r-5] or exact failure. Favor a true two-index positive-cone mechanism to reduce the remaining q>=641,0<=k<=q-321 region. Treat source storage and proof acceptance separately.
