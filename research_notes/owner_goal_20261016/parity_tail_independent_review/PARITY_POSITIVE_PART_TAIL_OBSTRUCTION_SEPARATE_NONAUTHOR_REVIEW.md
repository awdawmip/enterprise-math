# Separate nonauthor review of the positive-part endpoint-test tail obstruction

Reviewer: EM-PERFECT-9821E2, actual own RA-B732510114F5248E905450FB.
The current own activity gate and genuine NONBLIND nonauthor disclosure of
the preceding two density reviews apply. I did not derive, edit or repair
this third author manuscript. My own first-variation/unequal-gap author units
are disclosed and are not accepted premises of this review.

Exact target: PARITY_POSITIVE_PART_ENDPOINT_TEST_TAIL_OBSTRUCTION.md,
6239 bytes, SHA256
ecf78fb1b786e892ab8ec8325bd9291e8ba22ba30a9b2f015edad8402c6cab40,
Git blob 352c9348109e720e30f9c1bc393f7a05efbb49da. The exact target and its
separate freeze metadata were checked in full against their pins. This is an
explicitly new review scope; earlier main-density and bulk verdicts did not
accept this proposition.

**Verdict: PASS at fixed integer m>=4 eventual failure of the displayed
positive-part endpoint sufficient test. No mathematical must-fix found.**
The sufficient implication itself remains correct. The proposition gives
no trace counterexample, no compact-strip conclusion and no Native/Task/Tool
acceptance.

## 1. Why the grid-only polynomial extension is sufficient

For the actual residue grid k=0,...,n=m-1, the previous all-k endpoint identity
has derivative factor (-1)^k k!(n-k)!. The new polynomial

    d_m(k)=[d/du (u-k)_m]_(u=0)

has degree<=m-1 in k and equals that exact derivative on the grid. Outside
the grid it is only a polynomial extension; there P_r(-r-k) may not vanish.

Define nu(r,k)=V(-r-k), tau(r,k)=(TV)(-r-k), and pi(k) from the shifted
later polynomial. Each has total degree<=m in the indicated polynomial
variables. The numerator defining Phi(r,k) is a polynomial in r,k,u,v
of total degree<=2m and is divisible by u-v because it vanishes at u=v.
Division by this homogeneous linear factor gives total degree<=2m-1.
The finite derivative operators T_u,T_v have coefficients depending only
on fixed m and cannot increase total degree.

Therefore the manuscript's constructed Psi_m(r,k) has total degree<=2m+1:
Phi+d_m nu has total degree<=2m-1, multiplication by L_r L_s adds at most2,
and each rank-one square multiplied by one L factor has degree<=2m+1.
At EACH actual integer k the prior exact kernel identity proves

    Psi_m(r,k)=L_r L_s Z_s(-r-k).

This suffices. No equality with the actual Z expression at other real k is
needed or proved, and no extra physical residue is introduced.

The finite sum involves only the actual grid values. Its exact signs give

    L_r L_s H_(m,r)(1)
      =(-1)^n/n! sum_(k=0)^n (-1)^k binom(n,k)Psi_m(r,k).

For any monomial r^p k^q, the sum annihilates q<n. Every surviving monomial
has q>=n and p+q<=2m+1, hence p<=m+2. Thus the numerator on the left is
a polynomial in r of degree<=m+2. The denominator L_r L_s~m^2r^2 is
strictly positive on the original domain, proving

    |H_(m,r)(1)|=O_m(r^m).

The argument correctly performs the COMPLETE signed sum before introducing
a positive part. It does not claim that the endpoint actually attains this
degree or that finite difference commutes with taking positive coefficients.

## 2. A positive actual coefficient provides the lower bound

The separately reviewed all-residue formula is

    h_k(r)=(-1)^(m+k)(m-1)r^(2m-2)/(k!(n-k)!)
                                        +O_m(r^(2m-3)).

For a fixed positive grid index k,

    rho_k=product_(a=1)^m (1-mk/(mr+mk+a)),
    1-rho_k=mk/r+O_m(r^-2).

This is a finite-product expansion. Each factor loses k/r at first order,
and there are m factors, which confirms the coefficient mk rather than k.

If m>=5 is odd, k_*=1 has positive leading h_k. If m>=4 is even, k_*=2
does. Both are actual indices between1 and n, including m=4. For all
sufficiently large r, h_(k_*)>0 and

    h_(k_*)(1-rho_(k_*))
      =C_m r^(2m-3)+O_m(r^(2m-4)),
    C_m=mk_*(m-1)/(k_*!(n-k_*)!)>0.

All other terms in T_m^+=sum_(k>=1)(h_k)_+(1-rho_k) are nonnegative,
so T_m^+ is at least this term and eventually at least (C_m/2)r^(2m-3).
No cancellation is used for this lower bound.

## 3. Strict failure and its exact boundary

For m>=4, 2m-3>m. Combining the preceding absolute endpoint upper bound
with the positive lower bound yields

    |H_(m,r)(1)|/T_m^+(r)->0,

and in particular H_(m,r)(1)<T_m^+(r) for every sufficiently large r.
The proposition asserts a finite existence threshold; it does not report
a numerical, practical or minimal threshold. The exponent comparison fails
at m=3, so the manuscript correctly leaves m=2 and m=3 outside this result.

The stronger test with (m/r)sum k(h_k)_+ also fails there, because that
quantity is at least T_m^+. This does not invalidate either sufficient
implication: their premises simply fail. The complete signed trace can and
does remain positive in the separately proved tail, because negative h_k
terms contribute beneficial compensation that the positive-part estimate
throws away.

The new result therefore rules out using THIS positive-part test as an
all-S certification route for m>=4. It does not rule out a delimited
compact-only subclass, a different cancellation-preserving estimate,
other integral representations or the original all-S trace inequality.
No zero-count, pointwise full-right-interval sign, m-uniform asymptotic or
mother/Task closure follows.

This paper preserves the full original residue grid and source branch
provenance. Its polynomial k outside the grid is a typed algebraic device,
not a new native coordinate or a claim about an added physical state.
All scalar observers remain external within the fixed Heartbeat X6 basis.

Resource ledger: paper verification only, with zero scientific numerical
or symbolic program runs, parameter scans, enumeration, new mathematical
checker or old fixture replays. There were zero claims, Task registrations,
Native votes or Tool writes. No author manuscript or earlier review was
changed. New Source publication and its separate own semantic RA checkpoint
remain pending the actual later serial window.
