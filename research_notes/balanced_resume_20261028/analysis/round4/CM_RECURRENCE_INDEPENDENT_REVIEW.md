# CM24 recurrence: second nonauthor independent paper review

Reviewer: EM-ANALYSIS-1E507F; activity RA-9C879FA5E6538D45DD9AE10F.
Date: 2026-10-28.
Disposition: **NO_DEFECT_FOUND_IN_STATED_ALL_K_ARITHMETIC_PROOF_AND_CONDITIONAL_SEPARATED_QUOTIENT_COROLLARY**.
This is a nondecisive direct paper opinion, not a formal Driver/Task vote.

## 1. Exact object, independence and authority

I reviewed the complete frozen author paper

`research_notes/balanced_resume_20261028/cm/round4/CM24_P_POWER_INDEX_VALUATIONS_AND_SEPARATED_DIMENSION.md`

by EM-DIRECT-38A864, SHA256
`09e26d4322403c2f4e79f3050f5fbffb7acce9ec60c403ff24d68e26ad9023a1`,
12022 bytes. I recomputed that hash from actual local bytes before reading.

I did not participate in the author's proof construction or suggest the
pullback, valuation argument, or conclusion. I received the frozen paper
and source locations from the author. Before freezing this report I did
not read the first reviewer's current report, verdict, messages about
mathematical findings, or checking notes. Shared control/source context
and the old second-round interface are disclosed, so this is independent
nonauthor paper checking, not clean-blind review. Root supplies no
mathematical vote.

The current same-session RA startup guard, using registration Source
`09f96dc45a9cf71cd81cc52358842d256798881e`, returned activity/persistence
allowed and ACTIVITY_BOOKKEEPING_ONLY_NO_TASK_AUTHORITY. I did not claim
or execute an original formal Task, infer owner absence from UNKNOWN
runtime state, run a finite-prime/finite-coefficient census, or evaluate
kappa, Y, Z or a fixed endpoint source. I did not run the author's symbolic
checker. The calculations below are independent exact paper algebra;
file reading and byte hashing are not scientific computations.

The carrier remains the stated external arithmetic module. The project's
native Heartbeat space is the signed six-axis Cell torsor without a native
plane; no cohomological dimension below is interpreted as spatial dimension.

## 2. Dependency and normalization checks

The old second-round paper is

`research_notes/balanced_resume_20261028/cm/round2/CM24_SEPARATED_QUOTIENT_FIVE_SURVIVORS.md`,
SHA256 `60548b26b12a98b1d721b6e6f282c6fe3f063689ac7b928de2c3ad7b10bc9a10`.

I read its full author text, especially sections 2, 4, 6 and 7. Its local
bytes equal the actual captured connector response in
`wave8_readback_26.json`, whose blob is
`4e8ed5380e8980156417d82bd04ada7eef736b27`. The cited immutable Source is
`0d3b22c10ba255041b9ea88207f5fffa0ac62c76`. I use its already-reviewed
5-or-6 separated-dimension alternative and bounded row/scalar comparison
as inherited interfaces; this report does not re-certify that entire paper.

I also read the relevant original weak-normal-form sections 3–4 in

`research_notes/owner_goal_20261016/cm24_convergence_new_anchor/weak_six_boundary_normal_form/CM24_SIX_BOUNDARY_WEAK_COKERNEL_NORMAL_FORM_AUTHOR.md`

by EM-DIRECT-88303D at `56f5938da3f707c1d9db1b39afde124eac4634e3`.
The actual local source has the exact Git blob
`06a9fc065e334f4974bb43f0cd978502613c542a`.

That source fixes H'=Dinf H, H(0)=I and
`Dinf(0)=[[0,1/8],[0,0]]`. Its boundary observation is

    Q(b)=Res_z(-z^(-1)b(1/z)e1 H dz),
    Q(c0+c1 r+simple-pole terms)=(-c0,-c1/8).

Thus for the rational normal form of r^j its r-coefficient is exactly
`a_j=8[z^j]H_12`, and its constant coefficient is `[z^j]H_11`.
In particular a_0=0 and a_1=1. The original identity

    Kcal(r^j)=-4(j+1)(j+2)r^(j+2)
                  +(5j(j+1)+2)r^j-j(j-1)r^(j-2)

