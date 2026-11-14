# EC49FEO — Exact completion of fifteen 22-path five-BRC-key signature families

Date: 2026-11-08. Scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Research status: author-side exact finite computation and proof; independent Driver mathematical review remains pending.

## Exact mathematical claim

Fix the signed primitive native-X6 BRC operation alphabet `a,c,d,e,f,g`, signed step expansion, nine-state observation automaton and complete positive BRC keys `(x,y,z)` from EC49FEJ–FEN. At H2–H9 choose five high windows, each requiring exactly two distinct operation words with signatures `16,32`, and three low windows, each requiring four words with signatures `1,2,4,8`. Every horizon-h word has h operations, complete-key membership, and signed native-X6 endpoint `(+2,0,0,0,0,0)`. Allow arbitrary within-window mixing among **at most five complete BRC keys**, and charge one edge per distinct **ordered signed native-step prefix** of the resulting 22 words.

**The exact minimum in this finite 22-word model is 94 edges**. The explicit 94-edge certificate from EC49FDN/EC49FEG attains it.

## New three-family exhaustive calculation

| High windows | Complete key inventories | Infeasible low-signature quota | Depthwise certified >=94 | Depthwise inconclusive (bound 90) | Joint MILP optimum for latter |
|---|---:|---:|---:|---:|---:|
| H3,H5,H6,H8,H9 | 4608 | 0 | 4608 | 0 | — |
| H3,H5,H7,H8,H9 | 6912 | 0 | 6912 | 0 | — |
| H3,H6,H7,H8,H9 | 10368 | 6144 | 4208 | 16 | **98** |
| **Total** | **21888** | **6144** | **15728** | **16** | **16 resolved** |

**Exact symmetry reduction.** Every high-signature key at Hh has `x+y=h+1`; distinct high horizons force distinct full keys, and H3 has unique key `(3,1,1)`. The permitted high-key option sizes for H4,H5,H6,H7,H8,H9 are respectively 2,4,6,9,12,16. Apply the previously proved native-word involution `I=(c d)(f g)`, which induces `J(x,y,z)=(y+2z,x-2z,z)`, preserves the declared observer groups, exact BRC full-key membership and native-prefix cost. All three new families include H8 high. A fixed H8 key would require `x=y+2z` and `x+y=9`, hence `2(y+z)=9`, impossible. Thus every inventory forms an orbit of size exactly two, so 10944 representatives cover all 21888 inventories. The census validates exact orbit membership before reduction.

**Depthwise exact integer lower bound.** H2–H3 have four legal early selections, each costing 42 prefixes; their union has 54. At each signed primitive depth d, grant all 54 potential early prefixes free, discard the cross-depth consistency conditions, and calculate by integer bitmask set-cover DP the minimum new depth-d prefixes required to cover every signature group whose candidates all reach depth d. Summing these numbers and 42 gives a provable lower bound. This establishes >=94 for 15728 of the feasible inventories. It leaves exactly eight orbit representatives (16 inventories) with the bound 90.

**Joint full-prefix optimization.** For each of those eight representatives, all four H2–H3 choices were separately fixed. A binary variable chooses one original legal word per required H4–H9 signature group; binary prefix variables are ancestor-closed, and the objective is the exact new-prefix union cost plus 42. The word-to-model and model-to-word constructions prove equivalence for each fixed inventory/early choice. All **32** full MILPs were solved by SciPy/HiGHS with `status=0`, zero MIP gap, integer objective and dual bound **98**. The eight mirrored inventories inherit the same optimum. Independent direct path checks pass **32 full 22-word constructions = 704 native paths**, complete BRC keys, observation groups, signed endpoint and prefix count. A fresh independent check of the original 22-path witness confirms 94 edges and five full keys.

For a 98-edge joint-MILP example with keys `(3,1,1),(4,3,1),(4,4,1),(4,5,1),(4,6,1)`:
```json
{"2":["de","ed","ce","ec"],"3":["feg","gef"],"4":["dedg","eddg","cegc","eccg"],"5":["dedgg","eddgg","cegcg","eccgg"],"6":["feggfg","gefgfg"],"7":["feggfgg","gefgfgg"],"8":["feggfggg","gefgfggg"],"9":["feggfgggg","gefgfgggg"]}
```

Previously established **94-edge** full witness:
```json
{"2":["de","ed","ce","ec"],"3":["feg","gef"],"4":["fegg","gefg"],"5":["feggd","feggc","gefgd","gefgc"],"6":["fegggf","gefggf"],"7":["fegggfg","gefggfg"],"8":["fegggfgd","fegggfgc","gefggfgd","gefggfgc"],"9":["fegggfggf","gefggfggf"]}
```

## Fifteen-family combined result

EC49FEJ–EC49FEN previously resolved twelve families with 20160 key inventories (8172 quota-infeasible and 11988 feasible but certified >=94). Adding these three exhausts **15/15 signature families: 42048 inventories, 14316 quota-infeasible, 27732 feasible and all excluded at cost <=93**. Combined with the explicit 94-edge witness, this proves the stated fixed-22-word finite minimum.

This conclusion is about the declared 22-path signature regime. The separate mother objective continues exploring other path quotas/observer decompositions for `<=5` full keys and native-prefix cost `<=93`. Next investigate a genuinely different admissible signature-covering selection; carry forward original source/observer/BRC/X6 semantics.

## Sources and evidence

Original frozen scientific model: `EC49FEN_complete_evidence.tar.xz.b64` in immutable commit `8a855b061c39c118e7666a085697d6fe58cdb39a`; 94-edge witness: `EC49FEG_94_FRONTIER_AUDIT.py` in `24c6151e4dd69f1f3552bdf07299bd865cd85d1b`. This directory includes a current executable census reproducer and exact summary. The complete executed local archive also contains the raw 10944 representative records, all 32 HiGHS results, the full joint MILP code and independent witness audit. It was supplied as a downloadable conversation attachment with SHA-256 `1443445b7c31eb4a94a042e9be0d6849ce760de4b23845abd09a65e6ffab4097`; it is **not** claimed to be uploaded to GitHub as an archive.

Current rules were read separately from the frozen scientific pin. P000/worldview unchanged. GitHub author-side publication grants neither task CLAIM nor Source-native Result/Driver mathematical admission.
