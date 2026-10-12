# A finite two-index Heun certificate and the fully normalized CM kernel

Status: BOUNDED LOCAL PAPER RESEARCH / NEW FINITE LEMMAS PROVED /
FIXED OBSERVER COMPARISON OPEN / LIFT OPEN.

Prepared 2026-10-12. This is the authorized continuation of the locally
reviewed three-integral unit. It is not a registered or claimed formal Task,
Source publication, accepted Result, new native identity, or provider request.
No prime was instantiated and no prime campaign was run. Old source bytes and
native X6 / separately typed time are unchanged. The marked CM pair is kept.

The main contribution is an actual summand-level two-index telescoper,
including its finite modular endpoint, and an explicit transformation of all
three canonically normalized integrals and their pole repairs. This is not a
certificate of the final OLD-R comparison. That comparison remains open.

## 1. Premises and precision

Let p=6m+1 be prime, p=13 or 19 mod24. All new finite-field formulas below
are over F_p or its quadratic extension. We retain the explicitly supplied
finite transport H(x)=V(4x(1-x)), the full forcing / four-boundary theorem
for Xi, the fixed CM value theorem, and CM0: V(1/2)=0. We do not reprove or
enlarge those inputs. The preceding independent three-integral review is
PASS only at its stated conditional scope.

Use literally the old constructors

    V(w)=sum_(k=0)^m v_k w^k,
    v_k=(1/6)_k(1/3)_k/(k!)^2,
    D_r=2^(r-1)(r-1)!^2/[18(5/6)_r(2/3)_r],
    R=OLD-R=2 sum_(i=1)^m v_i2^-i
                       sum_(r=1)^i [1+6(i-r)]D_r,
    tau=-(1/9) int_0^(1/2) V(w)[(1-w)^(3m)-1]/w dw.

R and tau are independent of every constructor introduced here. In
particular neither is assigned from Xi, Lambda, Gamma, or a discrepancy.
The only unresolved target is

    Lambda+2q_3+R+6tau=0.                              (T)

The earlier paper defines W=(z+1)^(p-1)H(B), B=(3z-1)^2/(z+1)^3,
T_div=(W-1)/(3z-1), the three integrals I_W,I_T,I_E, P_hat, the two
pole repairs n(X)/d(X), P, and the exact functional

    Lambda=12P(zeta)-zeta P(0)
             -(3-zeta)P(3)-(zeta-1/3)P(1/3).          (1)

Those definitions, including every endpoint and repair, are retained.

The elementary congruences 1/6=-m, 1/3=-2m modulo p are used only after
reduction. We do not substitute them into a characteristic-zero identity
with arbitrary m. In particular define the separate integral polynomial

    V_tilde(w)=sum_(k=0)^m binom(m,k)binom(2m,k)w^k

over Z. Then V=V_tilde modulo p coefficientwise. This is because
(-m)_k(-2m)_k/(k!)^2 equals the displayed binomial product, and k! is
a unit for k<=m. This statement specifies the exact finite precision.

## 2. A terminating connection formula, proved over the integers

For every nonnegative integer m,

    V_tilde(1-u)=sum_(k=0)^m c_k u^k,
    c_k=(-1)^k binom(m,k)binom(3m-k,m).                (2)

Proof. The coefficient of u^k on the left is

    (-1)^k sum_(r=k)^m binom(m,r)binom(2m,r)binom(r,k)
    =(-1)^k binom(m,k)
        sum_(j=0)^(m-k) binom(m-k,j)binom(2m,j+k)
    =(-1)^k binom(m,k)binom(3m-k,m).

The last equality is the finite Vandermonde convolution, obtained by
replacing binom(2m,j+k) by binom(2m,2m-k-j) and taking the coefficient
of x^(2m-k) in (1+x)^(m-k)(1+x)^(2m). This proves all coefficients,
including k=0,m. Thus no infinite hypergeometric continuation is used.

