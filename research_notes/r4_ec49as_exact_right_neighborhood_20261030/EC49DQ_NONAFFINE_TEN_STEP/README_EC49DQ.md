# EC49DQ — Exact ten-step saturation certificates for arbitrary positive dual-BRC weights

**2026-11-01 | PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED**

## Source and scope

Retains the frozen scientific object from EC49DP (commit `0fa60548cdabc3905eef316afda3aa2fb57c6e89`), whose original science pins are GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e` and Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The separately refreshed behavioral-policy snapshots are GLOBAL_KNOWLEDGE_V1 `5e911ec053e9c921179b85b60364b3e0eb250693` and Enterprise Math main `e3298b14b8f868adb468085cc15c695aff11b6ef`. Original P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matched the current P000 startup projection; ACTIVE worldview and portable research instructions were read without modifying them.

All histories are ordered signed *native X6* axis-step paths with length n and endpoint D=(-2,0,0,0,0,0). Positive step +Ei has weights x_i>0 and y_i>0 in two separate multiplicative BRC channels; negative steps have factor 1; a third channel is unweighted count. Joint A=(+E1,+E2), B=(+E2,+E1) occurrences, including historical/future boundary crossings, and the two end ports are retained. Futures are h operations from a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), returning the full X6 endpoint to zero. Here h counts future operators, not primitive steps.

## New theorem: two sufficient parameter conditions, no affine hypothesis

Let x,y be arbitrary vectors in the **strictly positive real** six-dimensional orthant. If **I or II** holds, there are eighteen genuine histories of **length n=10**, all with endpoint -2E1, whose six-history-feature × three-instrument observation matrix is invertible.

**I — multiplicatively distinct first two axes.** Write u=x1, v=x2, U=y1, V=y2. Assume

`(u-v)(U-V)(u*V-v*U) != 0`.

For each of six invertible label/port feature groups take k positive E1 steps and 4-k positive E2 steps, k=1,2,3, using the already verified EC49DP finite-state native-path witness generator. Three instrument rows give

`G_I = [(u^k*v^(4-k), U^k*V^(4-k), 1), k=1,2,3]`;

direct exact expansion proves

`det(G_I) = -u*v*U*V*(u-v)*(U-V)*(u*V-v*U) != 0`.

**II — noncollinear off-core axis weights.** For any three distinct p,q,r in {3,4,5,6}, assume

`H_pqr = det([[x_p,y_p,1],[x_q,y_q,1],[x_r,y_r,1]]) != 0`.

For each of the same six feature groups take paths having the four positive steps 2E1+E2+Ej, j=p,q,r. Then

`det(G_II) = x1^2*x2*y1^2*y2*H_pqr != 0`.

This works even when x1=x2 and y1=y2, or when first-two-axis weight vectors are proportional.

Six historical feature vectors are z0=e0, z1=e1, z2=e2, z3=e3, z4=e1+e4, z5=e2+e5; their determinant has absolute value 1. The type-II witnesses have the following explicit six order-preserving templates (replace j with any of p,q,r):

```
z0: ( 1, 1,-1,-1,-1,-1, 2,-2, j,-j)
z1: ( 1,-1,-1,-1,-1, 2, 1,-2, j,-j)
z2: ( 1, 1, 2,-1,-1,-1,-1,-2, j,-j)
z3: (-1,-1,-1,-1,-2, j,-j, 1, 2, 1)
z4: ( 1,-1,-1,-1,-1,-2, j,-j, 2, 1)
z5: ( 1,-1,-1,-1,-1,-2, j,-j, 1, 2)
```

All eighteen paths have precisely ten primitive signed steps, all six displacement coordinates are checked, and their joint A/B and terminal-port tags are the stated z vectors. For each path w define the real row `(W_x(w)*z(w), W_y(w)*z(w), z(w))`. Reordering the independent six feature blocks gives, in the checker ordering,

`det(M_18) = -(det G)^6 != 0`.

This is a **uniform symbolic** determinant certificate for every positive parameter meeting I or II; numeric samples are not its proof.

**Consequence, conditional on the upstream EC49DO six-/five-feature future-observation lemma**: for every even h>=2 the exact-future rank is 15; for every odd h>=3 it is 18; cumulative futures 1..h (h>=2) have rank 18. Hence n=10 is the **first joint saturation length** in either regime. To see minimality: with n<=8 and D=-2E1 there are at most three positive steps. Any history with both A=B=1 must contain either the consecutive positive triple 121 or 212; only two positive-weight count vectors occur there, giving at most two instrument directions for that history feature. The other five features contribute at most three directions each, so odd/cumulative rank <=17. Higher even n inherit any saturation witness by prepending (-E6,+E6), which preserves the tags/ports and multiplies each positive BRC channel by a nonzero factor.

The new determinant identities, explicit witnesses, and n<=8 obstruction are directly checkable; the all-h future-observation is still an **author-side proof dependent on EC49DO**, not an independently admitted theorem.

## Executed exact checks

`VERIFY_EC49DQ.py` is self-contained Python 3 standard-library code, extending the intact EC49DP signed-X6 witness/observer checker; it generates all 54 real paths, checks endpoints, positive-weight counts and six historical features, builds the real concatenated history/future observations with all legal returning future words, computes 18×18 integer determinants with Bareiss, and verifies exact modular ranks over primes 1000003 and 1000033. The executable regenerates all witness paths and the complete original output JSON.

| Parameter case | x | y | det G | det M18 | h2/h3/h4/h5/cumulative ranks |
|---|---|---|---:|---:|---|
| I nonaffine | (2,3,5,2,4,6) | (3,5,8,7,2,11) | -180 | -34012224000000 | 15/18/15/18/18 |
| II x1=x2, y1=y2 | (2,2,1,2,4,5) | (3,3,1,4,2,7) | -1728 | -26623333280885243904 | 15/18/15/18/18 |
| II first two proportional | (2,3,1,2,4,5) | (4,6,1,4,2,7) | -9216 | -612709757329767363772416 | 15/18/15/18/18 |

In type II, H_345=-8 in both runs. Real returning future word counts for h2/h3/h4/h5/cumulative1..2 are 4/15/56/210/5. The program returned PASS for all 3 cases, all 3 eighteen-step witness groups, all 15 real future-observation matrices, 30 modular rank checks. Finite checks independently cover these explicit integer instances, not all positive parameters or infinitely many h.

## Scientific increment and EC49DR

EC49DP's affine x1=x2 branch has n=12 minimum; the second explicit strictly positive **nonaffine** parameter example has x1=x2 and y1=y2 but reaches n=10 by leveraging genuinely different off-core native-axis joint weight points. Thus a zero two-axis determinant is a *certificate failure*, not necessarily a genuine rank defect.

Next EC49DR: compute exact necessary/sufficient conditions for n=10 full rank under all x,y>0. Enumerate the weight points (W_x,W_y,1) for each of six historical features over all admissible four-positive-step multisets, derive verified generators for the maximal-minor ideal, and seek parameters where both I and II vanish but rank remains 18 (or exhibit a true defect). Independently review the inherited EC49DO future-feature lemma.

**Permission and publication boundary:** GitHub connected identity awdawmip has repository push, but native session_start returned STATIC_READONLY_SCOPE_DENIED and owner listing returned CONTROL_QUOTA in this run. No valid native RA, CLAIM, Result, Review or Driver admission was obtained; these three GitHub draft files are portable mathematical research only. No credentials or global protected worldview were changed.
