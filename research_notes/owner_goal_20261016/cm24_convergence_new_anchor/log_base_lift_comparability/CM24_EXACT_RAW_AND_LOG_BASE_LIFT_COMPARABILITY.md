# CM24: the raw lift and the logarithmic lift have different boundary types

2026-10-16 UTC. Author EM-DIRECT-88303D, direct TASK_RESEARCH.
New bounded paper candidate; UNREVIEWED. No scientific program was used.

**Result.** The saved full formal Frobenius already uses theta(t)=t^p,
exactly the parameter lift of the new LC-D log-PD paper. The older
Kummer comparison instead uses r->r^p. In t=r-1 this is
tau(t)=(1+t)^p-1. For every n>=2, tau is not a morphism of the
standard log base with chart N->(O/p^n)[[t]], 1->t. After inverting p
its logarithmic ramification is 1, whereas theta has ramification p.
Consequently a regular invertible comparison matrix for a nonzero
residue cannot be reused unchanged for both lifts. This is a precise
nontransfer test, not nonexistence of crystalline Frobenius.

## 1. The actual source maps, before any comparison

Keep the original allowed primes p=13 or19 mod24. Let O be the
unramified complete p-adic DVR of the saved formal paper, K=O[1/p],
and sigma its coefficient Witt lift. Set A_n=(O/p^n)[[t]]. Where the
LC-D paper uses Z_p coefficients, its specified base lift is the
restriction of the following theta. No cohomological base-change
theorem to a larger O is assumed here.

These are three different source statements, checked in their bodies:

1. The old Kummer paper, 14956B/e364fcaa..., sections4-5, explicitly
   fixes the ambient lift phi(r)=r^p on its punctured weak completion.
2. The saved full formal paper, 13743B/e17688c5..., section1, explicitly
   fixes t=r-1 and theta(t)=t^p, hence theta(r)=1+(r-1)^p. It expressly
   distinguishes this from the old ambient lift. Its residue relation
   R F_0=p F_0 R and formal classification use THIS theta.
3. The LC-D log-PD paper, actual Source09cf0b04..., 19244B/32d6cb01...,
   section4, fixes theta(t)=t^p and sends the base log generator to p
   times itself. Its coefficient map on Z_p is the identity.

Thus the saved formal construction is not a raw-tau construction
awaiting a change of lift. The two theta statements have the same
parameter lift. Identifying coefficient actions, bases, variance and
cohomology realizations remains separate from identifying that lift.
Exact full source/body pins and bounded dedup are in SOURCE_AND_REUSE.json.

## 2. A finite-level obstruction on the standard log base

Give Spec A_n the associated log structure of the chart N->A_n,
1->t. At its closed point the log monoid is A_n^times times N:
no positive power of t is a unit. A lift of a local ring endomorphism
to this log structure must therefore send the generator to (u,k),
with u a ring unit and k a nonnegative integer. Its ring image must be

    t |-> u(t) t^k.                                      (1)

This is a necessary condition even at the closed stalk, so its failure
precludes a global morphism of these specified log bases. The ring is
local and a power-series unit has unit constant coefficient.

For the raw lift expressed in the actual boundary parameter,

    tau(t)=(1+t)^p-1
          =p t+binom(p,2)t^2+...+t^p.                    (2)

If n>=2, its coefficient of t is nonzero p, which is not a unit.
In (1), k=0 would give a nonzero unit constant term, contradicting
tau(0)=0. For k>=2 the coefficient of t would be zero, contradicting
(2). For k=1 the constant term of u would be p, again contradicting
that u is a unit. These cases exhaust N. Hence no such (u,k) exists.

The identical argument works over O[[t]]. Modulo p the situation is
different: tau(t)=t^p, so k=p,u=1 is a log lift. The obstruction begins
at precision p^2 and persists at every higher precision. It is not a
claim about a different log structure or a changed boundary parameter.

Theta(t)=t^p satisfies (1) with k=p,u=1 at every precision. Therefore
tau and theta are congruent modulo p as ring maps, but cannot simply
be treated as two log-PD endomorphisms of this same integral log base.
This conclusion uses the chart condition, not a new PD/cohomology theorem.

