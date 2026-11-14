# EC49FBW — Exact early-window three-slot rigidity of the 158-edge native-X6 witness

Date: 2026-11-06. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent: EC49FBV author certificate at `080b4c9bc10e5e449f5177880e9f31b04737f9ff`. Status: author-side exact finite theorem.

## Precise result

Fix the 24 selected operation words of EC49FBU, the nine-state DFA and its required signature slots; H2/H3 remain `fe, ge, feg, gef`. H4/H5 have full positive-BRC key L=(4,2,1,0,0,0), H6-H9 have M=(7,3,2,0,0,0). Let `E(W)` be the number of distinct nonempty **ordered signed native-X6 primitive step prefixes** in the selected word family. The baseline has E=158.

For every unordered triple of **distinct required signature slots entirely within H4, H5 or H6**, replace their three selected words by arbitrary legal words of the same horizon, exact positive-BRC key and required terminal DFA signature; keep every other slot fixed. The minimum possible E is **158**, attained by the original witness. There are exactly C(10,3)=120 such triples and exactly **790,560** candidate replacement triples (counting each legal selection separately). Exhaustive exact evaluation of every triple establishes this restricted neighborhood theorem.

Combined with the 1-/2-slot result EC49FBV, any strictly better witness differing in at most three slots from this 158-edge construction must differ in exactly three slots, at least one of which belongs to H7/H8/H9. This is a route-selection conclusion for the fixed cache schedule and the fixed signature-slot design.

## Algorithm and finite proof

Operation alphabet is `acdefg` with expansions `a=(-1,-1)`, `c=(1,2,-1,-2)`, `d=(2,1,-2,-1)`, `e=(3,1,1,-3)`, `f=(1,-1)`, `g=(2,-2)`; signs and axis indices are not projected away. The exact frozen nine-state DFA is embedded in `VERIFY_EC49FBW.py`. For cache key (x,y,z) at horizon h let b=x+y-h-1; then #a=z-1, #e=z, #c+#d=b, #f=x-b-2z, #g=y-b. Enumerate all splits of b and distinct multiset operation words, and retain exactly the legal DFA terminal signatures. The resulting H4/H5/H6 candidate counts are 48/24/120; each of 10 signature slots has 12 or 30 candidates as appropriate.

For a triple (s,t,u), let R be the primitive-prefix union of the 21 fixed slots. Map each distinct signed primitive-prefix string to a unique integer bit. For a candidate word w set B(w) to its exact prefix-bit mask. The cost of choosing words p,q,r is
$
|R|+\operatorname{popcount}((B(p)\lor B(q)\lor B(r))\land\neg B(R)).
$
The mapping is injective over the finite generated candidate pool and all original words, so this equality is lossless and exact. The verifier evaluates the full Cartesian product for each of 120 triples and checks the minimizing witness by a separate direct set union of original signed prefixes. All 120 minimum costs equal 158.

## Executed evidence

Executed with CPython 3 and Python integers. Output: `slot_count=10`; `tested_triplets=120`; `complete_evaluations=790560`; `min_achieved=158`; `improvements=[]`. The committed `EXACT_SUMMARY_EC49FBW.json` records all 120 slot triples, the exact minimum and the baseline minimizing words. `VERIFY_EC49FBW.py` deterministically regenerates the more detailed `EXACT_REPORT_EC49FBW.json` on execution; its own selected minimizer can differ from the baseline on a cost tie. Each minimizer was checked by direct signed-prefix recomputation.

## Unfinished next step

Search triples containing H7/H8/H9 and larger coordinated replacements, or globally solve the losslessly compressed integer program. The 80≤E*≤94 mother benchmark concerns a broader variable-schedule family; this theorem concerns the specified 158-edge schedule and selected signature slots. Formal native CLAIM/Result and independent Driver admission require current session/ownership authority.

Sources: prior EC49FBU witness and EC49FBV radius-two proof on the same existing `research/r4-ec49as-20261030-exact-right-neighborhood` branch; frozen input pin above; current P000 and ACTIVE worldview were read without modification.
