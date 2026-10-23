# C268 / Research2 — 24 newly certified four-free positive pair hulls (AUTHOR_EXACT)

**Authority:** This is a non-canonical author mathematical handoff, NOT an authorized Source Result, CLAIM, independent Research Driver review, native six-dimensional GF(2)-BRC theorem, or amendment of P000. This evidence derives from the **C195/H168 79-node positive-rational auxiliary** only.

## Immutable evidence and reconciled frontier

- Actual verified GLOBAL_KNOWLEDGE_V1 main: `61cfa2a580230863c0d02b5f818381adbb3cb11b`.
- Actual verified Enterprise Math main: `3db580c241ef46110ff4251adf29a2185e50eaa1`.
- GitHub actor: `awdawmip`. The C265 author archive identifies 213 strict-negative witnesses, 103 continuous-positive proofs, 47 unresolved among 363 eligible two-box hulls. Two *unmerged* C266 author branches together add nine **distinct** positive pairs: (4,16),(4,26),(4,30),(12,29),(16,28),(17,28),(23,28),(23,29),(27,30). Hence the reconciled, **not Source-admitted**, frontier is 213 negative + 112 positive + 38 unknown.
- This research uses the existing 35 C254 proof rectangles, old C256 negative witnesses, and exact C265 algorithm, not new enumeration of historical 15,685 candidate configurations.

## Exact mathematical object

Put `I=(5,50,55,56)`, `J={0,...,78}\\I`, `Q=2^128`, `H=2^166`, `Z=141421356237309504880/10^20`, `A=6912*50000^2/17^2`. Let `u_0,...,u_78` be the strictly increasing original 79 rational nodes, embedded in the sibling complete replay script. Let `B_j=floor( (Q*A/H)/((2-u_j^2)*(3-u_j^2))^3 * product_(r != j) [(Z-u_r)/abs(u_j-u_r)] ) > 0` for fixed `j in J`.

Define the exact four-variable auxiliary function

`F(v)=sum_(j in J) B_j * product_(p in I)[(Z-v_p)/(Z-u_p)*abs(u_j-u_p)/abs(u_j-v_p)] + sum_(k in I) [Q*A/(H*((2-v_k^2)*(3-v_k^2))^3)]*product_(j in J)[(Z-u_j)/abs(v_k-u_j)]*product_(p in I, p!=k)[(Z-v_p)/abs(v_k-v_p)]`.

**C268 theorem:** For every admissible *real* quadruple in any of the following entire rational **closed** four-dimensional rectangles, `F(v)>=2^128+124257021339851230269272891404511>2^128`.

| Basic root | v5 | v50 | v55 | v56 | Strict leaves | Exact midpoint splits | min floor(LB)-Q |
|--|--|--|--|--|--:|--:|--:|
| (0,16) | [4/543,9/613] | [43/62,57/79] | [18/23,38/47] | [13/16,121/147] | 3088 | 3087 | 124257021339851230269272891404511 |
| (5,21) | [2/271,6/409] | [7/10,18/25] | [53/68,4/5] | [13/16,23/28] | 2779 | 2778 | 769356085001379917978497393182991 |
| (18,29) | [1/119,6/409] | [12/17,28/39] | [60/77,34/43] | [19/24,41/51] | 1023 | 1022 | 138370912573772422127818574647616 |

**Proof:** Each positive fixed branch has an exact monotone rational factor `(Z-x)/abs(u_j-x)` in a pole-free, order-preserving interval, so endpoints bound unretained coordinates below. For each moving branch, the log-second derivative in its own variable is strictly positive; the sum of fixed branches retaining one shared coordinate with that moving branch is also convex. The existing **BASE** and **SHARED_(5,50,55,56)** formulas combine endpoint positive lower bounds and a **single** exact common tangent of the kept-variable convex sum. Consequently each leaf's rational `LB(C)<=F(v)` for all `v in C`.

The sibling complete proof program embeds the original 79 nodes, re-creates all 75 integer `B_j` using the unchanged floor rule, decodes all three exact binary preorder trees, and verifies **all 6890 leaves** by standard-library `Fraction` with `floor(LB)-Q>0`. An internal `0/1/2/3` splits at the exact rational midpoint in that coordinate; closed children exactly cover the parent. A `B/A/C/D/E` terminal invokes BASE/SHARED, respectively. Thus the result is a **continuous full-box proof**, not a finite sample. Each root was separately run to successful strict exact completion; independent second-algorithm or formal checker admission is still **NOT DONE**.

## 24 newly proven complete positive two-box hulls

From root (0,16), 19 previously unresolved hulls are:
`(0,16),(0,17),(0,28),(0,31),(5,7),(5,16),(5,17),(5,28),(5,31),(7,16),(7,17),(7,22),(7,28),(7,31),(16,22),(17,22),(22,28),(22,31),(28,31)`.

From root (5,21), four additional are `(5,21),(16,21),(17,21),(21,31)`. From root (18,29), one additional is `(18,29)`. Exact inclusion was checked by rational interval comparisons against all C254 35 basic boxes; count newly classified relative to the **reconciled author evidence union** is `19+4+1=24`.

Reconciled author classification: `213 negative + 112 positive + 38 unknown -> 213 negative + 136 positive + 14 unknown` (eligible domain remains 363). This count is **not** an accepted canonical Source classification; 232 other two-box combinations remain outside this method's eligibility.

## Reproducibility, negatives and open scope

Run sibling `C268_R2_STANDALONE_EXACT_REPLAY.py` with Python 3 standard library only, no network, external package or previous archive. All three trees have SHA256 identities checked before arithmetic; each exact lower-bound margin must equal the values in the table. Exploratory floating-point splits selected the trees but cannot establish their theorem. Root (4,18) was tried heuristically and its exact replay **did not complete**, so it is **not** claimed here. No new native GF(2) phase/label/port/sequence-preserving BRC bridge has been established; positive mass is not a complex amplitude and four variables here are NOT four native X6 spatial axes.

Native `em_control_tasks` returned `CONTROL_QUOTA`; native researcher registration returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. The live owner remains unknown; no native session, CLAIM, Result freeze or Driver admission was obtained. This GitHub research branch is **author evidence only**. Drive was not used to evade native access denial; no credentials or permissions were exposed.

**Next smallest math question:** classify the remaining 14 unknown four-free pair hulls using a strictly checked full-box bound, or use the C267 separately convex 16-vertex upper bound to prove new negative-volume subboxes in an unclassified hull; obtain independent adversarial audit of the new 6890-leaf certificate and restore native authorized Source publication when available.
