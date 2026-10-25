# Stage 95 — exact affine minimax interval in an N=14 auxiliary iid testing model

**Scientific status:** complete author-side finite-model exact-rational argument; no independent Research Driver, native Task claim/Result, P000 change, or native BRC/X6/Heartbeat transfer.

**Fixed inputs:** GLOBAL_KNOWLEDGE_V1 canonical main@dccc6b5567fb4a8472081a38323f1beb74ce8eeb and Enterprise Math main@aeafef651dc2bfead4753b7eefbb1677bf10f3e1 were verified/read in this phase. The previous Stage94 certificate is the declared inherited frontier (source commit e94f1ef4d98109777f293e7080bc8ac97b3d956c). In the external finite model, observations from alphabet {0,1,2} are iid under P=(1/8,1/24,5/6) or Q=(1/12,1/12,5/6), with stopping time at most 14.

For a randomized ordered-history sequential decision procedure, write e_P=P(decide Q), e_Q=Q(decide P), t_P=E_P(tau), t_Q=E_Q(tau). Define V14(alpha)=min max(t_P,t_Q) over all procedures with e_P,e_Q<=alpha.

## Exact theorem

From the previous author-verified endpoint

\[
\alpha_{94}=\frac{5172467120921621243}{14900301753911083008},
\qquad
V_{94}=\frac{24273746381538068699}{1862537719238885376},
\]

define

\[
\eta_{95}=\frac{360546875}{75786853810176}.
\]

**For every real** \(0\leq\delta\leq\eta_{95}\),

\[
\boxed{V_{14}(\alpha_{94}+\delta)=V_{94}-\frac{217476}{71}\delta}.
\]

The right endpoint is

\[
\boxed{\alpha_{95}=\frac{5172538007321621243}{14900301753911083008}},
\qquad
\boxed{V_{95}=\frac{24246605376738068699}{1862537719238885376}}.
\]

The same affine supporting line is sharp on the right: it cannot attain the minimax optimum at any alpha strictly greater than alpha95.

## Finite exact Bellman dual

A count state is (n,a,b), with n observations seen, a symbol-0 occurrences, b symbol-1 occurrences. The remaining n-a-b observations are symbol 2. The likelihood ratio Q(w)/P(w) equals \(2^{a+b}/3^a\). Fix

\[
K_{95}=\frac{112428}{71},\quad
\lambda_Q=K_{95},\quad
\lambda_P=72+\frac89K_{95}=\frac{105048}{71},\quad
G=\lambda_P+\lambda_Q=\frac{217476}{71}.
\]

At n<14 use the exact recursion

\[
D(n,a,b)=\min\left\{
\lambda_Q\frac{2^{a+b}}{3^a},
\lambda_P,
1+\sum_{i=0}^2P_iD(\operatorname{child}_i(n,a,b))
\right\}.
\]

At n=14 the continuation alternative is absent. Induction in decreasing n shows that D(0,0,0) is the minimum over **all** possibly randomized history-dependent policies of \(t_P+\lambda_P e_P+\lambda_Q e_Q\).

The policy inherited from stage94 freezes A94=(10,5,1) to decide P, keeping previous endpoint actions and continuation at B=(12,0,1). Evaluation across all \(\sum_{n=0}^{14}{n+2\choose2}=680\) states and 1240 nonchosen alternatives finds exactly 1238 strictly positive gaps, no negative gaps and two zero gaps:

\[
A_{95}=(10,1,2):\ C=Q,\qquad B=(12,0,1):\ C=Q.
\]

Minimum positive gap = 44476991291/732688809984. The independently implemented minimization recursion returns the identical root:

\[
\boxed{D(0,0,0)=\frac{16745219816680354771525}{15557668007760101376}
=V_{94}+G\alpha_{94}}.
\]

Thus the inherited selected policy attains the global Bellman minimum at this dual parameter, rather than only on a finite sample of histories.

## Exact first-hit and suffix evidence

An ordered-word DFS, not only a multinomial count, finds:

| state | nominal words | real first-hit words | first-hit P mass | first-hit Q mass | old terminal suffixes |
|---|---:|---:|---|---|---:|
| A95=(10,1,2) | 360 | 260 | 5078125/322486272 | 5078125/120932352 | 15 |
| B=(12,0,1) | 12 | 12 | 48828125/725594112 | 48828125/362797056 | 5 |

At A95, replacing continuation by immediate Q cuts off 260*15=3900 complete ordered terminal histories. The analogous B old suffix tree has 12*5=60 ordered terminal histories.

The conditional suffix quadruples (P-error, Q-error, remaining expected samples under P, remaining expected samples under Q) are

\[
R_A=(4075/4096,\ 31/20736,\ 1955/1536,\ 75/64),
\quad
R_B=(63/64,\ 1/144,\ 9/8,\ 13/12).
\]

