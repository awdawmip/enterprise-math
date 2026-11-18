# EC49FFY — Sparse BRC prefix-state optimization: new exact range H31–H70

**2026-11-10 · Author-side computational theorem / unreviewed · Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.** Reuses EC49FFX state quotient (at `a12883f8a4585460ebbe9ef21e7618288c21d0c1`) and EC49FBS native code-prefix identity. P000 original signed X6 microstep order and nine-state BRC observer are preserved.

## Exact question and new result

Signed native-X6 operation codes are `a=(-1,-1)`, `c=(+1,+2,-1,-2)`, `d=(+2,+1,-2,-1)`, `e=(+3,+1,+1,-3)`, `f=(+1,-1)`, `g=(+2,-2)`. Legal length-`h` operation words have `#e=#a+1>=1`, `2#e+#f<=h`, positive full key `(x,y,z)=(h+1-#g,h+1-2#e-#f,#e)`, and one original BRC DFA signature.

Fix H2 baseline `ce,de,ec,ed` (signatures 4,1,8,2). For Hh choose one legal length-h operation word per signature 1,2,4,8, allowing **any number of complete keys**. Define M(h) as the minimum distinct nonempty **ordered signed-X6 microstep** prefixes of the eight paths. This is a precise eight-demand auxiliary model.

**New complete finite result:** `M(h)=4h+42` for each integer `31<=h<=70` (40 new globally optimized cases). Values: M(31)=166, M(40)=202, M(50)=242, M(60)=282, M(70)=322. Further independently optimized sampled windows yield M(80)=362, M(90)=402, M(100)=442. The entire range H3–H70 is covered when combined with previously proven EC49FFT/EC49FFV/EC49FFW/EC49FFX finite results.

**Universal upper-bound witness:** for signatures (1,2,4,8), take Hh words `gfe g^(h-4) d`, `fe g^(h-3) d`, `fe g^(h-3) c`, `gfe g^(h-4) c`, respectively. With H2 words `de,ed,ce,ec`, complete keys are exactly `(3,1,1)` and `(4,h-2,1)`. Exact native-prefix union is `4h+42` for all integers `h>=4`. `VERIFY_EC49FFY_WITNESS.py` checks the full DFA, cache keys, signed six-axis endpoint and explicit native prefixes for **every h=31..100**.

## Finite optimality and sparse algorithm

EC49FFX proved the exact recurrence. State `s=(k,#e,#a,#f,q)` tracks operation depth, letter counts and original nine-state DFA state. The H2 baseline adds edges only at depths 0 and 1. Hence for k>=2 two distinct operation histories with identical s have exactly the same future feasibility and 16-mask minimum incremental costs. The six operation-code words are prefix-free, so separate operation-prefix nodes have disjoint deeper signed-microstep descendants; no path/provenance information required by this cost is lost.

For selected outgoing symbols S the exact native edge count is the EC49FBS identity `F(S)=Σ_{u∈S}len(code(u))−1_{c,f⊂S}−1_{d,g⊂S}`. For baseline outgoing symbols B, pay `F(S∪B)−F(B)`. The DP distributes the four requested observation-signature bits as disjoint masks among feasible child paths; structural induction proves the 16-mask row minimizes complete native prefix union. Baseline H2 contributes 28 edges: `M(h)=28+DP_root[15]`.

The new C++ version retains the same DFA, guards and integer recurrences but changes `memo/cache/ready` from dense `9(h+1)^4` arrays into **sparse hash maps indexed by the original exact state tuple**. It caches only reached states. This is a memory optimization, not a claim of improved worst-case polynomial degree; expected hash-map performance and exact state count are recorded. At H30, local sparse process peak RSS was ~19 MiB versus the prior EC49FFX dense report ~271 MiB. For H100 the sparse run used ~1.71 GiB peak RSS, with 15,293,153 evaluated DP states.

## Reproduction / evidence

Run `g++ -O3 -std=c++17 VERIFY_EC49FFY_SPARSE.cpp -o sparse`; then `for h in $(seq 31 70); do ./sparse "$h"; done`, and `./sparse 80; ./sparse 90; ./sparse 100`. The report `EXACT_REPORT_EC49FFY.json` includes all 40 h, exact integer minima and evaluated state counts, plus the larger sampled results. Each computation in this run completed normally.

As an independent cross-check, the separately implemented Python mask subset-convolution DP from the EC49FFX author evidence produced H31=166, H40=202 and H50=242. The earlier dense C++ DP reproduced H31=166 as well. The independent `VERIFY_EC49FFY_WITNESS.py` verifies every integer H31..H100 with the full native microstep expansion.

**Research frontier:** the universal equality `M(h)=4h+42` for all integers `h>=10` is still an analytic lower-bound question. For H71..H100, only H80, H90 and H100 received exact unrestricted-key optimization this run; the witness checks provide upper bounds throughout. The distinct original mother problem has 24 observation labels including H2/H3 high signatures, full-key cap five and target at most 93 signed-native prefix edges. The next unit seeks an eventual-state/potential lower-bound certificate, a genuine counterexample, and a transfer to the actual frozen mother requirements.

Current 2026-11-10 exact native control query of legacy task text `EC49AS` returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`. This is an author-side checkpoint on unmerged PR #1730; no formal CLAIM, Source Result, independent Driver acceptance or Foundation promotion is asserted.
