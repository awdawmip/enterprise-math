# Stage211 — exact full-real optimum segment, external ternary IID N=14

**Classification:** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED (2026-10-28). This is mathematics of an external finite IID observer/readout class; no native P000 X6 Cell-dynamics or time-transfer theorem is claimed.

## Model and exact theorem

Under IID P=(3,1,20)/24 or Q=(2,2,20)/24, observe arbitrary ordered ternary words, stop by N=14, and declare P/Q with any real history-dependent randomization. Set e_P=P(declare Q), e_Q=Q(declare P), t_P=E_P(tau), t_Q=E_Q(tau); define V14(alpha)=inf over e_P,e_Q<=alpha of max(t_P,t_Q). The Stage210 right endpoint is alpha210=3731104217706856345/10517860061584293888 and V210=2138235535809836573/219122084616339456.

Let K211=1498483258683336/14189362560781, H211=65824604050284870080783351450117/777300675923843347325632118784 and Delta211=354734064019525/438244169232678912.

**Theorem:** for every real delta in [0,Delta211], including irrational delta,

V14(alpha210+delta)=V210-(2996966517366672/14189362560781)*delta.

New exact right endpoint:
alpha211=3739617835243324945/10517860061584293888;
V211=2100773454342753173/219122084616339456.

## Global lower bound including history-sensitive randomized competitors

For an ordered history h let s=(n,a,b), n=length(h), a=#0, b=#1. Strictly positive P,Q history masses have ratio rho(s)=Q(h)/P(h)=2^(a+b)/3^a. For K=K211, Bellman cost for t_P+K(e_P+e_Q) is

B(s)=min { K*rho(s) [declare P], K [declare Q], 1+sum_j P_j B(child(s,j)) [continue] },

omitting continue at n=14. IID future suffixes and rho depend only on s, so backward induction proves the lower bound for *every* full ordered-history policy; arbitrary real randomization preserves linearity. B(root)=H211, hence

V14(alpha) >= H211-2*K211*alpha.

An exact Fraction scan of 680 finite count states found 1238 positive action gaps (minimum 632064308823793/27584120818158264), with only ties W=(3,0,1) Q/continue and Z=(14,0,0) terminal P/Q.

## Exact full-real witness and error balancing

At W declare Q with real probability u in [0,1], else continue. At Z declare P with real probability z in [0,1], else Q. Elsewhere apply the unique minimizing Bellman action. Write O(u,z)=(e_P,e_Q,t_P,t_Q).

The exact coefficients are:

O0=(657926421538542899/1752976676930715648,107258603093947/320979616137216,2138235535809836573/219122084616339456,242516696633735/26748301344768),

D_W=(138627698175325/24346898290704384,-217996879775/53496602689536,-520306687042825/3043362286338048,-1212464178025/4458050224128),

D_Z=(-6103515625/78364164096,6103515625/78364164096,0,0).

Then O(u,z)=O0+u*D_W+z*D_Z+u*z*M, with M=(0,0,0,0). This exact interaction vanishes because W has already observed one symbol 1, whereas Z has zero symbol-1 count; monotone counts forbid W->Z, and terminal Z forbids Z->W.

Solving e_P=e_Q gives the exact balance

z(u)=216454311524401049/819200000000000000 + (256867740376359/4096000000000000)*u.

For all real u in [0,1], 0<z(0)<z(1)=267827859599672849/819200000000000000<1. Common errors increase affinely from alpha210 to alpha211. The endpoint gaps t_P-t_Q are respectively 151538756986279453/219122084616339456 and 173671714797480853/219122084616339456, both strictly positive. Thus the full affine family satisfies t_P>t_Q and max(t_P,t_Q)=t_P. Every selected action is a Bellman minimizer and t_P+K211(e_P+e_Q)=H211. The witness achieves the universal lower bound at each alpha in the continuous interval, proving the theorem even at irrational alpha.

Four deterministic coins (u,z)=(0,0),(0,1),(1,0),(1,1) were checked by rational suffix DP and a separate complete ordered-history integer-mass DFS, with respectively 50578,50578,45331,45331 visits, total 191818. Independent arithmetic audit of the rational certificate confirmed all affine coefficients, endpoints, coin legality, time dominance and support.

## Fixed-support strict-right separation; Stage212 dual-only candidate

The next first-switch exact scan gives K212=626616/6055 and H212=86217082286260423009/1036550173712449536. At this dual-only support the new tie is (10,3,1) P/continue, plus Z terminal P/Q. Exactly 680 Bellman states, 1238 positive gaps, minimum gap 632064308823793/15996144656056320, and exact contact

H212=H211+2*alpha211*(K212-K211), K212<K211.

Therefore, for every alpha>alpha211,

V14(alpha) >= H212-2*K212*alpha
 = H211-2*K211*alpha + (364069041882504768/85916590305528955)*(alpha-alpha211)
 > H211-2*K211*alpha.

This is strict separation from the *fixed Stage211 supporting line*, not a Stage212 primal theorem.

## Actual evidence, source pins, open obligation

Exact local execution: verify_stage211.py -> STAGE211_AUTHOR_EXACT_FULL_REAL_PASS 191818; audit_stage211.py -> STAGE211_CERTIFICATE_ALGEBRA_CROSSCHECK_PASS; scan_stage212.py -> STAGE212_DUAL_SCAN_PASS. The original scripts, four-corner full certificate, logs and hashes accompany the local research archive; a GitHub standalone reference is separate repository storage evidence.

Frozen scientific control sources: GLOBAL_KNOWLEDGE_V1 main c0ea478510dfb557f1bc70b551b4e3354d3c3e82; Enterprise Math main cf4614c32069e56df21e01ef7836668c173dc5a1; original P000 Git Blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Stage210 author commit 0b13b00328cae303823ffccd68e0fab295ad88da; activity checkpoint commit aa38fc8ff4dc0dff5ef04cdaccd6e2be1a528382. Native owner lookup reported CONTROL_QUOTA, so this is author proof, not a Source CLAIM/Result or independent Driver mathematical admission. Native X6 joint relation and time correspondence remain additional mathematical obligations.

**Next unit:** At Stage212 ties (10,3,1) P/continue and terminal (14,0,0) P/Q, compute all four exact randomized policy corners and mixed coefficient, prove an all-real primal segment and maximality or an exact rational obstruction.
