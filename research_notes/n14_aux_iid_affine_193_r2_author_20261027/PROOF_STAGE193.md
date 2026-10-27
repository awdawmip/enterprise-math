# Stage193 — exact real-interval stopping theorem (external ternary IID N14)

**2026-10-27 | AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED / PORTABLE_RESEARCH.** The native Heartbeat-X6 P000 ontology is unchanged. This is a finite external IID theorem, not a native Cell-dynamics correspondence, a physical claim or an independent Driver acceptance.

## Fixed input, provenance and theorem

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) and N=14. At each *ordered* prefix a randomized policy may stop and decide P/Q or continue (until N). Put eP=P(decide Q), eQ=Q(decide P), tP=E_P(T), tQ=E_Q(T), and V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ).

The author-level Stage192 verified endpoint is
alpha192=28155690184160278191317/80134219991312171532288,
V192=3399590889696427104405007/320536879965248686129152,
at the committed Stage192 research branch `7c956202de893f774340d61aeb96e34d0ee693b1`. The original Stage192 portable archive's SHA256 is `060f27647edcb0b61fffa9f8465d138ad62cb4f4a3f8a27bbbb347d9d1bbba2a`.

**Stage193 theorem:** for *every real* 0<=delta<=1062862066822451687/11447745713044595933184 (irrationals included),

V14(alpha192+delta) = V192 - (1355097158714110223891/4251448267289806748)*delta.

The exact endpoint is
alpha193=14081565109314017676563/40067109995656085766144,
V193=1695052604792714166418885/160268439982624343064576.
For alpha>alpha193 the *fixed Stage193 supporting line* lies strictly below V14(alpha).

## Universal Bellman certificate

The prefix likelihood ratio is ell(s)=Q(history)/P(history)=2^(a+b)/3^a at s=(n,a,b). Take
K=4745649819640336341093/29760137871028647236,
L=1185007572839608806536/7440034467757161809,
H=693979907486893979185323145246599977/5660680077056829506916627102302208.

Backward induction computes h(s)=min{K*ell(s),L,1+sum_i P_i*h(s+e_i)}, omitting continue at n=14. Exact rational evaluation of all 680 count states yields h(root)=H, exactly 1238 strictly positive nonminimal action gaps, minimum 76124522896713535114855/1851318656680950087257088, with exactly two ties: X=(8,0,1), Q/continue; W=(2,2,0), P/continue. Every ordered history has the count-state likelihood ratio and IID continuation law, so Bellman conditioning applies to all *full-history* randomized policies:

tP+K*eQ+L*eP >= H, hence V14(alpha)>=H-(K+L)*alpha.

Both K,L>0 and K+L=1355097158714110223891/4251448267289806748.

## Exact four-corner policy and full-real attainment

Choose Q with probability x at X, P with probability w at W, and use the unique Bellman-optimal action elsewhere. W cannot be an ancestor of X: W is depth 2 with a=2 whereas X has a=0 at depth 8. X cannot precede W by depth. Therefore all mixed randomization ancestry terms vanish; for O=(eP,eQ,tP,tQ),

O(x,w)=B+x*DX+w*DW, with mixed C=(0,0,0,0),

B=(610893050167412789/1752976676930715648, 113519136464879/320979616137216, 2343430294802530475/219122084616339456, 281967952895935/26748301344768),
DX=(84427421875/17832200896512, -58984375/15479341056, -326450234375/2229025112064, -26297890625/104485552128),
DW=(-97719987438661/584325558976905216, 96989077703/320979616137216, -524627314494505/24346898290704384, -325303135153/26748301344768).

The four deterministic corners (x,w)=(0,0),(0,1),(1,0),(1,1) agree exactly between independent Fraction suffix DP and unmerged ordered-history integer DFS (P numerators 3,1,20; Q numerators 2,2,20; denominator 24^14). DFS nodes 151906+139822+151138+139054=581920; each corner hits 8 ordered X prefixes, one W prefix and zero ancestor intersections. This is a *finite declared-observer* certificate, not a generic state/history compression theorem.

Solving eP=eQ gives the legal balancing law over all real w in [0,1]:

x(w)=27218381338339169/44937930240000000
      +(352649848004843/6419704320000000)*w.

At w=0 this matches the Stage192 terminal X coin. At w=1, x=2968693027437307/4493793024000000<1. The exact observables are

eP(w)=eQ(w)=alpha192+(1062862066822451687/11447745713044595933184)*w;
tP(w)=V192-(1355097158714110223891/45790982852178383732736)*w;
tP(w)-tQ(w)=208520687325852708669053/961610639895746058387456
 -(495307149918056834761/137372948556535151198208)*w.

The last line stays strictly positive, including the right-end value 102526768638213155412863/480805319947873029193728. The error increases strictly. Every selected action is a Bellman minimizer, and tP+K eQ+L eP=H. The ratio of the negative P-time slope to the error slope equals K+L. Given any real delta in the theorem's interval, choose w=delta/Delta193 and x=x(w); the feasible full-history policy attains the universal lower bound.

For strict support-line sharpness, every equality policy must use Bellman-minimizing actions at every reached prefix because positive gaps have full-support P,Q mass. Distinct ordered histories within a tied count state admit a single effective P-mass-weighted coin: their Q/P ratio and IID continuation responses coincide, and the two tie cones are disjoint. Thus every equality policy has observables O(x,w) for effective coins in [0,1]. With K,L>0, equality against H-(K+L)alpha forces both errors exactly alpha; the balancing law requires alpha<=alpha193. For alpha>alpha193 no equality policy exists. The finite randomized stopping-policy space is compact, constraints/objective continuous, and the minimum attained; separation is strictly positive.

## Sources, validation and next question

Scientific control reads: GLOBAL_KNOWLEDGE_V1 `main@90b04585448a8466a336c0edca93a67a3e831156`, with original P000 blob SHA matched to global projection; Enterprise Math `main@872dd27b755e8b33c8f7351a1f048188f210a42a`, including P000 V5, ACTIVE worldview, native-X6 typed-time, joint-observer preservation and portable research rules. The exact executed local code `VERIFY_STAGE193_EXECUTED.py` and complete certificate, raw execution log, Stage194 dual scan/code/log and SHA256 manifest are in `EM_STAGE193_AUTHOR_EXACT_PORTABLE_20261027.tar.xz` (SHA256 `912aa71b7da3ba95f33e206ec435753e2445421710f84f549ed570d53e4b159e`). A separate repository reference reproduction program accompanies this proof and must not be mistaken for remote execution.

Native control returned `research_authority_granted=false`, and the exact task listing was blocked by `CONTROL_QUOTA`. No current owner, CLAIM, official Result, independent review or mathematical admission was established. The GitHub author branch is preservation, not Source acceptance.

Stage194 **DUAL_ONLY** scan: K194=L194=33428504/210911, H194=2114050937763575719833221/17330721745693789126656; ties X=(8,0,1) Q/C and Z=(14,0,0) terminal P/Q; 680 states, 1238 positive gaps, min 5619528281901114949/541585054552930910208. Next compute full ordered four-corner X/Z policies, check possible ancestry and *nonzero* mixed coefficient, exact balance, primal interval or rational obstruction. Do not call Stage194 a proved primal segment.
