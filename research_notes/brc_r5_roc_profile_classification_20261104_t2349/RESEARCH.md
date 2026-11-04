# R5: complete single-merger LR-profile criterion; equal-TV strict separation

Date: 2026-11-04 Asia/Shanghai. Scientific evidence: author analytic proof; exact finite rational enumeration; independent review pending.

## Context and frozen inputs

This continues `research_notes/brc_r5_lawful_two_source_tv_jensen_20261104_t2245/RESEARCH.md` at immutable EM commit `5f9bb8746a3202ee14508ed2b9324102c4d79024`. That note used variation of terminal total variation across merged source histories. Here we prove a complete classification by the *entire terminal likelihood-ratio distribution* and find a case where terminal total variations are identical but hulls remain strictly separated.

Frozen scientific inputs are Global `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current normative policy was read separately. P000, Heartbeat World X6 and the future-operation joint-residual observer constraints remain in force; the finite BRC below is an explicitly typed probability/path observer, without native spatial or physical calibration claims.

## Model and definitions

Let H be a finite set. At t=1 a source h occurs with P(h)=Q(h)=w_h>0, sum_h w_h=1; hence all source histories share likelihood-ratio key (1,1). FULL observes h. Seedless LR sees only (t,R) and uses independent behavioral randomization at each key. The time-1 actions are STOP_P, STOP_Q and CONTINUE. Continuing produces a terminal signal s in S_h at t=2 with strictly positive conditional kernels P_h(s), Q_h(s), each summing to 1; at t=2 freely declare P or Q. The terminal LR is r_h(s)=P_h(s)/Q_h(s). Terminal LR keys may collide across h. Observe O4=(eP,eQ,TP,TQ), where eP=P(declare Q), eQ=Q(declare P), and T are expected stopping times.

Define the source-conditional *Q-law of terminal LR* as nu_h = sum_s Q_h(s) Dirac_{r_h(s)}. This positive finitely supported law has E_nu_h r=1. For k>0, define

    G_h(k)=min(1,k)-sum_s min(P_h(s),k Q_h(s))
          =min(1,k)-E_{nu_h}[min(r,k)] >= 0.

G_h(1)=TV(P_h,Q_h); the full function contains more information than that single value.

## Theorem — four equivalent criteria (all real behavioral strategies)

For every finite positive experiment just defined, these assertions are equivalent:

(1) conv O4(FULL) = conv O4(seedless LR);
(2) O4(FULL) = O4(seedless LR) as actual images;
(3) all source-conditional terminal LR laws nu_h are equal;
(4) all functions G_h(k) agree for every real k>0.

If they differ, there is a strictly separating four-dimensional linear functional and a valid FULL witness; for rational input kernels the separating coefficients and witness can be selected rational.

### Proof: exact support function and necessity

For k>0 and tau>=0, maximize the signed direction n=(-1,-k,-tau,0), equivalently minimize eP+k eQ+tau TP. At time 1, immediate stopping costs min(1,k)+tau: declaring P costs k and declaring Q costs 1. At terminal time 2, the optimal error cost conditional on h is sum_s min(P_h(s),kQ_h(s)), with time cost 2tau. The optimal terminal declaration compares r_h(s) with k, so it is seedless LR-compatible even when terminal LR keys are shared.

Hence the *exact* support functions are

    h_FULL(n)=-min(1,k)-tau + sum_h w_h (G_h(k)-tau)_+;
    h_LR(n)  =-min(1,k)-tau + (sum_h w_h G_h(k)-tau)_+.

The difference is the Jensen positive-part gap. Choose tau=barG(k)=sum_h w_h G_h(k), obtaining

    h_FULL(n)-h_LR(n)
      =sum_h w_h (G_h(k)-barG(k))_+
      =(1/2)sum_h w_h |G_h(k)-barG(k)|.

If convex hulls agree this gap must vanish for every k; since every w_h>0, all G_h are identical. When any G_h differ, this gives a strict linear separation in O4, with a sourcewise deterministic FULL policy maximizing n. The G_h functions for rational finite kernels are rational piecewise linear with rational breakpoints, so a distinguishing rational k and tau exist.

### Proof: risk profiles identify the terminal LR laws

Set F_h(k)=min(1,k)-G_h(k)=sum_r nu_h({r})min(r,k). For every k>0 its right derivative satisfies F'_h(k+)=nu_h((k,infinity)). Equality of F_h on all positive k implies equality of all these survival probabilities and hence equality of the finite positive laws nu_h. Conversely equal nu_h immediately give equal G_h. Thus (4) iff (3).

### Proof: constructive real-behavior image equality

Suppose nu_h=nu for every h. An arbitrary FULL strategy chooses sourcewise stop-P, stop-Q and continue probabilities a_h,b_h,c_h>=0, summing to 1. At (1,1), the seedless policy chooses a=sum_h w_h a_h, b=sum_h w_h b_h, c=sum_h w_h c_h. Both measures then have TP=TQ=1+c.

At each terminal LR r, average the FULL probability of declaring Q over signals with this r under Q_h, calling that d_h(r). For c>0 define the seedless terminal declaration-Q probability d(r)=sum_h w_h c_h d_h(r)/c (choose any d(r) if nu({r})=0). This is a legal [0,1] probability. Its terminal Q-mass at LR r declaring Q equals nu({r})sum_h w_h c_h d_h(r), exactly the FULL total, because each Q_h LR law is nu. Its P-mass is r times this Q-mass and also agrees. Sourcewise stop contributions match by a,b. Thus eP,eQ and TP,TQ all match. If c=0 no terminal decision matters. Hence every FULL four-vector is produced by a real seedless LR behavioral strategy; reverse inclusion is automatic. Conditions (3) implies (2), and (2) implies (1). QED.

## Equal-total-variation rational witness

Two sources A,B have w_A=w_B=1/2:

    Q_A=(1/2,1/2),         P_A=(1/4,3/4);           LR_A=(1/2,3/2).
    Q_B=(1/3,1/3,1/3),     P_B=(1/12,1/3,7/12);   LR_B=(1/4,1,7/4).

Every transition probability is positive and the five terminal LR keys are distinct. Both conditional total variations are 1/4; hence the predecessor's TV-only n=(-1,-1,-lambda,0) sees a zero Jensen gap for all lambda. At k=3/8, however, G_A=0 and G_B=1/24. Choose tau=barG=1/48 and n=(-1,-3/8,-1/48,0).

FULL: stop A with declaration P; continue B, declare Q at B's LR=1/4 terminal and P at its other two terminals. This yields

    W=(1/24,5/6,3/2,3/2)
    h_FULL(n)=-37/96,   h_LR(n)=-19/48,
    support gap = 1/96.

Since ||n||_1=67/48, dist_infty(W,conv O4(LR)) >= 1/134. These values were independently checked by exact enumeration of every 3^2*2^5=288 deterministic FULL and every 3*2^5=96 seedless LR policy in the rational example. The exhaustive computation checks this finite instance; the all-real classification rests on the analytic proof above.

## Relevance and next question

This completes the one-source-erasing-decision/terminal-only-future subclass. To pursue the R5 mother target (full four-dimensional hull equality but unequal actual images), construct a legal positive-P/Q tree with two interacting decision gates and at least one later LR collision; compare complete deterministic O4 hulls by rational decomposition or a strict Farkas certificate, then attempt semialgebraic nonmembership only on hull-equal candidates. Preserve labeled history, future-relevant residuals, the exact P/Q kernels and free declarations.

Prior art context: Ryan A. Anderson and Guido Montúfar, "The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes," ICML 2026, PMLR 306:2677–2715, https://proceedings.mlr.press/v306/anderson26a.html. That published infinite-horizon memoryless-policy result motivates semialgebraic testing but supplies no proof step above. No external originality determination is claimed.

State: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
