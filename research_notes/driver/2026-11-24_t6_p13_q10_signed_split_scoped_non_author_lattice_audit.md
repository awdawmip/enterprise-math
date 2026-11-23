# T6 maximal-p13 order-10 signed splits: scoped non-author lattice and combinatorial audit

Date: 2026-11-24 (Asia/Shanghai). Role: RESEARCH_DRIVER `EM-DVR-DEBB5E`, own SID `MCP-9b4714dc46b948afa4875a86c89c713c`. This is **scoped scientific review evidence**, not a Native Driver Review or Result admission. Original computation/contribution remains with the on-hour researcher, SID `MCP-7f3df4435e40430b832e8d5ff2137718`, Activity `RA-A468735D7C934B25C4B9614F`. Review is non-author but **not blind**: shared project and the author's exact certificates/kernel were consulted.

## Source and scope

Pin the researcher's original 13-adic six-congruence Python kernel:
`awdawmip/enterprise-math@de78443d23578a66d3ae79f2a045e4be8e756c50:research_checks/T6_P13_Q10_SPLIT2_8_NEG11111111_SLICE_REPLAY_20261123_2300.py`.
Exact author outputs under review:

- [split (2,8), negative q=1^8, complete finite roster](https://github.com/awdawmip/enterprise-math/blob/09377053714e6a3f43507fb989318e1abfa4da8a/research_checks/T6_P13_Q10_SPLIT2_8_NEG11111111_62528_75582_AND_FULL_FAMILY_AUTHOR_EXACT_CERT_20261124.json);
- [split (3,7), negative q=(7)](https://github.com/awdawmip/enterprise-math/blob/52a8412a2c718220b3c50017009a6f6e60da3297/research_checks/T6_P13_Q10_SPLIT3_7_NEG7_FULL_AUTHOR_EXACT_CERT_20261124.json);
- [split (3,7), negative q=(1,6),(2,5),(3,4)](https://github.com/awdawmip/enterprise-math/blob/3c626d934d0b16464c7a7d6d9b96b6d384fe543f/research_checks/T6_P13_Q10_SPLIT3_7_NEG_LEN2_ALL_THREE_AUTHOR_EXACT_CERT_20261124.json).

Frozen science: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`; side exponent-mass cap `C=2331`. Here the enumerated r=1..12 named rosters may form an over-inclusive superset of truly maximal-prime-13-smooth cofactors; elimination on that superset is safe.

## Independent exact combinatorial crosscheck

For positive q-total 3, allowed nondecreasing q-patterns `(3)`, `(1,2)`, `(1,1,1)` have respectively `12`, `12^2=144`, and `binom(14,3)=364` named r-rosters, giving **520** positive rosters.

A negative `(7)` gives `12` rosters, hence **6,240** raw signed pairs. No q-name overlaps can occur with these positive patterns.

For each negative q-pattern `(1,6)`, `(2,5)`, `(3,4)`, the named roster count is `12^2=144` and the raw pair count is `144*520=74,880`. Exact common-atom cancellation counts follow without trusting the exhaustive computation:

- `(1,6)`: each fixed q1,r negative atom occurs in `12` positive `(1,2)` rosters and `binom(13,2)=78` positive q1^3 multisets. Thus `144*(12+78)=12,960`.
- `(2,5)`: positive `(1,2)` contributes `12` matches per fixed negative, so `144*12=1,728`.
- `(3,4)`: exactly one positive `(3)` atom matches per fixed negative, so **144**.

Total raw pairs **224,640**, cancelled **14,832**, remaining **209,808**, independently matching all three published per-pattern counts. For q=(2,8), negative q1^8 is `binom(19,8)=75,582` rosters and positive q2 or q1^2 is `12+binom(13,2)=90`, giving **6,802,380** full-family named raw pairs as recorded.

## Lattice completeness argument checked against the actual kernel

Let `L_k(u)=sum_{r=1}^{12} u_r r^{-k} mod 13^k`. Starting with `Z^12`, at stage `k=1,...,6` the source chooses a basis row whose `L_k` coefficient is a unit modulo 13. Replacing that row by `13^k` times itself, and subtracting its mod-`13^k` multiple from all other rows, produces **exactly the kernel** of the new congruence within the previous lattice: any integer coefficients of a solution have a uniquely prescribed pivot coefficient modulo `13^k`. The lattice index multiplies by `13^k`. Hence the six-stage exact index is `13^{1+...+6}=13^{21}`, as asserted by the code. HNF and LLL perform lattice-preserving basis changes.

For q0 signed multiplicities `u`, let `w_r=13r-1`; for fixed vertical positive/negative mass `c_+,c_-`, every original-budget-valid solution satisfies
`||diag(w)u||_2^2 <= (C-c_+)^2+(C-c_-)^2 <= 2 C^2=10,867,122`.
This follows by separating positive and negative parts of `u`; no cancellation reduces mass. The code's exact Gram-Schmidt minimum is
`78577530278042129705264382752517501995032553011464356025 / 4243983974238642688103181306691645151538473248349`,
approximately **18,515,039.35**, strictly larger than `2C^2`. Thus each coordinate in descending Gram-Schmidt recursion must lie in the **two consecutive integers** `floor(-center)` or `floor(-center)+1`. The source's two-candidate recursion is complete for its stated radius (provided the pinned lattice/inverses and the author's full finite traversal are correct).

This checks the *mathematical search-reduction logic*, not the claimed counts of every GS node or every accepted search, which were not independently rerun here.

## One nontrivial signed witness independently recomputed

From the author's `(3,7)` negative two-atom certificate, take
`pos=((1,1),(1,4),(1,11))`, `neg=((3,9),(4,1))` and
`u=(-99,-22,7,18,4,0,-8,-3,2,1,-2,2)`.
Direct exact integer recomputation gives vertical masses **712** and **1,311**, final side masses **2,823** and **4,362**, and all six signed residues
`sum_r u_r r^{-k} + sum_pos(13q+r)^{-k} - sum_neg(13q+r)^{-k} = 0 mod 13^k` for `k=1,...,6`.
Thus this reported relaxed modular witness is real and correctly **fails both 2331 side budgets**.

## Review disposition and remaining obligations

**SCOPED NON-AUTHOR CHECK PASSED** for the raw roster/cancellation arithmetic, the conditional saturated lattice construction, the GS two-candidate completeness reduction, and the cited witness. **Full exhaustive-search verification NOT PERFORMED**: independent reproduction of all per-roster sphere traversals and source-correctness of every frozen model reduction remain separate obligations. This review neither substitutes for an independent Native Review nor closes the p13 branch or global T6 objective. The active researcher's next q-pattern work remains untouched; ownership and all original author credits are unchanged.
