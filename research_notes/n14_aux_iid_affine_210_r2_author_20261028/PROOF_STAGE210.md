# Stage210: exact full-real optimum for an external ternary IID stopping model

**Classification:** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED (2026-10-28). The model is an external finite IID auxiliary problem. No P000 native-X6 transfer, physical-time identification, formal Source Result, independent Driver review or project theorem admission is asserted.

## Quantified theorem

Every complete ordered ternary history of length at most N=14 is available to a real-randomized stopping/decision policy. Observations are IID under P=(3,1,20)/24 or Q=(2,2,20)/24. Write eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf over policies with eP,eQ<=alpha of max(tP,tQ).

The verified Stage209 author endpoint is alpha209=3730982047415656345/10517860061584293888 and V209=2138785208600876573/219122084616339456. Put
- K210=258616/2395; H210=6798931418530161042091/78719608898419949568;
- Delta210=61371875/5283615080448.

**Theorem:** For *every real* delta in [0,Delta210], including irrational parameters,
V14(alpha209+delta)=V209-(517232/2395)*delta.
The right endpoint is exactly alpha210=3731104217706856345/10517860061584293888 and V210=2138235535809836573/219122084616339456.

## Universal Bellman lower bound on unrestricted ordered-history policies

For a word h define state s=(n,a,b), where n is the length and a,b the numbers of symbols 0,1. Every word has strictly positive mass in both models, and Q(h)/P(h)=rho(s)=2^(a+b)/3^a. For any K>0 minimize conditional tP+K(eP+eQ) by the backward recursion

B(s)=min { K*rho(s) [declare P], K [declare Q], 1+sum(j=0..2) P_j*B(child(s,j)) [continue] },

where continue is omitted at n=14. Because both future IID laws and rho depend only on the count state, backward induction applies even to competing policies that choose different actions on two ordered words with the same counts. Randomization cannot improve below the minimum. Summing over ordered histories with their *positive P masses* establishes for every real-randomized full-history policy

tP+K(eP+eQ) >= B(0,0,0), hence V14(alpha)>=B(0,0,0)-2*K*alpha.

Exact Fraction enumeration for K210 covers C(17,3)=680 count states and yields root B(0,0,0)=H210, 1238 strictly positive alternative action gaps (minimum 1540319/125708760), no negative gap, and exactly two ties:
T=(8,2,2) has Q/continue; Z=(14,0,0) has P/Q.
All other chosen actions minimize uniquely.

## Complete ordered-history construction and four exact corners

At T choose Q with real probability u in [0,1], otherwise continue. At Z choose P with real probability z in [0,1], otherwise Q. Elsewhere choose the unique Bellman minimizer. Write O(u,z)=(eP,eQ,tP,tQ). Exact corner computations yield

O0 = (657781228481262899/1752976676930715648, 107277732053947/320979616137216, 2138785208600876573/219122084616339456, 242619849353735/26748301344768);
DT = (218811875/2641807540224, -25625/429981696, -828379375/330225942528, -268626875/69657034752);
DZ = (-6103515625/78364164096, 6103515625/78364164096, 0, 0).

The full corner expansion is O(u,z)=O0+u*DT+z*DZ+u*z*M, with M=(0,0,0,0). The zero mixed coefficient also has a structural proof: once T has seen two 0s and two 1s, it can never reach Z (where both counts are zero); Z is terminal and cannot be an ancestor of T.

Exact error balancing gives

z(u)=215705323471921049/819200000000000000 + (146286729/160000000000)*u.

Both z(0) and z(1)=216454311524401049/819200000000000000 lie strictly between zero and one, so every real u in [0,1] specifies a legitimate policy. eP=eQ varies *affinely and strictly increasingly* from alpha209 to alpha210. The corresponding tP-tQ gaps at u=0 and u=1 are respectively
151243402695079453/219122084616339456 and 151538756986279453/219122084616339456.
Both are positive, so tP>tQ for every interpolating real u. Every policy action is Bellman-optimal at K210, and the affine identity tP+K210*(eP+eQ)=H210 holds throughout. Thus the witness attains the universal bound and max(tP,tQ)=tP. Because u maps bijectively and affinely to alpha, the asserted interval is proved for all real deltas, without a grid or limit approximation.

The exact endpoint differences are alpha210-alpha209=61371875/5283615080448 and V210-V209=-828379375/330225942528 = -(517232/2395)*(alpha210-alpha209).

## Strict separation right of this fixed support

The exact first downward switch from K210 is a new *dual-only* candidate:
K211=1498483258683336/14189362560781,
H211=65824604050284870080783351450117/777300675923843347325632118784,
with new Q/continue tie (3,0,1), terminal P/Q tie Z, 680 count states, 1238 positive gaps and minimum positive gap 632064308823793/27584120818158264. Exact support contact is

H211=H210+2*alpha210*(K211-K210), K211<K210.

Therefore, for every alpha>alpha210,

V14(alpha)>=H211-2*K211*alpha
=H210-2*K210*alpha + [161457566944698752/33983523333070495]*(alpha-alpha210)
>H210-2*K210*alpha.

This compares the *fixed Stage210 supporting line*; it does not prove a Stage211 primal segment.

## Evidence and scope

The author's executed verify_stage210.py used exact Fraction suffix DP and a distinct unmerged integer P/Q-mass ordered-history DFS. Both yielded the identical four corner vectors; DFS visits: 56482, 56482, 50578, 50578, total 214120. The independently structured audit_stage210.py recomputed coin algebra and endpoint/contact equalities without Bellman or DFS and returned STAGE210_CERTIFICATE_ALGEBRA_CROSSCHECK_PASS. scan_stage211.py returned STAGE211_DUAL_SCAN_PASS. Reproducer and rational certificate are included alongside this proof; the local execution logs and original author sources are retained in the portable evidence package. GitHub source storage alone is not an execution assertion.

Source pins used in this author run: GLOBAL_KNOWLEDGE_V1 main c0ea478510dfb557f1bc70b551b4e3354d3c3e82; Enterprise Math main cf4614c32069e56df21e01ef7836668c173dc5a1; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488; predecessor immutable author commit b936bc3921cfe0105b3f142cf2061917252aeaef. Native em_control_tasks responded CONTROL_QUOTA, so the active Source owner, formal CLAIM/Result and independent Driver admission remain to be verified through authorized native procedures. This external IID proof does not imply preservation of native X6 relational observables or dynamics.

**Next research obligation:** Four deterministic corners and mixed interaction at Stage211 tie W=(3,0,1) Q/continue and Z=(14,0,0) P/Q, then all-real primal feasibility and next interval or an exact rational obstruction.
