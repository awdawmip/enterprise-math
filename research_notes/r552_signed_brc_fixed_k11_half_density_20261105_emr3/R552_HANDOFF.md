# R552 author-side research handoff

Objective: continue frozen R462 signed BRC Toeplitz-Hessenberg fixed-k sign-density program. Mother problem: sign behavior across arbitrary m and parameter k, with the separate s=3,m=63 classification still open.

**Completed unit (R552):** fixed k=11, prove the sets of m with D_m(11)>0 and D_m(11)<0 have natural densities 1/2 each. Use `R552_PROOF.zh-CN.md`, `R552_VERIFY.py` and `R552_EVIDENCE.txt` in this directory.

- Scientific frozen source: R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Reused R541 rational generating function and R551 single-prime noncyclotomic argument, no changes to P000/ACTIVE worldview.
- New exact facts: degree-21 Q; 21 rational Rouché disks radius 1/1000; 210 pairwise disjoint certificates; unique maximum-modulus nonreal conjugate pair with |lambda|>11 vs others <6. Root-ratio polynomial degree420; complete q<=352800 cyclotomic exclusion via 815 F_65537 gcd tests. Finite recurrence 0..1024: +515, -510, 0=0, 300 changes.
- Current authenticated GitHub identity: awdawmip. Native Researcher-ID: EM-DIRECT-51D8CE; activity RA-5F3A05195AD2B7CCBE766FA4; formal CLAIM and independent Driver review not obtained.
- Scope: an author-side exact-computation-assisted algebraic result under frozen auxiliary scalar definitions. Formal independent review remains due.
- Next discriminating task: k=12 root dominance + cyclotomic exclusion; parallel search for k-uniform certified root separation, as well as s=3,m=63 full parameter sign classification. Publish exact inputs and checker evidence at the task's actual authority level.

Remote evidence saved in the existing project Draft PR #1708 research branch. This handoff preserves the present frontier; no new execution authority or task publication is implied.
