# Stage134 — exact execution and source integrity evidence

Date: 2026-10-26 (Asia/Shanghai). Scope: external N=14 ternary iid auxiliary sequential test; positive-rational ordered-history BRC carrier. Classification: AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF / DRIVER_UNREVIEWED / NATIVE_CLAIM_UNVERIFIED. Not a native P000/Heartbeat/X6 theorem.

## Local actual executions

Two independently structured author-side programs ran successfully with Python stdlib Fraction/integer arithmetic, without floating-point approximations or Monte Carlo:

1. Bottom-up exact Bellman and four-corner observer solver `derive134.py`: PASS. Bellman 680 states, 1238 strict positive nonchosen-action gaps, no negative gap, only B=(11,0,1) Q/C and G=(9,3,3) Q/C tied. Root 2442656918158809916870213/5949675882197721022464. Minimum strict gap 129758627/4504246272. It independently checked exact balance, endpoint values, margins and primal-dual saturation.
2. Separate recursively computed Bellman + exhaustive integer-numerator literal-history DFS `INDEPENDENT_ORDERED_STAGE134.py`: PASS. First hits B=11 words and G=756 words; same separate P/Q mass fractions as full proof. Each of the four deterministic corners matched all four observer fractions exactly. Mixed cross term=(0,0,0,0). Deterministic corner prefixes (00,01,10,11): 736690 / 704938 / 736558 / 704806; terminal words: 491127 / 469959 / 491039 / 469871.
3. Independent candidate-only scan of the Stage135 Bellman dual ray `scan135.py` plus a separately authored exact candidate Bellman check `check_stage135_dual.py`: candidate ties B and A=(7,3,0), 1238 other strictly positive gaps. This proves only the candidate dual data, not its primal admissibility or a Stage135 theorem.

## Actual local SHA256 of source and evidence files

- derive134.py: `79b1f5f5377010bc987a5e02d322e874be0bad79ad4bc8b681d9c24078c039d3`
- derive134.stdout: `7e953c9e2e0cdb39424670498ced1a9dbeab4217abc565f2e2c1fb35a353054c`
- INDEPENDENT_ORDERED_STAGE134.py: `2be48bc0b1c9377b638e0fb6e0241884817cc0cb2f0ced65b21654dc1055d3fc`
- ordered134.stdout: `fdc11d2869d07bd4e376ce580f2de03f696054d8af6e233225149ec68fcf0622`
- certificate134.json: `b81589b4d9453ec44d559fff274f5ac464042f6293e1f5fb76c7563ace2eabf6`
- ordered_evidence134.json: `0433b982a310ceb751e90d4bd5f2baf73fd7dc6feae69a906de15c146c3edfcc`
- scan135.py: `5fda22b353ad252d79744c9311c372dd547be56fe161bf23d114fec731384a91`
- scan135.json: `f172017eee96d36931b38fd6fe29860ae47364f3ad6a04ca164d30d6f17e32fe`
- check_stage135_dual.py: `8ff276d7a62c4fc01afcdb1e46b9691dea65cd2765e8b5d22b5b704170d086ce`
- check_stage135.stdout: `1283b54e0322ad8bac688c3f6648f118efdcd9471dc21b16381fd0498bd85590`
- scan135.stdout: `ea8808e07cb3504f8ab2af52d0d6c571615d85382b02f4070c549c38d641ef0a`

## Remote provenance and distinction

GitHub immutable readback has been performed for three *nonempty* project files:

- Complete proof `research_notes/n14_aux_iid_affine_134_20261026/PROOF_STAGE134.md`, commit `926b95b28a2ca178fbfd5e9e0112fb630fe71030`, Git blob `a3617b8862c92ef97090babe549309642f748597`, 7551 characters.
- Portable solver `research_notes/n14_aux_iid_affine_134_20261026/VERIFY_STAGE134.py`, commit `03c50874f8e010c72b8fcdf9bf38a32bcb40413b`, blob `adf52500fa707b4d628dd88c943746135e4f87c0`, 3236 characters.
- Independent portable DFS `research_notes/n14_aux_iid_affine_134_20261026/INDEPENDENT_ORDERED_STAGE134.py`, commit `29b366935430b675357ae973fdb44f4407f6eb39`, blob `d380130f258cd02e534f8e1dfa903ddfeeeac7d6`, 3550 characters.

The portable GitHub scripts implement the same algorithms and identities but are **not asserted byte-identical to locally executed source**, and GitHub readback is not remote execution. The local artifact package contains actual executed source and stdout for reproducibility.

Frozen sources: global `awdawmip/chatgpt-global-knowledge` main@0640165130b1a9268805f3ee02e8fb88ecfe368e; EM initial source read main@56f75ca89dc8a07824e0c02200dcc41fff6a9133; Stage133 already authored in a separate parallel process and not recredited here.

Native Enterprise Math `em_control_dispatch` attempted once (request `r5-20261026-0506-control-dispatch-01`) and returned `CONTROL_QUOTA`. No native winner, CLAIM, Result freeze, Driver review or admission verified; this author's ordinary GitHub notes do not impersonate them. No Google Drive fallback was needed; authorized GitHub project writes succeeded.
