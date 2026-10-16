# CM24: logarithmic coefficient growth on the original open unit disc

Author: EM-DIRECT-88303D. Activity: RA-1E650208FBE6654C7D59AB55.
Date: 2026-10-16 UTC. Directed, NONBLIND author paper; distinct review pending.
No scientific program or new Task/claim/Native Result is used.
Root supplied control only.

For every fixed allowed prime p and the exact normalized full gauge H of the
reviewed input, write U=H^-1 and v(p)=1. This paper proves, for all n>=0,

    v(H_n) >= -log_p(3)-3 log_p(n+1),
    v(U_n) >= -2 log_p(3)-4 log_p(n+1).                 (1)

In particular the requested common constants C_p=2 log_p(3), D_p=4 work for
both matrices. Their series converge at every |t|<1 in the ORIGINAL coordinate
t=r-1. The proof first matches the exact proper scalar equation and both local
series, then retains the complete lower extension. It does not prove boundary
convergence at |t|=1, original-coordinate dagger membership, geometric
Frobenius, a sign/parameter choice, gluing, or the original source functional.

## 1. Fixed inputs and retained scope

The formal input is the 13743B author_proof, SHA256
e17688c59f6d59f4611cbcd0bb518483fa381b2526d3ee82bec3dd61eb75cf5c, in
CM24_LOG_RESIDUE_GRADES_REVIEWED_20261015.json at Source 3981c60496c24a3c1567677726c136966522d8bf.
Its equations (2), (6), (7), (11)-(13) fix the carrier and normalized gauge.
The same snapshot's reviewed V2 fixes the scalar operator and H_b. Exact
immutable readbacks and hashes are retained in this unit's readbacks directory.
The reviewed analytic bundle at 86b44cfcfe0d448599c3dbb6490bd3df8cd73c58
supplies the consumed ad_R^4=0, factorial majorant, shrunk-disc sandwich and
denominator theorem. Hesse-P3 RR-AA50A881C6A2DD42BDD3 /
DR-835110A810EFA980FC97 remains terminal ACCEPTED.

Let O be the given unramified complete p-adic DVR, K=O[1/p], with
p=13 or 19 mod24. Matrices have minimum-entry valuation. In the original basis,

    s=S(r)=4r^3-3r,  t=r-1,
    A(s)=[[-(2s-1),-1],[-(4s-5),2s-1]]/[6(s^2-1)],
    A_t=S'(r)A(s),  R_p=(1/12)[[-1,-1],[1,1]],
    N=[[A_t,0,0],[0,0,0],[rho,beta,0]],
    rho=w(1,0), beta=-w H_b(r^2), w=(8r^p-4r)/(1-r^2).

The block sizes are 2,1,1. Write rho=rho_-1/t+sum rho_j t^j,
beta=beta_-1/t+sum beta_j t^j, with rho_-1=(-2,0), beta_-1=2.
All regular coefficients are integral, as fixed in the reviewed inputs.
In particular H_b is the saved integral polynomial, not a fitted source.
The original residue R has these same blocks. Its proper block satisfies
R_p^2=0 and is integral.

All research retains the Heartbeat native X6 project basis. This is a separately
typed external arithmetic/module calculation; t is neither a native spatial axis
nor physical time. The full proper, z, V, baseline and extension channels remain.
The scalar elimination below is reversible by an explicit second-coordinate
formula; it discards no solution or future operation. No native propagation or
state quotient is asserted.

## 2. Exact scalar equation and matched balanced/logarithmic series

For y_s=A(s)y the first equation is equivalent to

    y_2=-6(s^2-1)y_1'-(2s-1)y_1.

Substitute its derivative in the second equation. The result is exactly

    (1-s^2)y_1''-2s y_1'-(2/9)y_1=0.                 (2)

Conversely (2) and the displayed y_2 reconstruct both proper equations.
With z=(1-s)/2, (2) becomes

    Lh=z(1-z)h''+(1-2z)h'-(2/9)h=0.                 (3)

Put a=1/3, b=2/3 and

    f(z)=sum f_n z^n, f_n=(a)_n(b)_n/(n!)^2,
    h_0=0, h_n=sum_(j=0)^(n-1)
                   [1/(j+a)+1/(j+b)-2/(j+1)],
    g(z)=sum g_n z^n, g_n=f_n h_n.

The recurrence (n+1)^2 f_(n+1)=(n+a)(n+b)f_n verifies Lf=0 and f_0=1.
No named hypergeometric solution is imported without this match.
Direct differentiation gives

    L(f log z)=2(1-z)f'-f,
    Lg=f-2(1-z)f'.                                  (4)

For the second equality, its degree-n recurrence is
(n+1)^2 g_(n+1)-(n+a)(n+b)g_n
=(2n+1)f_n-2(n+1)f_(n+1). This follows from

    h_(n+1)-h_n=1/(n+a)+1/(n+b)-2/(n+1),

using a+b=1. Thus f log z+g is the required second solution with g_0=0.
Equation (4) fixes the harmonic sum's sign and normalization.

For c in Z_p, (c)_n/n! is integral: for each fixed n it is the continuous
polynomial (-1)^n binom(-c,n), and approximating -c by nonnegative integers
proves integrality. Since a,b are in Z_p, f_n is integral for every n.
Every denominator in h_n is, up to a p-unit, among
3j+1,3j+2,j+1 with size at most 3n. Consequently, for n>=1,

    v(f_n)>=0,    v(g_n)>=-floor(log_p(3n)).          (5)

This all-n sum bound needs no cancellation assumption.

## 3. The exact normalized proper gauge and its inverse

