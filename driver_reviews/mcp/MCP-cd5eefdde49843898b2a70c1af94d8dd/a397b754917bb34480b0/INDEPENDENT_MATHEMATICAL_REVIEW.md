# Independent CM24 fixed-triangle flux and terminal review

Verdict: **PASS at the stated conditional finite auxiliary-arithmetic scope.** No mathematical error was found in equations (1)–(21), their legal windows, or the formulation of the remaining equation (22). The scalar comparison and all global mathematical parents remain **OPEN**.

This review is a directed local auxiliary review under Root's current Driver scope. It creates no native identity, Task, Claim, Result, acceptance, or publication authority. The finite fields and differential polynomials are external classical arithmetic observers. Native Heartbeat X6 and separately typed time are unchanged. The frozen Heun/CM premises are retained rather than reproved.

## Literal normalization and fixed triangle

The retained premises are `p=6m+1`, `N=3m`, `h_0=h_N=g=binom(3m,m) != 0`, and `sum h_n=1`. In particular, no step replaces `g` by 1. The actual fixed triangle can be reconstructed from the integer connection formula

    Vtilde(1-u) = sum_{k=0}^m c_k u^k,
    c_k = (-1)^k binom(m,k) binom(3m-k,m).

The coefficient formula follows by expanding `(1-u)^r`, using `binom(m,r)binom(r,k)=binom(m,k)binom(m-k,r-k)`, and applying finite Vandermonde. Its rational ratio is

    c_k/g = (-m)_k(-2m)_k / [(-3m)_k k!].

Only after reduction modulo `p=6m+1` do these parameters become `1/6`, `1/3`, and `1/2`. Thus `c_k=g a_k` in the field. Since the old cubic is `w(x)=1-z(x)`, the coefficient triangle is

    h_n = g sum_{k+j=n} a_k b_(k,j),
    b_(k,j)=binom(2k,j)4^j(-3)^(2k-j).

Both `j=0` and `j=2k` remain present. Consequently `sum h_n beta_n=g sum a_k T_k`; taking the constant observer gives `sum a_k=1/g`, because `sum_j b_(k,j)=z(1)^k=1`. This is a consequence of the frozen normalization, not a new scalar normalization.

For either finite functional `I_c` or `J_c`, the polynomial representation of the harmonic prefix is `(1-x^n)/(1-x)`. Linearity and `sum_j b_(k,j)x^(k+j)=z(x)^k` give equation (3). Subtracting consecutive rows uses the exact identity `1-z(x)=(1-x)(1-4x)^2`, giving

    T_(k+1)-T_k = U_k+V_k,  0<=k<m.

The largest polynomial degree is `3k+2<=N-1`; the denominators are at most `N` for `I` and `p-2` for `J`. The top increment uses `beta_N` and no extrapolated observer. Direct polynomial moments give `U_0=-23/36`, `V_0=308/45`, and increment `1117/180`.

## H/O polynomial fluxes

The flux subreview independently solved a coefficient ansatz `R=(4x-3)S`, `deg S<=4`, with the displayed `D_H` or `D_O` fixing the scale. The solved `B` and all coefficients of both `R` polynomials match the paper. This reconstructs the fluxes without deriving them from the scalar target. The cleared all-symbolic derivative rows, six endpoint values, and the combined sources were checked exactly. The factor `4x-3` makes the cleared rows polynomial identities, so no pointwise division at a critical point is used.

The legal simultaneous window is exactly `0<=k<=m-2`. In that window, the H primitive degree is at most `3k+6<=N`; the odd primitive degree is at most `6k+11<=p-2`. Every factor divided out in `D_H` and `D_O` is a nonzero integer smaller than `p`. Combining the endpoints leaves precisely the actual phases 1 and `1/2`, with sources

    2^(-k)(9k^2+30k+26)-9k-86/3,
    2^(1-k)(36k^2+96k+67)+144k+656/3.

These facts establish equations (6)–(11). They do not identify these systems with OLD-R or evaluate the scalar comparison. The extra H-only terminal value is legal but does not authorize a next J moment or `T_(m+1)`.

## Genuine Frobenius terminal

At `k=m-1`, reduction gives `k=-7/6`, `D_O=0`, `B_O=8`, and

    R_T(x)=4(4x-3)(16x^2-8x-1).

Set `G=z^(m-1)R_T`. Its degree is exactly `N`, with leading coefficient `C_top=16^(m+1)`, a unit. The specialized polynomial identity is

    (1+2x d/dx)G = -16 f_(m-1).

