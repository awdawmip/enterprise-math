# N=14 auxiliary iid sequential discrimination — exact 70th affine segment

**24 October 2026. Author-level exact rational finite-model proof; unreviewed by an independent Research Driver.** This is an external iid auxiliary model, **not** a theorem about native BRC, X6, or Heartbeat dynamics. It extends the exact 69th author endpoint from immutable source commit \`4c2560adafcc1d3b1105bfa9c8310c536c5481d8\`.

## Problem and exact theorem

Independent observations have laws P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), with maximal horizon N=14. For an arbitrary randomized stopping/decision policy on the **full ordered-history tree**, define eP=P(decide Q), eQ=Q(decide P), and tP,tQ as expected sample sizes. The global value is V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ).

The inherited 69th author endpoint is alpha69=2585943605277936457/7450150876955541504 and V69=24633048598563487079/1862537719238885376; its early-Q mixing probability at B=(12,0,1) is s69=4173507614280887/6963200000000000. A69=(5,5,0) is now a deterministic P stop. The inherited deterministic stopping tree is specified exactly in \`verify_n14_70.py\`.

Put K70=98126316/18523; lambdaQ=K70; lambdaP=72+(8/9)K70=88557048/18523; Gamma70=lambdaP+lambdaQ=186683364/18523; eta70=8983655/413897270941974528>0.

**Theorem (author checked).** For **every real** 0<=delta<=eta70, including irrational interior delta,

\[
\boxed{V_{14}(\alpha_{69}+\delta)=V_{69}-\frac{186683364}{18523}\delta}.
\]

Consequently the 70th right endpoint is

\[
\boxed{\alpha_{70}=\frac{2585943605439642247}{7450150876955541504}},\qquad
\boxed{V_{14}(\alpha_{70})=\frac{24633048191127045149}{1862537719238885376}}.
\]

The same affine support is not attained at any alpha>alpha70 (sharp right endpoint).

## Global Bellman lower bound

For state z=(n,a,b), where a,b count outcomes 0 and 1, every ordered prefix has likelihood ratio Q/P=2^(a+b)/3^a. In the P-normalized Lagrangian tP+lambdaP*eP+lambdaQ*eQ, the costs of immediate P, immediate Q, and continuation are

\[
C_P=\lambda_Q\frac{2^{a+b}}{3^a},\quad C_Q=\lambda_P,\quad
C_C=1+\sum_{i=0}^2P_iD(z+e_i)\quad(n<14),
\]

where D(z)=min(C_P,C_Q,C_C), with continuation absent at n=14. This count-state recursion lower-bounds the Lagrangian for **all** full ordered-history randomized policies, not merely count-based policies, because all prefixes with the same counts have identical conditional suffix laws.

Exact rational dynamic programming covers **680 states and 1,240 nonchosen comparisons**: 1,238 strict positive gaps, zero negative gaps and only two ties, A70=(9,4,4) with continue↔Q, and B=(12,0,1) with continue↔Q. The minimum positive gap is 6491/296368. The exact root is

\[
D(0,0,0)=\frac{3563071788120133078350431}{1014699593337113935872}=V_{69}+\Gamma_{70}\alpha_{69}.
\]

Hence, for every feasible policy, D(0)<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma70*alpha, which proves V14(alpha)>=D(0)-Gamma70*alpha.

## Exact ordered-history provenance, sensitivities and construction

At A70=(9,4,4), 630 ordered words nominally lead to that count; **291** survive all previous stopping decisions, leaving 339 already stopped. True first-hit masses are

\[
p_A=\frac{485}{2717908992},\qquad q_A=\frac{485}{859963392}.
\]

At B=(12,0,1), all 12 nominal histories survive, with pB=48828125/725594112 and qB=48828125/362797056.

The exact conditional continuation suffix risk quadruples (eP,eQ,tP,tQ) are

\[
R_A=(98221/98304,\ 41/248832,\ 15703/12288,\ 24331/20736),
\]
\[
R_B=(63/64,\ 1/144,\ 9/8,\ 13/12).
\]

As a provenance test, prior Q-stop (10,4,5) has 291 first arrivals, **all 291 via A70**; prior Q-stop (10,4,4) has 1425 first arrivals, **291 via A70**. Earlier stopping at A70 truncates those descendant paths. The BRC positive-rational labeled-branch law actually applied is W=sum over surviving ordered histories of product of step probabilities; the count state alone is not sufficient to reconstruct first-hit provenance.

Let u∈[0,1] be the probability of immediately declaring **Q** at A70; let s be the probability of immediately declaring Q at B. A trajectory cannot traverse both ties: A70 has a=4 and B has a=0, with a nondecreasing. All four risks therefore have exactly zero mixed u*s coefficient (verified again by four exact-rational corners).

Compute the positive sensitivities

\[
X=p_A(1-R_A.e_P)=\frac{40255}{267181325549568},\quad
Y=q_AR_A.e_Q=\frac{19885}{213986410758144},
\]
\[
E=p_B(1-R_B.e_P)=\frac{48828125}{46438023168},\quad
H=q_BR_B.e_Q=\frac{48828125}{52242776064}.
\]

Relative to (u,s)=(0,s69), exact changes are

\[
\Delta e_P=Xu+E(s-s_{69}),\quad
\Delta e_Q=-Yu-H(s-s_{69}).
\]

Equating both errors uniquely yields s=s69-h70*u, where

\[
h_{70}=\frac{X+Y}{E+H}=\frac{17080439}{139264000000000}.
\]

At u=1, s70=4173506760258937/6963200000000000, with 0<s70<s69<1; the full family is feasible. Both errors equal alpha69+eta70*u, as eta70=X-E*h70=H*h70-Y>0.

The endpoint values tP-tQ are, respectively,

\[
\frac{133290941048883881}{232817214904860672}>0\quad(u=0),\qquad
\frac{266582080047513187}{465634429809721344}>0\quad(u=1).
\]

There are no mixed terms, so all four risks are affine in u along the balance line; in particular tP>=tQ for every real u. Every chosen state action minimizes the exact Bellman cost, hence tP(u)=V69-Gamma70*eta70*u. Given any delta in [0,eta70], choose u=delta/eta70; this attains the global dual lower bound, proving the entire real interval.

## Sharpness and boundaries

The finite full ordered-history randomized policy polytope is compact. Equality to the **same** support line at alpha>alpha70 requires both positive-multiplier error constraints tight (eP=eQ=alpha) and zero-slack Bellman actions on every reached state. Only A70 and B are tied. Since the Q/P prefix likelihood ratio is constant within each count-state fiber, arbitrary history-dependent tie choices can be replaced by P/Q-weighted effective coin rates u and s without altering the four global risks. The two ties lie on disjoint trajectories. Error balance forces s=s69-h70*u and alpha=alpha69+eta70*u<=alpha70 for u<=1: contradiction. Thus the 70th support is right-sharp.

**Local verification actually executed:** exact Fraction main checker, separate author crosschecker that minimizes Bellman actions afresh and enumerates full ordered histories/backward risks, 680 states, 1240 comparisons, 630 nominal/291 true A histories, descendant truncations, four zero mixed risk coefficients and seven rational mixture checks. Both passed. The scripts share inherited author stopping sets; **this is not independent Driver review**. No native BRC/X6/Heartbeat fidelity mapping, formal Result freeze, current CLAIM or physical bridge is asserted.

**Next dual candidate only:** K71=5184 at A71=(11,1,2), continue versus Q. The 71st optimal interval is not yet proved.

Source pins: global main@73394886355700111e48ae3ed0da83221b14ad4e; Enterprise Math control main@a320c02c11ceedc9fa1a526137bc57abcb738b05; predecessor source@4c2560adafcc1d3b1105bfa9c8310c536c5481d8. P000/ACTIVE worldview retained as internal project assumptions, not promoted into an auxiliary/native equivalence. Tool reuse: positive-weight labeled ordered-history law REUSE_APPLIED; native execution not claimed. Native owner query returned CONTROL_QUOTA, session start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false), so no verified CLAIM.

Status: N14_70_AUTHOR_PROVED / TWO_AUTHOR_FRACTION_CHECKS_PASS / DRIVER_UNREVIEWED / NATIVE_CLAIM_UNVERIFIED / NO_NATIVE_BRIDGE.
