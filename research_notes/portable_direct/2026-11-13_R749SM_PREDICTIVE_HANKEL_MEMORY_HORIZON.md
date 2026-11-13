# R749SM — Finite-horizon predictive Hankel rank and a delayed two-bit provenance witness

Date: 2026-11-13 (Asia/Shanghai). Status: independent author-side exact mathematical derivation and finite rational verification. Continuation of R749SF/SI/SJ/SK/SL (R749SK and R749SL in draft PR #2183 @39bc65a4272f9d6cc836d9d96bee9c2b796b1eee); the existing shared X6 triadic-closure task remains separately owned. This paper is not an independent review or native V29/V39 permission.

Scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, including P000 signed X6, triadic closure definition, native spatial torsor and signed-source preservation. R749SF: `research_notes/portable_direct/2026-11-12_R749SF_EIGHT_LIFT_HIDDEN_SIGN_FILTER.md@066958c8da10e4d67395f3c9b6942a8d9d26daa7`. R749SL: `research_notes/portable_direct/2026-11-13_R749SL_EIGHT_LIFT_ADAPTIVE_FILTER_HIDDEN_MEMORY.md@39bc65a4272f9d6cc836d9d96bee9c2b796b1eee`. The model is the explicitly augmented, sign-adaptive controller on the abstract R749SF signed-Port kernel, not the original homogeneous P_p support-choice law.

## 1. Exact finite-horizon theorem

Let S be a finite *typed full hidden-state set* with N elements, including current named signs, private controller memory, and any finite controller phase necessary to make the update Markov. Fix a public initial support/context and a declared finite alphabet Y of publicly visible next-support/emission symbols. For a stationary policy in this augmented state, define nonnegative matrices Q_y, with

`Q_y(s,t)=Pr(next hidden state=t, observed letter=y | current hidden state=s)`, and `sum_y Q_y 1=1`.

For a word w=y1...yk let `f_w=Q_y1 ... Q_yk 1` (an N-vector); `f_empty=1`. For H>=0 define the truncated predictive row-span `V_H=span_Q{f_w: length(w)<=H}` when all weights are rational (over R otherwise), and d_H=dim V_H.

**Theorem 1 (sharp affine predictive carrier):** Over *arbitrary strictly interior priors* mu on S, the minimum number of independent affine-linear expectation coordinates that exactly reconstructs the probabilities of **every** future public word of length at most H, with arbitrary nonlinear readout allowed from the retained coordinates, equals

`c_H=d_H-1.`

Proof. Each word probability is the linear functional `mu f_w`. Because `f_empty=1` and `mu 1=1`, a basis for `V_H / span{1}` yields c_H sufficient affine coordinates. Conversely, if a carrier C mu has identical value on mu and mu+epsilon h with `h 1=0`, for all sufficiently small epsilon in the interior simplex, it must give equal `mu f_w` for every word. Hence `h f_w=0`; each f_w modulo constants must lie in the carrier row space. Thus at least dim(V_H)-1 coordinates are necessary. This is an exact minimum in the declared *affine statistical* class; no claim about arbitrary unrestricted encodings is made.

Define deterministic hidden-history equivalence `s equiv_H t` iff `f_w(s)=f_w(t)` for all |w|<=H. This precisely characterizes when two *point* hidden histories can be identified for the declared horizon. Its number of classes need not equal c_H+1, because distinct predictive law vectors may be affinely dependent. Therefore history-class count and mixed-prior statistical rank are separate exact answers.

**Theorem 2 (finite certificate for all future words):** For a stationary finite-state controller, start from V_0=span{1} and iterate

`V_{h+1}=V_h + sum_y Q_y V_h.`

The sequence stabilizes by `H<=N-1`, and the first equality `V_{h+1}=V_h` is a certificate of invariance under every Q_y, hence of equality to the all-future predictive span. Proof: each strict expansion increases dimension at least one, starting at dimension one and bounded by N; if no increase then Q_y V_h subset V_h for all y and every later word lies in V_h. This is the standard finite weighted-automaton reachable-space principle, specialized here to provenance-carrying BRC-style positive-rational branches. For public-history-dependent policies, the same finite-H rank theorem applies separately to the actual known history; the N-1 stationary bound requires an actual finite autonomous controller encoding of history/phase.

## 2. Explicit signed-Port construction: H=0,1,2 has ranks 1,2,4

Work on the six named axes 0..5 and p=1/2, where the R749SF forced conditional sign transfer is BSC with `theta=8/9`; nonforced updates forget the old-only signed axis and draw the new named sign fairly. Start with an initial directed unsigned state

`A0={0,1}, B0={1,2}`

and arbitrary private sign pair `Z=(Z0,Z1)` for axes 0 and 1, while axis 2 has a fair sign independent of Z. Observe two nonforced supports `C0={2,3}` and `C1={3,4}`. The first update forgets sign 0 and the second forgets sign 1; the private controller retains the *actual* discarded historical signs Z0,Z1. At the resulting directed support `S=({2,3},{3,4})`, all three current signs on axes 2,3,4 are exactly independent fair coins, **for every** prior on the four values of Z. This gives the same current eight-lift posterior for all four private histories.

A two-stage lawful support chooser uses only Z, not the current signs. On the next step it chooses the forced completion `{2,4}` with probability

`Pr(A=+1|Z)=(2+Z0 Z1)/4`,

and otherwise the nonforced `{4,5}` (public A=-1). For the subsequent step, conditional on the known first chosen support, it chooses the forced completion with probability

`Pr(B=+1|Z)=(2+Z0)/4`,

and otherwise a fixed nonforced completion: if A=+1 then forced `{2,3}`, nonforced `{2,5}`; if A=-1 then forced `{3,5}`, nonforced `{0,5}`. All these are legal adjacent two-axis supports, and all four public output words have strictly positive probability. Controller choices are fresh conditionally independent Bernoulli draws given Z. At each chosen unsigned support, the R749SF conditional signed transition law is used without modification. Its uniform current-sign distribution remains uniform after every such sign-blind conditional transition.

For `a,b in {-1,+1}`, exact joint public-word probability from a prior mu on Z is

`P_mu(A=a,B=b) = E_mu[(2+a Z0Z1)(2+b Z0)]/16`

`= (1 + (a/2)m01 + (b/2)m0 + (ab/4)m1)/4`,

where `m01=E[Z0Z1]`, `m0=E[Z0]`, `m1=E[Z1]`.

Thus one observation step needs exactly the parity coordinate `m01`; two steps need the three independent coordinates `(m01,m0,m1)`. In symbols,

`d_0=1, d_1=2, d_2=4`, hence `c_0=0, c_1=1, c_2=3`.

The four-by-four matrix `M_{(a,b),Z}=P(A=a,B=b|Z)` has determinant `+1/16` for row/column lexicographic order -1,+1. Its rank is exactly four. The first-step matrix has rank two. Therefore deterministic private histories form two predictive-equivalence classes at H=1 (indexed by Z0Z1) and all four are separated at H=2. For an arbitrary prior, the 3-coordinate lower bound is sharp and the three moments can be recovered from the public two-step law:

`m01=2 E[A], m0=2 E[B], m1=4 E[AB].`

With a sign- and memory-independent support policy after the second stage, later public support observations are conditionally independent of Z given the already observed word; the predictive rank stays four for all H>=2. The **additional source state is in the controller's historical memory**, not an additional native X6 spatial dimension.

## 3. Provenance and BRC observer interpretation

The pre-controller two-step signed-path population has four explicitly named historical-sign fibers over the same current eight-lift distribution. A one-step public observation collapses these four fibers into two predictive classes by their parity; the second step separates all four. The positive-rational branch weights are retained on those fibers, and the exact Walsh moments are a query-sufficient *readout* of the four-fiber weight distribution. The current signed-Port distribution alone is insufficient for the declared two-step adaptive controller, while the full 32-state joint (current sign, historical pair) need not be retained for this particular public-support query: the exact minimal affine source carrier is three coordinates. Point-history storage costs two binary bits; arbitrary mixed-prior statistics require three independent real/rational expectations. The two measurements are distinct.

For a general finite-state BRC-port/controller composite, the span construction provides an exact signed/provenance-safe reduction certificate for the declared future public alphabet. Changing the alphabet, adding signed-time joint queries, allowing hidden controller access or moving to an infinite-history policy changes the retained span and must be recalculated. This permits scoped safe compression, not erasure of typed source identity.

## 4. Verification and next discriminating problem

`R749SM_PREDICTIVE_HANKEL_EXACT_CHECK.py` checks all 120 legal unsigned directed supports, 960 legal next-support pairs and 7680 signed conditional (support,sign) rows with exact Fraction sums; verifies both nonforced historical-sign erasures and the uniform current eight-lift posterior for all four Z and all four later observation words; checks 4x4 determinant 1/16 and rank 2/4; and validates the explicit Walsh reconstruction for all 625 strictly positive integer-weight priors (weights 1..5 per private history). Exact output is in the companion JSON. The all-H/N-1 theorem is proved algebraically; the enumerator tests the finite six-axis instantiation at p=1/2.

Further work: build the exact observed-alphabet matrices Q_y for any genuinely source-authorized V29/V39 event with private provenance/controller memory, then compute this predictive span and compare its observer equivalence to any licensed native Cell/Link/Port quotient. This remains an event-specific guard/certificate question, not a consequence of the present abstract construction.
