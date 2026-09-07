# #1162 — branch-only rational Renyi recursion and orientation-degeneracy bridge

Status: RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-branch-renyi-rational-recursion-orientation-degeneracy-20260908
At: 2026-09-08T01:35:00+08:00
Parents:
- `research_notes/1158_1162_viete_probability_internal_basel_bridge_20260908.md`
- `research_notes/1162_alias_prime_valuation_thickness_semigroup_20260908.md`

## 1. Dyadic local probability algebra

Use the antiperiodic tree with the root inverse mass normalized to probability 1. At a refinement step from a cycle of size M to 2M, let p be a parent probability and p_+,p_- its two child probabilities.

The finite inverse-mass identities imply

p_+ + p_- = p,

p_+ p_- = p/M^2.

Therefore the child r-th power sum is the Lucas polynomial

p_+^r+p_-^r
=
sum_(j=0)^floor(r/2)
A_(r,j) M^(-2j) p^(r-j),

A_(r,j)=(-1)^j r/(r-j) binom(r-j,j).

This is exact finite branch algebra and uses no derivative or continuum interpolation.

## 2. Global finite Renyi recursion

At depth d set M=2^(d+1), t=4^(-d), and

R_r(d)=sum_a p_(d,a)^r.

Then

R_r(d+1)
=
sum_(j=0)^floor(r/2)
A_(r,j) M^(-2j) R_(r-j)(d).

Equivalently there is a polynomial F_r in Q[t], degree at most r-1, such that

R_r(d)=F_r(4^(-d)),

F_r(1)=1,

and

F_r(t/4)
=
sum_(j=0)^floor(r/2)
A_(r,j) (t/4)^j F_(r-j)(t).

For coefficients F_r(t)=sum_(k=0)^(r-1)b_(r,k)t^k, k>=1 is determined triangularly by

(4^(-k)-1)b_(r,k)
=
sum_(j=1)^min(floor(r/2),k)
A_(r,j)4^(-j)b_(r-j,k-j),

with b_(r,0)=1-sum_(k>=1)b_(r,k).

Hence every boundary integer Renyi moment

M_r=lim_d R_r(d)=F_r(0)=b_(r,0)

is rational by finite rational recursion.

First values:

M_1=1,
M_2=1/3,
M_3=2/15,
M_4=17/315,
M_5=62/2835,
M_6=1382/155925.

## 3. Internal even-zeta ratios from branch splitting alone

The #1158/#1162 bridge gives the internal boundary atom law

P(L=ell)=4/[Pi_rot^2(2ell+1)^2].

Therefore

M_r
=2(4^r-1) zeta(2r)/Pi_rot^(2r).

Thus

zeta(2r)/Pi_rot^(2r)=M_r/[2(4^r-1)].

The rationality of all even-zeta/Pi_rot ratios is therefore derivable from branch probability recursion itself, independently of the finite determinant/Newton route. The determinant route is a second exact carrier and cross-check.

For r=6,

M_6=1382/155925

contains twice the Bernoulli numerator 691; division by `2(4^6-1)` yields the same rational zeta(12)/Pi_rot^12 ratio as the determinant route.

## 4. Orientation quotient and the factor 2 in Euler normalization

The signed alias carrier is L in Z. The positive odd magnitude quotient is

K=|2L+1|.

Each positive odd K has two signed preimages:

K=2n+1 <- {L=n, L=-n-1},

with equal probabilities.

In particular the #1158 principal Viète atom is one orientation:

P(L=0)=4/Pi_rot^2.

The multiplicative prime-valuation event with every odd-prime valuation zero is K=1, which merges two orientations:

P(K=1)=P(L=0)+P(L=-1)=8/Pi_rot^2.

Since independent prime valuations give

P(K=1)=prod_(p odd)(1-p^(-2)),

we get the internal Euler normalization

prod_(p odd)(1-p^(-2))=8/Pi_rot^2.

Thus the factor 2 between the principal Viète atom and the Euler no-prime event is exactly the orientation degeneracy of the quotient L -> K. Boolean support alone would lose this multiplicity and is not an admissible carrier for the mass observer.

## 5. BRC significance

This note supplies two direct BRC examples:

1. moment transfer: finite branch shape determines the full rational Renyi hierarchy; total mass alone preserves only r=1;
2. quotient multiplicity: collapsing signed aliases to absolute odd magnitude is safe only if the two-preimage degeneracy is retained in the positive mass.

No new BRC Foundation theorem is claimed. The current positive-rational histogram implementation does not directly ingest the cyclotomic branch probabilities, but the typing law is exactly the existing count/mass/multiplicity discipline.

## 6. Status / next

Classical Lucas polynomials, Renyi moments, Euler products and even-zeta rationality are prior mathematics. The project synthesis is the derivation from one finite alias branch process and the exact observer/multiplicity accounting.

Next:
1. derive finite-depth rational approximants M_r(d) explicitly and compare their monotone direction with the general `(alpha,s)` rough phase;
2. map #1159 Wallis finite products, if possible, to a finite statistic of the signed-vs-magnitude quotient rather than only the common completion;
3. extend the orientation-degeneracy accounting to rational holonomy phases with larger symmetry orbits.
