# Euler routing memory: exact elimination, faster relaxation, and uniform safe truncation

Status: PROVISIONAL MODEL THEOREMS AND BRC OBSERVER CERTIFICATES / NOT FORMALLY ADMITTED.
Date: 2026-10-05. Same-conversation continuation, not independent replication.
Global read snapshot: d9e891b550f3785ed3fb25b4c0db3fa27fb6ced6.
Source read snapshot and prior frontier: 781b24b6e2a8b310cb6ebd101b4a548a3fd6da7e, research_notes/chatgpt_direct/20261005_ROUTING_MEMORY_HOLONOMY.md, blob 34fd6a2e0a96654d82ba8e7c7acef89408973da9.

## Scope and exact reuse

This unit adds no particle, spatial dimension, collision rule or native force. It analyzes the previously declared LOCAL three-channel contact and routing-persistence parameter p. Contact count is not physical heartbeat time. Local channel phase is not the shared-field C12 port observer. The results below do not automatically transfer to the earlier 35-state shared-field dynamics.

The positive update is unchanged: apply P or its inverse according to the retained routing sign, then retain that sign with weight p or reverse it with weight 1-p. Every explicit branch retains its binary triple, next sign, root, choice/history and positive CWM. Source weights remain rational. Signed formulas below are observer identities and error certificates, never positive mass or Cell addresses.

Recovered prior archive SHA256 c77d5d5b76ff653a1bbb21686bd6b0d108e0d26a08f59b52d79b315f48641c89; all 53 prior manifest entries match. Unchanged brc_route_memory.py SHA256 ce182a5861982d0e43120aeb15da06cf02c774300730975330a85ea86f3c979e actually supplies contact/signature_step. Its dependencies execute the existing positive CWM source brc_weighted.py, blob 3f205696709e847909958a153f8fe10d3f6b70f0. Existing alpha coefficient operations are used for the new observer certificates. REUSE_EXECUTED for the path, CWM and phase interfaces; EXTEND_EXISTING_TOOL for a finite-history observer, not a new accepted BRC family.

Current bootstrap/manual/project/P000/worldview and BRC-only definitions have unchanged verified blobs and are reused. Six native spatial axes, separate time, three-dimensional slice typing and positive mass distinctions are unchanged. No pi, classical trigonometry, numerical root, matrix exponential, Taylor/Pade/Cayley or alternative numerical world propagator is executed.

## 1. Eliminating a state variable does not eliminate its causal contribution

Let omega=alpha^4, alpha^4-alpha^2+1=0, and let u_n,v_n be unnormalized channel-phase sums in the two next-sign populations. The already proved source interface is

u_next=p*omega*u+(1-p)*omega^2*v,
v_next=(1-p)*omega*u+p*omega^2*v.

Define z=u+v, d=u-v, kappa=2p-1 and ell=(omega-omega^2)/2. Since ell^2=-3/4, the equivalent observer update is

z_next=-z/2+ell*d,
d_next=kappa*(ell*z-d/2).

Iterating only the second identity and substituting into the first gives, for n>=0,

z_(n+1)=-z_n/2+(-kappa/2)^n*ell*d_0
 -(3*kappa/4)*sum_(j=0)^(n-1) (-kappa/2)^(n-1-j)*z_j.

The empty sum is zero. This is exact, including the initial joint-correlation term. It does not assume a fair initial sign or a product preparation. The proof is finite substitution, not a Markov or independence assumption. The earlier second-order recurrence is consumed, not reclaimed as new.

For p=1/2, kappa=0 and, after the initial contribution, the history kernel disappears. For other p, deleting d while retaining only the old first-order rule generally deletes the displayed memory term. A marginally fair sign does not imply d_0=0 or future absence of correlation.

Primary context only: exact elimination of unresolved variables into memory is established in Mori-Zwanzig reduction; Woodward et al., arXiv:2301.07203, abstract inspected. The concrete scalar kernel and BRC fidelity proof here are the scoped contribution, not a new general reduction theory.

## 2. A rational example where slight persistence improves phase relaxation

Choose p=8/15, hence kappa=1/15. This parameter is a declared model comparison, not a native-derived constant. The existing phase recurrence factors as

z_(n+2)=-(8/15)z_(n+1)-(1/15)z_n,
lambda^2+(8/15)lambda+1/15=(lambda+1/3)(lambda+1/5).

With a fair sign independent of the initial channel state, z_1=-z_0/2. Therefore

z_n=c_n*z_0,
c_n=(9/4)(-1/3)^n-(5/4)(-1/5)^n.

The independent-resampling comparator p=1/2 has c_n^ind=(-1/2)^n. For every integer n>=2,

0<|c_n|<2^(-n).

