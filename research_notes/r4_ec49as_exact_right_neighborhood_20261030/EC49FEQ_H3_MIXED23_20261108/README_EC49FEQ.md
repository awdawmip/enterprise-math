# EC49FEQ — 23-path H3 mixed observer support: exact BRC-key feasibility census

2026-11-08 · Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` · author-side mathematical evidence, pending independent Driver review.

## Exact scope

Native six-axis signed-step path alphabet `a,c,d,e,f,g`, nine-state observer with nonzero singleton signatures `{1,2,4,8,16,32}`, full positive BRC key `(x,y,z)` and endpoint `(+2,0,0,0,0,0)`. At each horizon H2 through H9, selected operation words must jointly hit the four original observer masks `18,20,33,40`; cost counts **ordered native signed-step prefixes**.

EC49FEP had already proved four inclusion-minimal observer supports `{16,32}`, `{1,8,16}`, `{2,4,32}`, `{1,2,4,8}`, and the lower bound of 22 total words under a budget of five complete BRC keys. EC49FEO proved that all 15 equality-support patterns of 22 words have native prefix cost at least 94. The present work treats a different exact 23-word family; it is not a rerun of fixed-22.

H2 uses `de,ed,ce,ec` and its required key `K0=(3,1,1)`. H3 uses the mixed support **type B** `{1,8,16}` (two lows from late keys, high 16 from K0). Choose four late horizons from H4–H9 with high pairs `{16,32}` and give the other two late horizons low quartets `{1,2,4,8}`. Total paths `4+3+4×2+2×4=23`. Every low horizon may mix all five complete keys. The high-key equation `x+y=h+1` forces the four late high keys to be distinct and distinct from K0.

The respective high-key option counts for H4–H9 are `(2,4,6,9,12,16)`. The complete type-B inventory is the 4th elementary symmetric polynomial of this vector:

```text
sum_{S subset {4,...,9}, |S|=4} product_{h in S} m_h = 42048.
```

Every inventory was tested for the H3 low signatures `{1,8}` and the four low signatures at the two other late low horizons. The high-horizon pairs are present by key generation, and the H2 quartet is forced. Single-signature words are distinct, so signature feasibility is sufficient to select an explicit 23-word system for that inventory.

## New exact census

| Late high horizons | Total | H3 type-B possible | Full signature feasible |
|---|---:|---:|---:|
| 4567 | 432 | 432 | 0 |
| 4568 | 576 | 576 | 0 |
| 4569 | 768 | 768 | 432 |
| 4578 | 864 | 864 | 0 |
| 4579 | 1152 | 1152 | 1152 |
| 4589 | 1536 | 1536 | 960 |
| 4678 | 1296 | 1296 | 0 |
| 4679 | 1728 | 1728 | 1728 |
| 4689 | 2304 | 2304 | 2304 |
| 4789 | 3456 | 3456 | 1956 |
| 5678 | 2592 | 648 | 0 |
| 5679 | 3456 | 864 | 864 |
| 5689 | 4608 | 1152 | 1152 |
| 5789 | 6912 | 1728 | 1728 |
| 6789 | 10368 | 0 | 0 |
| **Total** | **42048** | **18504** | **12276** |

The proven operation-word involution `I=(c d)(f g)`, `J(x,y,z)=(y+2z,x-2z,z)` maps type B into type C `{2,4,32}`, preserving native costs and validity. The combined 23-path H3-mixed family contains **84,096** inventories, of which **24,552** admit a full signature-covering 23-word construction; **59,544** fail its exact signature conditions. This is a *feasibility* classification. Whether a feasible inventory admits <=93 native prefixes is the next optimization problem.

Independent audit used a count-state memoized nine-state DFA dynamic program rather than recursive word enumeration and compared signatures for **350** horizon/key pairs, obtaining identical sets. A separate direct enumeration of the signed native H2/H3 operation words verified the forced H2 quartet and H3 high key. The 42,048-inventory census was rerun and its counts matched.

## Checked 99-prefix witness

A valid full-key type-B construction is:

```json
{"2":["de","ed","ce","ec"],"3":["deg","ecg","feg"],"4":["fegg","gefg"],"5":["degfg","feggd","feggc","ecgfg"],"6":["feggfg","gefgfg"],"7":["feggfgg","gefgfgg"],"8":["gefgfggd","feggfggd","feggfggc","gefgfggc"],"9":["feggfggfg","gefgfggfg"]}
```

Direct independent native signed-step expansion verifies all 23 endpoints, observation masks, five full BRC keys `(3,1,1),(3,2,1),(4,3,1),(4,4,1),(5,5,1)` and **99 native prefix edges**. It is a witness, not a 99-edge optimum.

## Reproduction, evidence and next question

`EC49FEQ_H3_MIXED23.py` is the executed complete census. `EC49FEQ_INDEPENDENT_AUDIT.py` is the executed independent DFA check; `EC49FEQ_H3_CENSUS.json` and `EC49FEQ_INDEPENDENT_AUDIT.json` preserve the exact counts and checks. These reuse the native word-pool machinery pinned by EC49FEO/EC49FEJ, not an alternative spatial model. Full local archive also includes those pinned source modules, plus this README and a complete test witness.

**Next concrete subproblem:** on the 12,276 type-B feasible inventories, give every allowable H3 mixed early-prefix alternative proper treatment, compute a conservative exact depthwise set-cover lower bound, and solve any remaining <=93 bound cases by joint native-prefix integer programming. Involution handles all 12,276 type-C mirrors. Another independent route changes the mixed triple to H4–H9. The mother's target is **<=5 full BRC keys and <=93 ordered signed native prefixes**, while the existing 94-edge witness is retained.

Source anchors: previous immutable EC49FEO `1df1dd9682b881ef6ebb3f96f599bf5ce3a849e4`; EC49FEP current PR #1730. P000 and ACTIVE worldview unchanged. GitHub author publication does not change Source-native CLAIM or review authority.
