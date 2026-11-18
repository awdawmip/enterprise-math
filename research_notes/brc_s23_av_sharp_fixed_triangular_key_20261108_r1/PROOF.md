# S23/AV: sharp horizon of a fixed irrational-order integer key and exact unit-key gap multiplicities

Date: 2026-11-08 Asia/Shanghai. Status: author-side exact mathematical derivation plus finite exact-integer regression; independent review pending.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Current parent: PR #1777; prior universal adaptive rank/select (cd1a884b77ed33afc7bac4d03671f6559afa4ded) and the subsequent six/seventh exact plateau studies (including 24c35e02b959409960645753bd2bc8c92147a390).
Observer: two-point S23/AV auxiliary likelihood-sign observer. The joint counts of labels 1 and 4 remain intact; label 3 is padding. These results concern exact ordering of future threshold sets, not a new full S23 mother-model embedding.

## Theorem 1 — sharp fixed-key horizon for the triangular domain

Let r=ln(7)/ln(10/7), P=2074774, D=380295, M=P+D=2455069, and

  T_H = { r*v-j : v,j nonnegative integers, v+j<=H }.

For every integer 0<=H<M, the key

  K(v,j)=P*v-D*j

is injective on the defining triangle and induces EXACTLY the same strict order as the real thresholds, despite H possibly exceeding D. Moreover M-1 is the largest H on which this *unchanged* key can be injective: at H=M the two different points (0,0) and (D,P) share key zero.

Proof. The previously certified rational enclosure (45-term atanh logarithm bounds)

  LO/Q<r<HI/Q,
  Q=10^26, LO=545569623581288298975349314, HI=LO+1,

gives, by integer cross-multiplication,

  gcd(P,D)=1,
  D*max(|LO*D-P*Q|, |HI*D-P*Q|)<Q,
  (LO/Q)*D>P-1.

Thus |rD-P|<1/D and rD>P-1. For any pair x=(v,j), y=(v',j') in the triangular domain, write a=v'-v, b=j'-j. Compare the signs of r*a-b and (P*a-D*b)/D.

If a and b have opposite signs (zero included when the other coordinate is nonzero), their signs plainly agree because r and P/D are positive. If both are negative, swap x,y, reducing to the positive case. For a,b>=0, the triangle condition implies a+b<=H. If 1<=a<D, coprimality makes the integer Z=P*a-D*b nonzero. Since

  D*(r*a-b)=Z+a*(rD-P),     |a*(rD-P)|<1,

the sign is precisely the sign of Z. If a>=D, then b<=H-a<=P-1, and

  r*a-b >=rD-(P-1)>0,   P*a-D*b >=D>0.

The remaining a=0 case is immediate. Hence all distinct pairs are ordered strictly and identically. At H=M, (D,P) belongs to the triangle alongside (0,0) but both have K=0. Their actual thresholds differ by rD-P<0 (confirmed by the enclosure), proving sharpness of the fixed-key injective horizon. QED.

This extends the exact *fixed* (P,D) key from the earlier certified sufficient range H<=380294 to H<=2455068 (6.4557 times the previous maximal H). The adaptive continued-fraction theorem for arbitrary finite H remains valid separately.

## Theorem 2 — complete classification and counts of consecutive key-one gaps

Put u=(79,431), w=(D,P), epsilon=79r-431, eta=P-Dr. The exact enclosure proves 0<eta<epsilon and P*79-D*431=1. For 0<=H<M, *every* adjacent pair of points in T_H with integer-key difference exactly one has displacement precisely one of

  d_+=u=(79,431),               real width epsilon;
  d_-=u-w=(-380216,-2074343),  real width epsilon+eta.

Define A(t)=(t+1)(t+2)/2 for integer t>=0 and A(t)=0 for t<0. The exact number of adjacent bounded pairs of each type is

  C_+(H)=A(H-510),
  C_-(H)=A(H-2454559).

The d_- class first appears at H=2454559. For example, at H=30000,
C_+=434874286, C_-=0; this reproduces the earlier independently generated dominant-class count without traversing any of its 434874286 instances.

Proof. All integer solutions of P*a-D*b=1 are (a,b)=u+t*w for t in Z. If t>=1, both coordinates are positive and a+b>=M+510>H. If t<=-2, both are negative and |a|+|b|>=2M-510>H. The possibilities for a feasible displacement are exactly t=0 and t=-1, with coordinatewise sums 510 and -(M-510), respectively. For an all-positive or all-negative displacement d of coordinatewise length L, feasible translated endpoints in the triangle are counted by the triangular number A(H-L). This proves the two exact counts. By Theorem 1 all integer keys are distinct and preserve the real order; with difference one, no other integer key, hence no other threshold, can lie strictly between such endpoints. Direct evaluation yields widths r*79-431=epsilon and r*(79-D)-(431-P)=epsilon+eta. QED.

At the sharp boundary H=M the fixed key has a collision, so the theorem's strict-key counting contract ends exactly where its stated hypothesis ends. The actual real-valued threshold order remains well-defined by irrationality.

## Corollary — fixed-key random access with the correct lifted inverse

The preceding universal order-statistics work gives an exact floor-sum count C_H(m)=number of integer keys <m in the triangular domain, and binary-search select. The former often used D>H to invert a selected key into (v,j). For the present extended regime D<=H<M, invert without that restriction:

  v0 = (key * P^(-1)) mod D,   0<=v0<D,
  j0 = (P*v0-key)/D,          integer,
  t  = max(0, ceil(-j0/P)),
  (v,j)=(v0+D*t,j0+P*t).

All integer solutions have this form for some t, and t<0 would force v<0. The chosen t is the least nonnegative lift with j>=0. Each later lift increases v+j by M>H, so if the key belongs to T_H exactly this lift is feasible and unique. Thus the earlier floor-sum rank/select formula remains usable with the *same* fixed P,D up to H=2455068, with this inverse-lift correction. No new precision search is needed for these H.

## Verification and next work

VERIFY_TRIANGULAR_KEY.py was executed locally with Python standard-library exact integers. It checks strict rational error bounds, all rank/select/lifts for H=1..90, direct gap-one counts, and selected deterministic rank and coordinate round trips at H=510, 30000, 380294, 380295, 380296, 500000, 1000000, 2454559, and 2455068. The largest triangular domain has 3013683124915 points; only selected random-access queries are executed there, not a full enumeration. RUN_EVIDENCE.txt retains the console result. Theorem 1 and 2 are quantified symbolic proofs; finite tests independently check their arithmetic implementation.

The known subsequent plateau construction extends beyond H=M; this fixed-key theorem explains the precise arithmetic boundary at which the first key collision occurs and supplies closed-form multiplicities for a distinguished gap family in the regime before that transition. Next: replace the collided key by a certified lexicographic pair or the adaptive next convergent, and derive a similarly explicit post-M gap-class count to support exact continuation beyond the seventh plateau. No native task owner/CLAIM or independent scientific review is asserted by this author-side artifact.
