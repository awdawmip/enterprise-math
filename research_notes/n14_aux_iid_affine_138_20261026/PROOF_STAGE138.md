# Stage138 — exact full-real optimum and sharp right support (author proof)

**Status:** AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF. Complete rational calculations and two author-side algorithms (bottom-up Fraction, independent integer-weight literal-prefix DFS) passed locally on 2026-10-26. **Not** independently checked by the Research Driver; no Source CLAIM, formal Result, or P000/X6 transfer is claimed.

## 1. Exact external finite model

The auxiliary experiment is the ternary iid sequential test with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=14. Strategies may stop and declare either P or Q, adapt and randomize using the *entire ordered observed history*, and must decide at N. Write eP=P(declare Q), eQ=Q(declare P), tP=E_P[tau], tQ=E_Q[tau]; V14(alpha)=inf max(tP,tQ) subject to eP,eQ<=alpha.

Consume Stage137's exact author theorem at
alpha137=36707714001694332695/105616844785075617792,
V137=653786393599537203227/52808422392537808896.
Stage137's full-real interval and sharpness are inherited; they were not rerun as new theorems.

## 2. Theorem (whole continuum, not sampled points)

Let K138=3709800/6941, L138=3529544/6941, and
eta138=167776984375/25785362496356352.

For **every real** 0<=delta<=eta138,

> **V14(alpha137+delta) = V137 - (7239344/6941) delta.**

The right endpoint is

alpha138=4078711246246925855/11735204976119513088,

V138=217809339038053734409/17602807464179269632.

The *same optimal supporting affine line* is strictly below V14(alpha) at every alpha>alpha138. This is a right-sharpness statement for this support, not an impossibility of more permissive feasible tests.

## 3. Universal exact dual Bellman bound

For count state s=(n,a,b) with a=#symbol 0, b=#symbol 1, the likelihood ratio Q(prefix)/P(prefix) is r(s)=2^(a+b)/3^a. The rational Bellman recurrence is

H(s)=min{ K138*r(s) [declare P], L138 [declare Q], 1+sum_i P_i H(child_i) [continue, n<14] }.

All 680 count states (sum_{n=0}^14 (n+1)(n+2)/2) were covered by exact Fraction arithmetic. There are precisely 1,238 strictly positive nonchosen action gaps, none negative; the minimum positive gap is 4/187407. The only nontrivial tied states are B=(11,0,1), Q/continue, and H=(11,4,1), P/continue. The root is

H0=190052304168624227306189/506975463107337388032.

The count-state recurrence is valid for all *literal history-dependent* policies because the conditional suffix law and likelihood ratio are count sufficient for this iid model's declared four observers. Induction yields, without imposing a count-policy restriction,

H0 <= tP + L138*eP + K138*eQ
   <= max(tP,tQ)+(K138+L138)*alpha.

Hence V14(alpha)>=H0-(7239344/6941)*alpha.

## 4. Literal-prefix BRC carrier, first-hit masses and cross-check

The independent forward algorithm retains literal ternary word identity, exact positive P/Q integer numerator weights and stopping time, before the permissible iid observer quotient. P path weights use (3,1,20)/24 and Q use (1,1,10)/12.

For the strict policy before depth11, the *actual reachable* first-hit words are:

| critical state | count | exact P mass | exact Q mass |
|---|---:|---|---|
| B=(11,0,1) | 11 | 107421875/1451188224 | 107421875/725594112 |
| H=(11,4,1) | 1547 | 24171875/4586471424 | 24171875/11609505792 |

B and H have the same observation depth (11) and different counts, so no ordered word can contain both as first-hit states. Their future cones do not intersect; there is no mixed randomization term. The observed H count is 1,547, not the unfiltered multinomial 2,310: earlier strictly optimal stops eliminate some prefixes.

Let w in [0,1] be the **Q-stop** probability at B (rather than continue), and h in [0,1] the **P-stop** probability at H (rather than continue). All other actions follow the unique Bellman minimum. For M=(eP,eQ,tP,tQ),

M(w,h)=M00+w*dB+h*dH,

where the exact vectors are

