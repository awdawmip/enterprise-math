# PREFIX-590-R2 — Universal two-positive-channel linear lift for native-to-dual BRC endpoints

2026-11-08. AUTHOR-SIDE EXACT DERIVATION / EXECUTED INTEGER-RATIONAL CERTIFICATE / UNREVIEWED.

Parent science frozen at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Direct predecessor PREFIX-589-R2 at research commit c2386fcd4543db72d92422e6f4d5ace054d61549, PR #1797. The original native phase, source-axis, branch and gate semantics remain intact: 96 native ports, 576 tagged edges. The dual positive operator T=W^-1 A W uses the PREFIX-589 reversed-phase formula and 24 four-port blocks W_g=J4-I4.

## Theorem 590.1 — A universal positive linear two-channel lift

For each four-port block,

    W_g^-1 = J4/3 - I4 = (J4-I4)/3 - (2/3)I4.

Consequently, the entire 96×96 inverse is the difference of two fixed nonnegative matrices

    W^-1 = P-Q,   P = W/3 >= 0,   Q = (2/3)I >= 0.

Unlike the endpoint-specific uniform buffer PREFIX-589.3, this splitting is linear, input-independent and valid simultaneously for every original endpoint r>=0:

    W^-1 r = Pr - Qr,  Pr>=0, Qr>=0.

The positive part P sends every original singleton basis vector to the other three ports of its four-port group with coefficients 1/3; the negative part Q sends it to its own port with coefficient 2/3. Every singleton therefore uses one nonnegative positive channel with three supported ports and one nonnegative negative channel with one supported port. For any nonnegative r,

    sum(Pr)=sum(r),     sum(Qr)=(2/3)sum(r).

Entrywise optimality within fixed linear nonnegative splits: if P',Q' are any other entrywise nonnegative matrices with P'-Q'=W^-1, then P'>=P and Q'>=Q entrywise. Proof is independent in each matrix entry: a positive difference c demands P'>=c, whereas a negative difference -c demands Q'>=c. This uniquely determines the coordinatewise least split P=max(W^-1,0), Q=max(-W^-1,0). No new observer, physical positivity or unrecorded BRC factor has been assumed.

## Theorem 590.2 — Exact weighted path recovery via two positive streams

Let T_k=W^-1 A_k W, where every A_k is any nonnegative original six-axis/gate weighted native BRC step and T_k>=0 by PREFIX-588/589. For arbitrary original nonnegative input r and nonnegative output query l, put

    r_+ = Pr,       r_- = Qr,       l_* = W^T l >= 0.

Then for every finite horizon n and independently varying native weights,

    l^T A_n ... A_1 r
      = l_*^T T_n ... T_1 r_+
        - l_*^T T_n ... T_1 r_-.

Both terms on the right are sums of nonnegative dual-carrier path weights; the signed subtraction is explicit and essential. Proof: substitute A_k=W T_k W^-1, telescope, and insert W^-1r=Pr-Qr. The identity is polynomial/rational exact, retains all six original axis and gate variables and does not identify different original port histories.

The formula is a positive-only execution interface with two channels and an explicit final signed observer; it is not a single-channel stochastic conjugacy. For a general original r the direct dual state W^-1r may contain negative entries.

## Cost and relevance

The P-channel has exactly three nonzeros per column, the Q-channel one. Both can be prepared in O(96) scalar operations with one division-by-three per block or fixed-coefficient arithmetic; W^T l uses the existing three-support transform. Direct full dual evaluation of both streams takes at most 2×576 labelled weighted edge contributions per step, compared with the original single-channel 576 per step. Exact rational bit growth and potential cancellation remain part of the cost. Thus the new method is a universal local positive representation and provenance-preserving decomposition, not an algorithmic speedup claim. For multiple queries, streams may be shared according to the actual query shape, which needs a separate benchmark and solver design.

## Evidence, limits, next question

Companion standard-library code PREFIX590_R2_two_positive_channel_certificate.py imports the co-located author-side PREFIX-589 certificate data (native 48 phases/96 ports/576 labelled transitions), verifies the fixed exact decomposition across all 96×96 entries, all 96 singleton supports and signs, positivity and sharp constants, and equality of the recovered nonstationary scalar path observation for three nonnegative original boundaries over a length-three sequence of independently weighted native steps. Result: ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED. The universal identity is proved algebraically, not inferred from finite samples. Full native project import path and independent Driver review remain pending.

BRC reuse: COMPOSE_APPLIED / EXTEND_EXISTING_TOOL. Next PREFIX-591: compare shared positive streams against single-pass original state propagation for batched conditional queries with actual input/output recovery and exact arithmetic costs; test whether a suitable restricted query family benefits from the dual transition structure. Preserve signed cancellation and all native source/branch/gate observers.

Control: formal Source identity/active Owner/CLAIM/Native Result not established; GitHub author-side branch persistence does not grant mathematical admission.