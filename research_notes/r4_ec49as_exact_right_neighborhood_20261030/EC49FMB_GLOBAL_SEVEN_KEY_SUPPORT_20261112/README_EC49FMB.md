# EC49FMB — Global seven-full-key demand-support census

Date: 2026-11-12. Mode: author-side complete finite classification; scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Native CLAIM/Result and independent Driver admission not established.

## Theorem and definition

In the unchanged nine-state ordered signed-X6 BRC catalogue, all 178,850 legal words yield exactly 94 full raw cache keys and 24 (window,DFA-signature) observation demands. Each key k supports the exact 24-bit mask L(k) of demands realized by at least one legal word of that key. A seven-key set K is demand-coverable exactly when the bitwise union over its keys equals all 24 bits. Coverability is a necessary filter for the separate minimum signed-native prefix objective.

The demands (2,16) and (2,32) are respectively supported by only the full raw keys (3,0,1) and (2,1,1). Thus both keys are globally forced. Every coverable seven-key set is those two keys and exactly five of the other 92, and every other seven-key set is noncoverable.

**Exact full-universe result:** among C(92,5)=49,177,128 candidate seven-key sets containing both forced keys, exactly **108,434** cover all 24 demands, and **49,068,694** fail. The entire C(94,7) universe has exactly 108,434 coverable sets.

## Distance from the EC49FKX 84-prefix seed

The seed's nonforced keys are (3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1). Distances r count how many of these five are replaced with outside keys. Each r-class has exactly C(5,r)C(87,r) sets.

| r | All | Coverable | Not coverable |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 |
| 1 | 435 | 192 | 243 |
| 2 | 37,410 | 6,315 | 31,095 |
| 3 | 1,059,950 | 38,169 | 1,021,781 |
| 4 | 11,129,475 | 62,620 | 11,066,855 |
| 5 | 36,949,857 | 1,137 | 36,948,720 |
| ALL | 49,177,128 | 108,434 | 49,068,694 |

The r=0..3 values reproduce EC49FKX/FKY/FKZ/FMA; r=4..5 adds **63,757** newly classified coverable sets. The separate exact support counts for key cardinalities 2,3,4,5,6,7 are respectively 0,0,0,16,2,004,108,434 (the forced pair included).

## Exhaustive finite proof and independent computation

Regenerate 24-bit L(k) from every legal word via the frozen EC49FGW_RADIUS5_SCREEN.py generator and verify 178850 words, 94 keys, 24 demands, forced pair. The C++17 file ENUMERATE_EC49FMB.cpp visits all strictly increasing five-index tuples drawn from the other 92 keys, ORs the masks and counts exactly by seed intersection. Execution produced GLOBAL_ENUMERATION_EXACT_PASS and the six rows above. Completeness follows because each five-element subset has exactly one increasing index tuple.

The structurally different Python verifier VERIFY_EC49FMB_DP.py computes integer coefficients indexed by (chosen count, number of seed members, support-mask union). It processes each of the 92 keys exactly once, updating counts in descending chosen cardinality, and verifies each of the six coefficients against the same table. It yielded exactly 1,763 terminal mask/seed-count states and GLOBAL_COEFFICIENT_DP_PASS. Both programs use exact integers and bitwise operations.

The original generator pin is frozen. Read and run using the project tree where EC49FJD_RELEASE_B11_COMPLETE_20261111 contains EC49FGW_RADIUS5_SCREEN.py plus EC49FGJ_SEVEN_KEY_94_WITNESSES.json. The three additional files here contain the reproducible proof programs and exact output. A local complete evidence archive with frozen generator, full input masks, scripts, outputs and SHA256 manifest is retained as the separate conversation attachment.

## Open scientific question

The known lawful 84-prefix witness still gives C_min(7) <= 84 in this exact frozen model. The new census reduces the global seven-key prefix optimization to 108,434 coverable keysets, but does not evaluate their signed-prefix minima. Reuse the previous exact r=0/1/2 and the 114 solved r=3 cases; prioritize the 62,620 r=4 and 1,137 r=5 support-coverable sets and remaining r=3 cases, searching for a complete <=83-prefix witness or proving a global lower bound. Different cardinalities of full keys are a separate existing fixed-key cost problem.

Source/control state at creation: control task inventory request still RUNNING, session issuance SESSION_ISSUANCE_QUOTA, no current matching verified CLAiM. P000 and ACTIVE worldview unchanged.
