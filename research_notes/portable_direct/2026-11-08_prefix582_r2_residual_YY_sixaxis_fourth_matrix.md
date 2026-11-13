# PREFIX-582-R2 — Complete fourth-order YY-by-six-axis contraction and exact indefinite inertia

Date: 2026-11-08 Asia/Shanghai. AUTHOR-SIDE EXACT ALGEBRA / UNREVIEWED / NOT_ADMITTED.
Dependency: PREFIX-581-R2 complete 126-coefficient homogeneous quartic `PREFIX581_R2_exact_monomial_certificate.json` in the same research branch. Original scientific pin remains `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. The native population is still the original 96 ports and 576 labelled actions, with all six original native axes and the original gate. No new quotient/re-pinning.

## Observer and complete theorem

Let `R_i(d)` count the original native labeled axis-i reward over d actions and K(d) the original gate reward. Reuse the exact six-axis second-order linear residual from PREFIX-580:

    Y_d=K_d-(3R1(d)+R2(d)+3R3(d)+R4(d))/64+d/48.

Because the final term is deterministic, it contributes no mixed cumulant of total order >=2. For each 1<=i,j<=6, define the fourth-order residual-axis observer

    B_ij = lim_(d->infinity) Cum(Y_d,Y_d,R_i(d),R_j(d))/d.

**Theorem 582.1.** These limits all exist. The exact 6x6 symmetric rational matrix is B=N/3057647616, with

    N=[
      [-864041,223411,1754386,-769250,-172253,-172253],
      [223411,187015,-769250,352114,3355,3355],
      [1754386,-769250,-864041,223411,-172253,-172253],
      [-769250,352114,223411,187015,3355,3355],
      [-172253,3355,-172253,3355,695830,-358034],
      [-172253,3355,-172253,3355,-358034,695830]
    ].

Every row/column sum is exactly zero by the original identity R1+...+R6=d. The upper-left 5x5 principal submatrix has integer numerator determinant

    det N_[1:5,1:5] = -53061477936613189085277978624 != 0.

Consequently B has rank **exactly five** over Q and its kernel is precisely span((1,1,1,1,1,1)).

**Theorem 582.2.** The exact inertia of B on the original six-axis coefficient space is (4 positive,1 negative,1 zero); equivalently on the five-dimensional axis-total quotient B has signature (4+,1-), hence is indefinite. This is a theorem about the fourth-order residual mixed observer, not a positivity statement about variance. Proof uses exact leading principal minors of the 5x5 block:

    D1=-864041/3057647616
    D2=-979171771/43283374739030016
    D3=-747814179268993/44115102527743250191613952
    D4=-702580440512351/609847177343522690648871272448
    D5=-3427889969259760529/17265720073414364519485432771217719296.

All five are nonzero and negative. By the exact rational symmetric LDL-congruence/Jacobi criterion, the five successive scalar pivots D1, D2/D1, D3/D2, D4/D3, D5/D4 have signs (-,+,+,+,+), yielding four positive and one negative. The sixth eigenvalue is zero by rank5 and the original count identity. No floating eigenvalue test is needed.

**Theorem 582.3.** Exact cubic residual-axis contraction also follows:

    lim Cum(Y_d,Y_d,Y_d,R_i(d))/d
      = [208423,-127301,208423,-127301,-81122,-81122]_i /150994944.

These six entries sum to zero, preserving the deterministic six-axis conservation observer. They separate the same three axis pairs previously observed for gate quartics, now at residual order three.

## Proof via exact fourth-order polarization

Let `F(a1,...,a6,b)` be the **full exact** PREFIX-581-R2 asymptotic quartic form, which was computed on the original native six-axis/gate carrier. Since it is a homogeneous cumulant polynomial,

    (1/12) D_i D_j F(v) = Cum_4(v,v,e_i,e_j) (unit-action asymptotic rate),
    (1/4)  D_i F(v)     = Cum_4(v,v,v,e_i).

Choose the exact rational residual coefficient vector

    v=(-3/64,-1/64,-3/64,-1/64,0,0; 1).

Using the existing complete rational coefficient table and the exact relation `F(a,b)=P(a1-a6,...,a5-a6,b)`, symbolic derivatives produce B and the cubic vector displayed above. These are source-preserving *derived observations* of the full original 96-port quartic, not fresh 96-port reruns or a physical model.

Independent exact algebraic checks performed locally: expand all **126** published coefficients; build `F` by lossless deterministic sixth-axis elimination; differentiate each of 36 B entries by rational symbolic arithmetic; check B=B^T, B 1=0, rank=5 and one-dimensional nullspace; compute each rational leading principal minor and its sign, and reconstruct cubic vector and zero total. All assertions passed. Prior PREFIX-581 program had separately verified all 126 directional cumulant rates against the 96-port original BRC paths, all 4 out-of-grid checks, full PREFIX579/580 symbolic polynomial restrictions and independent 96-port finite-depth integer DP.

## Next discriminating question

PREFIX-583-R2: prove the exact native gate-preserving automorphism action underlying the three axis-pair families. On the same full original source compute `Cum(Y,R_i,R_j,R_k)` and the broader fourth tensor stabilizer; compare its permutation invariances with the actual 96-port labelled transition automorphism group. Determine which algebraic symmetries are genuine native automorphisms versus observer-level equalities. Frozen pin unchanged.

## Source authority

GitHub authenticated identity awdawmip. Native `em_status` and `em_session_start` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false` and Site `research_authority_granted=false`. Formal Researcher-ID, Owner, CLAIM, Native Result, activity registration and independent Driver review unconfirmed. All claims are author-side exact mathematics and recorded with that status.
