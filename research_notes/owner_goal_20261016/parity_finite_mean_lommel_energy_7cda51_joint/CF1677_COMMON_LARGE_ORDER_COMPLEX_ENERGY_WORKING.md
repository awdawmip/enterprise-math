# Common large-order factors: a uniform complex-disk component

NEW UNFROZEN AUTHOR WORKING, by the same CF1677 actor. This is a bounded
component for the new finite-Lommel line, not a paper, accepted tool, sign
result, independent review or Source publication. It does not modify the
unchanged UNREVIEWED_PARTIAL_WORK/HOLD archive at Source
3cc2c19343747407c078bf0cd0db2227377f25e2. The original CF registration,
NONBLIND history, local key, current10/24 receipts, old failed guard and
false pre-final history remain. Current directed ordinary TASK_RESEARCH
does not grant a formal Task, Native authority or a budget reset.

All mathematical estimates below were derived on paper. No scientific
program, import, coefficient generation, sampling, experiment, enumeration,
solver or Native call was performed. Document reads, hashes and custody
bookkeeping are separate from this mathematical derivation. This is an
author contribution; a common-author check is not an independent vote.

## 1. Exact input and bounded claim

I personally completely read the new, UNFROZEN packet
WORKING_EXACT_FINITE_MEAN_LOMMEL_BESSEL_PACKET_AND_ENERGY_OBLIGATIONS.md,
9919 UTF-8 bytes, SHA256
244e2cbe465d318beb986484b7edc627268e9a9e32a4a4dd36f024445f70faaf,
in this directory. Its actual parameters are integer m, t in {2,3,4,5},
n=m-t even, N=n-1, nu=t+1/2 and

    M=nu+N=m-1/2.

The packet assigns CF only the two COMMON large-order factors

    A_M(z)=-pi (z/2)^M Y_M(z)/Gamma(M),
    B_M(z)= pi (z/2)^M J_M(z)/Gamma(M),                 (1)

initially on the principal cut plane, followed by their entire extensions.
The finite-Lommel identity, low-order weighted-pair margin, zeta correction,
full-carrier norm and exact rising-T/coefficient questions are not proved
here. In particular the new packet is not silently an accepted theorem.

For every integer m>=100 and every complex z satisfying

    epsilon=|z|^2/m <= 1/64,                            (2)

write E=z d/dz. The following estimates hold on the SAME closed disk:

    |A_M(z)-1| <= epsilon,
    |E A_M(z)| <= 2 epsilon,
    |E^2 A_M(z)| <= 4 epsilon;                         (3)

    |B_M(z)| <= 2 m^(1-m),
    |E B_M(z)| <= 4 m^(2-m),
    |E^2 B_M(z)| <= 10 m^(3-m).                        (4)

Each of the three bounds in (4) is at most 2^(-m). No disk shrink is
needed for these Euler derivatives. The proof retains the vanishing order
2m-1 of B_M; this matters if a later argument multiplies it by a singular
low-order expression. A small constant bound alone would not license that
operation.

For real z in (2) these factors are real, so the immediate component-level
consequence is

    A_M(z)^2+B_M(z)^2 >= (1-epsilon)^2
                          >= (63/64)^2 > 1/2.         (5)

This is not a lower bound for the actual mean, its two weighted channels,
the full carrier, T or the COMMON coefficient.

## 2. Selected classical primary, branches and exact series

I independently used managed-web exact official opens. Initial attempts
to open the three selected .tex URLs returned unsupported content-type
results; those failures are retained and are not called successful reads.
Subsequent successful official HTML opens were

    https://dlmf.nist.gov/10.2#E2
    https://dlmf.nist.gov/5.5#E3.

My semantic reading scope was the displayed 10.2.E2 J series, 10.2.E3
noninteger Y/J connection, their nearby principal-branch qualifications,
and 5.5.E1 Gamma recurrence / 5.5.E3 reflection. I do not claim whole-page,
whole-chapter or any large-order uniform-asymptotic theorem consumption.
The actual saved tool-response JSON is
/tmp/native-free-CF1677/lommel-large-order-dlmf-selected-primary-web-observations.json,
24190 bytes, SHA256
5871d6a9ea20d4c3937860dff70faccf87f5c36bfb0863884462ce8741465b5a.
That is a hash of my saved observation JSON, NOT of the raw official HTML.
I do not borrow 7CDA's HTTP receipt or assert that I fetched her raw TeX.

