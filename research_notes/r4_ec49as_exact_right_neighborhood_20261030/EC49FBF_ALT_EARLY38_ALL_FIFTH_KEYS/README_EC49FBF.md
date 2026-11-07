# EC49FBF — all fifth-key exact optimum for the alternative 38-edge H2–H5 schedule

Date: 2026-11-05 (Asia/Shanghai). Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: AUTHOR_FINITE_EXACT_DP / TWO_IMPLEMENTATION_INTEGER_CROSSCHECK / UNREVIEWED / NOT_ADMITTED.

## Theorem

Work in the original frozen signed-native-X6 BRC seven-operation path model. The goal endpoint is (2,0,0,0,0,0), each horizon H2–H9 must give rational rank 9 across the nine-history/six-signature observation matrix, and the total number of full six-coordinate positive-step cache keys must not exceed five.

Fix H2={fe,ge}, H3={feg,gef}, H4={fegc,fegd,gefc,gefd}, H5={feggf,gefgf}. Their native signed primitive-prefix union has exactly 38 edges and uses four complete keys (2,1,1), (3,0,1), (3,1,1), (4,2,1), with three trailing zeros on every key. Now let all H6–H9 word sets and the remaining fifth key be chosen freely, subject only to the original conditions. Then

**min E(H2,…,H9) = 112, uniquely attained among fifth-key choices by K=(6,4,1,0,0,0).**

“Uniquely” concerns the fifth key, not the selected word sets. This extends EC49FAY's 112-edge family theorem from a fixed late key to all possible complete late keys for this early word schedule.

## Exhaustive classification of fifth keys

The original primitive signed-word expansions are a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). The endpoint excludes b because its negative E2 step has no positive E2 compensator.

For any word of length h and complete key (x,y,z,0,0,0), endpoint and key counting force #a=z−1, #e=z, #c+#d=x+y−h−1, #f=h+1−y−2z and #g=h+1−x, all nonnegative. The four fixed early keys have x+y≤6, whereas every word at Hh for h≥6 must have x+y≥h+1. Thus all of H6,H7,H8,H9 must use the **same fifth key**.

The exact nine-state observation automaton, applied to all possible integer count states, shows that the intersection of the rank-9 feasible keys at H6,H7,H8,H9 is precisely the following seven keys. This classification allows both the four early signatures and the two F/G signatures at H9, as appropriate to the actual operation counts.

| Fifth full key (last three coordinates zero) | Exact extra edges H6–H9 | Total edges |
|---|---:|---:|
| (5,5,1) | 107 | 145 |
| (6,4,1) | **74** | **112** |
| (6,5,1) | 134 | 172 |
| (7,3,1) | 107 | 145 |
| (7,3,2) | 122 | 160 |
| (7,4,1) | 134 | 172 |
| (7,5,1) | 158 | 196 |

## Complete exact finite optimization

For each of the seven keys and each h∈{6,7,8,9}, enumerate every compatible ordered operation word, retaining all c/d orientations, then compute native signed displacement, full positive-step key, and the original 9-state observer's exact final signature. The script's independent preliminary count-state DFA certifies the seven-key exhaustive classification.

For a signature s, define the four-bit rank-clause contribution from `(m&18),(m&20),(m&33),(m&40)`. The contributions of individual signatures s=1,2,4,8,16,32 are respectively 4,1,2,8,3,12. Thus 16 bits (four per H6–H9) encode the precise rank-nine requirement: complete OR-mask `65535`.

Create a trie of ordered **signed primitive X6 steps**, marking exactly the 38 fixed early prefixes as paid. Let D_v[M] be the minimum number of extra edges in the subtree rooted at v whose selected terminal word set attains exact clause-mask M. Initialize D_v[0]=0; choosing a terminal adds its clause mask at no extra charge. For each child u, update D_new[M|N]=min(D_new[M|N], D_old[M]+D_u[N]); add one for every nonempty selected subtree entering a nonfree node. Induction on trie height establishes that the recursion computes the minimum among every finite selected word subset, counting shared signed-prefix edges exactly once.

The executed Node.js integer OR/min-plus solver and an independently implemented Python standard-library integer OR/min-plus solver agree for **all seven keys**. They produce 112 as the unique least total among the seven families. The reproducible `VERIFY_EC49FBF.py` uses a separate primitive-word enumerator, count-state DFA, unpruned 16-bit trie DP and an end-to-end witness audit; its expected minima and native edge counts are embedded as checks.

## Explicit attaining construction

```text
H2 fe ge
H3 feg gef
H4 fegc fegd gefc gefd
H5 feggf gefgf
H6 fegccc fegddd gefccc gefddd
H7 fegccfg fegddgf gefccfg gefddgf
H8 feggfgfc feggfgfd gefgfgfc gefgfgfd
H9 feggfgfgf gefgfgfgf
```

Direct signed-prefix recount gives cumulative union costs H2 through H9: 12,16,32,38,70,82,106,112, with rank nine at every horizon and exactly five full keys.

## Provenance, verification and next unit

Earlier source results: EC49FAY at commit `ccd19ace0a348f769294cf96ad770b986ac5ddeb` (fixed late key), EC49FBE at the same Draft PR branch (seven-key classification for a different 39-edge early schedule). The scientific pin remains `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The current normative read snapshots were GLOBAL_KNOWLEDGE main `8155b038c9b5fac208f53d7aa62ec04ae078fe88`, EM main `5c59804576a9248e18c4b9aab645c8ce2745a4a5` (2026-11-05). P000 and ACTIVE Heartbeat World are unchanged.

Next EC49FBG: vary H4/H5 word sets and full fifth-key schedule jointly, with the H2/H3 initial root held fixed or separately varied. Compare exact native edge cost and the four-clause rank effect for key-mixed early schedules; seek a valid 93-edge witness or a broader lower bound. This is author evidence; formal CLAIM/Result and independent Driver admission remain governed by native current authority.
