# Bounded read-review of the fixed-C connected dictionary

Reviewed: `FIXED_C_COEFFICIENT_BOUNDARY_AND_GENUINE_ODD_SOURCE.md`.
Status: PASS / NO CORRECTION NEEDED / ORIGINAL SCALAR COMPARISON OPEN.
Scope: coefficient inverse (6), connected J coefficients, cubic tail
(12)-(15), harmonic prefix/endpoints, actual odd-source pairing (20)-(22),
successor signs (23)-(24), and literal g notation. This is a bounded
read-review with no additional research or checker execution. The main
95 and independent 46 checks remain the reported verification.

The connected inverse (6) is correct on every legal row. Write its
inner summand as w_r and the diagonal as mu_j. For j<N-1,
lambda_j e_(j+1)=mu_j e_j and mu_j e_j w_(j+1)=1/9 give the row by
subtracting adjacent inner sums. At j=N-1 the forward coefficient is
zero, cbar_N=0 is a separate literal convention, and the one remaining
summand gives cbar_(N-1)=-1/5. No e_N is defined or used. The denominator
(3/2)_j first vanishes at j=N; e_j through N-1 and the inner numerator
(3/2)_(r-1) through r=N are legal. The rewritten reciprocal D weight has
the correct power of 2 and factor 1/9.

The connected operator, adjoint and concomitant signs agree with the
independent derivation. The J coefficient convolution retains its exact
lower and upper limits, kappa_0 is fixed by J(1)=0, and
kappa_(4m)=a_m/6 is the actual nonzero top coefficient. The coefficient
product for tau/g has the correct factor 1/2, inherited from
C(1/2)A'(1/2)/4 and the derivative of A at 1/2.

The cubic coefficient range is correct: 2m+1<=s<=4m. The high-s
binomial terms vanish for N+1<=s<=4m by exactly one numerator p factor
and no denominator p factor. This removes those particular terms only;
the full prefixes in the connected J/tau dictionary remain. The residual
b_p sum is explicitly retained, without asserting its value. In degree
2p-2 the derivative kernel has precisely the constant and x^p terms,
so the zero-constant, zero-x^p primitive P_B gives (15) with both
kappa_0 and b_p/2. No derivative reconstruction discards a Frobenius term.

The harmonic moving endpoints stay in 1,...,4m<p. The marked branch
gives d_tau with the stated sign, and finite summation by parts gives
9tau=ell_m-g M_tau. Its upper endpoint (18) retains L_full(1/2) and
the distinct Frobenius coefficient 1/2 on H_(2m)(2). No harmonic
denominator p is introduced, and this tail is kept separate from b_p.

The genuine forcing calculation (20)-(21) preserves the original F_O,
all omitted i=0 constants, and the literal A(1)=1/g and A(1/2)=0. It
therefore gives the independently derived B_CM=(2/3)A'(1/2), with the
old odd-moment correction 2a_m16^m/27 explicit. Multiplication by the
original C(1/2) yields (22) without assuming that C is a unit. Its
second equality has the correct factor: (9g/4)*(8tau/(3g))=6tau.

Both successor residuals have the correct signs. Substituting (22) in
the preceding open comparison moves (9g/4)C_*B_CM to the left, giving
the minus sign in (23). Substituting 6tau=(2/3)ell_m-(2g/3)M_tau moves
the prefix term to the left with a plus sign, giving (24). Every original
g factor, T_m, 2W_m/g, OLD-R source and tau normalization is retained.
The paper explicitly distinguishes the unit g=binom(3m,m) from the older
p-adic memo's different g=f_p(1/2).

The scalar comparison is correctly left OPEN. These identities supply
two exact successor formulations and one actual source-to-boundary
pairing; they evaluate neither the remaining scalar residual nor its
zero/nonzero status. No parent theorem or operational state is promoted.
