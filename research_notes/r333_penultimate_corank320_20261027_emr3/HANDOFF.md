# R333 — Reproducible research continuation / owner intake

Purpose: exact Newton difference positivity of signed ordered-six-edge BRC auxiliary polynomials, not native X6 physical dynamics.

Pinned input: GLOBAL_KNOWLEDGE_V1 main e1cf9d381d32b4cd72648613189aa0ebbe0b0a2a. P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview blob 99238c3466eb0805748bae01fd1a20868a5a351e (both unchanged). EM Source main at start eb2ba75469454c5b6f6b46c683b1d4ecdce897b7. Prior source R330 commit 7c73f56263c3f0515aa28e55ced2d4c703b8e086 (exact all-r rational extraction/degree), R331 98e7ccce13c07fa91c816314b01f0681dc7c264e (r<=256), R332 16b2209bda28aa8d8082331820e0e1e62410fef3 (r<=300), existing Draft PR #1568.

Do not repeat completed units: universal penultimate c_(r,r-1)=6^r(6r-1)/5 and highest c_(r,r)=6^r for every integer r>=1, via low-order E0-E2 rational extraction, g_j(4/5), g'_j(4/5), exact top-two polynomial coefficients, Stirling conversion; full author-side proof in R333_PROOF.zh-CN.md. Twenty new exact corank bands r=301..320 for all u>=0 (on R330 degree identity), total 321 bands r0..320. Exact Python runs: 6230/6230 positive Fraction, B_s0..962, inside-triangle 464166 positive, 194675 exterior negatives retained, 20 extra-degree and leading-coefficient checks; SHA256 ordered c sequence b873ec12fd6c5f305fa962bf8244db68cdf09c7bb03af383f022f72402c31d17. Independent exact symbolic bracket identities plus original signed-tail r1..32 matched. Evidence JSON is compact; R333_VERIFY.py regenerates all per-r output and SHA.

Run:
python R333_VERIFY.py --min-r 301 --max-r 320 --out R333_EXACT_EVIDENCE.json
python R333_PENULTIMATE_SYMBOLIC.py --max-r 32 --out R333_SYMBOLIC_EVIDENCE.json
Optional --prior-r332 <full original R332 JSON> checks exact r300 overlap. No floating signs or pretruncation.

Next rigorous science unit: g_j''(4/5), E3, N2 -> closed all-r c_(r,r-2), positive proof or exact obstruction; then pursue 2-index invariant cone. r321 bounded computation is optional, not a uniform theorem. Existing difference cone uncovered q>=641, 0<=k<=q-321.

Researcher-ID EM-R333-9B1FB4 local, not Source issued; current GitHub login awdawmip, capability admin/push. Native em_control_tasks once CONTROL_QUOTA; owner not authoritatively verified, native claim/result/review not issued. AUTHOR_SIDE/UNREVIEWED/NOT_ADMITTED. Preserve prior authors and shared context, do not present as independent review.