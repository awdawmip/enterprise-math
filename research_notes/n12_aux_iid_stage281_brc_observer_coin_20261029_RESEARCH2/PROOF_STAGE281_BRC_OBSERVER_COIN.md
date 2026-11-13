# Stage281-B — Exact observer-optimal source-fiber coins versus Stage279 action-mass coins

Author proof (2026-10-29); PORTABLE_AUTHOR_PROOF / EXACT_FINITE_WITNESSES / UNREVIEWED / NOT_ADMITTED. Parent Stage280-B commit 2809951a5d8ef1e903b77157b051d42f7aae1814. External finite positive-rational ordered-history BRC, not native-X6 dynamics or physical assertion. Global read main 314ff1ecb8d348f87f9d97f51570d65256705595; project main b519a46c64db7b40581b618e67a3467cc40a542f.

## Model

Let C={h1,h2} be a depth-homogeneous ordered-history fiber, with strictly positive source reaching masses mu_P=(a,b), mu_Q=(c,d). Original action-1 probabilities are f=(f1,f2) in [0,1]^2. A compressed, source-blind policy chooses common coin x in [0,1]. The Stage279-B source-indexed local action-mass error is

  A(x)=max(|a f1+b f2-(a+b)x|, |c f1+d f2-(c+d)x|).

Declare a bounded source-indexed future observer with conditional action-1 versus action-0 continuation contrasts D_P=(1,0) and D_Q=(0,1), e.g., terminal reward 1 for action 1 at h1 only under P and at h2 only under Q. Source is used to evaluate expectations; quotient coin x never observes it. For THIS observer the actual distortion is

  O(x)=max(a|f1-x|, d|f2-x|).

The observer is explicitly source-indexed, not assumed common to all sources; policy and state carrier remain shared.

## Theorem

For any positive real a,b,c,d and f1,f2 in [0,1], write T=a+b+c+d. Exact minimax coins and observer value are

  x_A=((a+c)f1+(b+d)f2)/T;
  x_O=(a f1+d f2)/(a+d);
  min_{x in [0,1]} O(x)=ad|f1-f2|/(a+d).

Both are legal, and each minimizes its OWN risk (A or O, respectively). Their equality criterion and difference identity are

  x_A=x_O iff [ f1=f2 OR ab=cd ];
  x_A-x_O = (cd-ab)(f1-f2)/[T(a+d)].

In particular, for f1>f2, the exact observer excess from using the Stage279 action coin instead of the observer coin is

  O(x_A)-O(x_O)
   = a(x_O-x_A) if x_A<x_O;
   = d(x_A-x_O) if x_A>x_O;
   = 0 if x_A=x_O.

If f2>f1, interchange coefficients a,d in the two strict cases. Thus ab!=cd and f1!=f2 give strictly positive observer excess, with the displayed rational amount for rational inputs.

PROOF: Put wP=a+b, wQ=c+d and uP=(af1+bf2)/wP, uQ=(cf1+df2)/wQ. A(x)=max(wP|uP-x|,wQ|uQ-x|) is convex and minimized where weighted errors on the opposite sides balance, giving x_A=(wP uP+wQ uQ)/(wP+wQ); if uP=uQ the same formula gives the common zero-error coin. Likewise O(x)=max(a|f1-x|,d|f2-x|) balances at x_O=(af1+df2)/(a+d), with minimum ad|f1-f2|/(a+d). These coins are convex combinations of f1,f2, so belong to [0,1]. Subtracting and cancelling shows x_A-x_O=(cd-ab)(f1-f2)/[T(a+d)], proving the iff. For f1>f2, on [f2,x_O] the dominating term of O is a(f1-x) and on [x_O,f1] it is d(x-f2); taking differences at x_A yields the stated excess. If f2>f1 the slopes swap. QED.

## Exact symmetric case and strict counterexample

The Stage281 input originally proposed source masses P=(1/4,1/8), Q=(1/8,1/4) and f=(1,0). Here ab=cd=1/32, so x_A=x_O=1/2; the input demonstrates the equality criterion rather than a strict gap.

For positive source masses mu_P=(1/4,1/8), mu_Q=(1/8,1/8) and f=(1,0), x_A=3/5 and x_O=2/3. Exact observer risks are O(x_A)=1/10, O(x_O)=1/12, an excess of 1/60. Source masses extend to full positive four-word probability laws, e.g. P(00,01,10,11)=(1/4,1/4,1/8,3/8), Q=(1/4,1/8,1/8,1/2), so these are genuine reaching distributions rather than impossible source normalizations.

The executed Python standard-library Fraction verifier checks all 3^4=81 combinations of strictly positive masses from {1/8,1/4,3/8}, each of four deterministic original policies (324 cases), including both risk inequalities against 17 additional rational coins. It checks the algebraic difference identity, iff criterion, symmetric input, strict 1/60 gap. The exact output ends STAGE281_BRC_OBSERVER_COIN_EXACT_PASS. The general theorem follows from the proof, not from extrapolating 324 finite tests. Independent scientific review, native CLAIM/Result and formal proof checker are separate obligations.

## Successor

Stage282-B: two causally ordered fibers with source-dependent reaching masses, where early compressed coins affect later path occupancy. Solve a global observer-optimal two-coin problem or produce an exact obstruction, retaining mixed terms; specify a typed X6+time/port bridge before any native claim. Stage278-A N=12 Bellman next face is independently open. P000 / ACTIVE worldview unchanged.