gives exactly the new paper's recurrence by taking that normal-form
coefficient. This checks the carrier and gauge binding; a convenient
different solution of the same differential equation was not substituted.

## 3. Recurrence and formal pullback

Let A(z)=sum a_j z^j, P=4-5z^2+z^4. The four formal sum identities are

    sum (j+1)(j+2)a_(j+2)z^j=A'',
    sum j(j+1)a_j z^j=z^2 A''+2z A',
    sum j(j-1)a_(j-2)z^j=z^2(z^2 A''+4z A'+2A),
    sum a_j z^j=A.

They give `P A''+P' A'+(2z^2-2)A=0` with A(0)=0, A'(0)=1.
The constant leading coefficient P(0)=4 is invertible in Q, so the
solution is uniquely determined coefficient by coefficient. This argument
does not invert a zero residue modulo p.

For the Gauss coefficients

    c_n=(1/3)_n(5/6)_n/((7/6)_n n!),

their successive ratio gives
`t(1-t)F''+(7/6-13t/6)F'-(5/18)F=0`. The parameter sum is
1/3+5/6+1=13/6 and their product is 5/18, with denominator parameter
7/6, so both middle and constant coefficients agree.

I checked the proposed pullback without relying on the author's saved
symbolic output. Put x=z^2, R=4-3x, U=R/4. Then

    w=x^3/R^2,
    g=z U^(-2/3),
    ell=g'/g=(4+x)/(zR),
    w'=6z^5(4-x)/R^3,
    ell'+ell^2=4(12+x)/R^2,
    T=36x^2(4-x)/R^2.

First, `R^2-x^3=(1-x)(4-x)^2` proves
`P(w')^2=T w(1-w)` immediately.

For the F' coefficient, logarithmic differentiation of w' gives

    w''/w'=5/z-2z/(4-x)+18z/R.

Consequently the left side of the second claimed identity reduces to

    6x^2(4-x)/R^4 * (112-168x+63x^2-13x^3).

The parenthetical polynomial is `7R^2-13x^3`, which gives exactly
`T(7/6-13w/6)`.

For the F coefficient, multiply
`P(ell'+ell^2)+P'ell+(2x-2)` by R^2. Its numerator is

    4(4-5x+x^2)(12+x)
       +2(-5+2x)(4+x)R+(2x-2)R^2
      =-10x^2(4-x).

This is `-(5/18)T R^2`. All three identities therefore hold in Q(z).
They are rational identities, not a finite set of point evaluations.

The composition `gF(w)` is well-defined in Q[[z]] because w has order
six and U has constant coefficient one. It has constant term zero and
linear coefficient one. Substitution into the differential equation and
the already-checked uniqueness prove

    A(z)=z U(z)^(-2/3)F(z^6/(16U(z)^2))

for the exact original sequence. The temporary Laurent expression ell
does not introduce a singular solution or a free branch constant.

## 4. Every prime-power valuation level is counted correctly

For p congruent to 13 or 19 modulo 24, p>=13 and p congruent to 1
modulo 6. At a fixed level ell, write M=p^ell=6h+1. From

    c_n=3^(-n) product_(i=0)^(n-1)
                       ((3i+1)(6i+5)/(6i+7)) / n!

the residues of i giving a zero modulo M in the three linear factors are,
respectively, 2h, 5h and h-1. Direct substitution gives M, 5M and M.
All are valid residues in 0,...,M-1 and the factors 3 and 6 are units.

If n=QM+r with 0<=r<M, their counts in 0<=i<n are Q plus
the indicators `r>=2h+1`, `r>=5h+1`, `r>=h`. The factorial contributes
Q. Thus the complete level contribution is

    d_ell(r)=1_(r>=2h+1)+1_(r>=5h+1)-1_(r>=h).

Its values on the four successive integer ranges are 0,-1,0,1 as in
the author paper. Summing these divisibility counts over all ell counts
the full valuation, including every higher power; only finitely many
levels contribute for each n.

Let n_k=(p^k-1)/6. For ell<=k,

    n_k=p^ell (p^(k-ell)-1)/6+(p^ell-1)/6,

so its residue is exactly h and its contribution is -1. For ell>k,
n_k<h and the contribution is zero. This proves `v_p(c_(n_k))=-k`.

For every 0<=n<n_k, at every level ell>=k one instead has n<h,
hence zero contribution; the lower k-1 levels each contribute at least
-1. Therefore `v_p(c_n)>=-(k-1)` for all n<n_k. This includes k=1
and n=0. These are uniform statements in n,k, not observed patterns.

## 5. Formal substitution preserves the strict valuation gap

Expanding the proven composition gives a coefficient-wise finite sum

    A(z)=sum_(n>=0) 16^(-n)c_n z^(6n+1)U(z)^(-2n-2/3).

For fixed n the exponent belongs to Z_p. For each integer j>=0,
the function `alpha -> binom(alpha,j)` is a rational polynomial continuous
on Q_p. Approximation of alpha in Z_p by nonnegative integers shows its
value is in the closed set Z_p. As -3/4 is also integral, every
coefficient of U^alpha is p-integral. This argument is valid even when
j! is divisible by p; it does not assume its invertibility.

At index p^k=6n_k+1, no term with n>n_k contributes. The term n=n_k
uses the constant coefficient one of U^(-2n_k-2/3), and has valuation
-k because 16 is a p-unit. Each of the finitely many preceding terms
has valuation at least -(k-1), using the preceding-index bound and
integrality of the substitution. Their sum has that same lower bound.
It cannot cancel the unique term of valuation -k. The ultrametric
valuation law proves exactly

    v_p(a_(p^k))=-k  for every k>=1.

No coefficient can arrive from a later hypergeometric index, and no
extra denominator or change of lattice enters the substitution. This is
the needed noncancellation proof; merely knowing unbounded c_n would not
have sufficed.

## 6. Separated quotient and scope of the conclusion

The arithmetic result gives an explicit unbounded subsequence in the
original normalized K, where v_p(p)=1. The old second-round equivalence
therefore selects dimension five and comparison kernel K[(r,0)]. That
corollary correctly retains all assumptions of the inherited complete
unramified DVR, fixed integral localization/completion and row connection.
It is not asserted for arbitrary strong completions.

I also checked the concrete closure witness. The inherited rational
normal form is

    r^j-b_j-a_j r=Kcal(v_j),   b_j=[z^j]H_11 in O.

For j=p^k, division by a_j gives

    w_k-r=Kcal(v_j/a_j),
    w_k=(r^(p^k)-b_(p^k))/a_(p^k),
    ||w_k||<=p^(-k).

The numerator has integral partial-fraction coefficients and norm at
most one; |1/a_(p^k)|=p^(-k). Hence w_k tends to zero and -r is a
limit of scalar images, so r belongs to their closure. The bounded
row/scalar comparison and five surviving classes are inherited. This
proves a closure assertion, not an actual solution of L(h)=(r,0).

The paper correctly leaves actual strong-image membership, exact strong
horizontal dimension, and a classification of the non-Hausdorff part
unresolved. No kappa/Y/Z value or new prime-class CM conclusion follows.
Although the elementary valuation argument works whenever p is prime
and p congruent to 1 modulo 6, the stated CM consequence stays in its
original p congruent to 13 or 19 modulo 24 carrier.

## 7. Review outcome

I found no missing hypothesis, normalization error, pullback identity
error, divisibility-count gap, or cancellation gap in the stated new
arithmetic proof. No author repair or additional bridge is requested.
The new all-k theorem and its inherited-interface corollary are supported
at the paper-proof level described above. This opinion does not promote
them to formal acceptance, Working Truth or Foundation status and does
not re-review the entire preceding weak/strong comparison chain.

The report is independently frozen before receiving the other current
reviewer's conclusion. Subsequent comparison of reviews may identify a
real disagreement, but agreement alone is not additional mathematical
evidence or a reason to enlarge the theorem's scope.

Researcher-ID: EM-ANALYSIS-1E507F / TASK_RESEARCH
