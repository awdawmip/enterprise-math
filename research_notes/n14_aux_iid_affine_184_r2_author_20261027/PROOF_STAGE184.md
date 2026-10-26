# Stage184 — complete real affine interval, external N14 ternary IID

Status: AUTHOR EXACT / LOCAL COMPUTATION VERIFIED / NOT NATIVE RESULT OR MATHEMATICAL ADMISSION.
Frozen global knowledge: awdawmip/chatgpt-global-knowledge main@28f64a904bd2a8c659ab65dc4eccb0de5b49edff.
Frozen EM input: awdawmip/enterprise-math main@ad62145d6843aa8ac9c57629878b72e904aa0e5b.
Predecessor Stage183 author artifact: 8a985dc98c9762403b37ca51a38ccfabaded4187. Its dual184.json and task packet supplied the unproved input. This result does not alter P000, its ACTIVE six-axis Cell space, or the protected worldview.

## Model and theorem

Under P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), observe at most N=14 IID symbols from {0,1,2}. A policy may use the complete ordered history, arbitrary randomization, stopping time tau<=14, and a terminal choice P or Q. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P[tau], tQ=E_Q[tau], V14(alpha)=inf max(tP,tQ) with eP,eQ<=alpha.

Stage183 endpoint:
alpha183 = 6293786652175669191787/17990936586642819907584;
V183 = 50134108209086100977021/4497734146660704976896.

Exact dual:
K184 = 321331011187179/1679273916694;
L184 = 480139895871848/2518910875041;
M184 = K184+L184 = 1924272825305233/5037821750082;
H184 = 1816035087448322622333240298837/12544295497767083269983043584.

**Theorem (author proof): for every REAL delta in [0,D184]**, where
D184 = 2623865494834375/5205710817894334464,

V14(alpha183+delta) = V183 - M184*delta.

The new right endpoint:
alpha184 = 6302854731325816791787/17990936586642819907584;
V184 = 49268185437698746127021/4497734146660704976896.

The *fixed Stage184 Bellman support line* H184-M184*alpha is strictly below V14(alpha) for alpha>alpha184; this does not assert global continuation of that line or discontinuity of V14.

## Lower bound for arbitrary full-history strategies

For z=(n,a,b), n is prefix length and a,b counts of symbols 0,1. Every ordered prefix with the same counts has the exact Q/P likelihood ratio ell(z)=2^(a+b)/3^a (the third symbol has ratio 1).

In P-normalized units Bellman recursion is
B(z) = min{K184*ell(z), L184, 1 + sum_i P_i B(child_i(z))},
with the continuation candidate absent at n=14. Decision P costs K184 times Q-error probability, decision Q costs L184 times P-error probability. Backward induction holds pointwise at **each ordered history**, including randomized and history-dependent choices. It yields

tP + K184*eQ + L184*eP >= B((0,0,0)) = H184,

so every alpha-feasible policy has
max(tP,tQ) >= tP >= H184-(K184+L184)*alpha.

The exact fractions recursion exhausts 680 count states (sum_{n=0}^{14}(n+1)(n+2)/2), ties only
S=(9,0,1) Q/continue and T=(6,2,0) P/continue.
All other 1238 competing action gaps are strictly positive; the minimum is
7747768995607/181361583002952.
Count states are sufficient for THIS finite IID Bellman observer only, not a quotient of general ordered BRC paths or native X6 dynamics.

## Attaining policies for the entire interval of reals

At S choose Q with probability s, else continue; at T choose P with probability t, else continue; follow the unique strict minimizing action at all other count states. T at n=6,a=2 cannot precede S at n=9,a=0 (a cannot decrease), and S cannot precede T in time. Thus no history visits both ties and (eP,eQ,tP,tQ) has exactly affine form base+s*dS+t*dT with zero cross term.

Four deterministic corners (s,t in {0,1}) were calculated by TWO distinct algorithms: (1) rational memoized suffix dynamic programming, and (2) full unmerged ordered-history integer-weight DFS. The DFS uses exact per-symbol numerator weights P:(3,1,20) / 24 and Q:(1,1,10) / 12, preserving positive branch identity. DP and DFS agreed exactly for all four 4-tuples. DFS node counts were 215152,207682,214720,207250 (total 845804). First-hit paths/masses:
S: 9 ordered paths; P=390625/4478976, Q=390625/2239488.
T: 15 ordered paths; P=3125/27648, Q=3125/62208.

Exact error balancing eP=eQ gives

s(t) = 21925676597479349/37833811200000000
     + (12352512653/31528176000)*t.

Both probabilities lie in [0,1] for EVERY REAL t in [0,1]. The left end t=0 matches precisely alpha183,V183 and Stage183 S coin; at t=1 the outputs are precisely alpha184,V184. Common alpha grows strictly, tP decreases strictly. Therefore its affine image covers every real alpha in the stated interval, including irrational alpha.

The endpoint tP-tQ differences are positive:
t=0: 166070625793116812795/562216768332588122112,
t=1: 149857900062857106545/562216768332588122112.
The interpolation remains positive. Every selected action is Bellman-minimizing, so tP+K184*eQ+L184*eP=H184; balanced errors then attain the dual lower bound with max(tP,tQ)=tP. This proves equality on the full interval, not merely a grid.

## Support line sharpness

A finite horizon randomized decision policy can be parametrized by finitely many action simplexes. Its feasible strategy set is compact and observables are continuous; the minimum exists. Suppose equality with the Stage184 support line held for some alpha>alpha184. The positivity K184,L184 forces both errors to equal alpha, tP>=tQ, and only Bellman-minimizing actions along all reached histories. The 1238 positive gaps fix all other actions. In each of S and T, history-dependent coins can be replaced by effective aggregated coins in [0,1], because the likelihood ratio and strict suffix observer are fixed at the same count state. The ties have disjoint first-hit cones, so the effective observer is exactly the two-coin affine formula above. Balance then bounds alpha<=alpha184, contradiction. Hence strict support-line separation to the right.

## Evidence, limitations, next frontier

The complete locally executed source and logs are in the portable author research bundle EM_STAGE184_AUTHOR_EXACT_PORTABLE_20261027.zip (also available as a local conversation artifact), including VERIFY_STAGE184.py, certificate184.json, verify184.log, SCAN_STAGE185.py, dual185.json, scan185.log and exact SHA256 manifest. All 12 exact checks passed; raw verifier ended STAGE184_AUTHOR_EXACT_FULL_REAL_PASS. The dual Stage185 scan ended STAGE185_DUAL_SCAN_PASS. Neither artifact is an independent proof review, formal Lean checker result, native Source Result or Foundation admission.

BRC: REUSE_APPLIED to positive rational labeled branch weights, exact path multiplicity, independent P/Q masses and exact observer projection. Positive mass is not signed amplitude. This external auxiliary model does not exercise Heartbeat/BRC-Shor-specific native arithmetic and supplies no X6 transfer theorem. Native task lookup returned CONTROL_QUOTA; session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The active formal owner is UNKNOWN and no new CLAiM/Source Result/Driver review was obtained.

Stage185 dual-only new candidate: K185=L185=11700648/62533, H185=60828835377977479173913/428198791166048600064, ties S=(9,0,1) Q/C and Z=(14,0,0) P/Q, 1238 strictly positive other action gaps (minimum 3713241817841/107552181583872). Its primal optimality and next real interval remain to be proved; see NEXT_TASK_PACKET_185.md.
