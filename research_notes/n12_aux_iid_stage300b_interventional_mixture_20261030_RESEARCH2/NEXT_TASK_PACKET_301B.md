# Stage301-B — Adaptive interventional mixture minimax and minimal repair state

**Status:** Portable author handoff; `UNREVIEWED / NOT_ADMITTED`. Predecessor Stage300-B (proof, exact Fraction executable, executed stdout) in the Research2 Draft PR continuation. Researcher identity and current native Owner/CLAIM remain to be verified through Source; this packet makes no canonical task publication.

## Frozen mathematical input

Two equal prior hidden sources S=0,1. Initial X is fair and source-independent. At two successive steps the visible-history examiner chooses H or F. Each H yields independent Ber(1/2); each F yields independent Ber(p_S) conditional on persistent S, where p_0=1/4 and p_1=3/4. In fixed FF lexicographic word order, the two source laws are `(9,3,3,1,9,3,3,1)/32`, `(1,3,3,9,1,3,3,9)/32`, and the pooled law is `(5,3,3,5,5,3,3,5)/32`.

Verified Stage300-B: every free causal pooled process uses a policy-independent Bayes posterior; for fixed FF, unrestricted pre-randomized same-Theta conditionally IID triple has sharp pooled TV distance `1/12`, reached by `(1/6)*delta_(1/4)+(2/3)*delta_(1/2)+(1/6)*delta_(3/4)`. For fixed FF the source-labelled source-blind minimax is `1/4` both in free causal and shared-IID classes (different exact rational witnesses). There are 1024 deterministic visible-history adaptive H/F policies, verified by Fraction enumeration. A single F produces pooled uniform three bits, while two F calls expose missing source memory.

## Smallest next mathematical unit

Define one globally consistent physical simulator with a single real Θ sampled once, conditionally IID X and the two future output bits regardless of H/F actions. For the **same** Θ-mixture across all examiner policies, solve

`inf_{mu on [0,1]} sup_{pi} TV(PooledSource^pi, Q_mu^pi)`, and separately

`inf_mu sup_pi (TV(P_0^pi,Q_mu^pi)+TV(P_1^pi,Q_mu^pi))/2`.

Prove whether the supremum may restrict to a small explicit subset of deterministic histories; construct an all-real-μ dual lower certificate and a physical mixture attaining the bound. Any finite parameter scan is evidence only, not an all-real proof. Keep causal action semantics and source tags separate, and do not equate this interface with the source-sensitive intervention it cannot perform.

## Follow-up if minimax closes

Prove a minimal-state repair theorem for a two-slot private J retuning interface, including future observers that can read J, and compare exact strong versus prior-relative quotient conditions. Then test a native P000-X6 path lifting: six signed native axes, ordered unit-axis primitive steps, genuine three-force closure, branch multiplicity, typed time, exact six-field nonnegative address codec, and commuting future observers. Explicitly isolate the external Bernoulli model if no faithful lift exists. Stage278-A Bellman N=12 is independent.

## Evidence / return

Full theorem with quantifiers, permitted strategies, exact outputs and dual certificates; runnable Fraction reproduction and captured stdout; precise Source links and frozen pins; independent reviewer/admission pending. Reuse the Stage300-B 1024-policy test rather than mechanically rerunning it. Return a new scientific increment and its next bounded question; no claim that PR storage is native Result acceptance.
