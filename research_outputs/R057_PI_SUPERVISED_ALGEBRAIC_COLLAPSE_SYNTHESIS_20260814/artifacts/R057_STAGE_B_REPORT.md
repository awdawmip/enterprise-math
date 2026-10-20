# R057 Stage B — G000 / OP000 Discrete Collapse Synthesis

Researcher-ID: `EM-R057-6A31F2`  
Task: `RS-R057-PI-SUPERVISED-ALGEBRAIC-COLLAPSE-SYNTHESIS`  
Status: `STAGE_B_FROZEN / AWAITING_DRIVER_REVIEW`

## Frozen inputs

Stage-0 anchors and Stage-A TD000 corpus/catalog/checker remain immutable. Stage B uses exactly TD000 (108 circles), K=1..8, OP000, the frozen oriented-D6 packet classes, and the frozen cyclic boundary representation.

No K expansion, teacher-data expansion, operator primitive expansion, parser/context-state expansion, rational/algebraic coefficient fitting, R057-G selected-rule read, R057-X comparison, or Stage C work occurred.

## Parser used for deployable G000 grammars

For a fixed packet-class -> OP000 composition mapping, the global parser is a target-free cyclic shortest-path tiling over packet lengths 1..8. It minimizes effective OP000 perimeter. The stored boundary cut is semantically irrelevant: all possible packet-boundary offsets within K-1 edges are covered. Classical pi is used only offline to post-select the mapping; the deployable parser does not receive pi, radius target, or teacher error.

## B0 — simple baselines

- RAW/identity MSE: `0.7392180110936321344127604685825587801099951692182011672650143376526763133827407429351680044872177327`.
- All-K WHOLE_CHORD MSE: `0.0002876467953019322788263538890425817979448274841173980544306590570256733116206857581392651858278423793`.
- Every contiguous composition at each fixed k=2..8 was enumerated (254 fixed-k uniform candidates total).
- The best uniform composition is WHOLE_CHORD(k) for every k=2..8.
- The best fixed-k uniform grammar is k=7 -> WHOLE_CHORD(7), with MSE `0.0001043771019035336102732913384499457510861379692038704780110666264539749041366418262713839774907963094` and description_units `14`.

## B1 — structural type-to-operator search

Independent full class-specific OP000 searches were run for each k. The best single-k type search is k=7.

The fitted K7 map is:

- 14 of 15 oriented-D6 K7 classes -> WHOLE_CHORD(7);
- `K07-C0011`, turn word `[+1,+1,-1,+1,+1,-1]` -> PARTITION `[3,4]`.

Its MSE is `0.0001030204541276706346059833776213881374051343970815316023759602083777647159313507653084515721049045142`.

Crucially, the 15-independent-rule type lookup is semantically identical to a two-rule description: one shared WHOLE_CHORD(7) rule plus the single K07-C0011 exception. The low-complexity encoding has description_units `18` versus `44` for the uncompressed lookup representation.

Empirical candidate law from the independent per-k B1 searches:

- c(k)=1 for every class at k=2,3,4,5,6,8;
- at k=7, c(7,w)=1 except K07-C0011 where c=2 with `[3,4]`.

This is a TD000/G000 discovery pattern, not a theorem.

## B2 — high-capacity G000 overfit

All packet classes across K<=8 were allowed independent OP000 composition choices, with explicit provenance `PI_SUPERVISED_POST_SELECTED_OVERFIT`. A bounded multi-start coordinate search reached MSE `0.000009748449753217692525647374992231873410142061424170734226756678611250613477755142894309853476340972120`. A deterministic 400-iteration simulated-annealing reinforcement (seed 5705702) lowered this to `0.000009699365729044670260193040895059576290924137162203716650334963920999994465915168772473334679369669435` — only `0.5035%` further improvement — so Stage B freezes the first frontier rather than extending search without bound.

The final B2 representative uses 59 non-identity class rules, no continuous coefficients, description_units `251`. Its composition histogram is heterogeneous across K; no compact c(k) law is claimed for B2.

The optional target-conditioned segmentation/operator oracle was not run. It is explicitly absent rather than conflated with a deployable grammar.

## First complexity-error frontier