Proof: the bracket (9/4)3^(-n)-(5/4)5^(-n) is positive. Put R_n=2^n|c_n|. Then R_1=1 and

R_(n+1)-R_n=(3/4)[(2/5)^n-(2/3)^n]<0 for n>=1.

Thus the strict improvement is sample-by-sample for this preparation and this phase, not merely an asymptotic fit. The first factors are 1,-1/2,1/5,-11/150,29/1125. No finite c_n vanishes.

For one initially fixed binary triple with a fair initial sign, actual CWM is

count=2^(n+1), total=1, dominant=(1/2)(8/15)^n.

More concentrated largest-path weight can coexist with a smaller signed phase. It is not faster disappearance of positive mass. Each deterministic contact still cycles the channel triple. The improvement comes from correlations affecting subsequent signed readout alignment.

## 3. Asymptotic optimum within the declared parameter family

For the scalar phase modes the characteristic polynomial is
lambda^2+p*lambda+2p-1. Its discriminant is D=p^2-8p+4.
On the real-parameter formal extension, the worst modal radius is

r(p)=(p+sqrt(D))/2 for 0<=p<=p_c,
r(p)=sqrt(2p-1) for p_c<=p<=1,

where p_c=4-2sqrt(3). The first branch decreases: its derivative is
[1+(p-4)/sqrt(D)]/2<0 in the open interval. The second increases.
Consequently the unique minimum is

r_min=2-sqrt(3), p_c=2*r_min.

At the repeated root a polynomial prefactor in n may occur; this is an asymptotic modal optimum, not a guarantee of smallest error at every finite contact or smallest runtime. For the fair initial phase the critical formal sequence is
[1+(sqrt(3)/2)n]*[-(2-sqrt(3))]^n.

Only rational transition weights were executed. The irrational p_c is a formal boundary and the unattained infimum over rational p; it is not an implemented algebraic-weight CWM extension or a preferred physical value. Exact phase-ring auditing used sqrt(3)=2alpha-alpha^3, whose square is three, without numerical roots. A further executed rational point p=15/28 has roots -2/7,-1/4 and fair factor 7(-2/7)^n-6(-1/4)^n. Rational parameters can approach the boundary continuously.

General memory/lifted-chain improvements have prior literature: Apers, Sarlette and Ticozzi, Characterizing limits and opportunities in speeding up Markov chain mixing, Stochastic Processes and their Applications 136 (2021), 145-191, DOI10.1016/j.spa.2021.03.006. Its abstract was inspected for attribution; no literature-wide novelty, global mixing optimum or algorithmic speedup is asserted.

## 4. A sharp one-time memory-reset response

Compare a true joint preparation to a DIFFERENT preparation with the same channel marginal and an independent fair sign, then evolve BOTH with the same p=8/15 rule. Let d_0 be the true sign-conditioned phase difference and D_0=ell*d_0. Both current phases agree; their first next-phase difference is exactly D_0.

For every n>=0, their phase difference is

e_n=(15/2)[(-1/5)^n-(-1/3)^n]*D_0.

The scalar gain is zero at n=0, one at n=1, and its absolute value decreases for n>=1. Indeed (1/3)^n-(1/5)^n is positive and strictly decreasing there. Hence

sup_(n>=0) ||e_n||_infinity=||D_0||_infinity.

This is a uniform all-future coefficient bound, exact at the next sample. Ignoring this initial correlation is safe for the specified phase tolerance delta iff ||D_0||<=delta, under the unchanged update and observer. D_0=z_1+z_0/2 can be read from two exact phase observations of the true preparation.

This is a one-time comparison, NOT permission to reset the sign before every contact or to discard positive path/source data. A phase-equivalent correlation can remain distinguishable to another observation or control.

## 5. Finite history with a genuinely uniform recursive error bound

At p=8/15 the exact memory equation becomes

z_(n+1)=-z_n/2+(-1/30)^n*D_0
 -(1/20)*sum_(l=0)^(n-1) (-1/30)^l*z_(n-1-l).

Retain only the most recent m terms in this history sum and use the APPROXIMATE past outputs recursively. Keep the initial term (-1/30)^n D_0 exactly. Initialize the approximate z_0 to the exact one.

For any normalized positive population of binary channel triples, every coefficient of its exact phase has absolute value <=1: the four coefficients are (a-b,0,b-f,0) per branch. Therefore the discarded tail at one step is at most

delta_m=(3/58)*30^(-m).

The absolute total feedback weight retained by the recursive approximation is

a_m=1/2+(3/58)(1-30^(-m))<1.

If all earlier coefficient errors are <=B, the next is <=a_m B+delta_m. Starting with zero error, induction proves

sup_(n>=0) ||z_n-approx_z_n||_infinity
 <=delta_m/(1-a_m)=3/(26*30^m+3).

