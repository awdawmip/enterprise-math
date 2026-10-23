# N32 companion theorem: an absorbing non-gain region after two action-2 pulses

STATUS: AUTHOR-SIDE PROOF ONLY; not a Research Driver verdict, formal Task
Result, accepted Foundation theorem, or native P000 X6 statement.
Date: 2026-10-23. This companion uses exactly the N31 four-label
independent positive-mass occupancy observer.

## Exact two-count law

For z in [0,1], action 0 outputs labels (1,2,3) with probabilities
a=(1+z)/3, b=(1-z)/3, c=1/3; action 2 outputs (0,1,3)
uniformly. The good occupied-label sets are
G={{0,1},{1,2},{1,3},{2,3}}. Let delta_t=P(D_t in G).

For any nonadaptive word over {0,2} with s>=1 zero actions
and r>=1 action-2 pulses, all outputs are independent, hence delta_t
depends on counts, not order. Define F_(s,r)=delta_t; exact formula:

  3^r F_(s,r)=(2^r-3)a^s+2^r(a+c)^s+(a+b)^s+(b+c)^s-2c^s.   (1)

Proof by disjoint occupancy cases:
G={0,1}: a^s((2/3)^r-(1/3)^r);
G={1,2}: 3^(-r)((a+b)^s-a^s);
G={1,3}: (a+c)^s(2/3)^r-3^(-r)(a^s+c^s);
G={2,3}: 3^(-r)((b+c)^s-c^s).
Their sum is (1). At s=0 this calculation requires a separate
boundary treatment. The count quotient is safe for the final occupancy
probability, NOT the order-sensitive prefix history/maxima of R_t.

Put A=a^s+(a+c)^s>0 and
B=(a+b)^s+(b+c)^s-3a^s-2c^s.
Then F_(s,r)=(2/3)^r A+(1/3)^r B.

## Theorem A: adding a second/later action 2 never increases success

For s>=1,r>=1 and all z in [0,1], exact subtraction yields

  F_(s,r+1)-F_(s,r)=-(2^r A+2B)/3^(r+1) <=0.            (2)

Equality is possible only when r=1,s=1,z=1.
Indeed A+B=(a+c)^s+(a+b)^s+(b+c)^s-2a^s-2c^s.
For s=1 this equals 2b>=0, with equality only z=1.
For s>=2, (a+c)/a=(2+z)/(1+z)>=3/2, so
(a+c)^s>2a^s; moreover (a+b)^s=(2c)^s>=2c^s.
Thus A+B>0. Finally
2^r A+2B=2(A+B)+(2^r-2)A>=0 with the stated equality case.

For r>=2, the strict quantitative version is

  F_(s,r+1)-F_(s,r) <= -4/3^(r+s+1)<0.                (3)

Proof: 2^r A+2B>=4A+2B
=-2a^s+4(a+c)^s+2(a+b)^s+2(b+c)^s-4c^s.
Using (a+c)^s>=a^s>=c^s,
(a+b)^s=(2c)^s>=2c^s for s>=1,
and (b+c)^s>=c^s, gives 4A+2B>=4c^s.

## Theorem B: adding action 0 with two or more pulses is strictly negative

For every s>=1, r>=2, z in [0,1],

  F_(s+1,r)-F_(s,r) <= -1/3^(r+s+1)<0.                (4)

By (1), multiplication by 3^r gives the difference

 -(2^r-3)(1-a)a^s
 -2^r(1-a-c)(a+c)^s
 -(1-a-b)(a+b)^s
 -(1-b-c)(b+c)^s
 +2(1-c)c^s.

The last positive term is (4/3)c^s. The first, third and fourth
negative magnitudes are respectively at least
(1/3)c^s, (2/3)c^s and (2/3)c^s. For the fourth,
(1-b-c)(b+c)^s=a(b+c)^s
>=((1+z)(2-z)/3)c^s>=(2/3)c^s because
(1+z)(2-z)=2+z-z^2>=2 on [0,1].
The three negative magnitudes sum to at least (5/3)c^s; the
second term is nonpositive. Hence 3^r*delta<=-c^s/3,
proving (4).

## Structural consequence for residual growth

Take any nonadaptive {0,2} word with at least one action 0
BEFORE the second occurrence of action 2. The second pulse has
delta_t-delta_(t-1)<=0 by (2), and every later action 0 or 2
has delta_t-delta_(t-1)<0 by (3) and (4), because the counts
remain s>=1 and r>=2.

For M_t=max_(0<=j<=t)delta_j and
R_t=sum_(j=2..t)[delta_j-delta_(j-1)]_+-M_t,
a nonpositive delta increment implies BOTH the positive-part
contribution and the increment in M are zero. Therefore:

  R_t-R_(t-1)=0 at the second action-2 pulse and ALL later rounds
  of any such {0,2} word, for ALL z in [0,1].                   (5)

This is an all-round non-single-pulse analytic extension. It does not
establish a result for action 1 or action 3, for s=0 boundary histories,
or for native six-dimensional X6 dynamics. It does not decide global
all-strategy second-rebound length L_min. One must retain pulse
placement/prefix history when applying the R observer.

## Independent author-side exact checking

A stdlib Fraction/16-state occupancy-mask checker was actually run:
384 exact (z,s,r) formula/DP agreements; 320 action-0 margin checks;
320 action-2 margin checks; and 726 exact word-order permutations.
All passed. This finite evidence complements, not replaces,
the universally quantified algebraic derivations.

Sources: fixed global canonical main
7a56e3a5a31c6af97f47a09befb54ae4443c9b41 and EM source main
f768a9f34aa7b0a9521325c52e0638dc7fba0a27.
N31 author dependency at b70c8cf71b9557569da66eddf44ebdd4057d082c.
em_control_tasks=CONTROL_QUOTA; em_session_start=
STATIC_READONLY_SCOPE_DENIED with operation_sent=false.
Owner/CLAIM/Review/admission remain unverified.

Next research unit: introduce one action 1 or 3 into the post-second
pulse carrier and find an exact revival or a sufficient invariant.
Keep branch-identity and temporal-history semantics separate.