The selected classical formulas are

    J_v(z)=(z/2)^v sum_(k>=0)
                    (-z^2/4)^k/[k! Gamma(v+k+1)],
    Y_v(z)=[cos(pi v)J_v(z)-J_(-v)(z)]/sin(pi v),
    Gamma(v)Gamma(1-v)=pi/sin(pi v),
    Gamma(v+1)=v Gamma(v).                            (6)

The Y connection in (6) is used only for the noninteger half-integer M.
Powers and Bessel functions initially use the SAME principal branch. Since
cos(pi M)=0, substitution of J_(-M) and reflection gives exactly

    A_M(z)=sum_(k>=0) (-z^2/4)^k/[k! (3/2-m)_k],
    B_M(z)=pi (z/2)^(2m-1)/[Gamma(M)Gamma(M+1)]
                   *sum_(k>=0) (-z^2/4)^k/[k! (m+1/2)_k].  (7)

For example the constant multiplying the first series before reflection
is pi/[Gamma(M)Gamma(1-M)sin(pi M)]=1; no phase or sign is dropped.
The first Pochhammer parameter is a nonintegral half-integer and never
has a zero factor. Both series have infinite radius of convergence by
their coefficient ratios. Since 2m-1 is an integer, (7) gives an entire
EVEN extension of A_M and an entire ODD extension of B_M, respectively.
Their removable values at the origin are A_M(0)=1, B_M(0)=0. These are
claims about the normalized extensions, not raw Y_M being entire or
separately inserting Y_M(0). Termwise differentiation is licensed by these
entire power series, and their real coefficients also justify (5).

## 3. Uniform A bound, including the half-integer crossing

Set R=floor(m/2), a=3 epsilon/4 and define the nonnegative coefficient
majorants

    u_k=(|z|^2/4)^k/[k! |(3/2-m)_k|],   u_0=1.       (8)

For 0<=i<=R-1,

    |3/2-m+i| >= m-R-1/2 >= m/3,

where the last inequality holds for m>=100. Therefore

    u_k <= a^k/k!                    (0<=k<=R).       (9)

For EVERY integer k>=R, including both indices with a denominator factor
of absolute value 1/2 near k=m-2,m-1, one has

    u_(k+1)/u_k
      =(|z|^2/4)/[(k+1)|3/2-m+k|]
      <= (|z|^2/4)/[(m/2)(1/2)]
      =epsilon.                                      (10)

At z=0 all nonconstant terms vanish and the asserted bounds follow
directly. For z!=0 (10) proves

    u_(R+l) <= u_R epsilon^l   for every l>=1.         (11)

Thus (11) controls the ENTIRE tail beyond R, through and beyond the small
half-integer factors. It is not a fixed-k approximation, a truncated formal
expansion or an asymptotic in which k is held independent of m.

Because a<=1, (9) also gives

    u_R <= a,   R u_R <= a,   R^2 u_R <= a+a^2.       (12)

For the last inequality split R^2=R(R-1)+R and use (9), with R>=2.
Let H_q denote the head contribution, k=1,...,R, to the absolute
majorant for E^q(A_M-1), for q=0,1,2. Its coefficient weight is (2k)^q
(with q=0 meaning weight1), so positive exponential-series moments give

    H_0 <= a exp(a),
    H_1 <= 2a exp(a),
    H_2 <= 4(a+a^2)exp(a).                           (13)

These bounds deliberately majorize the finite head by an infinite
NONNEGATIVE series; they make no assertion about signs of the original
coefficients. Since a<=1/16, exp(a)<=1/(1-a)<=16/15, whence

    H_0 <= (4/5)epsilon,
    H_1 <= (8/5)epsilon,
    H_2 <= (17/5)epsilon.                            (14)

For the tails, the exact geometric moments in (11) yield

    T_0 <= u_R epsilon/(1-epsilon),

    T_1 <= 2u_R [R epsilon/(1-epsilon)
                          +epsilon/(1-epsilon)^2],

    T_2 <= 4u_R [R^2 epsilon/(1-epsilon)
          +2R epsilon/(1-epsilon)^2
          +epsilon(1+epsilon)/(1-epsilon)^3].         (15)

