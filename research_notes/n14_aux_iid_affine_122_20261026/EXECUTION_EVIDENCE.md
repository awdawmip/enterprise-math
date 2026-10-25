# Stage122 actual execution evidence

Author runtime: Python 3 standard-library Fraction and integer-weight literal DFS; no floating point rounding. The full local verification source and the portable checker were each executed successfully; the portable version printed:

PASS Stage122: 680 rational states, 1238 positive gaps, full real interval, four literal DFS corners [840811, 823333, 835771, 818293]

Actual observed dual: K=27085186670001462/35130967563833; L=25607353643447976/35130967563833; two ties A=(9,3,0), F=(3,0,2); zero negative gaps; minimal positive gap 968911136726508551639/90634038091307409604608. Actual first hits A=84 and F=3. Exact moments, all four corner checks, error balance, endpoint alpha/value and positive tP-tQ margins match certificate122.json.

Actual Stage123 one-sided sweep (local DISCOVER_STAGE123.py): 841 positive crossing candidates, first distance 12069734526005264514792/707172640851640831297 at state (10,5,4), giving K123=15175912302/20129609 and L123=14232343848/20129609. Full new Bellman exact tie set [A=(9,3,0):P/C, J=(10,5,4):Q/C], 1238 strict positive gaps, minimum 5078657746807/641138030936064; no negative gaps.

SHA-256 of **locally executed** versions:
- VERIFY_STAGE122.py (full execution source): 566f6cd5afb21240944c36eed7ab05b0dc3730fb3e776aeecd8a6e79cb1ce62a
- VERIFY_STAGE122_PORTABLE.py: d960ae6e375163f9a97a191b921cc5f672abc62c886cd10d897f2ef6d792f37a
- DISCOVER_STAGE123.py: 313fc9c3399db5f4bd9abf5a420904f5b8d0bbea7a6787e52fe79db51dd72548

The complete full-source executable, local output and independent portable checker are included in the local conversation archive. This GitHub package preserves the full mathematical argument, portable exact code, dual scanner and arithmetic certificate. A remote source readback is **not** remote code execution. Author proof is not independent mathematical admission.
