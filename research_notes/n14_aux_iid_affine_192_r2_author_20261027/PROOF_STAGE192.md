# Stage192 — Exact all-real optimal interval in the external N14 IID stopping model

2026-10-27. **AUTHOR_EXACT / PORTABLE_RESEARCH / NOT_ADMITTED**. No native Source CLAIM, independent Driver verdict or P000 X6 transfer is asserted.

## Frozen authority and question

GLOBAL_KNOWLEDGE_V1 canonical read snapshot: `main@fd68f262d614470f7aaf2b03d1591656e0dc0373`. Enterprise Math canonical scientific snapshot: `main@134c9337ccf235864e6bb7ed6588b27386ac60b5`. Read bootstrap/manual, P000 V5, ACTIVE worldview, joint observer preservation, BRC rules, native X6 typing and portable research protocol. Predecessor: Stage191 author-level branch `research/r2-n14-stage191-author-exact-20261027-1345-turn11`, adjacent proof and Stage192 dual-only packet. This work is by the current automation research conversation, not a transferred service identity.

For N=14 independent ternary observations, set P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). The policy may depend on the **entire ordered observation history**, randomize, stop by N and decide P or Q. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P T, tQ=E_Q T; define V14(alpha)=min max(tP,tQ) over eP,eQ <= alpha.

**THEOREM (all real parameters).** With
`alpha191=4019708522944196853791/11447745713044595933184`,
`V191=488968003499440699225081/45790982852178383732736`,
for every real 0 <= delta <=
`1477543629241684565/6677851665942680961024`,

```
V14(alpha191+delta)
  = V191 - (96604728331907459044/295508725848336913)*delta.
alpha192 = 28155690184160278191317/80134219991312171532288
V192     = 3399590889696427104405007/320536879965248686129152
```

Moreover the **fixed Stage192 Bellman supporting line** is strictly less than V14(alpha) for every real alpha>alpha192. This is not a global value formula beyond this endpoint.

## Universal dual lower bound (all complete ordered histories)

