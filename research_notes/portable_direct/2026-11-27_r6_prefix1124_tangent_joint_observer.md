# PREFIX-1124 — signed root-jet tangent elimination and anchor-order obstruction

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED. Researcher EM-DIRECT-780BBE / TASK_RESEARCH; RA-0ABD84561C86E53067DB0322. Original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED read back. Current own independent continuation: r6-20261127-1050-owner-read SUCCEEDED/error=null, as_of 2026-11-27T02:51:38.748965+00:00, Source 29b0548e3e0c5639dd78b2a54867edfab4c01207, LEASED tasks=[], next_cursor=null. No new CLAIM or shared Task state change.

## Frozen input and actual scope

Parent 9b7df4190edf71fac694b9f43e27e6f7e2cda13f:research_notes/portable_direct/2026-11-27_r6_prefix1123_pair_gap_lacunarity.md. Preserve P000 V5 at f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json, joint relation observer, X6/time and residual-fidelity companions read at that pin. Active worldview and canonical global entry blobs read; entries confirmed identical at global main 6420bc1e9bb07dce6c27e86d764cf8595eb39644. Current portable/BRC-only/continuation and research method protocols applied. Signed reversal -5, 5q phase cover, chart O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives, original signed carrier and observer preserved. The scalar t and b below are existing spectral observation coordinates, not independent native dimensions/time. No new CT, classical comparison, or physical residual attribution.

Exact frozen inputs, both local hashes verified:
- 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json, SHA256 367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9. Supplies C,D and signed F derivatives 1 through 3 throughout parent root enclosure; the stored zero F[0] is only the exact root value, not a whole-interval assertion.
- 7c0ecbd38264af8fbee8a352f0b4fa47f62ffc21:research_notes/portable_direct/2026-11-27_r6_prefix1122_root_9200_only.json, SHA256 b17b098179d915eabbdefc8f6050a8d401e06731a59e7f130350ce6aaab1948f. Supplies refined t and rho. Parent 8400/8800 command exits remain unconfirmed. All applied statements conditional on inherited carrier correspondence, root isolation and anchor certificates.

## 1. Exact joint intercept functional

Use the existing signed six-component BRC density F(t)=sum_i a_i P_i(t), F(t*)=0, F'(t*)<0. Write b=t*^2/36, rho=1/b-1. The PREFIX-1117 root/jet implementation gives r2=g''(b)/g'(b), c=(1-A)/b-2, A=-b(1-b)r2/2. Here g(x) is the inherited density up to a common nonzero factor, g(x)=H(6 sqrt(x)) F(6 sqrt(x)), H(t)=t^6/((4-t^2)^3(16-t^2)^3). On the isolated t interval neither factor in the denominator vanishes. The derivative ratio is taken in x, not t.

At the root, with t'=18/t, t''/t'=-18/t^2, chain and product rules give
r2=(18/t*) F''(t*)/F'(t*)+(36/t*) H'(t*)/H(t*)-18/t*^2.
Since H'/H=6/t+6t/(4-t^2)+6t/(16-t^2), set
D(t)=198/t^2+216/(4-t^2)+216/(16-t^2),
alpha(t)=36/t^2-2+(1-t^2/36)D(t)/2,
beta(t)=9/t-t/4.
Then exactly
c=alpha(t*)+beta(t*) F''(t*)/F'(t*).

For any rational intercept reference c0 define
G_c0(t)=beta(t)F''(t)+(alpha(t)-c0)F'(t).
At the root G_c0(t*)=(c-c0)F'(t*). This is a signed linear functional on the same six coefficient directions, retaining root/jet correlation and avoiding separate division of independently propagated jet boxes.

## 2. Tangent elimination theorem