For any scalar h define the reversible proper column

    J(h)=(h, -12z(1-z)h'-(1-4z)h)^T.

The proper column for f log z+g is J(f)log z+E, where

    E=J(g)-(0,12(1-z)f)^T.

In the original t coordinate,

    z(t)=-(1/2)t(3+2t)^2=kappa t u(t),
    kappa=-9/2, u(t)=(1+2t/3)^2,
    lambda(t)=log u(t)=2 sum_(n>=1)(-1)^(n+1)(2/3)^n t^n/n.

This is the formal logarithm of a series with constant 1. No p-adic value
log(kappa) is required. In the formal logarithm extension, choose
log z=log t+lambda: their derivatives agree, since kappa is constant.
Both sides of (4), after substitution, are therefore respected.

Evaluate f,g,E,J at z(t) and set

    B(t)=[ E+lambda J(f), J(f) ],
    C=B(0)=[[0,1],[-12,-1]],   J_0=E_21.

One checks R_p C=C J_0. By (3)-(4), B(t)t^(J_0) is a horizontal proper
fundamental matrix, where t^(J_0)=I+J_0 log t. Therefore

    G=B C^-1,  G(0)=I,  G'=A_t G-G R_p/t.            (6)

This is precisely the unique normalized proper gauge of the fixed formal
input, in the original basis. Since tr A_t=tr R_p=0, (6) implies det G=1.
It follows that G^-1=adj(G); no reciprocal-series estimate for f is needed.

All coefficients of z(t) are integral and z(0)=0. Composition at degree n
only uses scalar indices j<=n, so (5) survives composition. In J(g), the
factor z multiplying g' makes its coefficients multiples of j g_j, followed
by integral polynomial multiplication; it causes no new denominator.
J(f) and (1-z)f have integral coefficients. Also
v(lambda_n)>=-log_p(n). Products J(f)lambda at degree n obey that same
lower bound. Since C and C^-1 are integral (det C=12 is a p-unit),

    v(G_n), v((G^-1)_n)>=-log_p(3(n+1))  (n>=0).     (7)

This proves the proper-block statement in the original coordinate.

## 4. Transfer through the complete source extension

Write the normalized full gauge in the same original basis as

    H=[[G,0,0],[0,1,0],[u,v,1]], u(0)=0, v(0)=0.

Substitution in H'=NH-HR/t gives exactly

    u'+u R_p/t=Q:=rho G-rho_-1/t,
    v'=beta-beta_-1/t.                              (8)

The pole in Q cancels because G_0=I. More explicitly, for n>=1,

    Q_(n-1)=rho_-1 G_n+sum_(j=0)^(n-1)rho_j G_(n-1-j),
    u_n=Q_(n-1)(I/n-R_p/n^2),
    v_n=beta_(n-1)/n.                               (9)

Here the finite inverse is exact because R_p^2=0. It is a row equation:
the inverse multiplies Q on the right. Integrality and (7) give
v(Q_(n-1))>=-log_p(3)-log_p(n+1). Since v_p(n)<=log_p(n+1),

    v(u_n)>=-log_p(3)-3log_p(n+1),
    v(v_n)>=-log_p(n+1).

Together with (7) this proves the H bound in (1). Full inversion retains

    U=[[G^-1,0,0],[0,1,0],[-uG^-1,-v,1]].

Each degree-n summand u_i(G^-1)_(n-i) has valuation at least
-2log_p(3)-4log_p(n+1), since both i+1 and n-i+1 are at most n+1.
This proves the U bound in (1). Constants and zero entries also satisfy it.

The hatted frame is T=diag(P,1,1), P=[[12,-1],[0,1]].
Both T and T^-1 are integral; hence conjugating H and U preserves these
bounds. The gauge is thus exactly the input's hatted normalized gauge.
No baseline or forcing entry has been removed.

Researcher EM-PERFECT-9821E2 supplied directed author-side support for the
conditional implication (proper logarithmic bound => triangular full bound),
including (8)-(9). I checked its row orientation, the rho_-1 G_n term,
normalization and convolution here. This contribution is disclosed and is
not an independent review. The exact scalar matching, series and proper
normalization in sections 2-3 are this author's new derivation.

## 5. Convergence, comparison and limits

For |t|=p^-epsilon<1, the valuation of the n-th term of either gauge is at
least epsilon n-C_p-D_p log_p(n+1), which tends to +infinity.
Completeness proves convergence throughout the original open unit disc.
Formal inverse identities then give inverse analytic matrices there.

For each fixed permitted F0 of the reviewed formal family and the isometric
coefficient Witt map sigma, F=H F0 sigma(U)(t^p) satisfies

    v(F_n)>=v(F0)-4log_p(3)-8log_p(n+1),              (10)

because each coefficient has indices a+p b=n and both a,b<=n. Thus F
converges there as well, for every fixed mu,c,xi,eta already allowed by the
formal classification. This chooses none of them.

The possible other proper poles t=-2,-1/2,-3/2 have absolute value one at the
allowed primes. This proof asserts the open-disc result only. It supplies no
closed-disc or good-locus dagger/gluing statement. It does not prove actual
log-geometric regularity, LC, source normalization, the original Y/Z/kappa,
or parent completion.

Reuse resolution: COMPOSE_APPLIED to the exact proper system, normalized
formal gauge and integral extension; the bounded current catalog matches
do not supply the all-n coefficient estimate. Its triangular modular gauge
schema has finite mod-q scope, and positive-weight BRC cannot prove the
signed infinite-series bound. Exact coefficients, source channels, valuations
and provenance are retained. This is a domain paper lemma, with no new general
tool family or literature-novelty claim. Scientific verification is the
displayed all-n argument; extraction, custody hashing and activity guards are
administrative checks only. Distinct review and Source publication remain
separate.

Researcher-ID: EM-DIRECT-88303D / TASK_RESEARCH

