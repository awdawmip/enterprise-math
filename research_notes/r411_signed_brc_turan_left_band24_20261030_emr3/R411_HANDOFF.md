# R411 — Portable signed BRC research handoff

- Immutable inputs: GLOBAL_KNOWLEDGE_V1 main@07d09a5ffc60a64ebb38eee2ab1dabc900883d18; Enterprise Math main@bb6e9bc39ce163763e6ad3febc229a44bd53cf84; R410 in Draft PR #1708 at db4e02917c315bfdc15cb656b7a96b497d0af0ae.
- Exact author-side result: for integer r≥25, with δ_(r,s)=[t^r](1−t)(1+t)^(2s)(1+t²)^(r−s), H_(r,s)=binom(r+s,2s)δ_(r,s), D_(r,s)=H²−H_(r,s−1)H_(r,s+1), prove D_(r,24)>0.
- Artifacts: R411_PROOF.zh-CN.md (full rational-polynomial proof), r411_verify.py (exact SymPy certificates), r411_independent_verify.py (independent standard-library checks), R411_EVIDENCE.json (both complete positive coefficient lists, machine hashes).
- Reproduce: python r411_verify.py && python r411_independent_verify.py; expected R411_EXACT_PASS 2 49 49 96 288; R411_INDEPENDENT_INTEGER_PASS 10 points, 30 Catalan-kernel checks. Generated canonical JSON SHA256 28c6e68c88adf262bbe92f5bb394887697acb8e78eacf36c076083c69b109603.
- Scope: original twelve signed BRC branches only; precondition R404 Catalan kernel and R403 Jet transfer independently unreviewed. No native X6/physics bridge, no certified Result/Driver Review.
- Actual control: GitHub identity awdawmip; native manifest authority_granted=false and incomplete task packet; owner query CONTROL_QUOTA. Do not borrow predecessor claim, issue proof admission or imply checkpoint registration.
- Highest research frontier: left s≤24 and right r−s≤128. Remaining candidate domain s≥25, r−s≥129; first (154,25). Next unit fixed s=25, all integer r≥26, proof/counterexample; seek uniform in both s and k. Do not redo R411 unchanged.
- GitHub PR is primary handoff destination, immutable author-side source; proof of publication is separate from scientific correctness and native workflow admission.
