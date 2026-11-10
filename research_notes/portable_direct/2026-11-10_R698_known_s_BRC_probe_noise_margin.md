# R698 — Known-s BRC two-probe tomography: sharp deterministic error threshold

Date: 2026-11-10 (Asia/Shanghai)
Mode: Independent author-side research; no task CLAIM, Result, review or Foundation admission is asserted.
Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS.
Frozen candidate: R697 exact E* path model at \`2c1c87f9f543aa8046aa847c30c5b7581caba64c\`. Earlier task science pins remain unchanged.
Additional native semantic sources: current-main V29 network event ledger and V39 cycle-current/S3 operation-safe loop port.

## 1. Typed carrier, provenance and observations

Keep the population of 60 distinct labeled four-step X6 return paths from R692c/R696/R697. They have four S3 output classes with capacities \`N=(24,18,6,12)\`. A static binary path gate yields a histogram \`v=(e,t,c,z)\` with \`0<=v_i<=N_i\`. The gate retains exactly \`s=e+t+c+z>0\` paths. The histogram is a group-output observer; individual path identity, order, branch provenance and future legality are not silently identified with this quotient.

The frozen contextual-return probes R697 defined are

\`T3(v)=(4e+5t+z)/(10s)\`, and \`T8(v)=(2e+2c+z)/(5s)\`.

Put \`U=10s*T3=4e+5t+z\`, \`V=5s*T8=2e+2c+z\`.
For a common raw-probability absolute error budget, the natural scaled signature is

\`F_s(v)=(U,2V)=(10s*T3,10s*T8)\`.

All quantities are exact integers or rational numbers, with \`s\` supplied as an exact side-information input.

## 2. Sharp separation theorem

For each positive \`s\`, let \`X_s={v integral: 0<=v<=N, sum(v)=s}\` and define

\`d_s=min_{v!=w in X_s} ||F_s(v)-F_s(w)||_infinity\`.

Then

- \`d_s=2\` for \`s=1,2,58,59\`.
- \`d_s=1\` for \`3<=s<=57\`.
- \`X_60={N}\` is a singleton, requiring no probe.

**Lower bound and characterization of distance 1.**
R697 proved that the integer map \`v -> (s,U,V)\` has primitive kernel generator \`(3,-4,-7,8)\`. For fixed \`s\`, distinct box vectors give distinct \`(U,V)\`. Therefore \`||Delta F||_infinity>=1\`. For equality to 1, the even coordinate \`2 Delta V\` forces \`Delta V=0\`; after swapping endpoints we may take \`Delta U=1\`.

From \`Delta s=0, Delta V=0\`, derive \`Delta z=-2 Delta t\`, \`Delta e=Delta t-Delta c\`, and hence \`7 Delta t-4 Delta c=1\`.
Its integer solution family is

\`(Delta e,Delta t,Delta c,Delta z)=(1-3n,-1+4n,-2+7n,2-8n)\`, \`n in Z\`.

Since the box imposes \`|Delta c|<=6\`, the only possibilities are \`n=0,1\`. The first vector \`(1,-1,-2,2)\` is feasible precisely when the initial vector satisfies

\`0<=e<=23; 1<=t<=18; 2<=c<=6; 0<=z<=10\`.

These independent inclusive box intervals realize **every integer total 3 through 57**. The second vector \`(-2,3,5,-6)\` needs \`2<=e<=24;0<=t<=15;0<=c<=1;6<=z<=12\`, and its possible totals are 8 through 52. Thus distance 1 is realized for every 3<=s<=57 and is impossible for s=1,2,58,59.

**Distance 2 on the remaining totals.**
Choose an initial vector from \`0<=e<=24;0<=t<=18;1<=c<=6;0<=z<=11\`. This box realizes every integer total 1 through 59. The paired vector \`(e,t,c-1,z+1)\` remains admissible with unchanged s and has \`(Delta U,Delta V)=(1,-1)\`. Therefore the scaled \`L_infinity\` separation is exactly \`max(1,2)=2\`. This closes all 60 positive totals.

## 3. Optimal robust decoding

Suppose measured probabilities satisfy \`hat_T3=T3+eta3\` and \`hat_T8=T8+eta8\`, with exact known \`s\`. Write \`epsilon_s=d_s/(20s)\` for 1<=s<=59.

If \`max(|eta3|,|eta8|)<epsilon_s\`, then \`(10s*hat_T3,10s*hat_T8)\` lies within scaled \`L_infinity\` distance strictly less than \`d_s/2\` of the correct signature; finite nearest-neighbor decoding therefore uniquely recovers the integer histogram \`v\`.

The exact sharp uniform radii are

\`epsilon_s=1/(10s)\` at s=1,2,58,59,
\`epsilon_s=1/(20s)\` at 3<=s<=57.

For each \`s\`, an attaining pair exists. Its midpoint is within error exactly \`epsilon_s\` of each possible input, so if perturbations are allowed to equal that radius, no universal decoder can distinguish both. Use strict inequalities as above; at s=60 the known total already determines the sole histogram.

An alternative constant-cost decoder follows R697. Under componentwise stricter bounds \`|eta3|<1/(20s)\`, \`|eta8|<1/(10s)\`, round \`10s*hat_T3\` and \`5s*hat_T8\` to nearest integers U,V, then set \`A=U-s\`, \`B=V-s\` and use:

\`c=2(3B-A) mod 7\` (representative in 0..6),
\`t=(A-3B+4c)/7\`,
\`e=t+B-c\`,
\`z=s-e-t-c\`.

The improved boundary radius uses finite nearest-neighbor decoding rather than this conservative componentwise rounding.

## 4. Native V29 / V39 interface relation

The extant V29 grammar stores nonnegative passage counts \`M_x[a,b]\`. Its \`PASS\` increments exactly one such entry; a matched \`TRANSFER\` increments \`Rout\` and \`Rin\` instead. Consequently \`P(L)=sum_{x,a,b}M_x[a,b]\` has exact event increments \`Delta_PASS P=1\`, \`Delta_TRANSFER P=0\` and measures completed native PASS occurrences.

To identify this \`P\` with the number \`s\` of selected E* **complete return paths**, provide a genuine packet-to-event map, a common fixed positive PASS multiplicity \`ell\` per retained path, an observed baseline \`P0\`, exclusion or explicit accounting of unrelated PASS occurrences, and a labeled path-source correspondence. Under these conditions \`s=(P-P0)/ell\`. Four X6 axis steps alone do not establish four V29 PASS occurrences.

V39's \`Sigma_JH=(net cycle current, S3 frame transport)\` is the coarsest exact quotient for its **declared** based-loop language. It already notes that if future questions include primitive-event counts, the observer must be enlarged. It does not by itself return R697's \`s\`. The two contextual-return probes \`T3/T8\` also require a lawful native future operation realizing each E* mask kernel. These interfaces specify a concrete next bridge experiment without modifying P000 or the task's frozen science.

## 5. Executed integer certificate

\`R698_BRC_TWO_PROBE_NOISE_MARGIN.js\` and \`R698_BRC_TWO_PROBE_NOISE_MARGIN_RESULTS.json\` run and retain the complete discrete census. It enumerates **43,224** nonempty integer box vectors, checks fixed-s signature injectivity and tests **406,650** directed close-neighbor candidates. All 60 possible positive retained totals match the theorem. The verifier produces \`R698_ALL_EXACT_ASSERTIONS_PASS\`, one nearest-pair witness per nontrivial total, and each fixed-s population size. No floating-point mathematical comparison is used.

Proof status: exact integer theorem for the frozen E* static BRC histogram observer; independently runnable finite checker supplied. Reviewer status: UNREVIEWED.

## 6. Next unit

Build one actual legal V29/V39 native labeled packet realizing an E* group-valued four-step path, with its PASS count, full ordered origin and end Cell, triadic/frame state and based-loop transform. Try to realize the two frozen m=3/m=8 contextual continuation probes as admitted V39 event words. Compute their actual available \`s\` observer and legal signature rank; use the above sharp bounds only if this interface maps correctly. Preserve failure witnesses and the mother triadic-closure/rotation objective.