In particular g=V(1)=binom(3m,m) modulo p is a unit: all factorial
arguments are at most 3m<p. Reduction of (2) also gives

    c_k=g a_k,
    a_k=(1/6)_k(1/3)_k/[(1/2)_k k!] mod p,             (3)

because the exact rational ratio is

    c_k/binom(3m,m)=(-m)_k(-2m)_k/[(-3m)_k k!].

Here -3m=1/2 modulo p. Every denominator in (3), including its
extension to k=m+1, is a unit: the first zero in (1/2)_k occurs at
k=3m+1, while m+1<=3m.

## 3. The cubic coordinate and an explicit two-index coefficient triangle

Set

    t=(z-1)/(z+1), z=(1+t)/(1-t), s=t^p,
    u=t^2,
    w=(1-u)(1-4u)^2=1-u(4u-3)^2.                    (4)

Direct substitution gives

    B=(1+3t-4t^3)/2,
    4B(1-B)=1-(4t^3-3t)^2=w,
    W(z(t))=(1-t)V(w)/(1-s).

Thus let Y(t)=V(w(t)), an even polynomial of degree 6m=p-1, and
y(u)=Y(t). Formula (2) gives the independently determined coefficients

    Y(t)=sum_(n=0)^(3m) h_n t^(2n),
    h_n=sum_(k+j=n) C_(k,j),
    C_(k,j)=(-1)^k binom(m,k)binom(3m-k,m)
             binom(2k,j)4^j(-3)^(2k-j),
    0<=k<=m, 0<=j<=2k.                              (5)

This is exactly two indices, replacing the six binomial factors in the
original z expansion. It also proves

    Y(1)=Y(-1)=Y(1/2)=Y(-1/2)=1.                     (6)

For delta^2=2, take the same marked zeta=3-2delta and put

    a=(zeta-1)/(zeta+1)=-delta/2.

Then a^2=1/2, a^p=-a, zeta=(1+a)/(1-a), and w(a)=1/2. CM0 is the
explicit further premise sum h_n2^-n=0. The conjugate mark replaces
a by -a; no term is declared base-field-valued separately.

## 4. A genuine finite two-index telescoper with fixed endpoints

For k>=0 and n>=0 define

    q(k,n)=a_k binom(2k,n-k)4^(n-k)(-3)^(3k-n),

where a_k is the characteristic-zero rational rising-product sequence
in (3). A binomial coefficient with lower argument outside 0,...,2k
is defined as zero. Define q(k,-1)=0, and the flux

    G(k,n)=[2(2n+1)/3](3k-n-1)a_k
               binom(2k,n-k+1)4^(n-k)(-3)^(3k-n).    (7)

There is no division by n-k+1 in this flux. Powers of 3 with negative
integer exponent are ordinary rational units. The exact rational
summand identity is

    (n+1)(2n+1)q(k,n+1)
       -(10n^2+5n+1)q(k,n)
       +4n(2n-1)q(k,n-1)
       =G(k+1,n)-G(k,n).                             (8)

Proof in the interior. The three rational ratios are

    q(k+1,n)/q(k,n)
      =-3(6k+1)(3k+1)(n-k)
          /[2(3k-n+1)(3k-n+2)(3k-n+3)],
    q(k,n+1)/q(k,n)=-4(3k-n)/[3(n-k+1)],
    q(k,n-1)/q(k,n)=-3(n-k)/[4(3k-n+1)].

Moreover G(k,n)/q(k,n)=2(3k-n)(2n+1)(3k-n-1)/[3(n-k+1)].
Substituting these ratios into (8), putting over a common denominator,
and cancelling gives zero. Equivalently the left-side ratio is

    (2n+1)[27k^2+18kn^2+27kn+18k-2n^3+5n+3]
       /[3(k-n-1)(3k-n+1)],

which is exactly the forward flux difference from the first ratio.

