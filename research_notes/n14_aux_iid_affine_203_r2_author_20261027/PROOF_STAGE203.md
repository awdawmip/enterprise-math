# Stage203 — complete author-side all-real interval for external ternary IID N14

Status: **PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. Observed 2026-10-27. Scientific parent: immutable Stage202 author evidence `fc148f325b1a87193088445d8cd1c7c93fcd5f24`, Draft PR #1571. Canonical GLOBAL_KNOWLEDGE_V1 main read `73df6c0bcb2850ec1b0dc084692994224576d8d2`; Enterprise Math control main read `ec487c5347077af0374f6c71b046dd6094e311f3`; P000 startup projection matched original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. This finite external model is not a native X6 physical theorem, registered CLAIM, frozen Source Result or mathematical admission.

## Theorem with full quantifiers

Let `P=(3,1,20)/24`, `Q=(2,2,20)/24` be the three outcome probabilities, IID with horizon 14. Arbitrary randomized stopping and reporting may depend on **all ordered histories**. Let `eP=P(report Q)`, `eQ=Q(report P)`, `tP=E_P T`, `tQ=E_Q T` and `V14(alpha)=inf_{eP,eQ<=alpha} max(tP,tQ)`.

Define:
- `alpha202=3712577116979992345/10517860061584293888`,
  `V202=2226587199024284573/219122084616339456`;
- `K203=L203=17496/139`, `H203=188497771183924373447/1903623110104449024`;
- `Delta203=2484625/82170781731127296`;
- `alpha203=1237525705766008115/3505953353861431296`;
- `V203=2226587197356332573/219122084616339456`.

**Exact result.** For every real (including irrational) `0<=delta<=Delta203`:

`V14(alpha202+delta)=V202-(34992/139)*delta`.

For each feasible `alpha>alpha203`, the **fixed Stage203 supporting line** `H203-(34992/139)*alpha` is strictly below `V14(alpha)`.

## Lower bound including all full-history strategies

At count state `s=(n,a,b)` with `a=#symbol0`, `b=#symbol1`, the IID likelihood ratio is `Q/P=2^(a+b)/3^a`. Under P, the exact Bellman recurrence at K=L=17496/139 is

`h(s)=min{K*LR(s) [report P], L [report Q], 1+sum_i P_i h(child_i(s)) [continue, n<14]}`.

Exact Fraction backward induction visits **680** count states. Root h=H203, there are **1238 strictly positive** alternative action gaps, minimum `16319029/830103552`; precisely two ties:
- `T=(13,6,4)`: report Q / continue;
- `Z=(14,0,0)`: report P / report Q.

All other optimal actions are unique. Because the conditional IID suffix and likelihood ratio depend on counts only, this Bellman lower bound applies individually to **each** full ordered prefix, even for history-dependent randomized decisions:

`tP+K*eQ+K*eP>=H203`.

Thus every feasible strategy obeys `V14(alpha)>=H203-2K*alpha`.

## Achieving the lower bound and the mixed term

At T choose report Q with probability `t`, otherwise continue. At Z choose report P with probability `z`, otherwise report Q. Elsewhere use the unique Bellman minimizer. Define four-observer vector `O(t,z)=(eP,eQ,tP,tQ)`.

Exact four-corner suffix-DP plus independent unmerged ordered-integer DFS give

`O00=(637527963670398899/1752976676930715648,109862867795947/320979616137216,2226587199024284573/219122084616339456,259209256439735/26748301344768)`.

`DT=O10-O00=(17875/18786186952704,-17875/20061226008576,-17875/2348273369088,-17875/1671768834048)`.

`DZ=O01-O00=(-6103515625/78364164096,6103515625/78364164096,0,0)`.

`O11-O10-O01+O00=(0,0,0,0)` exactly. The zero mixed term has a structural proof: T has already observed six 0-symbols and four 1-symbols, whereas Z has no 0- or 1-symbols, so T can never lead to Z; Z is terminal so cannot lead to T. Hence for **all** real `t,z in [0,1]`, `O(t,z)=O00+t*DT+z*DZ`.

Error balance `eP=eQ` gives the exact affine law

`z(t)=112590665042401049/819200000000000000 + (121121/10240000000000)*t`.

Both values `z(0)` and `z(1)=112590674732081049/819200000000000000` are strictly between zero and one, so the policy is legal for all real t in [0,1]. Its common error is a **strictly increasing affine** function of t, from alpha202 at t=0 to alpha203 at t=1, of increment Delta203. The P time decreases from V202 to V203; `tP-tQ` is positive at t=0 (`103144970269975453/219122084616339456`) and at t=1 (`34381656981645151/73040694872113152`). Affine interpolation preserves positivity. The selected Bellman actions incur zero slack, giving `tP+K(eP+eQ)=H203`. For any real delta set `t=delta/Delta203` and `z=z(t)`; this attains the universal lower bound exactly.

## Strict-right proof for this fixed line

Finite-horizon randomized behavioral policies form a finite compact product of simplexes; observation maps are continuous and constrained minima exist. Equality in `max(tP,tQ)>=tP>=H203-K(eP+eQ)>=H203-2K alpha` for alpha>alpha203 forces eP=eQ=alpha, all P-positive reached decisions zero-slack, and max-time=tP. The non-tie actions are uniquely forced. Even if different ordered prefixes at T have different stopping coins, their conditional suffix laws and P/Q likelihood ratios coincide; their positive path-mass-weighted average gives one effective `t in [0,1]` with identical four-observer output. Z is one terminal all-symbol-2 prefix. Disjoint tie cones force O(t,z) above; equal errors force z(t), whose common error cannot exceed alpha203. Contradiction. Therefore strict inequality holds beyond the endpoint.

## Actual verification, typed carrier, and next unit

The actually executed primary source `verify_stage203.py` used exact Fraction Bellman and independent full ordered integer P/Q branch masses, with weights P=(3,1,20) and Q=(2,2,20), padding leaves by `24^(14-n)`. Four corner DP/DFS observations matched exactly. DFS per corner (t,z)=00:96406, 01:96406, 10:92974, 11:92974; **378760 nodes** total. First arrivals: 1144 ordered T paths, one ordered Z path, **zero** common visits. Actual stdout: `STAGE203_AUTHOR_EXACT_PASS 378760`. A second shorter independently runnable reference `REPRO_STAGE203.py` was also executed: `STAGE203_REFERENCE_EXACT_PASS 378760`. Exact corners and all checks in `certificate203.json`; execution summary in `RUN203_EXECUTION.md`.

BRC scope: preserve ordered branch identity/multiplicity and separate positive P/Q masses until the declared four-observer projection. Count compression is justified only for this finite IID suffix observer, **not** native X6 residual/field/time/rotation/three-dimensional slice dynamics; P000 transfer requires separate embedding, readout and relation-preservation evidence.

Next dual **candidate only**: `K204=L204=6550632/53665`, `H204=56640586903640112316369/587959333546792845312`, ties `(9,2,2)` Q/C and `(14,0,0)` P/Q. The 680-state exact scan found 1238 positive gaps, minimum `43804/1448955`; Stage204 primal is the next task (`NEXT_TASK_PACKET_204.md`).