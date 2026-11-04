# EC49FAX — Exact minimal nine-state signed-X6 observer and BRC transfer

Date: 2026-11-05 Asia/Shanghai. **AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED**. Frozen science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Predecessor: EC49FAW at `bf0262d78004110a10372faa531b9fdfbb5c80d7`. The P000 and ACTIVE worldview remain unchanged.

## Theorem 1 — Nine states suffice and are necessary

Use frozen endpoint-compatible operation alphabet a,c,d,e,f,g with literal native signed-axis step expansions:
`a=(-1,-1), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2)`.
These are ordered primitive signed axis labels, **not** Euclidean displacement coordinates. Nine original observer seeds: `(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(3,0),(4,0)`, with state 0..4 and remembered previous positive-step class 0,1,2. Step +2 after previous +1 applies 0→1, 2→4; step +1 after previous +2 applies 0→2, 1→3. The remembered class updates to 1,2,0 depending on the incoming primitive step.

Full reachability closure under the alphabet produces exactly **12** nine-history vectors. States 8..11 in BFS order are four absorbing rejecting vectors; quotient all four to sink 8. The nine-state transition table for `a,c,d,e,f,g` is:

|s|a|c|d|e|f|g|output|
|---:|---:|---:|---:|---:|---:|---:|---|
|0|1|2|3|1|4|5|reject|
|1|1|6|7|1|1|1|reject|
|2|2|2|8|2|2|2|C=ce|
|3|3|8|3|3|3|3|D=de|
|4|4|2|7|4|4|4|F=feg|
|5|5|6|3|5|5|5|G=gef|
|6|6|6|8|6|6|6|J=ec|
|7|7|8|7|7|7|7|E=ed|
|8|8|8|8|8|8|8|reject|

The program rebuilds all raw states using the original nine-history signed primitive step automata; all **72** original state transitions and all six signature labels agree with the table. The quotient is a transition congruence, hence induction on suffix length proves exact preservation of the six labeled signature outputs for **every finite operation word**.

**Minimality proof:** each quotient state is reachable by ε,a,c,d,f,g,ac,ad,cd, respectively. The six accepted outputs C,D,F,G,J,E are pairwise distinct and thus separated by the empty suffix. The remaining 0,1,8 all reject on the empty suffix: the suffix f distinguishes 0 from 1 and 8; the suffix c distinguishes 1 from 8. Thus all nine states are pairwise future-output distinguishable for the seven-valued Moore observer (six labels plus reject). Nine states are minimal.

## Theorem 2 — Rational multivariate weighted transfer

For operation o let the 9×9 integer transition matrix `P_o[i,j]=1` iff table state i transitions to j. With commuting indeterminates A,E,R,F,G define `M=A P_a+E P_e+R(P_c+P_d)+F P_f+G P_g`. For each accepted state s∈{2,3,4,5,6,7}, the formal series
`Phi_s=e_0^T(I-M)^(-1)e_s=sum_{n≥0}e_0^T M^n e_s`
is rational with nonnegative integer coefficients (the formal inverse exists because M has no constant term).

For a full positive BRC cache key `K=(x,y,z,0,0,0)` at horizon h set
`r=x+y-h-1; f=h+1-y-2z; g=h+1-x`.
If `z>=1, r>=0, f>=0, g>=0`, the **exact number of ordered endpoint-return words** with key K and signature s is
`[A^(z-1) E^z R^r F^f G^g] Phi_s`; otherwise it is 0.

**Proof:** native endpoint balance forces #b=0 and #e=#a+1. Put z=#e, r=#c+#d, f=#f, g=#g. Then #a=z−1, `x=2z+r+f`, `y=r+g`, `h=2z−1+r+f+g`, exactly inverting to the displayed formulas. Each ordered operation word contributes one matrix-product term, and the Moore transition retains its signed-native observer signature. Thus the coefficient counts each word once. This is an exact formal-series theorem internal to the frozen model.

## Execution and new computed census

Run `node VERIFY_EC49FAX.js` (Node >=18). The exact BigInt dynamic program retains `(e,r,f,g,observer state)` and transitions over the six operations, verifying the raw native observer quotient first. Its H2..H9 five-column census agrees exactly with the predecessor's independent literal enumeration; an independently executed Python standard-library checker also agrees on H2..H13.

|h|endpoint words|six-signature words|allowed cache keys|rank-9 single keys|
|---:|---:|---:|---:|---:|
|10|11,374,000|3,178,976|125|115|
|11|65,966,318|15,569,820|160|150|
|12|383,289,504|76,178,236|203|191|
|13|2,230,877,428|372,516,718|251|239|

Rank-nine checks use EC49FAR's exact signature clauses `(E|F)&(C|F)&(D|G)&(J|G)`; key-mask aggregation retains all six labels. This replaces direct word enumeration for endpoint-key-signature counting; it does not compute the minimum native signed primitive-prefix **union** cost.

## Next EC49FAY

Combine the exact 9-state transfer with a signed primitive-prefix trie to jointly minimize H4..H9 path-union cost over EC49FAW's 124 rank-feasible dual-cache-key pairs after H2/H3 16-edge seed. First compare pair (4,2,1),(6,4,1) with the known 112-edge witness, then the alternative H2/H3 31-edge/two-key seed. A complete <=93-edge nine-horizon witness would lower the current author-side 94 upper bound; a finite-family lower bound would be scoped to that family. Global author-side bounds remain `80<=E*_H9<=94`.

Native CLAIM, Result and independent Driver review require separate source authority and are not asserted by this author-side artifact.
