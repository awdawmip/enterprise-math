# Slow structure IV: certified threshold sampling and blockwise return bounds

Progress-Event-ID: slow-certified-sampling-20260928-6f6b1c93
Research-Activity-ID: RA-SLOWSTRUCT-6F6B1C93-D5DF97E7
Researcher-ID: EM-DIRECT-6F6B1C93
Session: local-chatgpt-slowstructure-6f6b1c93 (same local key; not an authenticated platform ID)
Status: AUTHOR_SYMBOLIC_DERIVATION / NOT_ADMITTED / NO_NEW_SCIENTIFIC_EXECUTION
Global read: c48036ef0431c6f6b8f0224dec0995e6c7981a08
Source control read: 69252ec43e972d8f178e51349627b1e00f8a41d7

## 0. Scope and actual reuse

Current user instruction: continue. Retain the three prior checkpoints and the same activity. The fixed scientific predecessor is enterprise-math@051a57aa522aa464ddf27cd27a87e47056e4d16b, research_notes/direct_followups/20260927_slow_carry_filter_6f6b1c93.md. Its predecessor is @6774a6dbfc729f6f7410f6baafaf0b7b3c37e110, research_notes/direct_followups/20260927_slow_correlation_closure_6f6b1c93.md. The source-bound two-arm law remains the package @951cc16cb09635fae9f93230d96030fdaa2035b3.

P000, residual fidelity and ACTUAL_TYPED_BRC_ONLY remain unchanged. This note symbolically composes the actual signed two-arm and two-carry observer interfaces. It executes no native scientific calculation, classical reference, waveform simulation or precision substitution. Reuse: COMPOSE_APPLIED / EXTEND_EXISTING_OBSERVER. Internal residual coordinates, ordered feedback, signed amplitudes and modular-label provenance remain intact. Claims here preserve the specified native bit law, not an independently established ideal-Shor or physical correspondence.

## 1. A less demanding target than a numerical probability

At positive-mass history h, set M=K_h(1,I), C=K_h(p,T). Exact child masses and the next-plus probability are

b_plus=(M+C)/2, b_minus=(M-C)/2,
p_h=b_plus/(b_plus+b_minus)=(M+C)/(2M).

For one independent U uniform on [0,1], the desired output is plus exactly when U<p_h. Equivalently,

C+(1-2U)M>0.                                                     (1)

Thus a certified sign decision suffices: evaluating p_h to a preset precision is not mandatory. This is inverse-transform comparison, not a new general random-sampling principle. U is conceptual; section 3 realizes its needed digits with unbiased bits.

Suppose a certificate gives p_h in [ell,u]. If U<ell, return plus; if U>u, return minus; otherwise refine the same instance. Never discard this U and redraw merely because it was ambiguous. A new independent U is drawn only for the next bit. Every certified early decision is identical to exact threshold comparison, so stopping early adds no statistical bias.

This does not permit erasing future-relevant state. Retain h, ordered source feedback, the query/certificate state and any reusable carrier. A new history may require reconstructing additional observations; that cost is charged.

## 2. Obtain a probability enclosure without trusting a point estimate

Assume sound nonnegative child-mass bounds

0<=l_plus<=b_plus<=u_plus,
0<=l_minus<=b_minus<=u_minus.

Then a valid probability enclosure is

ell=l_plus/(l_plus+u_minus),
u=u_plus/(u_plus+l_minus).                                       (2)

When the first denominator is zero, use ell=0; when the second is zero, use u=1. These are conservative conventions, not claims that the parent has zero mass. Inconsistent bounds are certificate failures and must not be silently repaired.

Proof: x/(x+y) increases with x and decreases with y on the nonnegative quadrant with x+y>0. Subsequent valid intervals may be intersected to make a nested sequence.

If the current random number is itself enclosed by [a,b], decisions can avoid division altogether:

(1-b)l_plus > b*u_minus  implies plus,
(1-a)u_plus < a*l_minus  implies minus.                          (3)

Equation (1) similarly permits direct threshold contraction. Sound bounds on M,C with absolute errors e_M,e_C give a bound e_C+|1-2U|e_M on its threshold expression for fixed U. This does not remove the difficulty of certifying sufficient relative resolution when M is tiny.

