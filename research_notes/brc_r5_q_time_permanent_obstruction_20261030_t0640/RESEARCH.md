# Enterprise Math R5 — optimal Q/time obstruction to **all P-only compensators**

Date: 2026-10-30 06:40 Asia/Shanghai. Researcher provenance: `EM-R005-Q0640` (self-resolved, author-side TASK_RESEARCH). Status: **AUTHOR_PROVED / EXACT_INTEGER_ENUMERATED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**.

## Pins, mother question, and carrier

Frozen account control: GLOBAL_KNOWLEDGE_V1 main `4ec0fb0b0b33a6104c1da35c2145e52405f8540c`; Enterprise Math canonical main `e69c62b9fbad1edb4cfc5cfeaad33b7a0e4de2a3`. Scientific predecessor: PR #1663 at `2f450c76ced7fa672b391f46483e6043d643ffdb`, `research_notes/brc_r5_uniform_stage3_compensation_20261030_t0536/RESEARCH.md`. Current P000, ACTIVE worldview, positive source-labelled BRC, joint-observer preservation and portable research rules apply. This note proves a *typed auxiliary two-law stochastic stopping theorem*, without asserting a native Heartbeat-X6 physical interpretation.

Mother target: equal convex hulls of four-observer FULL and seedless exact-likelihood-ratio (LR) behavioral strategies but unequal actual observer images. The preceding doubly colliding tree has two source labels, 14 natural history nodes, and 12 distinct (time,likelihood-ratio) decision keys. Natural P,Q transition kernels, cylinder masses and collisions are **unchanged**. In particular:
[
(P(A11),Q(A11))=(1/12,1/24),quad (P(B11),Q(B11))=(1/9,1/18).
]
At times 1,2,3, agents may stop, and otherwise stop at time 4. FULL sees history; LR sees only (time,L) and has no persistent random seed. Under BRC we retain exact labelled masses P(h),Q(h), rather than quotienting histories before the four-observer calculation.

For the Q Bernoulli error kernel use
[
q_0(t,h)=2/5-t/30+(t+2)L(h)/200,qquad L(h)=P(h)/Q(h).
]
Modify only `q(3,A11)=q0+eta`, `q(3,B11)=q0-eta`, with `eta>0` small enough for strict (0,1) rates. All other Q error rates remain q0. **Allow any admissible P Bernoulli terminal-error kernel** p(t,h), including independently signed compensation at A11,B11,A0 or arbitrary other stopped cylinders. These terminal P changes leave the *natural history P,Q masses and likelihood-ratio keys* fixed.

Four observers are `O=(eP,eQ,TP,TQ)`, with (T_mu=E_mu[	au]). Define
[
S=e_Q-41/100-T_P/200+T_Q/30,qquad D=8-T_P-T_Qge0.
]
The change-of-measure identity (Q(h)L(h)=P(h)), and (sum_hP(h)=sum_hQ(h)=1) over stopped cylinders, give the **exact all-real** identity
[
S=eta{Q(A11){f1}_{	au(A11)=3}-Q(B11){f1}_{	au(B11)=3}}
]
for deterministic policies; for behavioral policies replace each indicator by the relevant stopping probability flow. Crucially, neither S nor D contains any terminal P-error rate. The only two nonzero signed Q residual rewards are (+eta/24) and (-eta/18). Early stop at cylinder h incurs (D)-cost ((4-t)(P(h)+Q(h))).

## Theorem Q1 — exact optimal nonnegative time-penalty envelope

For every real (lambdage0), set (Psi_lambda=S-lambdaeta D). Then **for all real behavioral stop probabilities**, including endpoints and unreachable histories,
[
oxed{max_{m FULL}Psi_lambda/eta=max(0,1/24-lambda/8)}
]
and
[
oxed{max_{m LR}Psi_lambda/eta=max(0,1/24-25lambda/8)}.
]
Consequently their exact support gap equals
[
Delta_Q(lambda)/eta=
egin{cases}
3lambda,&0lelambdale1/75,\
1/24-lambda/8,&1/75lelambdale1/3,\
0,&lambdage1/3.
end{cases}
]
It has a **unique maximum** (oxed{eta/25}) at (oxed{lambda=1/75}) *within this penalty family*.

**Proof.** At each (time,information) key a path makes at most one decision. The expectation of every linear four-observer functional is multi-affine in the independent behavioral probabilities, even though a key is shared by multiple mutually exclusive paths. Maxima occur at deterministic 0/1 corners, proving the reduction for the full real hypercube. For FULL, only A11 offers a positive signed Q residual; selecting its time-3 stop while all other leaves wait to time 4 contributes (1/24-lambda/8), whereas no early stop contributes zero. Every other early stop adds a nonpositive local term; B11 contributes strictly negative Q residual. This gives the first envelope.

