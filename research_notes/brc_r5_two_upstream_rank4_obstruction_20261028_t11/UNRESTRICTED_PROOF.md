# R5 Addendum: exact GLOBAL policy-class exclusion of the two-upstream six-leaf tree

**Date:** 2026-10-28 Asia/Shanghai. **Mathematical status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. This supersedes the earlier pending unrestricted check for the **same** six-leaf P/Q model, without changing the original restricted result. Global here means *every admissible real behavioral policy for this exact variable-depth tree*, not every possible larger N=3 observation model.

## Full action scope and result

Retain the six strictly positive leaves and likelihood prefixes in RESEARCH.md. At t1, each distinct LR branch A,B may stop and declare P, stop and declare Q, or continue. At t2 side leaves A-L and B-H must terminate and may declare P or Q. At t2 the two distinct hidden histories A-C and B-C share the single signature (time 2,R=1), where seedless LR policies must use one common distribution over actions {stopP,stopQ,continue}; full-history policies may distinguish the two histories. If continuing C to t3, all four C leaves have distinct t3 LR and may declare P or Q. No persistent common random seed is allowed. Every local simplex parameter is any real number.

For O=(e_P,e_Q,E_Pτ,E_Qτ) and λ=(912,456,128,-194), the exact global inequality

    912 e_P + 456 e_Q + 128 T_P - 194 T_Q <= 857

holds for **all** real locally randomized seedless LR policies. The best complete-history policy reaches **868**, so the global support gap is exactly 11 and the full/LR convex hulls are unequal. This strict-positive model is therefore **excluded** from the mother target (equal hull, unequal true images).

## Standalone exact Bellman proof, no numerical optimization

For P mass p, Q mass q at a time-t stop, declaring P contributes 456q+t(128p−194q) and declaring Q contributes 912p+t(128p−194q) to λ·O.

Immediate t1 optimal stop scores are A=163, B=683. At t2, side-state best stop scores are A-L=44 and B-H=487. After exact leaf-level optimal t3 terminal declarations, the shared C actions have these values:

| Common t2 C action | Hidden A-C score | Hidden B-C score |
|---|---:|---:|
| stop, declare P | 54 | 81 |
| stop, declare Q | 130 | 195 |
| continue, optimally declare at t3 | 119 | 207 |

For any **fixed common** C action the distinct t1 branches optimize independently. Thus the complete Bellman table is

| Common C action | A max(163,44+C_A) | B max(683,487+C_B) | LR total |
|---|---:|---:|---:|
| stop P | 163 | 683 | 846 |
| stop Q | 174 | 683 | **857** |
| continue | 163 | 694 | **857** |

All LR deterministic policies thus have score ≤857, and equality occurs. Every real seedless behavioral policy also has score ≤857: a trajectory visits each (t,LR) information set at most once, so the finite expected score is separately affine in each local action distribution, and any global maximum over products of local action simplexes occurs at deterministic vertices. This does *not* introduce a shared persistent random seed.

Under full history, A can take the C stopQ option (max of t1 A stop 163 and continue 44+130=174), while B can take C continue (max of t1 B stop 683 and continue 487+207=694). Therefore the exact full maximum is 174+694=**868**. One full deterministic witness: t1 continue A and B; at A-C stop Q; at A-L stop P; at B-C continue; at B-H stop Q; at t3 B-C low declare P and high declare Q. A-C t3 suffix actions are unreachable and arbitrary.

Its exact observation vector is

    O*=(85/96,11/24,9/4,9/4),

and λ·O*=868. Thus λ·O* exceeds the sharp LR support bound 857 by **11**. QED.

## Independent exact exhaustive check and limitations

Actually executed Python Fraction verification `VERIFY_UNRESTRICTED.py` enumerating *all* full deterministic descriptions: 3²·3²·2²·2⁴=**5184**, and all LR deterministic descriptions: 3²·3·2²·2⁴=**1728**. Respectively **196** and **124** distinct exact four-vectors arise. The same signed λ has exact LR max 857, exact full max 868, and the declared full witness. `EXACT_UNRESTRICTED_OUTPUT.txt` ends `ALL EXACT UNRESTRICTED CHECKS PASSED`. The support proof is the Bellman table plus the all-real multilinearity argument, not a float search. A numerical 4D convex-hull search was used as *discovery only* to suggest λ and did not contribute to the final proof.

SHA256 of locally executed unrestricted verifier: `f7c024291b2d3d31fdafa9bd90f171c426390b0d671eded2ff357334aa87357f`. Output SHA256: `4fd7942a77b3bd2993dd1b54b708da354eced3b9d49b2ce57e1af9803644cb34`. Verify remote Git blobs against actual locally executed files (expected source `b006207082667743e3823d269bd6806e8ce08ceb`, output `d16918618e4ccf2ef635e5718085675afa92cd96`).

Model typing stays external finite probability / likelihood-ratio observation, with explicit X6 Cell history labeling and separately typed time per RESEARCH.md; it is not native X6/BRC physical dynamics. Source-native active Owner, CLAIM, RR or independent Driver review were **not** obtained: the gateway returned CODE_REVIEW_REQUIRED / research_authority_granted=false and CONTROL_QUOTA. A GitHub author proof is not canonical mathematical admission.

## Next research unit

Search a **different** rational strictly positive tree in which two independently controlled upstream LR signatures merge, yet the exact complete Bellman common-action optimum equals independent full-history choices for *all four-dimensional signed λ*. Only candidates passing global convex-hull equality proceed to semialgebraic all-real LR image nonconvexity tests. Reuse the three-row Bellman table as a fast candidate elimination tool, and the preceding single-root stop-masking theorem as a starting sufficiency mechanism; keep all native/observer information-preservation boundaries.
