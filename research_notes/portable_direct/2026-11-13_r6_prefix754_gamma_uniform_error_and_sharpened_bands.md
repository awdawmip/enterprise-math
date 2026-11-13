# PREFIX-754-R6 — A tighter global binary64 error certificate and strengthened continuous Gamma exclusion margins

Date: 2026-11-13 (Asia/Shanghai). Parent: PREFIX-675; predecessor: PREFIX-753-R6.
Researcher-ID: EM-DIRECT-D847AA. Research-Activity-ID: RA-16E805B70E0067F57A2645F1.
Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Scientific scope: the **external two-coordinate Gamma(max) auxiliary observer** built from the frozen 189-layer BRC stopped-survivor recurrence. No native X6/slice transfer is asserted.
Status: AUTHOR EXACT-RATIONAL FORWARD-ERROR PROOF + AUTHOR INDEPENDENT FULL-NUMERICAL-GRID REPLAY; UNREVIEWED / NOT ADMITTED.

## Question and outcome

PREFIX-752 used a uniform IEEE-754 absolute-error enclosure <1/100 for all 147456 endpoint-comparator values G, and PREFIX-753 inferred two continuous exclusion bands with gap constants 3/4 and 29/10. Can the arithmetic error bound be tightened **without changing the frozen model**, enabling stronger strict continuous margins?

**Theorem 754.1 (conditional uniform evaluation bound).** Under the IEEE-754 binary64, checked input-rounding, dot-product conditions and conservative tiny-term underflow allowance stated below, every one of the 384×384 endpoint-comparator entries computed by the published PREFIX-752 expressions obeys

    |G_hat(u,v) - G_exact(u,v)| < 1/100000.

The bound is uniform and is verified by exact rational arithmetic; an explicit conservative majorant is approximately 1.7340907130248891×10^-6.

**Theorem 754.2 (strengthened Gamma bands).** Under the frozen Gamma-moment definitions and the numerical conditions of Theorem 754.1, for all real q>=2 and all (p,z) in D=[0,1/2]^2,

    |p-z| <= 17/256  => V_q(0,3/20) - V_q(p,z) > (383/500) q^2,
    |p-z| >= 57/256  => V_q(0,3/20) - V_q(p,z) > (299/100) q^2.

Here V_q=q^2 Var(Y)-q E[Y] and Y=max(T_p,T_z) for the two conditionally independent Gamma clocks of the frozen model. These replace constants 3/4 and 29/10 on exactly the **same** 82482 fine cells. They add zero new geometric coverage to the cumulative historical union.

The numerical scan below is a new independent implementation of the original integer recurrence and entire 384×384 old comparator, not an import of PREFIX-751/752 or an acceptance/review claim.

## Precision proof (all conservative inequalities are global)

Set N=189 and binary64 unit roundoff u=2^-53. For k u<1 let gamma_k=ku/(1-ku). Each exact stopped-survivor tail T_n(x) lies in [0,1]. The published source explicitly checks relative rounding of every computed nonzero tail by an integer cross-product; exact zero remains exactly zero. The input matrices are

    C_nm = binom(n+m,n) 2^(-(n+m+1)),
    D_nm = (n+m+1) C_nm,     0 <= n,m < N.

All inputs are nonnegative. Bounds C_nm<=1/2 and D_nm<=(2N-1)/2 are immediate. C is formed by correctly rounded float(binomial) followed by exact binary scaling; D is one correctly rounded multiplication by a small exact integer. Thus relative input errors are <=u for T and C, and <= (1+u)^2-1 for D. The tail-array cross-product tests certify relative errors for nonzero input entries (including any exceptionally small inputs). Assume binary64 round-to-nearest for normal operations, no overflow, and gamma_N forward bounds on positive length-N inner products, with an absolute allowance of one minimum normal unit (2^-1022) per elementary tiny-term underflow or flush-to-zero. This allowance covers products that become subnormal even when the input factors are normal.

Define A_i=sum_n T_in, B_i=sum_n(n+1)T_in, X_ij=(TCT^t)_ij and Z_ij=(TDT^t)_ij. Their exact bounds are

    0<=A_i<=N,
    0<=B_i<=Bmax=N(N+1)/2,
    0<=X_ij<=Xmax=N^2/2,
    0<=Z_ij<=Zmax=N^2(2N-1)/2.

The exact Gamma moments as evaluated in PREFIX-752 are mu_ij=A_i+A_j-X_ij and M2_ij=2(B_i+B_j)-Z_ij. In this model 0<=mu<=2N and 0<=M2<=4Bmax.

Positive-sum forward error factors are

    r=(1+u)(1+gamma_N)-1,
    rX=(1+u)^3(1+gamma_N)^2-1,
    rZ=(1+u)^4(1+gamma_N)^2-1.

The factors rX and rZ account for rounding both tails, the C/D input and two BLAS stages; nonnegative products make the relative bounds valid even when terms are tiny.

Set m=2N and h=4Bmax. A safe absolute error bound for every mu entry, including the fixed competitor, is

    E_mu = 2N*r + Xmax*rX + 2N*(1+r)*u
           +u*(2N*(1+r)*(1+u)+Xmax*(1+rX)).

