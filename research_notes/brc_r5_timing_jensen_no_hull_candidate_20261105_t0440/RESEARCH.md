# R5 — Timing-only Jensen separation survives arbitrary second-gate compensation

Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Mother R5 target: a lawful positive P/Q BRC with equal complete four-dimensional FULL/LR convex hulls but distinct actual O4 real-behavior sets.
Frozen scientific source pins retained unchanged: Global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e.
Immediate predecessor: research_notes/brc_r5_two_gate_affine_kernel_annihilation_20261105_t0340/RESEARCH.md at 0f5c837ab7ac4bee254aa0969742392e739fbd6c.

## 1. General timing-support theorem

There are finitely many source histories h of positive weights w_h (sum 1). Their time-1 likelihood ratio is 1. The time-2 likelihood ratios are r=(1/2,1,3/2), and the strictly positive Q kernel from source h is

K_h=(k_h,1-2k_h,k_h), 0<k_h<1/2.

Its P kernel is r_j K_h(j), which has total 1. At time 1 and each time-2 node, STOP with free P/Q declaration or CONTINUE is allowed. Continuing at time 2 reaches a terminal time-3 node, with any strictly positive lawful P/Q kernel M_hj to terminal likelihood ratios, followed by a free P/Q declaration. FULL sees source h; seedless LR only sees (time,likelihood ratio). The declared O4 is (eP,eQ,TP,TQ).

Let u>0, v>0 and consider the O4 support normal n=(0,0,-u,v). Define kbar=sum_h w_h k_h and

t=v/u=(1+kbar/2)/(1+kbar) in (1/2,1).

Then the EXACT convex-hull support gap is

h_FULL(n)-h_LR(n)
 = [u/(4(1+kbar))] * sum_h w_h |k_h-kbar|.                 (T)

Consequently full four-dimensional hull equality for this family REQUIRES all k_h equal. If at least two k_h differ, FULL and LR are strictly separated, regardless of any lawful positive continuation kernels M_hj and regardless of terminal declaration freedom. This is a necessary condition within the declared family; k_h equality by itself is not asserted sufficient for FULL/LR four-dimensional equality.

## 2. Proof for every real behavioral strategy

For a fixed n, declarations never change the timing reward, so replace either STOP/P or STOP/Q by STOP for this support calculation. A time-1 STOP has weighted reward (v-u). A time-1 CONTINUE adds one timing unit (v-u), and at time 2 the optimized additional timing reward from CONTINUE at key r_j is (v-u r_j)_+ times its Q occupancy. No possible time-3 action alters that reward: time 3 is terminal and both declarations have identical timing. Random behavioral actions cannot improve a linear support function over deterministic actions.

Define G_h=sum_j K_h(j)(v-u r_j)_+ and z_h=v-u+G_h. The unrestricted FULL and the source-blind LR support functions are exactly

h_FULL(n)=(v-u)+sum_h w_h (z_h)_+,
h_LR(n)=(v-u)+(sum_h w_h z_h)_+.

The second expression follows because at time 1 LR chooses one common CONTINUE probability, and at time 2 it may freely choose by r_j. Since t in (1/2,1), only j with r_j=1/2 contributes, hence G_h=u k_h(t-1/2). Elementary substitution gives

z_h=[u/(2(1+kbar))]*(k_h-kbar), and sum_h w_h z_h=0.

Therefore the gap equals sum_h w_h(z_h)_+ = [u/(4(1+kbar))] sum_h w_h |k_h-kbar|, establishing (T), including all-real random strategies and arbitrary second-gate transition kernels. QED.

The carried BRC state retains positive source-labeled Q/P path masses and likelihood-ratio keys. The signed support difference is an observer diagnostic; it is not an individual negative branch probability. The proof does not equate equality for one policy under an affine-kernel compression with equality of full policy-image hulls.

## 3. Exact lawful candidate and certificate

Reuse the previous strictly positive source kernel:

w_A=w_B=1/2,
K_A=(1/4,1/2,1/4), K_B=(5/16,6/16,5/16),
r=(1/2,1,3/2).

Use either the original affine second kernel at terminal ratios s=(1/8,1,15/8),

M=(1/56)*[[37,14,5],[21,14,21],[5,14,37]],

or the lawful nonaffine perturbation M' with its middle row changed by (1,-2,1)/56. Both have every entry strictly positive, unit Q row sums and P moments r_j. They are immaterial to the timing support.

Here kbar=9/32. Take u=82 and v=73. The two source timing threshold margins are z_A=-1, z_B=+1. Hence

h_FULL(0,0,-82,73)=-17/2,
h_LR(0,0,-82,73)=-9,
gap=1/2.

A realizable FULL strategy STOPs at t=1 on source A; on source B it CONTINUEs to t=2 and CONTINUEs again only for key r=1/2 (else STOPs). Declare P whenever stopping. This has

W=(eP,eQ,TP,TQ)=(0,1,101/64,53/32).

Its support value is -17/2. Every seedless LR strategy, even randomized, obeys n.O4<=-9, so

W not in conv(O4(LR)),
dist_infinity(W,conv(O4(LR))) >= (1/2)/(82+73)=1/310.

The inequality is exact, not a floating hull approximation. The candidate family is therefore ruled out as a mother-R5 hull-equality example, even though the predecessor exhibited a nonzero source-covariance residual that a particular common affine continuation kernel annihilated in a particular policy.

## 4. Verification and relevance

VERIFY.py implements fully independent exact Fraction enumeration of 256 FULL binary STOP/CONTINUE schedules (2^2 first-gate patterns times 2^6 time-2 patterns), and 16 seedless LR schedule encodings (9 distinct effective schedules). It checks their exact support maxima, the analytic z values, the explicit four-dimensional witness, distance bound, and strict P/Q kernel normalization for both affine and nonaffine M. EXACT_OUTPUT.txt is the locally executed output. The general theorem is proved above; the enumeration is only the fixed rational case.

This is a genuine no-go for a specific lawful family, not a negative conclusion about every BRC or every possible R5 topology. It advances R5 candidate selection by replacing an inconclusive single-policy residual-annihilation test with a complete-convex-hull necessary condition.

## 5. Next unit

Search for a lawful positive finite BRC in which all source histories sharing an early time/LR key have equal timing-threshold values (the timing Jensen obstruction is zero), yet a later coupled observer retains a nontrivial non-linear actual-image residual. Check ALL four O4 coordinates and exact hull equality first, then semialgebraic nonmembership of a FULL real-behavior point. Alternative route: study whether full equality of timing Jensen profiles across ALL early control keys implies an exact finite state aggregator under restricted future kernels. Do not modify P000, ACTIVE worldview or frozen scientific pins.