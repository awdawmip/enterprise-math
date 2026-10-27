# Stage189 — full-real exact optimal interval, external N14 ternary IID model

Date: 2026-10-27. Status: author-level exact mathematical proof with rational software certificates; distinct mathematical review and native Result admission remain future actions. This result concerns an external stopping experiment and makes no P000 X6 or native three-dimensional-slice theorem claim.

## Frozen scientific sources

GLOBAL_KNOWLEDGE_V1 was verified as main@1a00e852e385e2421cdb9a1015a75a3aa5e45b25, including 00_BOOTSTRAP.md, OPERATING_MANUAL.md, the ACTIVE worldview, P000 projection and original SHA1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Enterprise Math source-control snapshot was main@1fe0c6cd378fe9e50b10c46858a90593ee47232b; docs/PORTABLE_RESEARCH_PROTOCOL.md governs the research return. Stage188 predecessor source: immutable proof at a45268285ad8312bfbe6f421014329a348350442; original exact evidence ZIP has SHA256 ce0e134532aa0e687d97fc3446f3b48202e4d86fa5fa49a6a8b7404ca793359f.

Let N=14. Independent symbols have laws P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). A randomized stopping/decision policy may use its full ordered history, stops no later than time 14 and selects P or Q. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P[T], tQ=E_Q[T], V14(alpha)=min_{eP,eQ<=alpha}max(tP,tQ).

## Theorem

With

alpha188 = 9370003598922725167379/26711406663770723844096,
V188 = 1153476444134184737662789/106845626655082895376384,

for **every real**

0 <= delta <= 2299888625/11179439172895113216

one has

V14(alpha188+delta) = V188 - (479665061/1388612)*delta.

The new endpoint is

alpha189 = 28110010813253777166137/80134219991312171532288,
V189 = 3460429309624219796220367/320536879965248686129152.

For every real alpha>alpha189, the *fixed Stage189 supporting affine line* is strictly below V14(alpha). The theorem does not assert a global formula for values beyond alpha189.

## Bellman proof, all history policies

At count state s=(n,a,b), the likelihood ratio of any *ordered* history is ell(s)=2^(a+b)/3^a. Put

K=241967493/1388612,
L=59424392/347153,
H=209137371682549614928313/1584768521683668566016.

Backward induction on all 680 possible count states uses h(s)=min{K*ell(s), L, 1+sum_i P_i*h(s+e_i)}, omitting continuation at n=14. Its root h(0,0,0)=H. Only two states tie: X=(8,0,1), Q/C; T=(13,6,4), Q/C. Exactly 1238 alternative-action gaps are positive, with exact minimum 66370340952961/3582466457075712; no negative gaps. At each ordered history every randomized action cost is a convex combination of the Bellman choices, so tP + K*eQ + L*eP >= H even for policies depending on the complete ordered history. Thus V14(alpha)>=H-(K+L)*alpha.

## Four exact corners and structural disjointness

At X use coin x=probability of deciding Q (else continue). At T use coin t=probability of continuing (else decide Q). Every other state follows its unique minimizing action. This T-coin convention matters: at the Stage188 endpoint T's unique action was Q, so Stage189 starts at t=0. For observations O=(eP,eQ,tP,tQ), exact backward suffix DP and an independent integer-weight DFS over the *unmerged* ordered history tree establish

O(x,t)=B+x DX+t DT+xt C,

B=(612777804249889049/1752976676930715648,
37637050405523/106993205379072,
2373868601584350935/219122084616339456,
94671870059855/8916100448256),

DX=(84427421875/17832200896512,
-58984375/15479341056,
-326450234375/2229025112064,
-26297890625/104485552128),

DT=(-6625/2348273369088,
6625/2507653251072,
6625/293534171136,
6625/208971104256),

C=(0,0,0,0).

A strict combinatorial obstruction proves C=0: going from X at depth 8 to T at depth 13 leaves 5 further draws but must increase the count of the first symbol from 0 to 6. This is impossible; reversing the ancestry violates depth ordering. Hence the two tie first-hit cones are disjoint. This also corrects the provisional Stage189 packet's suggestion that count feasibility permits ancestry.