This argument includes accumulated recursion error; it is not merely a bound obtained by truncating a sum whose remaining history is exact.

For m=0,1,2,3,4 the bounds are respectively
3/29, 1/261, 1/7801, 1/234001, 1/7020001.
Thus two retained history corrections suffice for coefficient tolerance 1/1000 under this contract. This does not specify physical sensor precision.

An actual finite-window evaluator retains the current output, at most m older outputs, and one four-coefficient initial-memory term updated by multiplication by -1/30. Its predictions were checked against the full recorded-history implementation. Fixed slots do not imply bounded integer/rational bit length. The exact positive six-bin joint carrier remains available; no computational advantage over that tiny exact carrier is claimed. The truncated object is observer data, never a positive population, energy, or Cell.

Only the normalized unit-count six-state sector was used for exhaustive support tests. The displayed coefficient-bound proof also covers mixtures of any of the eight binary triples. For total positive mass W, all bounds scale by W. Input measurement errors, uncertain p, interventions and history-sensitive controls require additional bounds; none is silently included here.

## 6. Geometry and the operational meaning of the residual

In the previous fair-resampling example the average phase simply multiplies by -1/2. Here it is a sum of two exact decaying, sign-alternating modes. The individual channel trajectories still rotate through three directions. Their averaged scalar trajectory is not required to trace that circle or preserve its radius.

Memory can support echoes, but can also systematically oppose the current phase and reduce its magnitude faster. Dropping it changes a causal term, not necessarily removing negligible noise. Conversely, retaining every historical label forever is unnecessary for the declared observer: a proved history kernel, an exact two-sample recurrence, or the finite-window approximation can encode the required predictive information. These are three representations with different exactness/resource contracts.

None of these conclusions derives the incoming-channel relation or p from P000. No finite coefficient error is automatically a native physical residual. The new results do not assert the same rates for the shared-field 35-state process, and do not license source/path-sensitive inversion after deleting its needed state.

## 7. Executed evidence and unresolved administration

The final suite passed 56,001 exact assertions, including 53 prior-manifest checks. New coverage: 16 atomic channel/sign inputs at seven p values through 13 contacts for the elimination identity; all eight binary triples at p=1/2 and 8/15 through 40 contacts; all 63 nonempty normalized binary supports on the six-state joint sector through 48 contacts; one-time resets, finite-history bounds for m=0..4 and actual finite-window agreement; explicit labelled/quotient agreement through eight contacts and 3,066 inverse-history checks; two rational factorizations and symbolic phase-ring critical identities.

Actual unchanged CWM calls: cwm_edge141788, cwm_propagate185884, cwm_recoalesce102040. The finite test horizon supplements the displayed universal proofs and is not their infinite-domain evidence. No prior research suite was replayed as new work. A 40,566-check developmental version preceded the bounded-window implementation; final revalidation is not independent replication.

New brc_memory_kernel.py:4980 bytes, SHA256 6cdfd12ddf6b6b27de711c61156250506b6a37bca56e9f7ff11531d6e77dd628.
New check_memory_kernel.py:9015 bytes, SHA256 098bea937b7cdb78520c78a83e9fff72af6493463fbb01bbce52af761054bfdf.
Final evidence/summary.json:30817 bytes, SHA256 23cf4817353aa2aa7b7283eca3fde104c4aa0cc313593db7a4ee526e7a81948e.
Run python check_memory_kernel.py, Python3.10+, standard library. Source stores this new proof/validation frontier, not every executable attachment byte. The complete conversation package retains all exact dependencies, code, logs and manifests.

An initial inspection attempted an unavailable SOURCE_LOCAL attribute before scientific tests; it was removed, not interpreted as a residual. Both successful suite processes returned exit code0; their stderr also records unrelated environment spreadsheet-warmup warnings. These warnings did not supply any scientific calculation. The first container inspection returned TooManyRequests; the available Python runtime was used for local files/execution, never for remote GitHub transport.

Prior source-bound research registration remains unverified/REGISTER_PENDING on the evidence already recorded for this logical conversation. This turn did not acquire new identity, CLAIM, formal run, activity-checkpoint admission, independent review or successful final gate, and did not retry the previously rejected prerequisite or safety-blocked payloads. This is new scientific continuity, not an administrative workaround. Global journaling and source storage are not mathematical acceptance.

Completed bounded unit: exact memory elimination, rational all-contact improvement, formal modal infimum, sharp one-time reset response, and recursively stable finite-history compression. Next: validate a specific native or sourced incoming-orientation transport law against the local closure assumptions; for uncertain or state-dependent p, derive a robust joint-state/error contract rather than reuse the constant-p bound. Do not repeat this unit as new progress.
