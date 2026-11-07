# S23/AV: exact bounded-future sign observer capacity

Status: AUTHOR_SIDE_PROOF, exact arithmetic examples; 2026-11-07.
Use the same frozen lawful θ₀, θ₁ and likelihood Λ(k,ell)=7^ell(7/10)^k as the companion PROOF.md. This supplement establishes a second theorem: allowing a bounded suffix radically changes the exact minimal observer state capacity.

## Definition

For each prefix length n and allowed future horizon h≥0, define S(n,h) as the smallest number of deterministic states that permits correct sign(P₀(wu)-P₁(wu)) for every full-label length-n prefix w and every future suffix u of length at most h, where the suffix itself is supplied unchanged.

The suffix likelihoods form M_h={(7/10)^k 7^ell: k,ell≥0, k+ell≤h}; by unique factorization, |M_h|=C(h+2,2). For each possible suffix likelihood R, its sign test is the threshold comparison Λ(w) vs 1/R.

## Theorem (finite-h exact quotient)

For every n,h, the minimal observer identifies prefixes exactly when their sign vectors

    (sign(Λ(w)R-1))_{R∈M_h}

are equal. All thresholds 1/R are distinct. No prefix likelihood can equal a threshold other than 1: equality would imply Λ(wu)=1, and unique prime factorization forces both w,u to contain no labels 1 or 4. Thus the prefix all-3 class at Λ=1 is the sole equality class. The remaining optimal classes correspond to the open intervals of R_+ cut by the M=C(h+2,2) distinct thresholds that actually contain an attainable length-n prefix likelihood.

Consequently

    S(n,h) ≤ min(C(n+2,2), C(h+2,2)+2).

For each fixed h there is a finite N(h) such that

    S(n,h)=C(h+2,2)+2 for all n≥N(h).

For each fixed n there is a finite H(n) such that

    S(n,h)=C(n+2,2) for all h≥H(n).

### Proof

Sufficiency of the sign-vector partition follows because each suffix determines one coordinate of that vector; necessity follows because differing vectors have a suffix at which signs differ, so merged prefixes could not both be decoded correctly. Injectivity of (k,ell)↦Λ gives |M_h| as stated.

If Λ(w)R=1, then Λ(wu)=1. The unique-factorization argument from PROOF.md gives total counts k(wu)=ell(wu)=0, so w,u both use only label 3 and Λ(w)=R=1. No other threshold is exactly attained. Each of the M+1 open intervals between the M thresholds gives one signature when occupied by some prefix, plus the equality class at 1. The two upper bounds follow.

The set of prefix likelihoods realized over all lengths is dense in (0,∞) by the signed logarithmic irrational-rotation argument in PROOF.md. For a fixed h there are finitely many nonempty open threshold intervals; choose one finite-length prefix realizing a likelihood in each interval. Padding all choices with label 3 leaves ratios unchanged and extends them to any common length n≥N(h), showing every interval is occupied. Hence the upper bound M+2 is eventually attained. For fixed n, only finitely many distinct count-pair likelihoods exist; each distinct pair is separated by a finite suffix as proved in PROOF.md. Taking the maximum of finitely many separating suffix lengths yields H(n). QED.

## Sharp one-step result

For h=1, the suffix thresholds are 1/7, 1, and 10/7. There are five possible optimal classes: (0,1/7), (1/7,1), {1}, (1,10/7), (10/7,∞).

At n=0, only the all-3 (empty prefix) class is present: S(0,1)=1. At 1≤n≤5 the extreme small-likelihood interval is empty because (7/10)^n≥(7/10)^5>1/7, and the near-positive interval (1,10/7) is empty: if ell≥1 then Λ(k,ell)≥7(7/10)^(n-1)≥7(7/10)^4>10/7. The other three classes are realized by all-1, all-3 and all-4 prefixes. At n≥6 all five classes are realized by padding the following six-symbol representatives with 3s: 111111 gives Λ=(7/10)^6<1/7; 133333 gives Λ=7/10 in (1/7,1); 333333 gives Λ=1; 111114 gives Λ=117649/100000 in (1,10/7); 433333 gives Λ=7>10/7. Thus the exact closed form is

    S(n,1)=1 for n=0;  S(n,1)=3 for 1≤n≤5;  S(n,1)=5 for n≥6.

This isolates n=6 as the first prefix length where exact one-future-step observation requires more than the current likelihood sign alone.

## Exact evidence and next work

VERIFY_FINITE_H.py executes pure Fraction arithmetic. It verifies the one-step formula at n=0..30, and finds the smallest h for full-future-state saturation at n=1..7 as H(n)=(0,6,11,17,22,28,33). For h=0..4 it checks eventual maximal interval occupancy at N(h)=(1,6,11,17,22). RUN_FINITE_H.txt is the executed stdout. Analytical all-(n,h) conclusions use the threshold-partition proof; finite calculations are regression evidence.

Open: determine a closed-form or controlled bound for N(h), H(n). The observed N(h)=floor(h ln 7/ln(10/7))+1 for tested h=1..10 is a computational conjecture, not established by this theorem. Mother-model transfer and the full-lawful δ₄ minimax question remain separate.
