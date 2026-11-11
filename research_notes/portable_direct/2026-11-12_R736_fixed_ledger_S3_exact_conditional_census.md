# R736 — Exact named-S3 census and exponential conditional mixing in a fixed BRC ledger

Date: 2026-11-12 (Asia/Shanghai). Author-side mathematical derivation and exact integer verification; independent review pending.

Mother Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5, unchanged). Direct predecessor: R735, commit dedb2aee4c7a55ca6c68b53f823efdcb7921f9fd (following R734 at 368f50c86c77451822d6e6b649535d297abcff25).

## Domain and observer

Work *inside the explicit rooted three-step CNB/V17 free submonoid* constructed for both 15-arc carriers A and B in R735. Its three distinguishable legal length-three rooted excursions have slot holonomies I, p, q, where p and q are distinct transpositions in S3. R735 establishes that the complete directed-arc count N and, independently, the pooled twelve-counter four-port/two-PASS ledger Y recover the triple (c,a,b) of generator counts *within this submonoid*. All orderings of c I-returns, a p-returns and b q-returns are legal, with distinct source histories. Each such history has length 3(c+a+b).

The question is the *number* of ordered branch histories producing each **named final S3 holonomy**, conditional on the same ledger, not merely which holonomies are accessible. It is a positive integer BRC word-count theorem. Other histories in the ambient 15-arc carrier are not part of this conditional census. No P000 Cell, native signed-force, phase or physical-time realization is assumed.

## Theorem 1 — exact named-holonomy census for every ledger triple

For all a,b,c >= 0 define B=binom(a+b,a), J=binom(a+b+c,c) and

$$s_{i,j}=[x^iy^j](1-x^2-y^2+xy)^{-1},\quad s_{i,j}=0\ \text{when }i<0\text{ or }j<0.$$

These are exact integers, computable from s(0,0)=1 and, away from (0,0),

$$s_{i,j}=s_{i-2,j}+s_{i,j-2}-s_{i-1,j-1}.$$

Let H(a,b;g) count the ordered P/Q words of multiplicities a,b with product g in S3. Set r=pq (one three-cycle), so r^2=qp.

When a+b is even:

$$\boxed{H(a,b;1)=(B+2s_{a,b})/3,\qquad H(a,b;r)=H(a,b;r^2)=(B-s_{a,b})/3.}$$

All odd permutations have count zero.

When a+b is odd, set t=pqp=qpq, u=s(a-1,b), v=s(a,b-1). Then:

$$\boxed{H(a,b;p)=(B+2u-v)/3,\quad H(a,b;q)=(B-u+2v)/3,\quad H(a,b;t)=(B-u-v)/3.}$$

All even permutations have count zero. For a complete fixed (c,a,b) three-generator ledger, multiply each displayed count by J to account for every order-preserving insertion of c identity-return blocks. All formulas are integral, include zero-count boundary cases, and hold at every history length.

**Proof.** Let rho be the ordinary 2D irreducible representation of S3, and A=rho(p), D=rho(q). A^2=D^2=I and AD+DA=-I. An integral model is A=[[0,1],[1,0]], D=[[1,0],[-1,-1]]. As formal bivariate power series,

$$(I-xA-yD)^{-1}=(I+xA+yD)/(1-x^2-y^2+xy).$$

The coefficient of x^a y^b on the left is the exact sum of standard-representation matrices for *every ordered P/Q word* with these counts. Its coefficient on the right is s(a,b)I for even a+b, and s(a-1,b)A+s(a,b-1)D for odd a+b.

The same words contribute B in the trivial representation and (-1)^(a+b) B in the sign representation. Orthogonality of the six irreducible characters (regular-representation inversion) gives, for each g in S3,

$$H(a,b;g)=\frac{B+(-1)^{a+b}\operatorname{sgn}(g)B+2\operatorname{tr}(\rho(g^{-1})M_{a,b})}{6}.$$

In even degree the possible traces are 2s,-s,-s at 1,r,r^2. In odd degree they are 2u-v,-u+2v,-u-v at p,q,t. These yield exactly the asserted identities. Inserting c identity blocks multiplies counts by binom(a+b+c,c). QED.

