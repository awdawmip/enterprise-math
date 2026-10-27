# Stage206: full-real exact optimum segment in the external ternary-IID N14 model

**Classification:** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. The following is a finite external statistical theorem. There is no asserted transfer to P000 native X6 Cell dynamics, nor a native Source CLAIM, Result, or independent Driver admission.

## Question and precise result

Let observations be IID under P=(3,1,20)/24 or Q=(2,2,20)/24. A sequential policy may depend on the entire ordered observation history, randomize using arbitrary real probabilities, stop no later than N=14, and announce P or Q. Let eP=P(announce Q), eQ=Q(announce P), tP=E_P(tau), and tQ=E_Q(tau). Define

\[
V_{14}(\alpha)=\inf_{\pi:e_P,e_Q\leq\alpha}\max(t_P,t_Q).
\]

Stage205's existing right endpoint is

\[
\alpha_{205}=\frac{1237831920550008115}{3505953353861431296},\qquad
V_{205}=\frac{2222034154437932573}{219122084616339456}.
\]

For K=25155568056/213144883, H=1091477712445072832515830191/11676187772066443309350912 and Delta=666077759375/855945643032576, the **Stage206 theorem** is

\[
\boxed{V_{14}(\alpha_{205}+\delta)=V_{205}-\frac{50311136112}{213144883}\delta
\quad \text{for every real }0\leq\delta\leq\Delta.}
\]

The exact right endpoint is

\[
\boxed{\alpha_{206}=\frac{413520058350802705}{1168651117953810432},\qquad
V_{206}=\frac{2181785245548332573}{219122084616339456}.}
\]

This includes irrational delta and arbitrary history-dependent randomized competitors.

## Global optimality lower bound

At an ordered history h of length n, let a count observation category 0, b count category 1, and s=(n,a,b). Every branch has positive probability. The likelihood ratio is Q(h)/P(h)=(2/3)^a 2^b = 2^(a+b)/3^a. Set the exact rational Bellman cost

\[
B(s)=\min\big\{K\,2^{a+b}/3^a,\ K,\ 1+\sum_{j=0}^2P_jB(s+e_j)\big\}
\]

for n<14, omitting continuation when n=14. The three actions respectively declare P, declare Q, or continue. All possible ordered histories with the same s have identical conditional future laws and likelihood ratio; by induction on remaining depth, this Bellman value bounds the Lagrangian of **every** history-dependent randomized policy. In particular,

\[
t_P+K(e_P+e_Q)\geq B(0,0,0)=H.
\]
For eP,eQ<=alpha this implies V14(alpha)>=H-2K alpha.

The exact Fraction backward enumeration covers 680 count states, with precisely 1238 strictly positive action gaps (smallest 69107093/34529471046). The only ties are W=(5,0,1): declare Q / continue, and Z=(14,0,0): declare P / declare Q.

## Attainment at every real alpha in the segment

At W declare Q with real probability u in [0,1], otherwise continue; at Z declare P with real probability z in [0,1], otherwise declare Q. Follow each other state's unique minimizing action. Let the four-observation vector be O(u,z)=(eP,eQ,tP,tQ). A path reaching W has b=1, whereas Z has b=0 and is terminal. Since observation counts cannot decrease, neither tie state can precede the other along a stopped path. Thus the mixed u*z coefficient is identically zero.

Exact conditional suffix dynamic programming, separately checked against a full unmerged ordered-history DFS carrying **independent positive integer P/Q branch masses**, gives

\[
O(u,z)=O_0+uD_W+zD_Z
\]
with
\[
O_0=\left(
\frac{636707406567150899}{1752976676930715648},
\frac{36689728636649}{106993205379072},
\frac{2222034154437932573}{219122084616339456},
\frac{258766634953735}{26748301344768}\right),
\]
\[
D_W=\left(
\frac{887702853125}{142657607172096},
-\frac{15601803125}{3343537668096},
-\frac{3275464590625}{17832200896512},
-\frac{250737078125}{835884417024}\right),
\quad
D_Z=\left(-\frac{6103515625}{78364164096},\frac{6103515625}{78364164096},0,0\right).
\]

The exact balance eP=eQ is

\[
\boxed{z(u)=\frac{106748677752881049}{819200000000000000}
+\frac{894746757}{12800000000}u.}
\]
For all real u in [0,1], 0<z(0)<z(1)<1, hence the policy is valid. Its common error is alpha(u)=alpha205+Delta*u with Delta>0. Meanwhile, the affine tP-tQ is positive at both endpoints:

\[
(t_P-t_Q)(0)=3785847440627239/8115632763568128>0,\qquad
(t_P-t_Q)(1)=127698192615335453/219122084616339456>0.
\]

Consequently max(tP,tQ)=tP throughout. As every selected action is a Bellman minimizer, tP+2K alpha(u)=H. The policy attains the universal lower bound, and the affine alpha map ranges over every real number in the claimed interval. Its u=0 observations agree exactly with Stage205's endpoint.

## Strictness of the old fixed support beyond the endpoint

An additional exact first-switch scan gives

\[
K_{207}=\frac{1262124458472}{11368289293}<K,\qquad
H_{207}=\frac{6891276038721445301535256357}{77845101512617870328070144}.
\]
The first new tie is (4,0,1) continue / Q; terminal Z remains. All remaining 1238 alternative gaps are strictly positive. The exact contact identity is

\[
H_{207}=H+2\alpha_{206}(K_{207}-K).
\]

Thus for every alpha>alpha206,

\[
V_{14}(\alpha)\ge H_{207}-2K_{207}\alpha
=H-2K\alpha+2(K-K_{207})(\alpha-\alpha_{206})
>H-2K\alpha.
\]

This proves strict separation from **Stage206's fixed supporting line**, not the unproved Stage207 primal formula.

## Evidence, reusable method and limit

The author verifier and standalone reference use Python standard-library Fraction arithmetic, finite Bellman enumeration, rational suffix recursion and unmerged ordered-history integer-mass DFS; all four deterministic corners agree exactly, and 313384 DFS nodes were visited across them. The attached rational certificate and reproduction program contain checkable inputs/outputs. A separate first-switch dual scanner yields Stage207 candidate and exact contact. BRC is used as an exact positive-weight branch carrier with ordered-path provenance/multiplicity and distinct P/Q measures; count-state compression is valid here by proved finite IID conditional sufficiency for (eP,eQ,tP,tQ). No general state-compression theorem for X6 is inferred.

Scientific input pins: GLOBAL_KNOWLEDGE_V1 main a935c2321a618259b517ed476e73b3b0d81fca60; Enterprise Math main 9b67d426c1eaed49ed517342e0b4a226ca572b6d; global P000 startup/original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; project P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. This external finite probability theorem supplies no X6 Cell update, layer embedding, native readout, third component, or future-operation bridge.

Native task inventory read returned CONTROL_QUOTA, and the service capabilities advertised research_authority_granted=false. Author-side GitHub publication and mathematical correctness are distinct from native Source task ownership, Result freezing, and independent Driver acceptance.