For LR, stops at non-reward branches can be removed unless they prevent a negative B11 contribution; the only potentially useful prevention before time 3 is a time-1 stop of B, or the shared time-2 A1/B1 stop. The latter simultaneously kills the A11 positive reward, hence cannot make the support positive. With time-2 collision continued and time-3 shared collision stopped, enumerate the two root continuation bits ((alpha,eta)). Their scores are: ((1,1)): (-1/72-7lambda/24<0); ((1,0)): (1/24-25lambda/8); ((0,1)): (-1/18-19lambda/6<0); ((0,0)): (-6lambdale0). Stopping no reward nodes is never profitable. A policy with no early stops gives zero. This establishes the LR envelope and, by subtraction, the piecewise gap.

At (lambda=1/75), every LR observation satisfies (Psile0), while FULL can stop at A11 alone with (Psi=eta/25). This is a signed supporting-hyperplane certificate independent of all allowed terminal P-error modifications. As FULL includes every LR policy, **the FULL/LR four-dimensional convex hulls are strictly different throughout this entire P-only compensation family**. The result applies even if another P-only signed support gap is tuned to zero.

## Exact integer separator and positive rational witness

Take (eta=arepsilon=1/1000) and the predecessor's valid P rates at (ho=1), i.e. +(arepsilon) at `p(2,A1)`, -(arepsilon) at `p(2,B1)`, and +(arepsilon) at each `p(3,A11)` and `p(3,B11)`. The valid FULL policy stopping **only A11 at t=3** gives
[
O^*=(891/2000,;21433/72000,;47/12,;95/24).
]
The (lambda=1/75) separator is
[
oxed{75000e_Q-374T_P+2501T_Qle30758}quad(mathrm{LR hull}).
]
At O* its left side is exactly **30761**, a strict integer gap **3**. The normal's (ell_1) norm is (75000+374+2501=77875), giving (operatorname{dist}_infty(O^*,operatorname{conv}O_{m LR})ge 3/77875). The value of eP changes under arbitrary P compensations, but this inequality and its violation persist for the same FULL stop rule.

## Corollary Q2 — exact three-parameter P-direction necessary wedge

To close the previous P/time direction (Phi=R-(arepsilon/22)D), separately let (delta_A=aarepsilon) and (delta_B=barepsilon) modify p(A11),p(B11), and (gamma=carepsilon) modify p(A0 at time 2). Keep the earlier ±(arepsilon) p-errors at A1/B1. All formulas below hold for real a,b,c with admissible error rates.

Put (U=3/22, V=a/12-1/176, W=b/9-1/132, H=max(0,c/6-2/33)). Exact maxima are
[
egin{aligned}
max_{m FULL}Phi/arepsilon&=H+max(U,V)+max(0,W),\
max_{m LR}Phi/arepsilon&=max{H,;-3/11+max(0,3/22+V+H)+max(0,3/22+W)}.
end{aligned}
]
The difference **vanishes if and only if** (Vge U) and (Wge0), equivalently
[
oxed{age75/44,quad bge3/44}
]
regardless of c. Proof: in any FULL maximizer, both roots continue. A1 at time 2 yields strictly positive U; B has zero as a feasible baseline. Every LR policy attaining the FULL support must likewise continue both roots (otherwise incur a strictly negative root deficit). It cannot stop at the shared A1/B1 key at time 2, as that incurs a strictly negative B1 reward and removes B's optimal choice. To match the positive A source maximum it must stop at the shared A11/B11 key at time 3, requiring (Vge U); matching B's maximum requires (Wge0). Conversely, under both inequalities the common LR rule continuing both roots and A1/B1, then stopping A11/B11 at time 3, realizes the FULL support, and the A0 choice maximizing H is also LR-feasible. This wedge is only a **one-signed-direction** condition; Theorem Q1 excludes all P-only compensators irrespective of it.

## Verification, scope, next discriminating question

The standalone `VERIFY.js` uses exact integer cylinder masses with common denominator 360 and accumulates (Psi/eta) in units 1/27000. It reconstructs 14 nodes / 12 LR keys and checks positive P/Q Bernoulli rates at the displayed instance, both collisions, complete deterministic supports (**16,384 FULL** and **4,096 LR** policies), the integer witness, and 216 exact signed three-parameter regression points for Corollary Q2. Recorded stdout is in `EXACT_OUTPUT.txt`. A second Python `Fraction` enumeration of all 20,480 policies agrees (author execution, independent implementation). The all-real theorem follows from the proof, not regression samples. Git publication is research preservation, not Source claim, Result, independent review, X6 correspondence, novelty priority or mathematical admission.

**Next:** To search for hull equality, one must **change the Q-terminal error family or natural P,Q transition geometry** in addition to P compensators. Retain the double LR collisions and labelled BRC positive masses, choose a Q adjustment outside A11/B11 with a counterbalancing signed effect, and first test both P/time and Q/time optimal signed directions. Reject on any strict support gap; only then undertake exact all-signed four-dimensional hull inclusion (every FULL deterministic vertex a rational combination of <=5 LR vertices) and finally real-image semialgebraic nonmembership if hulls match.