A's word cone and B's word cone do not intersect: any history reaching A already has one symbol 0, while B requires zero occurrences of symbol 0. The exact first-hit probabilities are positive.

Let u in [0,1] be the probability of immediately deciding Q at A, with all other frozen decisions unchanged. At B immediately decide Q with probability s, and otherwise continue. The stage94 endpoint has

\[
s_{94}=\frac{27729595280088847}{41779200000000000}.
\]

If pA,qA,pB,qB denote the measured first-hit masses, define

\[
X=p_A(1-R_{A,P\mathrm{err}})=\frac{35546875}{440301256704},\quad
Y=q_A R_{A,Q\mathrm{err}}=\frac{157421875}{2507653251072},
\]

\[
E=p_B(1-R_{B,P\mathrm{err}})=\frac{48828125}{46438023168},\quad
H=q_B R_{B,Q\mathrm{err}}=\frac{48828125}{52242776064}.
\]

The nonoverlapping cones make both errors **exactly affine**:

\[
e_P=\alpha_{94}+Xu+E(s-s_{94}),\qquad
e_Q=\alpha_{94}-Yu-H(s-s_{94}).
\]

Therefore equality e_P=e_Q forces

\[
s=s_{94}+hu,\quad
\boxed{h=-\frac{X+Y}{E+H}=-\frac{117923}{1632000}}.
\]

At u=1 this is

\[
\boxed{s_{95}=\frac{24710766480088847}{41779200000000000}},
\quad 0<s_{95}<s_{94}<1.
\]

Consequently this is a valid randomized policy for every u in [0,1], with

\[
e_P=e_Q=\alpha_{94}+\eta_{95}u,\quad
\eta_{95}=X+Eh=-Y-Hh=\frac{360546875}{75786853810176}>0.
\]

Only Bellman-tied actions are randomized, so the exact identity
\(t_P+\lambda_P e_P+\lambda_Q e_Q=D(0,0,0)\)
holds throughout the family. Hence \(t_P=V_{94}-G\eta_{95}u\).
The endpoint gaps t_P-t_Q are

\[
\frac{775383214032140755}{1241691812825923584}>0,\qquad
\frac{2415929098096422265}{3725075438477770752}>0.
\]

These expectations are affine in u, so t_P>t_Q for the whole interval and max(t_P,t_Q)=t_P. For every feasible competing policy,

\[
\max(t_P,t_Q)\ge t_P\ge D(0,0,0)-G\alpha.
\]

Our family attains equality for alpha=alpha94+eta95*u. This proves the boxed formula for the entire real interval, not merely for eight sampled values.

## Sharp right endpoint and next dual candidate

To attain this same supporting line at alpha>alpha95, both type-error constraints must saturate because lambda_P,lambda_Q are strictly positive. Further, only dual-minimizing Bellman actions may have positive mass. As only A95 and B have zero alternative gaps, all such policies have u,s in [0,1] and equality e_P=e_Q forces s=s94+h*u, hence alpha=alpha94+eta95*u<=alpha95. This contradiction proves right-end sharpness.

Freezing A95 to Q, the next **dual** root is

\[
\boxed{K_{96}=19683/13,\quad A_{96}=(14,7,4):\ Q=P}.
\]

At K96 the sole other zero gap is at B. Its new terminal tie is reached by 11467 genuine ordered histories, with P mass 1433375/150289495621632 and Q mass 1433375/160489808068608. At K96-1/10000, the old Q decision at A96 has alternative gap -13/2733750. **There is no Stage96 primal-interval theorem here.**

## Reproduction, scopes, evidence

Run Python standard-library scripts derive95.py and crosscheck95.py with their inherited unchanged dependency modules derive94.py down through derive88.py. Both were executed on exact Fraction rational arithmetic and passed. derive95 computes Bellman chosen-action values, positive branch-weight forward reachability, exact first hits and suffixes, and the next dual comparison. crosscheck95 separately enumerates ordered paths and computes the min Bellman recursion. They **share the inherited deterministic action table**; neither provides clean independent Driver review or a separate native Result.

The mathematical carrier is a **positive rational weighted branch family**: serial observation multiplies exact probabilities, disjoint histories add them, and ordered provenance is retained. BRC reuse is applied to this typed auxiliary scope only. This finite theorem establishes no signed/phase cancellation, RH, asymptotic claim, six-axis X6 embedding, native three-dimensional slice, or physical Heartbeat correspondence. P000 and ACTIVE worldview are unchanged.

Native control was not granted: control inventory reported CONTROL_QUOTA and session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Live owner, native CLAIM/Result, and independently activated Driver status remain unverified. GitHub author-source persistence is not formal admission.