To cover the support edges, use the binomial form (7). At n=k-1
only q(k,n+1) and -G(k,n) survive, and their coefficients agree by
(-3)/4. At n=3k+1 only q(k,n-1) and G(k+1,n) survive; both equal
4(3k+1)(6k+1)a_k4^(2k). At n=3k+2, the latter flux's prefactor is
zero. At n=k, divide both sides by the nonzero rational quantity
a_k(-3)^(2k). The left side is

    -(8k/3)(k+1)(2k+1)-(10k^2+5k+1),

and the right side is

    -(6k+1)(3k+1)-(4k/3)(2k+1)(2k-1).

Both expand to -16k^3/3-18k^2-23k/3-1, including k=n=0.
For k+1<=n<=3k the interior ratio proof applies without an edge
division. Outside all these ranges the four relevant binomial
coefficients vanish. This establishes (8) for all k,n>=0 with the
stated conventions. After clearing to the binomial form, modular
reduction never divides by any of the interior ratio denominators.

Now sum over the fixed finite range k=0,...,m and reduce modulo p.
Formula (3) identifies h_n=g sum q(k,n). The lower flux G(0,n) is
zero because binom(0,n+1)=0. At the upper endpoint a_(m+1)=0 modulo p:
its numerator contains m+1/6, and all its denominators are units.
Therefore G(m+1,n)=0. This terminal zero is a derived modular fact;
the upper flux generally does not vanish in characteristic zero.

Consequently the actual finite coefficient recurrence is

    (n+1)(2n+1)h_(n+1)
       -(10n^2+5n+1)h_n+4n(2n-1)h_(n-1)=0,          (9)

with h_(-1)=0, h_0=g, and h_n=0 for n>3m. For 0<=n<3m the forward
coefficient is a unit; at n=3m it is zero and the terminal condition is

    h_(3m)=4h_(3m-1).                               (10)

The equation at n=3m+1 also holds, since its only remaining coefficient
contains 2n-1=p. One must not divide through the terminal zero.

An independent differential proof verifies the same all-index lemma.
Pull back the homogeneous finite Gauss equation

    w(1-w)V''+(1-3w/2)V'-V/18=0

under w=(1-u)(1-4u)^2. After clearing derivatives, all three coefficients
have the common factor (3/2)(4u-3)^3(4u-1)^2. Dividing in F_p(u)
and clearing the remaining polynomial equation gives

    2u(u-1)(4u-1)y''+(20u^2-15u+1)y'+(4u-1)y=0.      (11)

