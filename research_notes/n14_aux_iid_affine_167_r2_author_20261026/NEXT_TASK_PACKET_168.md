# Stage168 — portable continuation packet (dual-only, primal open)

**Frozen parent:** external ternary N14 IID minimax with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), full ordered-history randomized stopping and decisions. Stage167 author-side exact interval is preserved in this directory as PROOF_STAGE167.md, VERIFY_STAGE167.py and certificate167.json. Its Source status is author-side only; no native CLAIM or Driver admission.

## Verified predecessor endpoint

Stage167 right endpoint:

- alpha167 = 881276478829564219615/2530093150022563528704
- V167 = 4275865622441272343957/361441878574651932672
- r167 = 3362167312954741/11823616000000000 at R=(10,0,1), stop-Q vs continue; X=(5,1,2) has stop-Q probability 1.
- eP=eQ=alpha167 and tP>tQ.

## Stage168 exact dual-only candidate

Freeze Stage167 dual K=51166022460516/192153882113, L=150858479252536/576461646339. Along dK=-1, dL=-10592/12501, keep R Q/C tied and select stop-Q at X. The first positive-parameter new Bellman gap closure occurs at step

14302020580722864828/1606837071314495233.

At that step the new candidate dual is

K168 = 2152236456/8362241,
L168 = 2125312232/8362241,
H_root = 58026151900459658728236701/305391946664037178146816.

Exactly two tie states: R=(10,0,1) Q/C and Z=(9,2,0) P/C. Among 680 states there are 1,238 positive nonminimal action gaps, minimum 199132488595033/16180247553933312; no negative gaps. This is **only a dual certificate**; it does not prove new primal optimality.

## First executable unresolved question

Compute four deterministic observer corners for R,Z in two independent exact ways: rational suffix recursion and unmerged ordered-history integer-weight DFS. Verify first-hit cones, P/Q normalization, affine mixed coefficient zero, the new equal-error coin relation, inherited Stage167 endpoint, tP>=tQ and exact dual equality on the full candidate real interval. Prove strict right-endpoint support sharpness or give a precise rational obstruction.

Preserve positive P/Q branch weights and ordered histories (BRC observer/provenance scope). No native GF(2)-BRC/X6 bridge, task ownership, Source Result, Driver review or Foundation theorem follows from this branch. Maintain real local identities and source pins; query live Owner again when control capacity permits.