## 3. Exact sampling from finite random-bit prefixes

For each h assume an interval procedure I_s(h), s>=1, which terminates and certifies

p_h in I_s(h), width(I_s(h))<=2^(-s).

For the sharp bound below the interval sequence is determined by h and, optionally, a seed independent of the fresh threshold bits. Width and validity must hold for every allowed seed; statistical confidence intervals require the additional error accounting in section 4.

At level s, reveal the first s+2 bits of the same U, giving a dyadic cell Q_s of length delta_s=2^(-s-2). If Q_s lies entirely below I_s return plus, entirely above return minus; otherwise continue. Weak boundary comparisons are valid up to null endpoint events; a strict implementation may simply refine on equality.

For a fixed interval of width w_s, the dyadic cells meeting it have total length at most w_s+2 delta_s. Therefore

Pr(unresolved after s | h) <= (3/2) 2^(-s).                     (4)

Previous stopping can only decrease this event. Its probability tends to zero, so the procedure terminates almost surely and returns exactly Bernoulli(p_h). Repeating with fresh bits at each history gives the exact entire native bit-string law by conditioning and induction.

With R the number of queried refinement levels, tail summation yields

E[R | h] <= 1 + sum_{s>=1}(3/2)2^(-s) = 5/2.                    (5)

The first level reveals three bits and each additional level one more, so expected threshold-bit use is at most 9/2. These count levels and random bits, NOT BRC work, coefficient bits or runtime. Almost-sure termination alone does not imply finite expected runtime.

If the interval construction adapts to the threshold U, sound pathwise bounds still make each certified decision exact. However (4) cannot simply be reused: containment and the width bound only imply |U-p_h|<=w_s+delta_s on ambiguity, hence the conservative bound (5/2)2^(-s). The independent-sequence version is the primary interface here.

## 4. Finite budgets and global error

Stop refinement after S levels. On an unresolved instance use a declared total fallback, not resampling or output-conditioned rejection. Coupling to exact threshold comparison gives single-bit TV error at most (3/2)2^(-S). For t adaptive output bits,

TV(exact native string, capped string) <= min(1,(3t/2)2^(-S)).    (6)

Taking S>=ceil(log2(3t/(2 epsilon))) gives error at most epsilon. Histories impossible under the exact law may use a declared fallback in the capped program; the first-divergence coupling covers them.

More generally use the exact-history-weighted sum of conditional unresolved probabilities. For probabilistic certificates, charge the probability that any requested certificate is unsound. Fixed-sample confidence statements cannot be reused at adaptive stopping without simultaneous coverage or an explicit union bound. A known native-to-ideal discrepancy must be added separately.

## 5. The cost condition, not just a constant number of calls

Let D_s(h) bound the additional charged work of level s given h: actual typed BRC construction/actions, coefficient bit lengths, block certificates, reuse bookkeeping and threshold comparisons. With the independent interval interface,

E[work | h] <= D_1(h) + sum_{s>=2}(3/2)2^(-(s-1))*D_s(h).        (7)

For S-capped sampling stop this sum at S. The full exact expected cost is obtained by weighting each history with its exact prefix mass and summing over rounds. A uniform D_s=poly(n,s), n=ceil(log2 N), is sufficient for polynomial expected exact sampling. This is conditional and is not established for modular-return queries.

For illustration of the condition, if D_s<=A(n)2^(alpha s), the series converges for alpha<1. At finite S the bound grows as O(A(n)S) for alpha=1 and O(A(n)2^((alpha-1)S)) for alpha>1. An exponential first-level cost remains exponential. A constant expected number of refinement calls is not a constant-cost Shor algorithm.

## 6. Feed the sampler with certified blocks, not unverified smoothing

The previous note provides

K_h(g,A)=L^(-2) sum_d J_h(d,A) F_g(d),
F_g(d)=1[c^d=g mod N], L=2^m, |d|<L.

Let L_k^0,L_k^1 denote exactly the prior two-carry linear maps on the pair (X,Y). For a nonnegative digit cylinder

D(u,k)={d=u+2^k v: 0<=v<2^(m-k)}, 0<=u<2^k,