M00=(
2430334654032070769/7011906707722862592,
149098923687847/427972821516288,
10888421528901503711/876488338465357824,
1274918259612433/106993205379072
);

dB=(
4619140625/2229025112064,
-751953125/417942208512,
-25673828125/278628139008,
-17939453125/104485552128
);

dH=(
-1136078125/63403380965376,
555953125/20061226008576,
-15059078125/2641807540224,
-4036703125/1671768834048
).

Two differently structured algorithms agree at **all four deterministic (w,h) corners**. The integer-word DFS visited 709624, 709492, 691060, and 690928 nodes at (0,0), (1,0), (0,1), and (1,1). The exact mixed difference M11-M10-M01+M00 is the zero four-vector. The local JSON certificate stores four complete corner vectors, path masses and digest observations; the source programs reproduce the decisive assertions.

BRC resolution: **REUSE_APPLIED** to the ordered labeled positive-rational branch carrier. The only quotient is the exact finite iid-sufficient one for these four observables and this horizon. No signed/phase cancellation, native six-dimensional transfer or physical inference is used.

## 5. Explicit primal family proves all-real attainment

The equality eP=eQ is equivalent to

w(h) = 1136555606328589/2467840000000000 + (2999633/254496000)*h.

At h=0 and h=1, respectively,

w0=1136555606328589/2467840000000000,
w1=38466217568843437/81438720000000000,

both strictly between 0 and 1. Thus w(h) is a valid probability throughout the **entire real** interval 0<=h<=1.

Substitution into the exact vector gives

eP=eQ=alpha137+eta138*h,
tP=V137-(7239344/6941)*eta138*h,

and the endpoint gaps tP-tQ are

h=0: 28703243336799108269/52808422392537808896 >0;
h=1: 85737739727005324807/158425267177613426688 >0.

By affinity, tP>tQ throughout. Direct exact substitution also gives
tP+L138*eP+K138*eQ=H0. Together with the universal lower bound this proves the theorem for all real delta in [0,eta138], including both endpoints.

## 6. Sharpness (complementary slackness)

If the same support attained V14(alpha) for some alpha>alpha138, finite-horizon policy compactness ensures an attaining behavioral strategy. Equality in the two inequalities in §3, with positive K138,L138, forces both errors to equal alpha, tP=max(tP,tQ), and every positively used action to be Bellman-minimizing. All other actions have strictly positive gaps, so only B and H can randomize. Their disjoint ordered-prefix cones and iid-sufficient conditional suffix law allow mass-weighting arbitrary history-dependent coins into the two effective probabilities w,h without changing (eP,eQ,tP,tQ). Equal errors force w=w(h), and then alpha=alpha137+eta138*h with 0<=h<=1, a contradiction. The support therefore is right-sharp.

## 7. Evidence boundary, frozen inputs and next task

Read pins for this research turn: GLOBAL_KNOWLEDGE_V1 canonical main a197792a7db5d01e0f517fde56d717be4bfb56c5; Enterprise Math main c4095e2200437eb9e0586ead5f40548bdde5e165; Stage137 proof Git blob a714ba1a488624d568fd7e70e5f085178024dc34; Stage138 continuation packet blob ce09e3b45ec9ec2b043922db9b5a78415ccd4b9f; P000 locked bootstrap projection Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. The ACTIVE residual-faithful worldview and the current Portable Research Protocol govern interpretation. Verification is local author computation, not independent Research Driver review.

Native control inventory: CONTROL_QUOTA (no owner decision); native session_start: STATIC_READONLY_SCOPE_DENIED, operation_sent=false. The GitHub account is awdawmip with ordinary repository push permission, but this confers **no** native Researcher session, ownership or CLAIM. This is an external finite iid auxiliary result, not a P000/Heartbeat X6 or three-dimensional slice theorem.

Next exact research unit: Stage139 dual candidate for the ray (dK,dL)=(-1,-112/129) and new state C=(6,3,0), P/continue. Verify actual first-hit history masses and possible ancestral interaction with B; derive primal affine interval (or an exact obstruction), continuing only within the author-evidence channel pending independent review.
