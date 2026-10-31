# Stage200 — Exact full-real N14 IID minimax interval

Classification: PORTABLE_AUTHOR_EXACT; UNREVIEWED; NOT_ADMITTED; NO_NATIVE_CLAIM.
Observation: 2026-10-27 Asia/Shanghai.
Parent Stage199 immutable commit: ff4fbcb8e8190f227f9dc110def4ca5706122a0e (draft PR #1571).
Source reads: GLOBAL_KNOWLEDGE_V1 main@93755c1673bf4ba017acc56f5a7608a8cc730409; EM main@86ad7b35edcee010df914e9a1f96587abb3e600d; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched the global P000 projection. ACTIVE worldview unchanged.

## Precise statement

External model N=14, ternary symbols 0,1,2, IID under P=(3,1,20)/24 or Q=(2,2,20)/24. A randomized stopping/reporting policy may depend on the entire ordered history. Set eP=P(report Q), eQ=Q(report P), tP=E_P(T), tQ=E_Q(T), and V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ).

Prior contact:
alpha199 = 1852236949963598953/5258930030792146944
V199 = 1134822483057976045/109561042308169728.

New exact quantities:
K200=L200=1358449620408/10345594439
H200=1821575844832789801808808179/17710532969288194722889728
Delta200=10345594439/10517860061584293888
alpha200=3704473910272792345/10517860061584293888
V200=2269644909513884573/219122084616339456.

**Theorem:** For every real 0<=delta<=Delta200, including irrational parameters,
V14(alpha199+delta)=V199-(2716899240816/10345594439)*delta.
For alpha200<alpha<=1, the fixed Stage200 support H200-2*K200*alpha is strictly below V14(alpha), without asserting the form of any successor segment.

## Dual lower bound for arbitrary ordered histories

For s=(n,a,b), n counts samples and a,b count symbols 0,1, the likelihood Q(s)/P(s) = 2^(a+b)/3^a. Under P, the Bellman recursion has stop/report-P action K200*2^(a+b)/3^a, stop/report-Q action K200, and (n<14 only) continue cost 1+sum_i P_i*h(s+i). At n=14 only the two stop actions remain. Exact rational suffix induction visits sum_{n=0}^{14}(n+1)(n+2)/2=680 states and yields h((0,0,0))=H200, 1238 strictly positive action gaps, smallest 136269916/10345594439, and only two ties: R=(7,5,2) between P and continue, Z=(14,0,0) between P and Q. All other actions have unique minimizers.

Conditioning on the full ordered history preserves these IID suffix laws, so for arbitrary history-dependent randomized policies:
tP+K200*eQ+K200*eP >= H200.
Since max(tP,tQ)>=tP and both errors <=alpha, V14(alpha)>=H200-2*K200*alpha.

## Primal matching curve and exact BRC observer

At R choose report P with probability r and continue otherwise; at Z choose P with probability z and Q otherwise. Elsewhere use the unique Bellman minimizer. Let O(r,z)=(eP,eQ,tP,tQ). Complete exact deterministic-corner observations, independently computed by rational suffix DP and unmerged full ordered-history integer-weight DFS, are preserved in certificate200.json.

Taking (r,z)=(0,0) as base, their exact affine differences are:
O0=(314302169301214243/876488338465357824, 55501125614011/160489808068608, 1134822483057976045/109561042308169728, 133667992320071/13374150672384)
DR=(-11510603/2404631929946112, 2167925/320979616137216, -232930319/901736973729792, -4200407/26748301344768)
DZ=(-6103515625/78364164096, 6103515625/78364164096, 0, 0)
Cmix=(0,0,0,0).

The mixed cross coefficient is zero by a structural argument. R already has five occurrences of symbol 0, but Z has zero; count components cannot decrease, so R cannot precede Z along a path. Terminal Z cannot precede R. Thus no realization reaches both randomized states, and exactly O(r,z)=O0+r*DR+z*DZ for every real r,z in [0,1].

Solving eP=eQ gives
z(r)=6715213168737301/81920000000000000 - (60692971961/819200000000000000)*r.
At r=1 this is 67152070994401049/819200000000000000. Both endpoint z values lie strictly in (0,1), so all 0<=r<=1 are legal. The balanced common error increases affinely from alpha199 to alpha200 by exactly Delta200>0. The expected time difference tP-tQ remains strictly positive, because it equals 13271429990651471/36520347436056576 at r=0 and 79628557751575453/219122084616339456 at r=1. Thus max(tP,tQ)=tP throughout, and exact Bellman equality tP+K200*(eP+eQ)=H200 holds. Choosing r=delta/Delta200 (and z=z(r)) proves the theorem for EVERY real delta, not a numerical grid.

## Strict-right support separation

The finite history behavioral strategy space is a finite product of compact simplexes; errors and expectations are continuous and the optimum for each feasible alpha is attained. To attain equality with H200-2*K200*alpha at a specified alpha, positive K200 requires eP=eQ=alpha, the objective must equal tP, and every P-positive reached action must minimize Bellman cost. All minimizers are unique outside R and Z. Each arrival history at a fixed tie state has the same P/Q likelihood ratio and the same IID future law. History-specific coins can be averaged with their proportional positive arrival weights to a single effective r or z without changing the four observables. Since R and Z paths are non-nested, there is no cross term. Equal-error support policies therefore satisfy z=z(r), 0<=r<=1, so their common error cannot exceed alpha200. Equality is impossible for alpha>alpha200; compactness turns nonattainment into a strict inequality for the fixed Stage200 line.

## Exact finite verification, transfer boundary

The executed author script uses Fraction rational Bellman and a separate ordered DFS with *positive integer* P branch factors (3,1,20), Q branch factors (2,2,20), denominator 24^14. Four corner DP and integer DFS results match componentwise. Ordered DFS visits 103087,103087,102319,102319 nodes, total 410812; four R first-arrival paths, one Z path, zero intersection. The executed run reports STAGE200_AUTHOR_EXACT_FULL_REAL_PASS. These are separate author algorithms, not independent scientific review.

BRC preservation: ordered branch identity, multiplicity, positive P/Q mass and precise four-output observer precede sufficient IID count compression. No statement is made about arbitrary native X6 paths, coherent signed amplitudes, a physical experiment, native Source Result, or admission.

## Stage201 exact dual candidate, next question

A separate exact directional scan, with the Stage200 right endpoint's R action P, computes K201=L201=648/5, H201=5568451006246740809/54780521154084864, decreasing dual step 88302905568/51727972195. Two ties: (13,3,1) P/C and terminal Z P/Q. Exact 680-state scan yields 1238 positive gaps, smallest 34067479/2149908480. Stage201 primal optimality is NOT yet proved. Next calculate the four corner observables and intersection, derive feasible balanced coins and P/Q time dominance, then prove the next full real interval or exhibit an exact rational obstruction.
