# R517 continuation — signed BRC s=3, m=40

Date: 2026-11-04. Frozen input R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Immediate predecessor R516 @ `78a568ed73fd8372631c58dd665e810e3903b665`. Durable destination: Draft PR #1708, branch `research/r388-signed-k3-corank16-20261029-emr3`.

Mother question: classify all-positive-integer signs of right-edge signed BRC Toeplitz minors and identify algebraic mechanisms of sign switching.

Completed author-side exact unit: conditional `D_40(k)>0` for `1<=k<=7` and `k>=29`, `D_40(k)<0` for `8<=k<=28`. R516 yields `D_39(k)<0<D_40(k)` for every `k>=29`.

Proof/reproduction: `R517_PROOF.zh-CN.md`, `R517_VERIFY.js`, `R517_EVIDENCE.json`. Full integer certificate uses 80 Newton coefficients, 241 integer polynomial identity checks, all 80 shifted coefficients strictly positive at k=29, 28 finite signs, 20 direct 40×40 Bareiss checks and 800 signed branch equivalences. Independent: `R517_INDEPENDENT.py` and `R517_INDEPENDENT_EVIDENCE.json`, 17 direct 40×40 SymPy Berkowitz checks and 800 formula comparisons.

Next independent executable unit: `s=3,m=41`; degree <=246, 82 Newton coefficients, 247 integer polynomial checks. Separate structural route: dominant poles/phase of fixed-k rational order generating functions at k=7,8,28,29. Review prerequisite: verify frozen R452/R462 polynomial lemma and this exact certificate.

Control: GitHub principal `awdawmip`; Sites read-only and backend disabled for this connection; Owner listing returned `CONTROL_QUOTA`, no native Researcher-ID, CLAIM, Result, or Driver admission asserted. Project evidence is an author-side draft; immutable scientific input, P000 and ACTIVE worldview preserved.
