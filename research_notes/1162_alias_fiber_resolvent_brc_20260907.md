# #1162 — alias-fiber conservation, exact resolvent refinement, and derivative-free Basel branch proof

Status: RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-alias-fiber-resolvent-brc-20260907
At: 2026-09-07T23:56:00+08:00

## 1. Scope correction consumed

This note continues `research_notes/1162_resolution_admissibility_correction_20260907_b62d.md` and preserves the user correction that microscopic/high-order differentiation is not automatically a stable observable under the project's rough finite-resolution relation. The present route therefore uses only finite cycle matrices, integer refinement, finite rational probes, Schur elimination, and branch conservation. Classical trigonometric/continuum limits are used only as a typed compatibility layer at the final Basel calibration.

## 2. Finite cycle operator and alias fibers

For circumference parameter L>0 define the N-cycle operator

A_N=(N/L)^2(2I-R_N-R_N^*)

with eigenvalues

lambda_(N,k)=4N^2/L^2 * sin^2(pi k/N).

Under integer refinement N -> qN, partition fine modes into exact alias fibers

k+rN, r=0,...,q-1.

For every nonzero coarse k=1,...,N-1,

sum_(r=0)^(q-1) lambda_(qN,k+rN)^(-1)=lambda_(N,k)^(-1).

Equivalently, inverse spectral mass is conserved fiber-by-fiber. This is the finite csc-square multiplication identity expressed in the refinement carrier.

The zero coarse fiber is singular. Its nonzero fine children have total

sum_(r=1)^(q-1) lambda_(qN,rN)^(-1)=L^2/(12N^2)*(1-q^(-2)).

Define the unresolved zero-fiber potential

Z_N=L^2/(12N^2).

Then

Z_N = [released nonzero child mass] + Z_(qN).

Therefore

I_N := Tr'(A_N^(-1)) + Z_N

is refinement invariant for every integer q>=2. Since N=1 has no nonzero mode,

I_N=L^2/12,

hence the exact finite trace formula

Tr'(A_N^(-1))=L^2/12*(1-N^(-2)).

No N-derivative or interpolation is used.

## 3. BRC moment consequence: p=1 is the unique additive moment

Fix a nonzero parent fiber and put

x_r=lambda_(qN,k+rN)^(-1)>0,

x=lambda_(N,k)^(-1).

The exact conservation law is sum x_r=x. Hence for every real p>0,

sum x_r^p > x^p for 0<p<1,
sum x_r^p = x for p=1,
sum x_r^p < x^p for p>1,

with strict inequalities when q>1. Thus inverse-first spectral mass is the unique positive moment observer exactly additive under alias refinement. Higher inverse moments contract under branch splitting; sublinear moments expand.

This is an exact Weighted-BRC branch statement, not a differential criticality heuristic.

## 4. Consistent probability tree

For fixed nonzero k, at depth m of repeated q-refinement write descendants as

k+aN, a=0,...,q^m-1,

and masses

x_(m,a)=lambda_(q^m N,k+aN)^(-1).

Then sum_a x_(m,a)=lambda_(N,k)^(-1) at every depth. Normalizing gives consistent cylinder probabilities

p_(m,a)=x_(m,a)/lambda_(N,k)^(-1).

The child transition is exactly

Pr[a -> a+r q^m] = x_(m+1,a+r q^m)/x_(m,a).

Therefore a genuine common probability space / nested-cylinder refinement process exists; this satisfies the project's martingale/transport discipline rather than using martingale language informally.

## 5. Dyadic branch-boundary proof of Basel

Set L=1 and start from the unique nonzero mode of C_2:

lambda_(2,1)=16,

so its inverse branch mass is 1/16.

After m further dyadic refinements, its descendants are exactly the odd indices j of the 2^(m+1)-cycle, and finite fiber conservation gives

sum_(1<=j<2^(m+1), j odd) lambda_(2^(m+1),j)^(-1)=1/16

for every finite m.

For each fixed odd positive j,

lambda_(M,j)^(-1) -> 1/(4 pi^2 j^2),

and the opposite endpoint M-j supplies the negative frequency. The middle-tail mass is uniformly bounded using

