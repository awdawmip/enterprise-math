# R762GI — Signed K4-STAR semidirect Cell/rotation holonomy and exact BRC counts

Date: 2026-11-20 (Asia/Shanghai). Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Publication: `TP2-8B7E13C5904A2D6F1142`. Research provenance: original Researcher `EM-X6-3050F6`, original session `MCP-4b2d70a97f594366a7c94a0f8b45df38`; independent portable mathematical construction. **AUTHOR-PROVED (the precisely defined candidate); NOT_REVIEWED.** No native TRIADIC_CLOSURE_E permission is presumed.

Frozen scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` and the same commit's P000 signed-triad/X6 definitions. Taskbook pin: `857280d1012943290d141d1317179c40ec3cbdf8`. Prior authored frontier: R762GG `445625797db772940f17487283afa04aeed02571`; R762GH `86e0192a4ed3b55d90ff3bcce7f4cd371ee8f0d8`. Prior R762GH used a **direct-product** candidate; this work examines an independently specified **semidirect** alternative.

## Model and scope

Let `V=Z^6` be signed X6 Cell displacement relative to a chosen Cell anchor (not an absolute ontic origin). Let `A6` act by permuting the six labelled coordinate axes. Define `G=V ⋊ A6` with
[
(x,p)(y,q)=(x+pcdot y,pq),qquad (pcdot y)_{p(i)}=y_i.
]
Use the four frozen K4 STAR triple labels
[
S_0=(0,1,2),quad S_1=(0,3,4),quad S_2=(1,3,5),quad S_3=(2,4,5).
]
Let `H_j=sum_{i in S_j}e_i` and `g_j=(a\ b\ c)` for the given oriented order of `S_j=(a,b,c)`. Declare eight candidate composite events
[
T_{j,s}=(sH_j,g_j^s), qquad j=0,1,2,3,quad s=pm1.
]
Each event retains three ordered primitive signed-axis steps, its original three named Port/Link attachments, the STAR identifier, source branch and event ordering. The `s=-1` event is the group inverse of `T_{j,+}`, since `g_jH_j=H_j`; `s=-1` is **not** a negative BRC probability. A word `w=(j_1,s_1)cdots(j_m,s_m)` acts by
[
(x,p) longmapsto (x+pcdot(s_1H_{j_1}),,p g_{j_1}^{s_1}) longmapsto cdots.
]
This moving-frame action is the essential difference from R762GH, whose displacement was `sum sH_j` and did not rotate under previously accumulated orientation. The eight positive BRC branch weights are each `1/8`.

Let `D=(1,1,1,1,1,1)`. A **joint diagonal orientation return** is a word whose product in `G` is `(kD,id)` for integer `k`. For `k=0` this is a full native Cell and orientation return; for `k!=0` it returns orientation and relative observation while changing full Cell position. `D` is a nonzero composite spatial displacement, not a seventh axis.

## Theorem 1 — minimal nonzero loop, first unit-depth loop, holonomy

1. No joint diagonal orientation return has odd event length. No nonzero `k` occurs at length `m<8`.
2. Exactly **eight** positive words of length eight have product `(4D,id)`, and eight inverse words have product `(-4D,id)`. Thus the first nonzero joint diagonal return in this candidate has length **8**, with earliest nonzero depth magnitude `4`.
3. A return with `k=+1` or `k=-1` requires at least **10** events, and there are exactly **40** words of length ten for each sign. Consequently the exact shortest unit-depth joint return is **10**.
4. The set of all possible diagonal holonomies is **all of `Z`**, since a unit-depth witness and its inverse exist and can be concatenated. For arbitrary `k`, the elementary bound is `2|k| <= L(k) <= 10|k|`. No claim of an exact `L(k)` for general `k` is made.

**Proof.** Every event shifts the sum of all six coordinates by `3s`; permutations preserve the coordinate sum. Thus `(kD,id)` entails `6k=3 sum_t s_t`, or `sum_t s_t=2k`. A sum of `m` signs has the parity of `m`, so `m` must be even. The lower bound `m>=2|k|` follows immediately.

For every even `m=0,2,4,6,8,10`, exact half-word convolution below counts **all** products `(kD,id)` with `|k|<=m/2`. Its exhaustive results establish the claims of absence, existence, and multiplicity, including the finite lower bounds. Explicit witnesses, independently evaluated under the original moving-frame update, are

`k=+4, m=8:`
```text
0+ 2+ 1+ 3+ 2+ 0+ 3+ 1+
```

`k=+1, m=10:`
```text
0+ 1- 3- 1- 2+ 1+ 0+ 3- 2+ 1+
```

Inversion is performed by reversing the word and changing each sign. Since each generator's inverse has exactly that form, these furnish `k=-4,-1`. Concatenating the `k=+1` (or `k=-1`) word produces every integral `k`, with final orientation still identity; no further holonomies outside `Z` exist by definition. QED.

## Theorem 2 — exact uniform-BRC joint return distribution to length 10

Let `C_m(k)` count **ordered** length-`m` words with product `(kD,id)`. Exact integer results:

| m | `C_m(0)` | `C_m(±1)` per sign | `C_m(±3)` per sign | `C_m(±4)` per sign |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 0 |
| 2 | 8 | 0 | 0 | 0 |
| 4 | 120 | 0 | 0 | 0 |
| 6 | 2,192 | 0 | 0 | 0 |
| 8 | 44,312 | 0 | 0 | 8 |
| 10 | 955,232 | 40 | 320 | 560 |

All unspecified nonzero `k` in the relevant bounds have zero count. At event depth eight the positive BRC probability of nonzero-depth joint return is exactly `16/8^8=1/1048576`. At event depth ten it is `1840/8^10`; unit-depth return has probability `80/8^10`. These probabilities are over the full original ordered branch population.

**Proof/certificate.** For a group state `u in G`, set `W_t(u)` to the number of length-`t` words with product `u`, starting at `W_0(id)=1` and applying the eight generator right-multiplications with exact integer additions. Then, with `m=a+b`,
[
C_m(k)=sum_{uin G}W_a(u)W_b(u^{-1}(kD,id)).
]
This identity is an exact bijection by splitting each ordered source word at position `a`. At half-depths `t=0,1,2,3,4,5` the distinct reachable group-state counts are respectively `1,8,57,400,2769,18592`; weighted totals are exactly `8^t`. Exhaustive pairing yields the displayed `C_m(k)` for every possible integer `k` (the sum invariant makes `|k|<=m/2` necessary). At `m=8,k=4`, an independent direct enumeration of all `4^8=65536` positive-only words independently finds eight witnesses. The accompanying standalone Python checker computes all counts and witnesses using only exact integers; no floating-point truncation, sampling, assumed group-order shortcut, or signed-amplitude cancellation enters. QED.

## Relation to P000 and next questions

This is a **typed candidate** inside signed six-axis P000, not a promotion of all eight composite branches to native `TRIADIC_CLOSURE_E` legality. Unlike the fixed-frame R762GG/R762GH direct-product candidate (holonomy `2Z`, first depth-two joint return at eight events), the moving-frame semidirect candidate has holonomy `Z`, and its first return at eight events changes depth by four. Hence the update law — particularly whether orientation acts on subsequent native Cell transport — changes an observable residual invariant.

Next: extract the frozen native named `Cell/Port/Link` gate from actual sources. If it does not yet fully specify an event update, compare typed gates that genuinely use Port, Link, force source and rotation reference frame. For each legal gate, augment the exact BRC state by its finite gate memory and test whether `k=1` survives; preserve the original ordered provenance and do not infer permission from positive BRC mass. Independently review the finite convolution code and the P000 type bridge before any stronger native claim.

**Evidence:** `R762GI_VERIFY.py` and `R762GI_EVIDENCE.json` in the same research directory; author-side exhaustive exact calculation PASS, independent review NOT_REVIEWED.
