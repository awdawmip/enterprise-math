# Stage201 — all-real exact optimum for external N14 ternary IID

**Status:** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM.
**Research date:** 2026-10-27 (Asia/Shanghai). GitHub connector identity: awdawmip; local author identity EM-R2-STAGE201-20261027T1934 is not a service-issued session or task owner.

**Scientific predecessor:** the completed Stage200 author result already in Enterprise Math [draft PR #1571](https://github.com/awdawmip/enterprise-math/pull/1571), observed at head 7f66ae09e450c30dce7c70ee96ea1678ca95ce03. The Stage200 theorem and Stage201 dual candidate were consumed, not recomputed as new discoveries. Input pins: GLOBAL_KNOWLEDGE_V1 main@63642a91a9dc85e64eef6f87e182fbc53acd9ca3; Enterprise Math main@549175b8d514ae4da9a126edca4387213f2647d1. P000 startup and original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc match; ACTIVE worldview and portable protocol govern scope.

## Exact theorem

For 14 IID observations on symbols {0,1,2}, let P=(3,1,20)/24 and Q=(2,2,20)/24. Arbitrary randomized stopping/decision rules may depend on the entire ordered history. Let eP=P(report Q), eQ=Q(report P), tP=E_P T, tQ=E_Q T, and V14(alpha)=min_(eP,eQ<=alpha) max(tP,tQ).

Take the Stage200 contact

- alpha200 = 3704473910272792345/10517860061584293888;
- V200 = 2269644909513884573/219122084616339456.

**For every real delta in [0, 4150390625/53496602689536],**

V14(alpha200+delta) = V200 - (1296/5) delta.

The new exact endpoint is

- alpha201 = 3705289910272792345/10517860061584293888;
- V201 = 2265238509513884573/219122084616339456.

Moreover, for alpha201<alpha<=1, the *fixed Stage201 Bellman supporting line* lies strictly below V14(alpha). No conclusion about the later optimal segment is implied by this last assertion.

## Dual bound for arbitrary complete histories

Use count state s=(n,a,b), where n is draws so far and a,b count symbols 0,1. Every ordered prefix with those counts has the same likelihood ratio Q(prefix)/P(prefix)=2^(a+b)/3^a and the same conditional IID suffix law.

Put K=L=648/5 and H=5568451006246740809/54780521154084864. Under P, the exact Bellman recursion selects the minimum of K*2^(a+b)/3^a (report P), L (report Q), and 1+sum_i P_i*h(child_i(s)) (continue, for n<14); continue is unavailable at n=14.

Exact Fraction induction over the complete finite count-state set gives h(0,0,0)=H, **680** states, **1238** strictly positive action gaps (minimum 34067479/2149908480), and precisely two non-unique minimizers:

- R=(13,3,1): report P versus continue;
- Z=(14,0,0): report P versus report Q.

All other actions at their states have strictly larger Bellman cost. Induction can be conditioned on *each full ordered prefix*; hence it applies to every history-dependent randomized policy, and gives

tP + K*eQ + L*eP >= H.

Together with eP,eQ<=alpha and max(tP,tQ)>=tP, this proves the universal lower bound V14(alpha)>=H-(1296/5)alpha.

## Primal matching curve

At R choose report P with probability r and otherwise continue. At terminal Z choose report P with probability z and otherwise Q. Follow the unique Bellman minimizer at all other states. Write O(r,z)=(eP,eQ,tP,tQ). A Fraction suffix DP and a separately implemented, unmerged ordered-history **integer-weight DFS** agree componentwise on all four deterministic corners, as recorded in certificate201.json.

With O00=O(0,0), the exact affine coefficients are

O00 = (
  628604330211198899/1752976676930715648,
  111002253395947/320979616137216,
  2269644909513884573/219122084616339456,
  267335980439735/26748301344768
).

D_R=O10-O00 = (
  -830078125/990677827584,
  830078125/835884417024,
  -830078125/41278242816,
  -830078125/69657034752
).

D_Z=O01-O00 = (
  -6103515625/78364164096,
  6103515625/78364164096,
  0, 0
).

The mixed term O11-O10-O01+O00=(0,0,0,0). This is an exact *structural* identity, not a floating-point cancellation: R contains three symbol-0 and one symbol-1 observations whereas Z contains none of either. Counts cannot decrease, so R cannot precede Z. Since Z is at horizon n=14, Z cannot precede R. The tie cones are disjoint and O(r,z)=O00+r*D_R+z*D_Z for all real r,z in [0,1].

The equal-error condition eP=eQ solves to the **exact coin law**

z(r) = 67152070994401049/819200000000000000 - (3009/256000)r.

Its endpoints z(0)=67152070994401049/819200000000000000 and z(1)=57523270994401049/819200000000000000 are both strictly in (0,1), so all r in [0,1] are feasible. Along this arc the common error increases strictly and affinely from alpha200 to alpha201.

The exact time differences tP-tQ are 79628557751575453/219122084616339456 at r=0 and 77833357751575453/219122084616339456 at r=1, both positive. Affineness gives max(tP,tQ)=tP for the entire arc. Every selected action has zero Bellman slack, hence tP+K*(eP+eQ)=H throughout.

For each real delta in the theorem choose r=delta/(alpha201-alpha200), and z=z(r). It exactly attains the universal bound H-(1296/5)(alpha200+delta), proving the identity including at irrational parameter values.

## Strict-right bound

The finite ordered-history behavioral strategy space is a finite product of compact probability simplexes; errors and expected stopping times depend continuously on policy parameters. A feasible constrained optimum is attained. If equality V14(alpha)=H-2K*alpha held for alpha>alpha201, strict positivity of K and the full chain of lower-bound inequalities would force both errors to equal alpha and the policy to select only Bellman-minimizing actions at all P-positive reached prefixes.

Outside R and Z the minimizing action is unique; all P prefix probabilities are positive. Full-history coins at one tie state have equivalent effective averages for these four observers because every arrival with the same count state has identical P/Q likelihood ratio and IID suffixes. Disjoint tie cones make the effective global policy exactly O(r,z), with r,z in [0,1]. Equal-error support enforces the displayed z(r), whose maximal common error is alpha201. Contradiction for alpha>alpha201. Since the constrained infimum is attained, the inequality is strict for that fixed supporting line.

## Exact executable evidence and BRC type boundary

The executed full checker (author file verify_stage201.py; SHA256 4e030991ac61f36cd207c44fcec29356bbe9e367020b0a560b3e8a8beedd0bf4) performed exact Fraction Bellman/suffix DP and independent unmerged ordered integer P/Q-weight DFS. Each ordered prefix retains symbol sequence, multiplicity and both positive integer weights: P-factor (3,1,20), Q-factor (2,2,20); stop leaves are lifted to denominator 24^14. Counts are compressed only for Bellman recursion under the declared finite IID suffix observer; this does **not** assert a lossless quotient for native residual/X6 dynamics, coherent phase amplitudes or P000 three-dimensional slices.

Four full-ordered DFS traversals visited 102319,102319,98494,98494 nodes (**401626 total**). First arrivals at R:1275, Z:1, both:0. All four 4-component corner observations matched. Bellman states, minimum gap, endpoint contact, coin feasibility, P-time dominance and dual equality passed with exact rationals. Executed result: STAGE201_AUTHOR_EXACT_FULL_REAL_PASS.

The smaller **REPRO_STAGE201.py** was *also locally executed* (STAGE201_REFERENCE_FULL_REAL_PASS 680 1238 401626), and its remote Git blob 3dc836b20f56de7ae18088cb607158b2b3404ad3 matched the executed bytes. The complete rational observation certificate is certificate201.json; the remote certificate contains the exact deterministic corners, affine coefficients, coins and endpoint equations.

## Stage202 handoff

A separate exact downward-directional scan from the Stage201 r=1 selected action found the **DUAL-ONLY** candidate K202=L202=94363551/741293 and H202=18568821153724089963922211/185638477110285856407552. The two Bellman ties are (6,0,1) Q/continue and Z=(14,0,0) P/Q; 680 states, 1238 positive gaps (minimum 16319029/1441073592). Stage202 primal matching/obstruction is the next unit. See NEXT_TASK_PACKET_202.md.

**Authority and admission:** Native em_status v0.6.11 reports research_authority_granted=false; bounded control-task read reported CONTROL_QUOTA. This is author-side portable evidence on a Draft PR. Native live owner, CLAIM, Source Result and distinct Driver mathematical admission require their actual authorized actions.