For four deterministic pairs (x,t)=(0,0),(0,1),(1,0),(1,1), the independent DFS visits respectively 186574, 196750, 185806, 195982 nodes: total 765112. Every corner matches the suffix-DP four-vector *exactly*. First hits are 8 ordered X histories and 3392 ordered T histories, with zero ancestor intersections. DFS P and Q path weights are separate nonnegative integers divided by 24^14. The complete four corners and per-corner observations are preserved in the full exact local certificate attached with this research return.

## Balance, all-real primal attainment, sharpness

From eP=eQ, the unique balanced line is

x(t)=1289209864733261/4993103360000000 + (6413/10030788000)*t.

For every real t in [0,1], both coins lie in [0,1]; even x(1)=11602917512839349/44937930240000000 is strictly interior. The balanced observations satisfy

alpha(t)=alpha188+(2299888625/11179439172895113216)*t,
tP(t)=V188-(3177781029125/44717756691580452864)*t,

tP(t)-tQ(t)=960164553826484768591/3957245431669736865792
             +(7800594490625/134153270074741358592)*t.

The common error increases strictly, tP exceeds tQ strictly throughout, and the attained action choices saturate the Bellman lower bound: tP+K*eQ+L*eP=H. Since K+L=479665061/1388612, this proves the exact value for *every real* alpha across the specified interval, including irrational parameters, and proves the stated endpoint.

For strict sharpness, every Bellman-equality policy must use the unique actions except at X and T. Every history reaching either tied count state has the same positive Q/P likelihood ratio and the same suffix statistics. With disjoint tie cones, replacing all history-dependent coins at X by one P-mass-weighted effective x and at T by one effective t preserves eP,eQ,tP,tQ exactly. Therefore every Bellman-equality policy is represented by O(x,t). Equality with the fixed lower supporting line at alpha>alpha189 would require both eP=eQ=alpha and legal effective coins, which forces x=x(t), 0<=t<=1 and alpha=alpha(t)<=alpha189: contradiction. The finite behavioral-strategy space is compact, so the minimizer is attained and separation is strict for all alpha>alpha189.

## Stage190, evidence, and admission scope

Stage190 exact dual-only scan, after forcing T=continue and retaining X Q/C, follows dK=-1080671/869760 and dL=-1. The former T Q alternative opens with rate 2430071/118885320. First new closure is Y=(4,2,0): P/C at step 575402119429806852000/149674079525324584469, yielding

K190=219205722106707916/1293441907677519,
L190=72144743665153672/431147302559173,
H190=27408936515658794949498678792123439/212566265355324633731370212917248.

Fresh 680-state scan has ties Y P/C and X Q/C, 1238 strict positive gaps, minimum 8957179515094375931/362080953867613958784. Stage190 primal interval is an open research unit.

The originally executed local evidence used fractions.Fraction, a suffix DP, and a separate integer-weight history DFS. The local run ended STAGE189_AUTHOR_EXACT_FULL_REAL_PASS; the successor scan ended STAGE190_DUAL_SCAN_PASS. A standalone reference rational checker and exact summary are stored alongside this proof. The full executed code, raw logs, full corner certificate and hashes are in the portable archive EM_STAGE189_AUTHOR_EXACT_PORTABLE_20261027.tar.xz, whose SHA256 is eaa467157119fc07fe4ad849a2535b23dceb906b9ceaf44a78db3c74a37ece1b.

BRC resolution: REUSE_EXECUTED for rational positive-branch masses, ordered-source provenance and IID-specific observer sufficiency. Signed amplitudes and native X6 phase dynamics are outside this theorem. P000 native transfer would require explicit slice embedding, third coordinate semantics, readout and preserved relations/update law.

Identity/owner status observed 2026-10-27: the connected GitHub identity was awdawmip with repository push permission. The native owner inventory returned CONTROL_QUOTA, and native session creation was rejected as STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The author's local activity record is research metadata, not a native CLAIM, independent review or mathematical admission.
