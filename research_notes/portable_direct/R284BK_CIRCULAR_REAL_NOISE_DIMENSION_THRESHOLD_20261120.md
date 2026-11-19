# R284BK — Sharp two-versus-three channel threshold for a modular Port scalar with circular real noise

Date: 2026-11-20 Asia/Shanghai. Scientific predecessors: R284BA/R284BB and R284BJ. Scope: auxiliary directed-star finite-field determinant observer, not a native X6/heartbeat physical statement. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.

## Observation and real-error semantics

The source selects a prime p and nonadaptive controls d_0,...,d_(n−1),z_1,...,z_(n−1) in F_p, and emits the exact determinant residue P_C(d,z) represented as a point on the *real circle of circumference p*, R/pZ. The scalar received is P_C(d,z)+epsilon on this circle, where an adversary may choose any **real** epsilon with |epsilon|<=rho. Cyclic distance on R/pZ is the shorter arc length. This is a separately specified post-modulus real-noise channel, not an ordinary integer raw determinant and not an unqualified physical error model.

## BK1: The sharp dimension boundary

For known H>=2 and any finite real rho>=0:

* If n>=3, there exists one fixed setting of finite-field controls and a prime p such that **one** circular real-noisy scalar recovers every C∈{1,...,H}^{n×n} for all |epsilon|<=rho.
* If n=2, such worst-case recovery is possible **if and only if** rho<1/2, even allowing adaptive repetitions for the impossible half.

### Proof for n>=3

Let N=H^(n²), J=binom(N,2), M=n!(H+2)^n and t=floor(2rho), an integer. Choose a prime

[
p>max{2M, 4(n-1)(2t+1)J}.
]

Use independent uniform controls in F_p. The R284BB nonconstant-coefficient theorem shows that for any pair C≠C' and any integer c, the polynomial P_C-P_C'-c is nonzero after reduction modulo p. Its degree is at most n-1. By Schwartz–Zippel, Pr[P_C-P_C'=c] ≤(n-1)/p.

Two integer residue centers have overlapping closed real arcs of radius rho only if their integer cyclic distance is ≤2rho, equivalently there exists c∈{-t,...,t} with P_C-P_C'=c mod p. There are 2t+1 offsets. The union bound over J pairs is smaller than J(2t+1)(n-1)/p<1/4. Thus a setting with disjoint closed arcs exists (and random controls work with probability >3/4). Exact nearest-candidate matching recovers C from one point on the circle; no polynomial-time decoder is claimed. Bertrand again gives log p=O(n²log(H+1)+nlog n+log(1+rho)).

### Proof for n=2

Take the two strictly positive binary matrices

[
C_0=egin{pmatrix}1&1\1&1end{pmatrix},qquad
C_1=egin{pmatrix}1&2\1&1end{pmatrix}.
]

Their complete star-Port determinant polynomials differ by the constant 1 under *every* control choice; this equality survives reduction modulo every prime. For rho>=1/2 the radius-rho circular arcs always overlap. An adversary can return their common midpoint at every adaptively chosen step, so no finite adaptive protocol distinguishes them.

Conversely if rho<1/2, all that is needed is a setting giving distinct integer residues. Every 2×2 positive matrix can be reconstructed from the *formal* polynomial coefficients: the coefficients of d_0,d_1,z_1 determine C_11,C_00,C_10; its constant coefficient C_00C_11-C_01C_10 then determines C_01. Hence polynomials of distinct C are different over Z. Choose prime p>max(2·2!(H+2)^2,4 binom(H^4,2)); the finite-field polynomial collision bound (degree at most 1 after cancellation of d_0d_1) and a union bound give positive probability for a common fixed setting with distinct residues. Any two distinct integer residues have cyclic distance at least 1>2rho, so one real-noisy read is sufficient. QED.

## BK2: Exact one-symbol packing lower bound

Let the noiseless centers be the N integer residues. Disjoint closed real-noise arcs of radius rho require each successive cyclic integer gap to be strictly larger than 2rho, hence at least `g=floor(2rho)+1`. Summing all N cyclic gaps yields

[
pge N(lfloor2hofloor+1).
]

This lower bound and BK1's upper bound have the same asymptotic transmission-bit order; the chosen randomized construction has an approximately factor-two leading cardinality exponent. This is a one-symbol *readout* result under the explicitly named modular channel, not a lower bound for the old raw integer source.

## Exact finite checks and provenance

The companion `R284BK_circular_real_error_checker.py` uses rational radii, exact modular arithmetic and the full enumeration checker from R284BJ. Seed 20261120:
* n=2,H=2: all 16 candidates, p=487, minimum cyclic gap 1, so rho=49/100 succeeds; rho=1/2 has an unavoidable pairwise obstruction regardless of settings.
* n=3,H=2: all 512 candidates, p=13,604,881, gap 10, so rho=9/2 succeeds.
* n=4,H=2: all 65,536 candidates, p=335,002,337,287, gap 79, so rho=39 succeeds.

These are exhaustive checks for the particular displayed control settings. R284BJ's proof, checker and fixture hashes are reused at their exact pins: proof@ba9ac42ee03c61e34a057ede0d57561d0c418f6b; code@f411befb59de7d64011aecc67eab36ca2a436a88; evidence@3eb2b319813577427975e1e2686733cbf998b847. They do not constitute independent proof review.

## Remaining scientific problem

Find deterministic succinct finite-field control settings with certified global separation and **polynomial-time** decoding; quantify native modular-det sensor access and noncircular real-world noise/precision models. P000, ACTIVE six-dimensional worldview, joint-provenance preservation, and X6/BRC-specific native arithmetic are unchanged and not invoked as false substitutes for this finite auxiliary algebraic theorem.