the complete UNFILTERED block sum sum_{d in D(u,k)} J_h(d,A) is computed as follows: use L_j^{u_j} for the fixed low k bits, then L_j^0+L_j^1 for each free high bit, and retain the same final no-overflow contraction. Linearity distributes the product over all free bits, exactly once per d. It still uses m layers and two observer matrices; no commutation is introduced.

This block contraction becomes a filtered contribution if F_g is certified constant on the block. Two sound certificate types use only explicitly available group operations:

* If c^(2^k)=1, then c^d=c^u throughout the block. Equality with g certifies all-one; inequality certifies all-zero.
* Let chi be an actually available, evaluated multiplicative character. If chi(c^(2^k))=1 and chi(c^u)!=chi(g), then F_g is zero throughout the block. No converse is asserted. A character is not supplied for free or evaluated using the unknown order.

Certified zero blocks cost no contraction; certified one blocks use the summed two-carry maps. Mixed blocks are split or retained as bounded remainders. For negative d use the predecessor identity J_h(-d,A)=J_h(d,A^T) and the inverse target g^(-1); count d=0 once. A negative-domain block containing zero subtracts its explicit zero term. Dyadic cylinder cardinality and sum of d have closed integer expressions, so their triangle bounds do not require enumerating addresses.

For ||A||<=1, orthogonality of the actual feedback gives ||alpha_e||=1 and

|J_h(d,A)| <= L-|d|.                                             (8)

Hence any unresolved set R contributes at most

E_R=L^(-2) sum_{d in R}(L-|d|)                                  (9)

in absolute value. This yields sound, although possibly weak, intervals. Resolve more blocks to shrink them; intersect with nonnegative child mass and |C|<=M constraints. Once (3) decides the sample, stop work on that bit, without asserting that unused information is safe to erase for later bits.

## 7. A falsifier for the naive interval provider

Do not hide an exponentially expensive interval oracle behind section 3. The total triangular envelope is

sum_{|d|<L}(L-|d|)=L^2.

If only q individual signed lags have been removed from the unresolved set, each removed envelope term is at most L. The generic remaining-radius certificate therefore satisfies

E_R >= 1-q/L.                                                   (10)

Thus pointwise testing of only poly(m) lags cannot substantially reduce this certificate when L=2^m. To reduce its radius below 1/2 requires q>L/2. This is a bound on THIS triangle-only certificate strategy, not an information-theoretic lower bound on exact/approximate contractions. Known signs, correlated remainders, arithmetic block certificates and direct contrast bounds can do better. Certifying many lags at once is the concrete next target.

## 8. Result and next finite unit

New interface result: sound coarse probability intervals can already give EXACT individual samples; finite random-bit comparison terminates almost surely under geometric refinement, with explicit expected-level, cost and capped-TV bounds. The threshold algorithm retains history and future-relevant provenance. It does not rely on storing a smooth plot.

New connection to the previous carry result: whole low-bit cylinders have exact unfiltered contractions, and explicit constant-mask/character certificates can turn them into cheap filtered contributions. A complete mask need not be constructed first. The triangle-only pointwise variant is quantitatively inadequate.

Remaining scientific implementation: build these block tests and summed carry maps through the unchanged typed BRC backend, then certify interval widths and charged D_s on declared native inputs. No actual runtime, bandwidth theorem, new ideal reference or independent admission is claimed here. The next report should separate number of individual lag queries, number of whole-block certificates, interval width at each level, and complete charged work; a list of level counts alone is insufficient.

## 9. Prior art and read scope

Inverse-transform comparison and exact discrete sampling from fair bits are established methods, not claimed as novel. Devroye and Gravel, Random variate generation using only finitely many unbiased, independently and identically distributed random bits, arXiv:1502.02539: public author abstract/metadata read; full HTML attempt unavailable. No full-paper proof audit claimed. Bravyi, Gosset and Liu, arXiv:2112.08499v2 / PRL 128,220503: public author abstract rechecked; its amplitude-query reduction remains background, not a proof of our block oracle or equation (7).

https://arxiv.org/abs/1502.02539
https://arxiv.org/abs/2112.08499

The task-specific claims are the source-bound compositions and proofs above. Their mathematical review and actual typed execution remain separate.