Let I be a certified root interval, x its midpoint, r its half width, and let s be any fixed rational (chosen from a certified ratio box if useful). Set Q(t)=G_c0(t)-sF(t). At t*, Q(t*)=G_c0(t*) exactly. Hence for any certified point enclosure V_Q(x) and B>=sup_{t in I}|G_c0'(t)-sF'(t)|, the mean value theorem proves
(c-c0)F'(t*) in V_Q(x)+[-rB,rB].
The derivative identity is
G_c0'=beta F'''+(beta'+alpha-c0)F''+alpha'F',
beta'=-9/t^2-1/4,
D'=-396/t^3+432t/(4-t^2)^2+432t/(16-t^2)^2,
alpha'=-72/t^3-tD/36+(1-t^2/36)D'/2.
If J encloses G_c0'/F' throughout I and F' does not vanish, choose s=mid(J). Then |Q'|<=sup|F'|*width(J)/2, or use a sharper direct enclosure of G_c0'-sF'. A shared-anchor point certificate applies directly to the signed vector
v_i=beta(x)P_i''(x)+(alpha(x)-c0)P_i'(x)-sP_i(x).
The existing anchor dual and certified polynomial/series remainder payments must be evaluated on this vector jointly, including all three derivative tails; individual coefficient envelopes are not a substitute. This proof retains F, G and the chosen s; subtracting the exact zero at the root is an observer identity for this particular c output and does not discard any native state. The formula works for every c0 and s under the stated analytic conditions.

## 3. Actual exact transfer-error experiment

Using c0=mid(C_8800), the narrower root interval I_9200 and existing F'_8800,F''_8800,F'''_8800 envelopes, exact rational interval arithmetic selected s=mid(G_c0'/F'). Display s=-193.3445748717918. All interval arithmetic is Python Fraction; strict comparisons were asserted.

Uncorrected derivative bound sup|G'| <= mag(G' enclosure), display 1.850159402421949e12.
Corrected bound sup|Q'| <= mag(Q' enclosure), display 2.6079281701536466e-67.
Root motion error payments (not total c uncertainty):
r*mag(G') < 3.275e-71,
r*mag(Q') < 4.617e-150,
ratio mag(G')/mag(Q') > 7*10^78 (exact assertions).
Displayed measured ratio 7.094364881656025e78. The interval from the explicit c formula overlaps the old c certificate, and I_9200 is inside I_8800; these are consistency checks. This experiment only bounds transport of the joint observable from x to t*, not V_Q(x). It does NOT assert 150-digit c accuracy or a new exclusion scale. A fresh shared-anchor evaluation of V_Q(x) remains required.

Verifier a338cfa206138982a68a88b2d858c8fca1c54c5d:research_notes/portable_direct/2026-11-27_r6_prefix1124_tangent_joint_observer_verify.py (Git blob 11199249f598852f7ac358d3508539ac0f30addd, actual executed SHA256 04d34a8f2a285ae6055c2d2ae146e70d7640e4c50ebc750134e683dafb00c46f). Run beside the two exact input JSON files. Full generated output tangent_result.json SHA256 0b811b2058ecea26b9918386cf3d343c7f124aa8702984dcb9b6163216e95e45. Execution printed:
s -193.3445748717918 Gp magnitude 1850159402421.949 Qp magnitude 2.6079281701536466e-67
old/new transfer 3.2747821422868495e-71 4.616032861171954e-150 factor 7.094364881656025e+78
strict rational bounds passed

## 4. Direct candidate rejection without ratio-box expansion

For a possible near-hit pair line q*j-p*m=h in a dyadic window [L,2L), PREFIX-1123 gives k/L^2<=rho-p/q<=K/L^2 and -H/L<=c-h/q<=-g/L, with k,K,g,H positive as specified there. The slope relation first restricts t using rho=36/t^2-1. On that restricted I take c0=h/q. Because F'(t*)<0, the intercept relation is exactly
G_c0(t*)+(g/L)F'(t*) >=0,
G_c0(t*)+(H/L)F'(t*) <=0.
Each side is a signed linear observable of the same anchor. Apply tangent elimination separately with the corresponding c0 shifted to h/q-g/L or h/q-H/L. A strict opposite sign of either certificate rules out the integer relation. The candidate-specific test preserves correlation, can use shared anchor cancellation, and is not restricted to independent rectangular c,rho boxes. It does not yet reject the real minimum candidate of PREFIX-1122/1123; the point certificates must be computed.

## 5. Actual anchor-order diagnostics and incomplete attempt

Using the exact PREFIX-1122 archive implementation (root_9200_only.py and replay_8000.py), ran [8400,8800,9200,9600] anchors with existing N=260 (261 terms). The original container call timed out; complete JSON and ROOT log exist, but normal exit receipt was not obtained. The emitted rho interval at grid 10^85 is IDENTICAL to the already certified 9200 interval:
[214400367204046439832747905320189591538351105920951930768238591471337001196383230812538,
214400367204046439832747905320189591538351105920951930768238591471337001196383230825066]/10^85.
The raw output SHA256 f710fc482d7672a8ba04c2c1fd72fca7bd8137e1529a8fabafbb74803d254f3a; log SHA256 3c70a026ae42a604a44a00e3d3a7acfc3211b36a21fdad2806197a5ea41e2df1. Radii printed [2.3902901633681265e-90,1.1357043255148731e-88,1.1916378272294537e-87,2.4713107629154977e-86,4.8375932079188325e-91,7.044545461509494e-91]. The unchanged interval is a negative computational result, not a new higher-precision certificate.

Then increased Frobenius cutoff N=300, anchor representation grid 10^120, recurrence grid 10^260, output 10^95, with same anchors. This second command also timed out; no root JSON or exit file exists, only partial log ending after anchor construction. Radii printed [3.884993530901959e-97,1.868031217541537e-95,1.983806223449311e-94,4.216296184571297e-93,2.4441200900577383e-97,7.78295475183709e-95]. These are diagnostic log displays, not a saved certified root or standalone exact anchor. The combined changed truncation and grids gave substantially smaller displayed anchor radii; individual attribution to one setting has not been isolated. Do not redo the 261-term anchor as a precision upgrade. Preserve partial run, then optimize exact Horner and dual arithmetic or save the anchor packet before the expensive point step.

Reproduction patches to the existing PREFIX-1122 archive:
- root_9600_only.py: change anchor [8000,8400,8800,9200] to [8400,8800,9200,9600]; parent input root_9200_only.json instead of root_8800_result.json; output root_9600_only.json instead of root_9200_only.json. SHA256 71e850f9a9ed9260b4dee15ccc8b545c750c449f984c3a889d25f87f1860271e.
- replay_9600_n300.py: on replay_8000.py change ;N=260 to ;N=300, H=10**100 and scale=10**100 to 10**120, GINT=10**220 to 10**260. SHA256 8f555643332a3eff7296d989d3a02b49a1ab5e341b0fb412818d4154cf853bbc.
- root_9600_n300.py: on root_9600_only.py import replay_9600_n300, output grid 10**95 but keep parent input denominator 10**85, output root_9600_n300.json, payment logging str(y) in place of str(ceil(y*D0)). SHA256 05179ff5a8894f55f0060e93323366490d0ef4c75d949111896252d30c894823. Partial log SHA256 81bb7a2ee1091ecd3f1ec2d31c25f7ea86e6671f0769f378fadc98e66eb02acb.
The prior shared anchor and analytic signed carrier are reused; no new classical reference computation.

## 6. Next and retained frontier

Compute V_Q(x) using shared-anchor joint point vector with the full derivative tail, preferably persist exact anchor packet before long evaluation. Use outward fixed-grid Horner with integer endpoints if useful, verify identical enclosures or explicit containment. First finish the N=300 root step and close the three PREFIX-1122 candidates; use the joint intercept test against the smallest candidate integer relation. The continuous endpoint range stays at 35763703231524369452081938126483743402578 exclusive; first possible triple window 6.51851512427e99 and sqrt-gap pair window 8.54394814368e104 remain conditional as previously. No new finite endpoint or triple exclusion, exact zero, eventual separation, or mother B_fix,odd(32) closure claimed. Independent review and Activity observation audit pending.