| Representative | MSE | MAE | Signed bias | Max abs error | Phase spread | Description units |
|---|---:|---:|---:|---:|---:|---:|
| BEST_SIMPLE_DISCRETE | 0.0001043771019035336102732913384499457510861379692038704780110666264539749041366418262713839774907963094 | 0.009503824790847505945855541396234680749559066479653548531813344493899457205313448974368257195673616130 | 0.008632187267776053082920205017963829455652400946069846988736252088301640191392896547387569259050623414 | 0.01681997295244836448778633345436733919622775183851663257845521674302267222087759248288144400912104402 | 0.018232956984906503475032379195834124912585167999275528284846651732424653345299907040202596429643746 | 14 |
| BEST_LOW_COMPLEXITY_STRUCTURAL | 0.0001030204541276706346059833776213881374051343970815316023759602083777647159313507653084515721049045142 | 0.009405414262795132494167763873873939491012539749306739360784669987236437410337466057518982295776034157 | 0.008730597795828426534607982540324570714198927676416656159764926594964659986368879464236844158948205386 | 0.01681997295244836448778633345436733919622775183851663257845521674302267222087759248288144400912104402 | 0.013132652991159180960155310319453928642419940025855546166300558772201372045512769529720886613874286 | 18 |
| BEST_TYPE_TO_OPERATOR_STRUCTURAL | 0.0001030204541276706346059833776213881374051343970815316023759602083777647159313507653084515721049045142 | 0.009405414262795132494167763873873939491012539749306739360784669987236437410337466057518982295776034157 | 0.008730597795828426534607982540324570714198927676416656159764926594964659986368879464236844158948205386 | 0.01681997295244836448778633345436733919622775183851663257845521674302267222087759248288144400912104402 | 0.013132652991159180960155310319453928642419940025855546166300558772201372045512769529720886613874286 | 44 |
| BEST_HIGH_CAPACITY_G000_OVERFIT | 0.000009699365729044670260193040895059576290924137162203716650334963920999994465915168772473334679369669435 | 0.002630444081864409909706298816130098756820716715633439339158011865711820080221829316261059693978433754 | 0.002041365659649564846510354469914413432529330326560647068919698364565214398230843107081632111585057819 | 0.008212654244374002958299902861880099672402806637622838822536745343614669390663858990612408823285817982 | 0.011644919560434029328693786852533700866419159706373194366872089078699281781623415199975328554034604 | 251 |

RAW -> BEST_SIMPLE reduces MSE by about 7082x. BEST_LOW_COMPLEXITY -> BEST_HIGH_CAPACITY reduces MSE by about 10.62x. The high-capacity point is not claimed as theorem or compressed algebra.

## Independent checker

`R057_STAGE_B_EXACT_CHECK_RESULTS`: `PASS` with `32/32` checks passing and zero failures.

The independent checker uses an 8-state min-plus cyclic tiling automaton, algorithmically distinct from the search-time cut-window DP. It independently recomputes all four representative scores and verifies cyclic-start/reflection invariance for the diverse high-capacity grammar on all 108 teachers.

## Frozen hashes

- `R057_G000_SEARCH_RESULTS_SHA256 = b7be23991e5d8345c1b8eb86726cb84f654971f73a0fd792a51438bf8e371934`
- `R057_G000_FRONTIER_SHA256 = df23c5c45f9fc1fd129ee1345ec26cb202530e694be401e6ad514da93f210f4b`
- `R057_GRAMMAR_GENEALOGY_SHA256 = 83b85dbeee26f4289e662f84b3e57182d30f34410f1919dedd572c13bf532f07`
- `R057_OPERATOR_LIBRARY_GENEALOGY_SHA256 = 376d299de90abc933d0255d94e775e0acc382a6819951e05f4590e617aa41ccc`
- `R057_STAGE_B_EXACT_CHECK_RESULTS_SHA256 = d3dbb2b6f5ad43e90172c85f9ba1b4d6779029b140fa48db9fea32bd81176f5b`
- `R057_FIRST_SERIOUS_GRAMMAR_CHECKPOINT_SHA256 = bc991398000dd1b18ef53967a15b5f2d07c99afee8bdb17cd0a411c73d5cd6bd`

## Stop boundary

Stage B stops here for Driver review. R057-G firewall remains ACTIVE. No Stage C expansion has begun.
