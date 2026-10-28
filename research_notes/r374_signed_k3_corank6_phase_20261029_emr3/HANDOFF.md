# R374 handoff — signed BRC K3 corank6 exact global PF2 phase

Research scope: AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED, no native CLAIM/Result/Driver approval. The canonical project note is `R374_PROOF.zh-CN.md`; checker is `R374_verify.py`, machine report is `R374_EVIDENCE.json`.

Frozen pre-run input: GLOBAL_KNOWLEDGE_V1 `main@5a25b3103a078bdd076640d171840d7aa4d61f2d`; Enterprise Math `main@5fa950a7d2f6e75cf091f5fd60e85dcf4a4a574a`; existing Draft PR #1592 source HEAD `3797ab05af7000d240a170f0301bb313d900fae2`. Original R346 K/J and R369 independent route Git blobs in proof.

Verified increment: all real theta > -1, corank6 13 finite raw-D Newton coefficients are PF2 iff theta <= sigma6 (unique c0 root in (901/1000,902/1000)). First 6 finite coranks' common PF2 interval shrinks from (-1,tau1] to (-1,sigma6] conditional on prior r1-r5 author-side classifications; exact witness theta=1: r1-r5 PF2, r6 c0=-645658536000000000. 28 interval-polynomial groups and 439 strictly positive rational Bernstein coefficients; plus 6 unbounded-tail coefficients. 13/13 independent symbolic route passed. No R363 extraction assumption, no native X6 transfer.

Reproduce in PR checkout (no input ZIP): `python research_notes/r374_signed_k3_corank6_phase_20261029_emr3/R374_verify.py --independent`; optional omit flag for faster solo verification. The program imports only R346; `--independent` also imports R369. Requires SymPy. Compare report with R374_EVIDENCE.json, including full 13-row polynomial digest. No historical large coefficient file is required.

Next: r7 fifteen raw-D coefficients, full Bernstein certificate on (-1,sigma6], then global obstruction cover if threshold changes. Audit R363 all-index theorem separately. Never infer formal Source owner, native result or P000 amendment from a GitHub commit.