## 3. Why punctured validity and characteristic-zero residue differ

For 1<=j<=p-1, binom(p,j) is divisible by p. Thus in A_n[t^-1],

    tau(t)/t^p=1+p h(t),
    h(t)=sum_(j=1)^(p-1) [binom(p,j)/p] t^(j-p).       (3)

This is a unit: its inverse is the finite sum
sum_(i=0)^(n-1)(-p h)^i. Consequently the chart obstruction disappears
on this punctured locus, where the t-log structure is trivial. The
old punctured Kummer construction is not invalidated by section2.
No new claim about its weak convergence or normalization is made.

Over K[[t]], equation (2) instead factors as

    tau(t)=t u_K(t), u_K(0)=p in K^times.              (4)

It has order1, and dlog tau=dt/t+du_K/u_K. Theta has orderp and
dlog theta=p dt/t. Inverting p changes the unit test; it does not
make these two logarithmic ramification factors equal. In particular
tau(t)/t^p has a pole of order p-1 over K[[t]], rather than being a
regular boundary unit. Finite-level punctured inverses in (3) must
not be silently interpreted as such a regular characteristic-zero unit.

## 4. An exact unchanged-matrix nontransfer lemma

Let N(t)=R/t+B(t), with B in Mat_d(K[[t]]), sigma(R)=R and R nonzero.
Use solution-transport convention. Suppose F in GL_d(K[[t]]) solves

    F'=N F-F theta'(t) sigma(N)(theta(t)).            (5)

Its constant matrix F_0 is invertible. The pole coefficient of (5)
is R F_0=p F_0 R. For tau, (4) shows that the pullback of the residue
term has coefficient R/t; the pullback of B is regular. Therefore a
regular solution of the corresponding tau equation must satisfy

    R F_0=F_0 R.                                    (6)

The SAME matrix F cannot satisfy both equations: subtracting their
residue conditions gives (p-1)F_0 R=0, impossible in K because F_0 is
invertible and R is nonzero. The saved full residue has these exact
hypotheses; its rational entries are sigma-fixed and its proper
2-by-2 block is (1/12)[[-1,-1],[1,1]], which is nonzero.

This lemma rules out unchanged reuse, including a proposed identical
regular boundary matrix. It does not rule out two different matrices
or an explicitly proved change-of-lift comparison. Nilpotent R and
pR can be conjugate over K; no obstruction to every possible gauge
is inferred. An irregular/punctured comparison is outside (5)-(6).

## 5. The legitimate same-lift matrix interface

There is no lift obstruction between the actual saved formal theta
and the LC-D paper's theta. To state the usable matrix interface
without identifying different cohomology objects, suppose its concrete
matrix M and connection B satisfy, in a stated common coefficient ring,

    delta M+B M=p M theta(B), delta=t d/dt,
    det M=p.                                        (7)

Set G=(M^T)^(-1). Direct differentiation, using (7), gives

    delta G=B^T G-p G theta(B)^T.                    (8)

If N_proper=B^T/t, (8) is precisely the proper solution-transport
equation for theta, with det G=1/p. For the displayed LC-D connection
C(s) and saved formal A(s), their literal matrices satisfy A=C^T.
This checks variance and parameter compatibility at the matrix level;
it neither imports a raw-tau matrix nor proves a new PD-site theorem.
No assertion that an independently named full/global realization is
this module follows. The two full extension constants, their source
normalization, a geometric full comparison and the original functional
still require their actual bridges. No value of mu is selected here.

The n>=2 obstruction in section2 concerns only the raw lift on the
specified integral log base. It does not deny the intrinsic crystalline
Frobenius already constructed through theta and embedding systems,
does not strengthen the older fixed-central-representative node no-go,
and does not alter any accepted CM24 unit. Native Heartbeat X6 semantics
are retained; t,r and n are external arithmetic observers, not spatial
axes or physical time. All parents remain OPEN.

Researcher-ID: EM-DIRECT-88303D / TASK_RESEARCH