For M2, the doubling by 2 is exact in the normal range:

    E_M2 = 4Bmax*r + 4Bmax*(1+r)*u + Zmax*rZ
           +u*(4Bmax*(1+r)*(1+u)+Zmax*(1+rZ)).

For W(e)=M2(e)-mu(e)^2 and any explicitly evaluated mu^2, valid errors are

    E_W = E_M2+2m*E_mu+E_mu^2+u*(m+E_mu)^2
          +u*(h+E_M2+(m+E_mu)^2*(1+u)),
    E_sq = 2m*E_mu+E_mu^2+u*(m+E_mu)^2.

For P=max(0,(mu(e)-mu(a))/2), the map max(0,x/2) is 1/2-Lipschitz. The binary halving of the finite normal difference is exact, hence

    E_P = E_mu+u*(m+E_mu).

There are at most three further rounded arithmetic operations in the expression

    G = W(e)-M2(h)+mu(a)^2-P.

Using the absolute gamma_3 summation bound on these signed additions/subtractions,

    E_G = E_W+E_M2+E_sq+E_P
          +gamma_3*(2h+E_W+E_M2+(m+E_mu)^2*(1+u)+m+E_mu).

The underflow allowance propagates through at most two N-term positive matrix products and the scalar formulas. Using N=189, |mu|<=378, |M2|<=71820, and the displayed monotone positive-operation bounds, a conservative additional total error below 10^9*2^-1022 covers every such tiny term (including flush-to-zero). Set E_G_total = E_G + 10^9*2^-1022. The added rational term is far smaller than 10^-100. Exact Fraction evaluation of the complete displayed expressions (including this term for E_G_total) gives

| Quantity | Decimal approximation of the *rational majorant* |
|---|---:|
| E_mu | 7.6553063887987627e-10 |
| E_M2 | 2.8784584665820590e-7 |
| E_W | 8.6662670989507147e-7 |
| E_G | 1.7340907130248891e-6 |

The independent Fraction program directly asserts E_mu<10^-8, E_M2<10^-6, E_W<10^-6 and **E_G_total<10^-5** without relying on those printed decimal approximations. This proves Theorem 754.1 under its declared arithmetic conditions.

## Entire-grid numerical replay and continuous transfer

The independent stand-alone NumPy checker reimplements the 189-layer integer width predicate and count recursion and obtains exactly 9529 nonzero survivor positions, zero final survivors, and the original 137168 positive fine-cell G entries out of 147456.

For offsets d=|i-j| it obtains:

| Fine-cell band | Cell count | Minimum recomputed binary64 G | Uniform exact lower bound |
|---|---:|---:|---:|
| d<=51 | 36900 | 0.76648683062603595 | G>383/500=0.766 |
| d>=171 | 45582 | 2.9909054345243931 | G>299/100=2.99 |

All computed G entries have absolute value above 0.0185. Different valid BLAS summation order changes the sixth-plus decimal places of selected values but not these strict margin comparisons; the original PREFIX-753 near-band minimum was 0.7664868306305976. The assertion on reported grid minima is a numerical finite scan coupled to the **separately proved** global rational forward error bound, not a claim of exactly representing every G as a float.

For any (p,z) with |p-z|<=51/768=17/256, it belongs to a closed fine cell with |i-j|<=51, including equality grid boundaries via an adjacent cell. Similarly |p-z|>=171/768=57/256 belongs to a closed cell with |i-j|>=171. For each such cell, monotone Gamma moments establish the PREFIX-712 endpoint inequality

    [V_q(e)-V_q(p,z)]/q^2 >= G_ij,      for every real q>=2.

Combining this exact inequality with E_G_total<1/100000 and the two recomputed band minima yields the stated gap constants. The global maximizer corridor from PREFIX-753 stays

    17/256 < |p-z| < 57/256.

This improves the certified **magnitude of exclusion**, not the extremizer corridor.

## Reproducibility, provenance, and limits

- Rational certificate: PREFIX754_R6_GAMMA_FLOAT_ERROR_BOUND.py (Python standard library, no external dependencies). Executed as an independent Python process and returned ALL_CHECKS_PASS.
- Stand-alone full-grid replay: PREFIX754_R6_INDEPENDENT_GRID_REPLAY.py (Python 3 and NumPy, single-threaded OpenBLAS). A source-equivalent local independent program was executed and returned ALL_CHECKS_PASS; the published script has not separately been re-executed byte-for-byte from the remote commit.
- Machine data: PREFIX754_R6_GAMMA_SHARP_BANDS_RESULTS.json.
- Comparator definitions and frozen scientific input: PREFIX-752/753 and source pin above. No revision to the recurrence, comparator point or BRC model.

This proof audits numerical evaluation under stated IEEE/BLAS premises. Independent evaluation of the Gamma analytic identity, stochastic monotonicity, and the complete historical 140662-cell union remains valuable. The result is AUTHOR-checked, not an independent mathematical review, Result admission or native X6 theorem.

## Next research unit

Obtain exact uncovered fine-cell coordinates from the previously published 6794-cell author-level complement and test a genuinely uncovered swap-pair with exact multi-comparator or coupled-moment certificates. Independently review the Gamma analytic identity and compare the strengthened forward error assumptions against the deployed NumPy/BLAS arithmetic semantics.