The top coefficient is killed because `1+2N=p`. Equivalently, `tG(t^2)` has degree exactly `p` and a nonzero `t^p` term. Removing that explicit term gives a legal canonical odd primitive of degree at most `p-2`. Coefficientwise integration therefore gives

    16 J_c(f_(m-1)) = C_top c^(N+1)-c z(c)^(m-1)R_T(c).

The sign and coefficient of the Frobenius correction are correct. It is a derivative-kernel term rather than an arbitrary constant. Under the retained marked-branch relations `2^N=-1`, `4^N=1`, the three terminal moments are exactly those in equation (15), and combining their literal coefficients gives

    V_(m-1)=(16^m-19)/3-2^(1-m).

An additional independent check shows why `J_c(f_m)` cannot be silently assigned. The coefficient of `x^N` in `f_m` is

    16^m(18m^2+3m+1),

which reduces to the nonzero unit `16^m` when `m=-1/6`. Its J denominator is `2N+1=p`. Thus the undefined next moment has a genuine obstruction; zeroing its product with `D_O` would omit the Frobenius correction.

## Gauss adjoint, literal OLD-R and tau

The independent coefficient ratio gives `lambda_k a_(k+1)=mu_k a_k`, with `lambda=9(k+1)(2k+1)` and `mu=(6k+1)(3k+1)`. The finite last row is literally zero; no `a_(m+1)` is used. The canonical forcing construction produces the prefix flux

    j_k=-sum_{r=0}^k a_r,  k<m.

At the last adjoint row, `a_m(K*F)_m=j_(m-1)=a_m-1/g`. Hence the exact forced terminal defect is `1-(g a_m)^(-1)delta_m`. This agrees with the Green sign and with the nonzero retained total. The preserved Heun defect `g^(-1)` remains separate.

For any prescribed finite vector, ordinary finite summation by parts with this prefix flux gives equation (19). A free-vector coefficient check found the exact remainder before imposing normalization:

    (g sum a_k-1)(T_m+2W_m/g).

It vanishes under the retained `sum a=1/g`, confirming every literal g factor in equation (21).

OLD-R is unchanged because `a_k t_k=v_k 2^(-k)` coefficientwise. Its actual triangle difference is `Htri_k-Htri_(k-1)=D_k+6Ptri_(k-1)`, and `t_k/t_(k-1)=(2k-1)/(4k)` gives precisely the displayed `Z_k`. The diagonal coefficient is 1, so `D_m` is retained. At the lower boundary, `D_1=1/10`, `t_1=1/4`, and `Z_1=1/40`. All indicated denominators are units.

The tau carrier is also unchanged. With the frozen `w(t)`, `P(t)` and `E(t)=t(4t^2-3)C(w(t))/6`, independent polynomial checks give the original concomitant coefficients `w(1-w)` and `w/2`. At `a^2=1/2`, the CV' prefactor is exactly `1/4`; using the frozen CM zero removes the terms containing V. Thus the boundary is the original `-tau`, and its coefficient remains `6tau`.

## Exact residual and remaining lemma

Applying the same endpoint-correct summation identity to T and W gives exactly

    kappa+sum h_n beta_n+OLD-R+6tau
      = kappa+T_m+2W_m/g+6tau
        +sum_{k=1}^m a_k lambda_(k-1)F_(k-1)
                       [g(U_(k-1)+V_(k-1))+2Z_k].

Therefore equation (22) is precisely the remaining assertion that the final pairing equals `-kappa-T_m-2W_m/g-6tau`. It is equivalent to the original scalar comparison under the retained premises and proved identities. It has not been proved, disproved, or fitted. A future proof must retain the Heun defect, Gauss defect, odd Frobenius correction, and original tau boundary together. Existence of the adjoints alone provides no vanishing theorem.

## Evidence and limits

The new independent work passed **139 exact symbolic checks**: 100 fixed-triangle/H/O flux checks and 39 terminal/Gauss/OLD-R/tau/residual checks. These are independent scripts and are not the author's reported 222 checks. No prime instance, old prime campaign, scalar fit, or provider query was used. Author/frozen checker source was not inspected, imported, or executed; checker bytes were hashed only as part of the pin audit.

All 50 deduplicated declared current/frozen paths matched before and after review, including the 36 frozen manifest entries. No reviewed input was changed. Receipts and reproducible independent scripts are saved in this directory. The verdict is conditional on the explicitly retained frozen Heun/CM inputs and literal normalization; it does not promote the scalar comparison, LIFT, weighted p^3, raw period normalization, or complete native X6 propagation.