For s=(n,a,b), the likelihood ratio of every ordered prefix with these counts is ell(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a. Exact parameters are

```
K=48460834424347609212/295508725848336913
L=48143893907559849832/295508725848336913
H=75225538324811500070605605945717953/599560074353758700400961143177216
```

Backward recursion `h(s)=min(K*ell(s),L,1+sum_i P_i*h(s+symbol_i))`, with no continuation at n=14, has root H. It tests exactly 680 states. Only two ties: X=(8,0,1) Q/C and Y=(3,2,0) P/C; exactly 1238 other action gaps are positive, minimum `380166467087574396707/9191503408786671341952`. Every prefix under arbitrary full-history policy satisfies the same conditional Bellman action bound; randomized actions preserve it by convexity. Backward conditioning therefore proves `tP+K*eQ+L*eP >= H` universally, hence `V14(alpha)>=H-(K+L)*alpha`. Both multipliers are positive.

## Four exact corner policies and BRC carrier

At X, x=Pr(decide Q) (else continue); at Y, y=Pr(decide P) (else continue); elsewhere choose the unique minimizing action. Y cannot be an ancestor of X: its first-symbol count a=2 at depth 3 cannot decrease to a=0 at depth 8. X cannot precede Y by depth. Thus the tie first-hit cones are disjoint and the exact bilinear mixed term is zero.

With observation vector O=(eP,eQ,tP,tQ), two independent finite calculation routes establish `O(x,y)=B+x DX+y DY`, where:

```
B  = (611612348641150649/1752976676930715648,
      113284954538369/320979616137216,
      2354998878605994935/219122084616339456,
      282753724278565/26748301344768)
DX = (84427421875/17832200896512,
      -58984375/15479341056,
      -326450234375/2229025112064,
      -26297890625/104485552128)
DY = (-19980513159385/48693796581408768,
      39030321085/53496602689536,
      -107116516698745/2028908190892032,
      -130961897105/4458050224128)
C  = (0,0,0,0).
```

The rational suffix-DP and separately unmerged *ordered-history* integer-weight DFS agree at all four deterministic corners, with P integer weights (3,1,20) and Q weights (2,2,20), each divided by 24^14. DFS node counts for 00/01/10/11: 166990, 151906, 166222, 151138, total **636256**; the X first-hit count is 8, Y first-hit count 3, and both ancestry counters zero. Precise corner values and coefficients are preserved in the source-linked certificate and the complete local executed evidence archive. Positive branch mass is not signed-amplitude cancellation; count compression is used only for the exact finite IID four-observer horizon, retaining ordered provenance in the DFS. BRC result: `REUSE_EXECUTED`.

## Full-real primal attainment

Solve eP=eQ exactly:

```
x(y) = 3031949890455107/6419704320000000
       + (99912201752557/748965504000000)*y,   0<=y<=1.
```

The initial x(0) is **exactly** the Stage191 endpoint coin. At y=1, x=27218381338339169/44937930240000000<1. Thus all intermediate **real** randomizations are valid, and Y reaches its coin boundary first.

Direct exact substitution yields

```
eP(y)=eQ(y)
 = alpha191+(1477543629241684565/6677851665942680961024)*y;
tP(y)
 = V191-(120755910414884323805/1669462916485670240256)*y;
tP(y)-tQ(y)
 = 31077266276180245476059/137372948556535151198208
   -(23490043248460962665/2504194374728505360384)*y.
```

Common error grows strictly. P time decreases strictly, and the last time gap is positive at y=0 **and** y=1 (at y=1: `208520687325852708669053/961610639895746058387456`), hence positive throughout. Every selected action is a Bellman minimizer; affine interpolation therefore obeys `tP+K*eQ+L*eP=H` identically. The ratio of negative time slope to positive error slope equals K+L=`96604728331907459044/295508725848336913`. Choosing y=(alpha-alpha191)/(alpha192-alpha191) attains the dual lower bound at every real alpha in the interval; max(tP,tQ)=tP.

## Strictness to the right

Finite-horizon behavioral policies form a finite product of compact simplices and the objective/constraints are continuous; the optimizer exists. Equality with the fixed line at alpha>alpha192 forces (i) **both** eP=eQ=alpha, since K,L>0, and (ii) Bellman-minimizing actions at all reached complete histories. Only X and Y may randomize. Prefixes hitting one tie have the same positive P/Q likelihood ratio and IID suffix statistics, so P-mass-weighted averaging of any history-specific tie probabilities gives one effective x or y preserving all four observations. Disjoint tie cones give the same O(x,y) for every equality strategy, not just count-state strategies. Error equality then forces the displayed x(y), and legal y<=1 implies alpha<=alpha192 — contradiction. Compact attainment turns inequality into **strict separation** for every alpha>alpha192.

## Exact evidence, limits, continuation

The actually executed local `VERIFY_STAGE192_EXECUTED.py` ended with `STAGE192_AUTHOR_EXACT_FULL_REAL_PASS`; it uses `fractions.Fraction`, suffix DP and separate unmerged integer DFS. This branch's `REPRO_STAGE192.py` is a source-linked reference checker derived from the previously published reference implementation; do not mistake remote source storage for remote execution. Full proof, original executed code, raw stdout, rational certificate and per-file SHA256 hashes are in the linked portable archive `EM_STAGE192_AUTHOR_EXACT_PORTABLE_20261027.tar.xz`, archive SHA256 `060f27647edcb0b61fffa9f8465d138ad62cb4f4a3f8a27bbbb347d9d1bbba2a`. Remote reference and local executed code may differ textually; they implement the same stated model.

A fresh exact Stage193 dual-only scan identifies X Q/C and W=(2,2,0) P/C, with 680 states and 1238 other positive gaps. See `NEXT_TASK_PACKET_193.md` and adjacent `REPRO_SCAN_STAGE193.py`. The Stage193 **primal** interval is not yet proved.

The connected native status was read-only: `research_authority_granted=false`; current Source owner was not authoritatively established and no official CLAIM/Result/independent review is inferred. For any native P000 X6 theorem, separately supply an explicit six-dimensional Cell slice/readout, third-coordinate semantics, preserved relations and update law. Existing source authors, review and protected worldview remain unchanged.