For example the cleared leading coefficient before division is
w(1-w)w', the middle one is (1-3w/2)(w')^2-w(1-w)w'', and the constant
one is -(w')^3/18. Each is the common factor times the corresponding
coefficient in (11). Taking [u^n] proves (9), including its endpoint
coefficients. This division is a rational-function identity, not an
evaluation at either apparent singularity.

This proves a finite Heun coefficient certificate. It does not compare
the Heun observer with R or tau and thus does not prove (T).

## 5. Exact canonical transforms of all three unit integrals

Write L_N(x)=sum_(r=1)^N x^r/r, with L_0=0, and L=L_(p-1).
Every denominator used below lies in 1,...,p-1. Define polynomials

    N_W(t)=sum_(r=1)^(3m) t^(2r)/r
                -2 sum_(n=0)^(3m) h_n L_(2n)(t),
    N_T(t)=-(1/6)L(-2t)-(1/3)L(t)
                +(1/2)sum_(n=0)^(3m)h_n4^-n L_(2n)(-2t),
    N_E(t)=-(1/3)L(t)-(2/3)L(-2t)+L(-t).              (12)

For F=W,T,E the exact normalized transformation is

    I_F(z(t))=[N_F(t)-N_F(1)]/(1-t^p)
                    -[N_F(-1)-N_F(1)]/2.             (13)

In particular the term N_F(1) is a real Frobenius pole repair and the
last term is the real zero-at-z=0 normalization. Neither can be omitted.

Proof for W. With s=t^p held fixed under differentiation,

    dI_W/dt=2/(1-s)[Y/(1-t)-(1+s)/(1-t^2)]
      =2/(1-s)[(t-t^p)/(1-t^2)
                 -sum h_n sum_(j=0)^(2n-1)t^j].

Here sum h_n=Y(1)=1, and
(t-t^p)/(1-t^2)=sum_(r=1)^(3m)t^(2r-1).
Thus its numerator primitive is precisely N_W.

For T, set b=-1/2 and use Y(b)=1. Polynomial division gives

    (Y(t)-1)/(1+2t)
      =(1/2)sum h_n sum_(j=0)^(2n-1)b^(2n-1-j)t^j.

The exact chain-rule expression is

    dI_T/dt=Y/[(1-s)(1+2t)]-1/[(1-t)(1+2t)]
      ={[(1+2t)^(p-1)-(1-t)^(p-1)]/3
              +(Y-1)/(1+2t)}/(1-s).

Integrating the displayed polynomial numerator gives N_T in (12):
the binomial coefficients of the two (p-1)st powers are (-2)^j and1,
and the divided-polynomial term integrates to
(1/2)sum h_n4^-n L_(2n)(-2t).

For E the chain rule, followed by elementary partial fractions, gives

    dI_E/dt={-(1-t)^(p-1)/3
                   +4(1+2t)^(p-1)/3-(1+t)^(p-1)}/(1-s).

The degree-(p-1) coefficient cancels, and integration gives N_E.
The N_W,N_T polynomials have degree at most p-1; N_E has degree at
most p-2. No integration divides by p.

For each F, the right side of (13) has derivative N_F'/(1-s), hence
the correct derivative. Its numerator vanishes at t=1, reducing the
possible pole order p to at most p-1. It is finite at infinity and
vanishes at t=-1, which corresponds to z=0. The original I_F(z(t))
has the same pole bound and is also finite at infinity. Their difference
has derivative zero, hence belongs to F_p(t^p). Any finite pole of a
nonconstant such function has order at least p. The bound p-1 excludes
all such poles, and finiteness at infinity excludes a polynomial part.
Thus the difference is constant and its value at -1 is zero. This proves
(13), with its full normalization, rather than just matching derivatives.

Two useful exact endpoint consequences are

    I_F(1)=-[N_F(1)+N_F(-1)]/2,
    I_F(-1)=[N_F(1)-N_F(-1)]/2.                     (14)

The second is the limit t=infinity, not a discarded branch.

## 6. The entire original pole repair and observer in the new coordinate

Put A_F=N_F(1), B_F=N_F(-1), C_F=N_F(a),
D_F=N_F(1/2), E_F=N_F(-1/2). Here the labels A,...,E are evaluations,
not the rational map A or forcing polynomial from earlier units.
The old leading pole coefficients become, by (14),

    r_+=16(A_W+B_W+A_T+B_T)/9+8(A_E+B_E)/9,
    r_-=32(A_W-B_W)/9-256(A_T-B_T)/9
                                     +64(A_E-B_E)/9,
    n_0=-(r_++r_-)/2, n_1=-(r_+-r_-)/2.             (15)

These remain the independently fixed pole repairs from the old paper.
Their contribution to (1) is exactly

    [3(9a+5)/64]n_0+[3(7a+3)/64]n_1.               (16)

For verification of this arithmetic, apply (1) to
(n_0+n_1X)/(X^2-1)^3, using X=z^p at the three rational nodes and
X=(1-a)/(1+a) at CM; reduce by a^2=1/2. This gives (16) directly.

At z=3 the old alpha,beta,chi are -1/18,-5/9,-5/72; at z=1/3 they
are 0,0,9/8. At CM, 12alpha=-2-3a, 12beta=-2, 12chi=2+3a.
Substitute (13) and (15)-(16) into the full observer (1). The resulting
weights on the three N polynomials are the following exact table:

| evaluation | N_W weight | N_T weight | N_E weight |
|---|---:|---:|---:|
| t=1 | -1/2 | 4 | 0 |
| t=-1 | 5(4a+3)/18 | -2(4a+3)/9 | 2(4a+3)/9 |
| t=a | -2a-1 | 4(a-1) | 2a+1 |
| t=1/2 | -4a/9 | -40a/9 | -5a/9 |
| t=-1/2 | 0 | 0 | -3a-2 |

This table computes Lambda, not P_hat alone. For example its CM weights
are (-2-3a)/(1+a)=-2a-1, -2/(1+a)=4(a-1), and the negative of the
first; its other weights include (16). Formula (15), the three displayed
alpha/beta/chi triples, (13), and (16) prove every table entry by ordinary
rational substitution with a^2=1/2. All denominators are units for the
stated p classes. The row at -1/2 is retained even though the original
I_E(1/3)=0; its normalized finite-log identity must be used, not silently
erased before the repair.

## 7. An explicit two-index kernel for Lambda+2q_3

Define independent q_2=(2^(p-1)-1)/p mod p as well as the retained q_3.
For 0<=n<=3m put rho_n=4^-n, and define

    K_n(a)=L_(2n)(1)+2rho_n L_(2n)(-2)
       -5(4a+3)L_(2n)(-1)/9
       -(4a+3)rho_n L_(2n)(2)/9
       +2(2a+1)L_(2n)(a)
       +2(a-1)rho_n L_(2n)(-2a)
       +8a L_(2n)(1/2)/9
       -20a rho_n L_(2n)(-1)/9,                     (17)

    Gamma(a)=-8(1+2a)q_2/3+3q_3
                                 -4aL(a)+2L(-a).    (18)

Then the fully fixed observer has the exact value

    Lambda+2q_3=Gamma(a)+sum_(n=0)^(3m)h_nK_n(a)
       =Gamma(a)+sum_(k=0)^m sum_(j=0)^(2k)
                                             C_(k,j)K_(k+j)(a). (19)

K_0=0. This is a new explicit evaluation interface with independently
fixed kernels, not a definition of OLD-R or tau.

Proof of the finite-log constants. The polynomial identity

    L(x)=[1-x^p-(1-x)^p]/p mod p

means reduction of the integral polynomial obtained after dividing its
integer coefficients by p. For rational x with unit denominator it gives

    L(1)=0, L(-1)=L(2)=-2q_2,
    L(-2)=2q_2-3q_3, L(1/2)=q_2,
    L(-1/2)=q_2-3q_3/2.

Also sum_(r=1)^(3m)1/r=L(-1)=-2q_2, because L(-1)=H_(3m)-H_(6m)
and H_(6m)=0. Reindexing r to p-r proves L(x)=-x^pL(1/x).
At a, this gives L(-2a)=-2aL(-a), while
sum_(r=1)^(3m)a^(2r)/r=L(a)+L(-a).

The pieces of (12) independent of h_n consequently have values

| t | N_W base | N_T base | N_E |
|---|---|---|---|
| 1 | -2q_2 | -q_2/3+q_3/2 | 2q_3-10q_2/3 |
| -1 | -2q_2 | q_2 | 2q_2 |
| a | L(a)+L(-a) | -L(a)/3+aL(-a)/3 | -L(a)/3+(1+4a/3)L(-a) |
| 1/2 | 2q_2-3q_3/2 | 0 | 2q_2-3q_3/2 |
| -1/2 | 2q_2-3q_3/2 | -q_2/3+q_3/2 | 2q_2/3+q_3/2 |

For N_W the indicated base is the first sum in (12), and for N_T it
is the first two terms. Substituting this table into the weights from
section 6, and adding the original 2q_3, gives (18). The h_n-dependent
pieces of N_W and N_T give exactly (17). This proves (19) with both
original q_3 contributions and all pole/interpolation terms. The
conjugate formula is obtained by a->-a. Individual K_n and Gamma may
lie in F_(p^2); only their whole combination has the inherited scalar
membership from the supplied Xi/CM theorem.

## 8. What the new certificates do and do not settle

The outstanding comparison is now explicitly

    Gamma(a)+sum_(k=0)^m sum_(j=0)^(2k)C_(k,j)K_(k+j)(a)
                      +OLD-R+6tau=0.                 (20)

Its zero is not proved. The successful telescoper (8) certifies the
coefficient triangle and its endpoint; it supplies no identity between
the kernel (17) and the independent OLD-R / adjoint forcing observers.
The finite-field Heun equation (11), its terminal relation (10), and
CM0 do not by themselves evaluate (20).

The disjoint helper also proved a different genuine higher-order
certificate for the frozen OLD-R triangle. If

    H_n=sum_(r=1)^n[1+6(n-r)]D_r, R_n=2sum_(i=1)^nB_iH_i,

then Delta^2H_n=D_n+5D_(n-1). The resulting fourth-order recurrence for
R_n, with its explicit rational initial values, is in the helper paper.
Its exact modular terminal equation is 9600(R_(m+1)-R_m)=0: it fixes
the next increment and supplies no scalar condition on R_m. This
precisely explains the limit of that successful higher-order ansatz.
No division by potentially vanishing interior polynomial coefficients
is licensed. The helper's failed polynomial factorization and single
diagonal flux concern only those expressly prescribed forms; the older
one-variable rational no-go is not promoted to a general two-variable,
higher-order, finite-field, or LIFT impossibility statement.

## 9. Executable next comparison ansatz

The new formulas allow a concrete coefficient comparison without
expanding W into six binomial indices or re-extracting 3p pole terms.
Using (3), write (20) literally as Gamma+sum_(i=0)^m v_i F_i=0, where

    F_i=g i!/(1/2)_i
           sum_(j=0)^(2i)binom(2i,j)4^j(-3)^(2i-j)K_(i+j)(a)
      +2^(1-i)sum_(r=1)^i[1+6(i-r)]D_r
      -(2/3)sum_(r=1)^(3m)(-1)^rbinom(3m,r)
                                      2^(-i-r)/(i+r). (21)

The last sum is precisely the independently defined 6tau coefficient;
the middle sum is precisely the old R coefficient. Here i+r<=4m<p,
and (1/2)_i and every old D denominator are units. The constants g and
Gamma are independently evaluated in (3) and (18), not fitted boundaries.

For a multi-flux search the usable summand ratios are the displayed
q ratios in section 4 and v_(i+1)/v_i=(i+1/6)(i+1/3)/(i+1)^2, together
with the old D ratio. Truncated logs are updated exactly by

    L_(2n+2)(x)-L_(2n)(x)
                     =x^(2n+1)/(2n+1)+x^(2n+2)/(2n+2).

Use this only for n<3m: the next update at n=3m would divide by p and
must instead be treated as the fixed terminal boundary. One can seek
an inhomogeneous discrete adjoint for (9), or simultaneous finite fluxes
for the i,j triangle and the independently fixed r kernels in (21).
Any candidate must display the i=m+1, j=0 and j=2i+1 boundaries, retain
Gamma, and use CM0 explicitly where needed. Checking the homogeneous
coefficient telescoper alone is not such a comparison certificate.

## 10. Validation and immutable scope

The included symbolic checker proves 12 exact rational algebra checks:
the summand telescoper, all three Heun pullback coefficients, recurrence
coefficients and terminal specialization, and full observer kernel / log
constants. The observer-weight script independently performs the complete
old pole repair and (1) substitution. No prime is instantiated by either.
These are corroboration of the paper proofs, not substitutes for them.

Newly proved: the exact terminating finite connection (2), the two-index
triangle (5), the summand flux (8) and modular endpoint (9)-(10), the
Heun pullback (11), canonical normalized transforms (12)-(14), the full
observer weights including pole repair, and the explicit kernel (19).
The helper contributes its independent OLD-R fourth-order recurrence.
Still unproved: (20), equivalently the original (19)/(21), LIFT, the
weighted p^3 supercongruence, raw period normalization and full native
X6 propagation. The forcing, transport and CM0 premises stay explicit.