sin(pi j/M)>=2j/M for 0<=j<=M/2:

sum_(R<j<M-R, j odd) lambda_(M,j)^(-1) <= (1/8) sum_(n>R) 1/n^2 <= 1/(8R).

Hence the finite branch mass has the boundary decomposition

1/16 = 1/(4 pi^2) * sum_(ell in Z, ell odd) 1/ell^2.

Therefore

sum_(n>=0)1/(2n+1)^2 = pi^2/8,

and the elementary odd/even split

zeta(2)=sum_odd n^(-2)+(1/4)zeta(2)

gives zeta(2)=pi^2/6.

The native finite part of the proof is the exact positive alias tree. The pi/Fourier endpoint identification is an explicit classical compatibility step, not silently imported into the finite carrier.

## 6. Exact finite resolvent RG

For u>0 define

R_N(u)=Tr(A_N+uI)^(-1).

Let

a_N=L^2/(4N^2),

y=1+2a_N u/q^2.

Define

u_(q,N)(u) = [T_q(y)-1]/(2a_N),

Z_(q,N)(u) = U_(q-1)(y)/q,

where T_q and U_(q-1) are Chebyshev polynomials. Then the exact finite identity is

R_(qN)(u)=Z_(q,N)(u) R_N(nu_(q,N)(u)).

With L=1,

nu_(q,N)(u)=2N^2[T_q(1+u/(2q^2N^2))-1],

Z_(q,N)(u)=q^(-1)U_(q-1)(1+u/(2q^2N^2)).

For q=2 this becomes the rational law

R_(2N)(u)=(1+u/(8N^2)) R_N(u+u^2/(16N^2)).

Thus rational N,q,u remain in exact rational arithmetic. Since A_N+uI has rational entries for L=1, R_N(u) is rational.

## 7. Schur / port-collapse form

Retain every q-th vertex of the qN-cycle and Schur-eliminate the remaining vertices. The exact matrix identity is

Schur_retained(A_(qN)+uI)
=
[q/Z_(q,N)(u)] [A_N+nu_(q,N)(u)I].

Hence the Chebyshev probe map is the exact finite operator left on the retained ports after hidden-state elimination.

For L=1,

A_N+uI=(2N^2+u)(I-W_N(u)),

where W_N(u) is nonnegative rational with clockwise/counterclockwise edge weight

N^2/(2N^2+u)

and row sum 2N^2/(2N^2+u)<1. Therefore this finite positive-rational resolvent problem lies inside the stable recurrent BRC domain.

Reuse resolution: COMPOSE_APPLIED with `src/enterprise_math/brc_weighted_recurrent.py`, `src/enterprise_math/brc_recurrent_invariants.py`, and especially `src/enterprise_math/brc_recurrent_ports.py`; the latter performs exact Schur port collapse for stable positive-rational hidden blocks. The present cycle/Chebyshev formulas identify the closed-form signature of that existing port operation. No new top-level BRC family is claimed.

## 8. Semigroup / path independence

The exact finite refinement maps compose because Chebyshev polynomials compose. Equivalently, eliminating hidden vertices in stages or in one step gives the same Schur complement. Therefore the finite resolvent transport is path-independent under integer refinement.

At u=0 the nonzero-fiber law is strict mass conservation, while the zero fiber carries the residual potential Z_N and releases positive mass under refinement.

## 9. Status and next frontier

Proved finite identities / elementary consequences:
- nonzero alias-fiber inverse-mass conservation;
- zero-fiber residual conservation;
- exact finite trace invariant;
- unique p=1 additive positive moment;
- consistent BRC probability tree;
- derivative-free dyadic Basel branch proof with explicit uniform tail bound;
- exact positive-u resolvent RG and Schur-collapse identity.

No novelty claim or Foundation promotion is made here.

Next: derive the full boundary law of the q-adic refinement probability tree. In particular prove that the boundary measure is supported on the embedded integer aliases and identify its weights directly from finite refinement. Then test whether rational-holonomy/Dirichlet character packets can be obtained as finite BRC quotients of this same boundary tree without reintroducing unstable analytic differentiation.
