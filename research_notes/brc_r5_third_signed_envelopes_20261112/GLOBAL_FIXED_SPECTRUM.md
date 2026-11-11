# R5 — a global exact persistence certificate for all 1,144 fixed capacity phases

Date: 2026-11-12 (Asia/Shanghai). Status: author-side **exact finite theorem** in the immutable external P/Q–BRC Blackwell observer. This is a further consequence of the same frozen 28-rational/15-labeled-atom fixture and is stronger in parameter coverage than the adjacent-chamber classification in RESEARCH.md.

## Theorem (complete admissible parameter interval)

Retain the fixed 15 labeled atom changes `M_a`, original 28-vector `X`, total residual `D`, and observer-preserving perturbation `H`. Let

- `x=X_(target0,source3)=155682221/25142124560000000`;
- `r=eta/x`, `X(r)=X+x*r*H`;
- `epsilon_max=9/115400000`.

The exact largest **closed** parameter interval on which both the initial and complete 15-atom endpoint vectors are nonnegative is

`I=[-427508577031693280/628800490619, 1/23]`.

The negative endpoint is forced by the complete terminal mass at (target 6, source 1), the positive endpoint by the initial mass at (target 1, source 3). The initial state is strictly positive throughout `I` except at its positive endpoint; all terminal states are nonnegative throughout. These constraints are exact affine inequalities in r.

Let the 15 labeled integer weights at exposed coordinate `k0=(target 0, source 3)` be

`w=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)`.

Their finite subset sums run from -1348 to +1348 and take exactly 2293 distinct integer values. The set

`N={-h : h is a subset sum of w, h<=-3}`

has **exactly 1144 elements**, minimum 3 and maximum 1348. For every `n in N`, put

`T_n=36*x/n`.

**Claim.** For every real `r in I` and every `n in N`, there exists a labeled prefix subset `S_n` such that the nonnegativity capacity threshold of that prefix is **exactly** `T_n`. Moreover, `S_n` can be chosen **once per n, independently of r**, and works across the entire interval `I`. Thus the entire set of 1144 fixed first-capacity phases **persists globally** over the full admissible perturbation interval, even though individual winning coordinates of other masks switch as r varies.

This is a persistence statement for the exposed 1144 fixed forms. The complete threshold spectrum at remote r values may additionally contain other moving or newly dominant coordinate forms; identifying them remains a separate question.

## Exact finite proof

Let `P_S=36 sum_(a in S) M_a` be the integral 28-vector for any subset S of the 15 labeled operations. For each n, the certificate selects a mask `S_n` satisfying `P_(S_n)[k0]=-n` and the following **56 exact rational inequalities**:

`X[k] + x*r_-*H[k] + (T_n/36)*P_(S_n)[k] >= 0`

and

`X[k] + x*r_+*H[k] + (T_n/36)*P_(S_n)[k] >= 0`,

for every one of the 28 coordinates k, where `r_-` and `r_+` are the exact endpoints of I.

Every expression is affine in r, so the same 56 inequalities imply nonnegativity of the prefix result at `epsilon=T_n` for **every real r in I**. The initial vector `X(r)` is also nonnegative. Therefore, by linear interpolation in epsilon, the entire prefix path `X(r)+epsilon*P_(S_n)/36` stays nonnegative for `0<=epsilon<=T_n`. Since its k0 mass reaches zero exactly at `T_n` and becomes negative for larger epsilon, the prefix capacity threshold is exactly T_n.

The attached verifier exhaustively constructs the subset-sum set N and enumerates all `2^15-1=32767` nonempty masks. It chooses the first qualifying mask for each n and verifies every endpoint inequality. All **1144** n obtain a witness. This proves the stated universal real-parameter claim with a complete finite rational certificate, without parameter sampling.

Part of the exact witness checksum:

- `n=3`: mask 1050.
- `n=420`: mask 1024.
- `n=910`: mask 30724.
- `n=1348`: mask 31744.
- Sum of the 1144 first qualifying mask IDs: **9,387,630**.
- Minimum and maximum selected mask IDs: **1024** and **32641**.

The checksum is supplementary. The load-bearing evidence is the complete exact Boolean-subset enumeration and endpoint inequality verification in `VERIFY_GLOBAL_FIXED_SPECTRUM.py`.

## Scientific interpretation and limits

The 1144 fixed phase values survive every observer-preserving r for which the initial and complete-ray terminal states are nonnegative. This is stronger than the previously verified local signed minimizer chambers. The same labeled atom decomposition, 28 transport coordinates and frozen observer are preserved. The result does not assert that the fixed phases are the *only* phase values throughout the full interval, does not supply a universal 15-operation connectivity theorem, and does not promote this auxiliary model into native X6 dynamics.

Original science pins: global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`; immutable fixture `435e77af0d180eac32bd1f9c4c464bc4010b7551`. P000 and ACTIVE worldview unchanged. No formal Source Result or independent mathematical review is claimed.

## Reproduction and next question

`VERIFY_GLOBAL_FIXED_SPECTRUM.py` uses the original immutable parent fixture via Python stdlib `runpy` and `fractions.Fraction`. `GLOBAL_FIXED_EXACT_OUTPUT.txt` records a locally executed equivalent independent transcription, including the witness census. The published wrapper requires separate clean-checkout execution from its exact remote bytes.

**Next**: classify which additional (non-fixed) capacity phase forms emerge as r moves far beyond the small local minimizer chambers within the exact admissible interval, and determine the next envelope switches after `r=5/5083` and `r=-1/1633`. Investigate whether the endpoint-witness construction generalizes to other BRC residual decompositions with a fixed exposed coordinate.
