# R88 — Cubic Lie compression: 70-coordinate one-probe tomography
Date: 2026-10-17. **AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED**. Read pins: GLOBAL_KNOWLEDGE_V1 `main@fb9349bd3044f563df4e4fc1ecdd79c25375e31a`; Enterprise Math `main@0af9e429ddfe16c7d1461cea3e891a44ff86c291`; P000 `ACTIVE_LOCKED`. Follows unreviewed R87 (150 prestate quintic coordinates sufficient).

## Declared formal observer
Let (R_5=\mathbb Z\langle X_1,...,X_6\rangle/(X_i^2,\operatorname{deg}>5)) and (S(w)=\prod_t(1+\epsilon_t X_{i_t})=1+T_1+...+T_5) for a finite ordered signed native-axis path. Signed integer word coefficients retain ordered provenance; they are **not** direct positive-rational BRC mass readings, and no physical readout is claimed. There are 150 legal cubic and 3750 legal quintic words (adjacent letters unequal).

## Exact theorem: 70-dimensional cubic Lie image
Because (X_i^2=0), each factor equals (exp(\epsilon_t X_{i_t})). Thus the cubic component of (log S) is the projection of a Lie polynomial:
[
L_3=T_3-\tfrac12(T_1T_2+T_2T_1)+\tfrac13T_1^3.
]
For zero-displacement CYCL paths, (T_1=0) and (L_3=T_3). The six-generator degree-3 Lie image has dimension **70**: for every (i<j<k), two independent multilinear brackets ([X_i,[X_j,X_k]]), ([X_j,[X_i,X_k]]) (40 total), plus 30 repeated-letter brackets ([X_i,[X_i,X_j]]=-2X_iX_jX_i) with (i\ne j). Distinct-triple coefficients satisfy, if (a=[ijk]L_3, b=[jik]L_3),
[
[ijk,jik,ikj,jki,kij,kji]L_3=(a,b,-a-b,-a-b,b,a).
]
For repeated letters only (iji) is legal. Hence the 70 coordinates
[
U=\{ijk,jik:i<j<k\}\cup\{iji:i\ne j\}
]
determine all 150 cubic coefficients once (T_1,T_2) are known. Rational intermediate BCH coefficients are handled by the integer identity (6L_3=6T_3-3(T_1T_2+T_2T_1)+2T_1^3) (no floating point; final exact divisibility). The bracket coefficient of (iji) **need not be even** for actual paths; no parity claim is made.

## Exact theorem: 70 quintic readings at each of two times
Append one native four-step loop (c_{ab}=(a,b,-a,-b)), (a\ne b), and write
[
Q_2=X_aX_b-X_bX_a,quad Q_3=-X_aX_bX_a+X_bX_aX_b,quad Q_4=X_aX_bX_aX_b.
]
Then (Delta_5=T_5(wc_{ab})-T_5(w)=T_3(w)Q_2+T_2(w)Q_3+T_1(w)Q_4).
The nuisance (N=T_2Q_3+T_1Q_4) is known. For each selected (u\in U), choose ((v_u,s_u)=(uab,+1)) if the last letter of (u\ne a), and ((uba,-1)) if it equals (a). Both are legal. Then
[
\boxed{[u]T_3(w)=s_u( [v_u]T_5(wc_{ab})-[v_u]T_5(w)-[v_u]N).}
]
The 70 different (u)'s yield 70 **distinct** quintic readout words. These 70 prestate and 70 matching poststate readings, plus known (T_1,T_2), recover all 150 cubic coefficients by the Lie relations above. If CYCL boundary safety is required, choose (a,b) away from the two boundary axes; at least four of six axes remain.

Compared to R87's 150 prestate readings, the sufficient prestate budget falls by 80 (=53⅓%); 70/3750=7/375≈1.8667% of the entire quintic observer at each time. **This is sufficiency, not global sample-count optimality**; no arbitrary-order or physical measurement claim is made.

## Exact finite evidence and reproducibility
The separately packaged `verify_r88.py` checks the theorem directly with integer truncated-word dynamic programming and (6\log S) relations: 184 path samples (93 zero displacement), 552 path/probe cases, **110400 coefficient comparisons**, 38640 selected prestate readings; no errors. It tests open and closed paths, up to 20 steps, and three probe axis-pairs. Cold-unzip rerun: `R88_70_BASELINE_PASS`; four source hashes verified. The mathematical proof is algebraic, and these checks are only a bounded experiment.

Portable evidence ZIP SHA-256: `2677d55ffb005cbadd4d137851a605bfd5cf92b1d09ccda592269edfcf244a30`.
File checks: `PROOF_R88.md=de37f36f7f4019985a5c2154df4bb516d46434f8c33a7a2b4fa01fc4b6b68dfd`; `verify_r88.py=a4e70ee210c347de7b35756afc3bfc8b85eda3e38855fa5db061069835152365`; `R88_CERTIFICATE.json=1d04845362e6cd7c0c1f72784c55d2c6e10f586df03df1ca3e9f270476bc706f`.

## Authority, residual, next unit
Native owner read: `CONTROL_QUOTA`; Researcher session attempt: `STATIC_READONLY_SCOPE_DENIED`. Thus this commit is an **author-side preservation surface only**, not canonical Task/CLAIM/Result/Driver review. Full code/certificate are in the portable local bundle, not asserted as persisted here. R86/R87 long-path claims were not rerun.

Next: determine whether fewer than 70 prestate quintic readings suffice when post-probe information is available, using source-realizable CYCL collisions rather than an abstract 70-dimensional information bound. Establish weighted BRC interface normalization before claiming any physical/native readout.