## Theorem 2 — exact balanced-ledger bias and exponential mixing

Put a=b=n >= 1, c >= 0 arbitrary, and define the positive central trinomial number

$$T_n=[z^n](1+z+z^2)^n=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n!}{j!^2(n-2j)!}.$$

Homogeneity of the rational series gives

$$s_{n,n}=[x^ny^n](x^2+y^2-xy)^n=[z^n](z^2-z+1)^n=(-1)^n T_n.$$

Consequently, under a *uniformly chosen ordered source history within this exact fixed ledger fiber*,

$$\boxed{\Pr(1)=\tfrac13[1+2(-1)^nT_n/\binom{2n}{n}],\quad
\Pr(r)=\Pr(r^2)=\tfrac13[1-(-1)^nT_n/\binom{2n}{n}].}$$

For even n the identity is strictly more frequent than each three-cycle; for odd n it is strictly less frequent. The bias changes sign with n, is nonzero for every finite n, and is independent of the number c of identity-return blocks.

The total variation distance from uniformity on these three even permutations is exactly

$$\boxed{TV_n=\frac{2T_n}{3\binom{2n}{n}}\le\frac{2(2n+1)}3(3/4)^n.}$$

This all-n bound follows from T_n <= 3^n and binom(2n,n) >= 4^n/(2n+1). Thus conditional holonomy becomes exponentially balanced as both *distinct transposition multiplicities* grow together. This is a fixed-ledger phenomenon, distinct from R728/R730's full-carrier length-marginal mixing; merely increasing c leaves the bias unchanged.

More precisely, the diagonal series is sum_n s(n,n) z^n = (1+2z-3z^2)^(-1/2). Standard central-coefficient asymptotics give T_n ~ (sqrt(3)/2) 3^n/sqrt(pi n), and so

$$TV_n\sim(\sqrt3/3)(3/4)^n.$$

The preceding finite bound is already a complete non-asymptotic convergence proof.

| a=b=n | P/Q orders | identity | each three-cycle | identity minus each cycle |
|---:|---:|---:|---:|---:|
| 1 | 2 | 0 | 1 | -1 |
| 2 | 6 | 4 | 1 | 3 |
| 3 | 20 | 2 | 9 | -7 |
| 4 | 70 | 36 | 17 | 19 |
| 6 | 924 | 402 | 261 | 141 |
| 8 | 12870 | 5028 | 3921 | 1107 |

The n=2,4,6,8 rows reproduce R735's fixed-PASS-ledger counts for both carriers A and B. The formulas additionally resolve all unbalanced fibers and all balanced odd-n fibers.

## Exact reproducibility

Companion **R736_FIXED_LEDGER_DIHEDRAL_VERIFY.py** contains a completely independent integer dynamic program directly over the six permutations, the rational-series coefficient recurrence and formula, and raw enumeration of small generator words. It validates all 861 pairs with a+b<=40, all small raw words with 0<=a,b<=7 and a+b<=11, the balanced central-trinomial identity through n=16, the R735 fixed-ledger counts for r=1..4, and insertion/multinomial counts for 0<=c<=4, 0<=a,b<=7. All arithmetic is exact; the companion JSON records the concrete results and declared coverage. The infinite result comes from the group-representation argument, not from a finite extrapolation. Independent mathematical review remains open.

## Connection to the parent P000 objective and next test

The conditional distribution quantifies an information difference *inside a single exact PASS ledger*: source ordering controls named terminal relation, while positive count observers aggregate it. The next discriminating native problem is to introduce three nonzero signed primitive force quanta with exact Cell attachment and a typed TRIADIC_CLOSURE_E incidence in a frozen X6 chart; then test whether one event-time/port scheduler can realize the four ordered roots PPQQ, PQPQ, QPQP, QQPP, all with the correct relations under an invariant count ledger. Require rotation-covariant event/update semantics and preserve BRC branches. A failure applies to that proposed scheduler, not automatically to all possible P000 dynamics. This derivation does not promote a carrier return to a native Cell return.

Scientific input pinned to the original P000 commit above; current behavioral rules read separately. Source persistence, official Source CLAIM/Result and independent admission are distinct records.