Using (12), epsilon<=1/64 and the weaker reciprocal estimate
1/(1-epsilon)<=16/15 gives

    T_0 <= (4/5)epsilon^2 <= epsilon/80,
    T_1 < 6a epsilon = (9/2)epsilon^2
                                      <= (9/128)epsilon.  (16)

For complete detail on the second derivative, after applying (12) the
bracket in T_2/(4a epsilon) is at most

    (17/16)(16/15)+2(16/15)^2
                  +(17/16)(16/15)^3
        =15857/3375 <5.

Consequently

    T_2 <=20a epsilon=15epsilon^2 <=(15/64)epsilon.  (17)

Combining (14),(16),(17), the three total majorants are bounded by

    (13/16)epsilon < epsilon,
    (8/5+9/128)epsilon <2epsilon,
    (17/5+15/64)epsilon <4epsilon,

respectively. This proves all of (3), including z=0 by (7).

## 4. B bounds with the exact high-order zero retained

Write r=|z|, L=2m-1, gamma=m+1/2 and

    P=pi (r/2)^L/[Gamma(M)Gamma(M+1)],
    x=r^2/(4gamma).                                 (18)

All Gamma factors are positive real numbers here. Since
(gamma)_k>=gamma^k, the positive exponential-series majorants in (7)
give the more informative inequalities

    |B_M| <= P exp(x),
    |E B_M| <= P exp(x)(L+2x),
    |E^2 B_M| <= P exp(x)[(L+2x)^2+4x].              (19)

For example E acts on each monomial z^(L+2k) by L+2k; the second moment
is (L+2x)^2+4x. Thus (19) retains the exact r^L factor even arbitrarily
close to zero, rather than inferring derivative bounds from a constant
supremum that forgets the zero. At r=0 each expression is interpreted
by continuity and is zero.

Gamma reflection at 1/2 gives Gamma(1/2)^2=pi. Together with recurrence,

    Gamma(M)Gamma(M+1)
       =pi M [product_(h=1)^(m-1)(h-1/2)]^2
       >=pi M [ (m-1)!/2^(m-1) ]^2.                 (20)

The elementary integral estimate
log(q!)>=integral_1^q log(s)ds=q log(q)-q+1 and exp(1)<3 implies

    q! >= (q/3)^q        for every integer q>=1.     (21)

Equations (18),(20),(21) now imply

    P <= r/(2m-1) [9r^2/(m-1)^2]^(m-1).            (22)

On the disk (2), r/(2m-1)<=1 and (m-1)^2>=m^2/2. Hence

    9r^2/(m-1)^2 <=18/(64m) <=1/m,
    P <=m^(1-m).                                    (23)

Also x<=epsilon/4<=1/256, exp(x)<2, L+2x<2m and
(L+2x)^2+4x<=5m^2. Substitute these into (19) to get (4).
Finally the largest of these three displayed bounds is at most

    10m^(3-m) <=16*16^(3-m)=2^(16-4m) <=2^(-m)

for m>=100. This argument uses exact products and elementary inequalities,
not a nonuniform Stirling approximation or a numerical Gamma evaluation.

## 5. Actual domain inclusion and precise unfinished arrows

The proposed packet scale m>=2^1000, |z|<=pi m^(1/100) is contained in
(2). Indeed pi<4 gives

    |z|^2/m <=16m^(-49/50) <=16*2^(-980) <1/64.

This inclusion changes no sign domain by itself. The bounds here concern
the SAME M=m-1/2 for both actual t and t+2 channels; they do not replace
their distinct original prefactors. I have not proved any low-order pair
condition, full-carrier HS bound, zeta-tail absorption, Z0 absorption,
relative origin-disk condition, deficit estimate, C/E/E^2 estimate,
rising-T positivity or actual COMMON coefficient positivity here.

Selected DLMF series, connection and reflection are classical REUSE;
the proof above is COMPOSE_APPLIED to the specified actual normalized
large-order factors with a fully quantified disk and derivative interface.
No general new Bessel theorem, generic Tool, global novelty or complete
library-absence claim is made. Formal/product cumulative budget remains
UNKNOWN. These are warm, exact dynamic proof dependencies, not a new
cold startup or a claim that unmeasured cumulative usage passed a cap.

This component is available for genuine joint-author checking and later
whole-unit assembly only. There is no independent review, Source or new
activity event for it now. Mother Goal remains OPEN; no FINAL permission
is inferred from this bounded component being complete.
