# T6 p13 q10 splits (0,10) and (1,9): complete smooth-domain exact Driver audit
2026-11-24. Continuation of Driver lane EM-DVR-DEBB5E from authenticated r550. Original author EM-DIRECT-D03BC9, RA-A468735D7C934B25C4B9614F. Shared prior source and lattice method; independent implementation and execution of the smooth-domain finite search and separate DP/witness verification. No clean-blind claim or native admission.
Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca, each side mass cap 2331, conditional on prior high-valuation/high-prime exclusion and common named atom reduction. Author aggregate certificates actually read:
- fb3d08aa97c4003c7f1bfd370fc33dae97cae602:research_checks/T6_P13_Q10_SPLIT0_10_FULL_COVERAGE_AUTHOR_AUDIT_20261124.json (blob fc405b95c6d4fb64e44363e22723e112d902cb9e).
- 537232330df7532ce0cd0e0cefbb9cc82ca9227f:research_checks/T6_P13_Q10_SPLIT1_9_FULL_COVERAGE_AUTHOR_AUDIT_20261124.json (blob a8c72dbe6fa9edc2b364a848df3b21903dcf2fc4).
Prior independent split37/46/55 frontier 8454389 searches, r550 readback.

## Complete exact executed audit
|split|partition families|literal raw|literal disjoint|literal mass eligible|smooth raw|smooth common|smooth vertical overcap|smooth searched|GS nodes|ball leaves|budget valid|two-child nodes|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0,10|42|5098938|5098938|2795372|518398|0|211410|306988|840250|4|0|903|
|1,9|30|20036640|13781820|12619239|1861101|710613|98834|1051654|2528141|5|0|14|
|total|72|25135578|18880758|15414611|2379499|710613|310244|1358642|3368391|9|0|917|

Python actual enumeration times 7.655 and 9.810 seconds (container, excluding basis preparation). Separate JS DP verified every one of the 72 literal pattern count rows against the two author aggregates, as well as the smooth totals independently. Recomputed all 107 original witness masses and all six modular residues with BigInt Euclidean inverses. All are overbudget, 98 nonsmooth; all nine smooth witnesses agree exactly with independently decoded vectors and masses.

## Important branch correction
The prior one-nearest-integer decoder requires 4*radius_sq < min(D). It must not be extended unconditionally to (0,10) or (1,9). Actual exact search encounters 903 and 14 two-child nodes respectively. Here radius_sq=(2331-cp)^2+(2331-cn)^2 <= 2*2331^2 < min(D), so both adjacent integers around the center suffice, including ties; more distant integers have squared displacement >=1 and cannot fit. Enumerating both and applying exact accumulated GS norm pruning closes the branch. No claim that a one-nearest implementation would necessarily miss a final leaf; the two-child counts establish its single-path justification is unavailable at these nodes.

## Smooth witnesses
|split|positive roster|negative roster|masses|norm_sq|radius_sq|
|---|---|---|---|---:|---:|
|0,10|empty|11,11,13,13,3:11,3:11|1632/5460|3702638|5499610|
|0,10|empty|12,15,18,24,26,39|2183/6806|5322211|5475586|
|0,10|empty|11,17,17,1:12,1:12,29,31|2110/6818|4607340|5433682|
|0,10|empty|12,13,13,15,18,18,1:11,39|2377/6435|5077473|5433705|
|1,9|17|12,21,22,22,29|959/6622|4419826|4661633|
|1,9|1:11|12,12,12,15,29,39|2280/5669|3388440|4273121|
|1,9|11|13,18,18,1:12,22,33|3673/4465|4199022|4743604|
|1,9|15|17,17,17,18,1:12,22,22|2369/4649|2650846|4455428|
|1,9|17|11,13,13,13,18,18,18,18,1:11|3019/5226|3798151|4310084|
Roster shorthand qr denotes (q,r) for single digits, q:r otherwise. Every negative mass alone exceeds 2331. All nine satisfy six homogeneous mixed congruences and relaxed weighted sphere condition.

## Reproduction
Use saturation, weighted HNF/LLL, rational GS, integer scaling and particular vectors from a466be736446891b423809b0ba23cb37ec123502:research_checks/T6_P13_Q10_SPLIT3_7_NEG1123_INTEGER_GS_REPLAY_20261124.py. Reconstructed lattice det=13^21, verified every homogeneous row and each particular vector, and exact integer scaling.
Q=4826809, min(D)=78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349.
Extend c_atom to q=1..10, retaining only r with 13q+r smooth over {2,3,5,7,11,13}. Residue lists q=1..10:
[1,2,3,5,7,8,9,11,12]; [1,2,4,6,7,9,10]; [1,3,5,6,9,10,11]; [2,3,4,8,11,12]; [1,5,7,10,12]; [2,3,6,10,12]; [5,7,8,9]; [1,4,6,8]; [3,4,8,9,11]; [2,5,10].
For each integer partition of each side q total (empty tuple for 0), group repeated q and generate combinations_with_replacement over its smooth residues; Cartesian product across groups. Compute vertical mass sum(169q+13r-1) and sum of particular coordinate numerators mod Q. For each pair exclude common named atom, exclude either vertical mass > cap, run the exact two-child recursion:
```python
def descend(i,spent):
    if i<0:
        u=[sum(z[j]*Urows[j][t] for j in range(12))//Q for t in range(12)]
        # assert divisibility before division, verify all residues, norm, original masses
        return
    center=c[i]*(L[i]//Q)+sum(z[j]*B[i][j] for j in range(i+1,12))
    near=(-center)//L[i]
    for v in (near,near+1):
        ns=spent+T[i]*(center+v*L[i])**2
        if ns<=radius*K:
            z[i]=c[i]+v*Q
            descend(i-1,ns)
    z[i]=c[i]
```
c=(positive numerator-negative numerator) mod Q, z=list(c), start descend(11,0). At each leaf recover exact integral u; verify original masses cp+sum(W*max(u,0)), cn+sum(W*max(-u,0)).
Independent count DP: for each q multiplicity m, coefficient table dp[k][s], dp[0][0]=1, iterate permitted r, then k=1..m and s=r..120 increasing, add dp[k-1][s-r] into dp[k][s]. Convolve dp[m] across distinct q. For split1 exclude positive rho from negative q1 alphabet; sum over allowed rho. Eligible residue sum S<=floor((2331-169*q_negative+length)/13). Run with literal 1..12 and smooth lists separately. This independently verifies all author row counts and smooth totals above.

Combined prior split37/46/55 plus these two branches = 9813031 exact smooth searches, zero budget-valid vectors, five of six unordered q10 signed splits. Remaining split(2,8) independent decoder audit, and upstream reductions/other q/prime/H0 mother scope remain open. No formal Result/Task closure.
## Control
Current em_status and r550 exact checkpoint read successful. Original own recovery request dvr-20261124-2000-own-recovery-metadata-v1 control_result read returned UPSTREAM_OUTCOME_UNKNOWN, operation_sent=true; retain original ID, no write replay. Original author r136 checkpoint shows split28 coverage audit ongoing (20/22 families), preserve author activity and attribution. No new protected review or claim performed.
