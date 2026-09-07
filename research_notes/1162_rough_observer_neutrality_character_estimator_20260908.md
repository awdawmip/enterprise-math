# #1162 — rough-observer neutrality and derivative-free finite character estimators

Status: RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-rough-observer-neutrality-character-estimator-20260908
At: 2026-09-08T00:40:00+08:00
Parents:
- `research_notes/1162_alias_boundary_renyi_observer_lattice_20260907.md`
- `research_notes/1162_q_chain_markov_gauge_stabilization_20260908.md`

## 1. Two-dimensional neutrality theorem

Let a parent positive branch mass x split into positive child masses x_r with sum x, and let child alias labels be distinct. Consider the power-family observer

O_(alpha,s)=sum_r x_r^alpha |ell_r+theta|^(2-s).

Require invariance under arbitrary admissible positive redistributions of a fixed total mass among distinct labels, i.e. robustness to both branch splitting and loss of unresolved alias provenance.

Mass additivity for all positive splits forces alpha=1. Label blindness for distinct alias magnitudes forces the label exponent 2-s=0, hence s=2.

Therefore the unique universal neutral power observer is

(alpha,s)=(1,2).

Interpretation: Basel sits at the intersection of the unique additive branch-mass moment and the unique label-independent zeta/Hurwitz readout. This statement is finite and quotient-based; it does not use microscopic differentiation.

## 2. Finite centered alias estimator for real Dirichlet characters

Let chi mod d be a real Dirichlet character with parity chi(-1)=(-1)^a. Let M be an even multiple of d. For each fine mode j=1,...,M-1 choose its centered integer alias n_j in (-M/2,M/2], with the Nyquist term harmless because M/2 is divisible by d when M/d is even.

Define the finite branch estimator

Lhat_M(s,chi)
=
2pi^2 sum_(j=1)^(M-1)
lambda_(M,j)^(-1)
chi(j) sgn(n_j)^a |n_j|^(2-s),

with circumference normalization L=1.

Pairing centered modes +/-n gives the explicit finite formula

Lhat_M(s,chi)
=
sum_(1<=n<M/2)
chi(n)n^(-s)
[(pi n/M)/sin(pi n/M)]^2.

No holonomy derivative is used. The character is a retained integer-label observer on the common positive inverse-square branch mass.

For every s>1,

Lhat_M(s,chi) -> L(s,chi)

as M -> infinity through even multiples of d.

## 3. Universal explicit error bound

For 0<x<=pi/2,

sin x >= x(1-x^2/6).

Hence with

C0=pi^2/[3(1-pi^2/24)^2],

`[(x/sin x)^2-1] <= C0 * n^2/M^2`

after x=pi n/M.

Using |chi(n)|<=1 and K=M/2 gives the fully explicit bound

|Lhat_M(s,chi)-L(s,chi)|
<=
C0/M^2 sum_(n=1)^(K-1) n^(2-s)
+ K^(-s)+K^(1-s)/(s-1).

This is coarse but uniform in the real character and contains no microscopic derivative or interpolation error.

## 4. Exact finite sector at s=2

If chi is even, then at s=2 the alias label power is constant and chi is constant under +/- pairing. Fiber mass conservation therefore gives

Lhat_M(2,chi)=L(2,chi)

for every allowed finite M.

Equivalently,

L(2,chi)=2pi^2 sum_(b=1)^(d-1) chi(b) lambda_(d,b)^(-1)
=pi^2/(2d^2) sum_b chi(b)csc^2(pi b/d).

Thus the exact total/residue-only finite sector is precisely `s=2 + even character`. Odd characters at s=2 require endpoint orientation provenance; higher s require alias magnitude provenance.

## 5. Riemann zeta one-sided finite certificates

For dyadic M>=4 define

zhat_M(s)=1/(1-2^(-s))
sum_(1<=n<M/2, n odd)
n^(-s)[(pi n/M)/sin(pi n/M)]^2.

Finite branch splitting gives

- 1<s<2: zhat_M(s)<zeta(s), increasing under refinement;
- s=2: zhat_M(2)=zeta(2)=pi^2/6 for every M;
- s>2: zhat_M(s)>zeta(s), decreasing under refinement.

Explicit one-sided errors:

for 1<s<2,

0<zeta(s)-zhat_M(s)
<= [K^(-s)+K^(1-s)/(s-1)]/(1-2^(-s));

for s>2,

0<zhat_M(s)-zeta(s)
<= C0/[M^2(1-2^(-s))] sum_(n=1)^(K-1)n^(2-s),

K=M/2.

Thus s=2 is the exact crossing point of a derivative-free lower/upper refinement certificate family.

## 6. BRC observer lease

This note distinguishes:
- total branch mass;
- residue/orientation labels;
- full integer alias magnitude;
- signed character readout.

A quotient may discard a coordinate only when the requested future observer factors through the quotient. The two-dimensional neutrality theorem is the exact power-family witness of this rule.

The Fourier branch weights are generally cyclotomic/algebraic, so current finite positive-rational BRC implementations are not automatically applicable to the individual branch histogram. The observer/future-language discipline is applied; the rational positive-u physical-space resolvent remains the direct Foundation-compatible port-collapse carrier.

No Foundation promotion or novelty claim is made.

## 7. Next

1. sharpen the finite character error bound using periodic cancellation while retaining sign provenance;
2. formulate endpoint-orientation-only quotients and determine exactly which L-values factor through them;
3. use exact determinant coefficient carriers for higher even moments instead of recovering discarded data by analytic jets.
