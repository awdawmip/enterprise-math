# EC49FTN addendum — exact C-infinity positive-prior counterexample beyond exponential tilts

Date: 2026-11-19. AUTHOR_PROVED / EXACT_FRACTION_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED.

This is a complementary proposition to EC49FTN_EXPONENTIAL_PRICE_PRIOR_STOCHASTIC_ORDER_PROOF.md on the same original-index frozen BRC16943 affine Bellman parent. It proves that the preceding theorem's universal stochastic-order assertion cannot be extended to all independent strictly positive smooth external price priors. It does not modify native observer profiles, the frozen science pin, the parent Bellman tree, P000 or formal project ownership.

## Model and explicit smooth prior

Use the same external price rectangle A=[3/4,49/64], B=[7/16,57/128], the original optimized exchange-gap M and optimizer Z, and the previously proved inverse affine map

b(m,z)=1/27-m/54+(10/9)z.

Choose a to be uniform on A, independently of b. Put

s0=441/1000, s1=442/1000, c=1/20.
h(b)=exp(-1/((b-s0)*(s1-b))) for s0<b<s1, and 0 otherwise.
I=integral_[s0,s1] h(b) db > 0.
g(b)=[1+c*h(b)/I]/[(57/128-7/16)+c] for b in B.

The standard flat-bump construction h is C-infinity on the whole real line, with all derivatives zero at s0,s1. Therefore g is a strictly positive C-infinity probability density on B. It is not an exponential tilt. Its entire additional mass relative to Lebesgue density 1 is exactly c on [s0,s1], by definition of I; the unknown transcendental value of I does not enter any calculations below. This defines a fully explicit independent price design and is not a limit-only existence assertion.

## Exact failure of first-order stochastic monotonicity

Let

m_lo=5767/256, m_hi=11611/512, and t=950309/1280000.

Both m values lie strictly in (11457/512,1461/64), where the inherited uniform-prior support formula is

L(m)=(4m+2647)/3696, U(m)=(64m+1411)/3840.

For each fixed m in this strip, the change of variable b=b(m,z) has constant positive derivative db/dz=10/9 and uniform a density, so the conditional Z law is exactly the normalized g-weight on the b-interval [b(m,L(m)), b(m,U(m))].

Direct rational evaluation gives

b(m_lo,L(m_lo))=85/192,
b(m_hi,L(m_hi))=169/384,
b(m_lo,U(m_lo))=b(m_hi,U(m_hi))=57/128,
b(m_hi,t)=s1.

The exact ordered geometry is

169/384 < 441/1000 < 442/1000 < 85/192 < 57/128,

and both L(m_lo)<t<U(m_lo) and L(m_hi)<t<U(m_hi).

Thus the low-m conditional b-fiber excludes the bump entirely, and its conditional CDF at t is

F_lo(t)=(t-L(m_lo))/(U(m_lo)-L(m_lo))=7177/9000.

The high-m conditional b-fiber contains the entire bump below its threshold b(m_hi,t)=s1, so its conditional CDF at that same t is

F_hi(t)= [(s1-169/384)+c]/[(57/128-169/384)+c]=47/50.

Consequently

F_hi(t)-F_lo(t)=47/50-7177/9000=1283/9000 > 0.

But m_lo<m_hi, and first-order stochastic increase would require F_hi(t)<=F_lo(t) at every threshold t. This explicit exact inequality refutes the all-independent-smooth-positive-price-priors extension of the EC49FTM conditional stochastic-order theorem.

## Verification and scientific meaning

The attached EC49FTN_SMOOTH_PRIOR_COUNTEREXAMPLE_VERIFY.py uses only Python Fraction arithmetic: it checks the domain, both source-fiber intervals, the threshold mapping and both conditional probabilities, including the exact rational difference. The corresponding actual execution log is preserved. Evaluating or approximating I is unnecessary; it cancels exactly by construction. This is an exact counterexample on the inherited affine-price BRC optimality region, not a new native Bellman computation and not a physical-state probability assertion.

Together with the positive exponential-tilt theorem, this yields a mathematically sharp *qualitative* distinction: a two-parameter family of nonuniform priors preserves conditional monotonicity for all real tilt parameters, while smooth positive priors in general may destroy it. A maximal analytic condition remains open; a promising next question is a total-positivity or monotone-likelihood-ratio condition for the pushed-forward joint density including the clipping boundary atom.

Native Bellman parent: PR #2774; conditional-law parent: PR #2783; same frozen input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. No formal CLAIM, Result, Review or Activity write is claimed.
