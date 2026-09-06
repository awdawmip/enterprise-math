# Free Research — Pi-to-Prime Geometry Frontier V2

Status: `FREE_RESEARCH_CURRENT_FRONTIER / ANCHOR_EXPOSED / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_UNVERIFIED`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`

## Current strongest two-channel statement

Let `tau = Pi_*` be the current endogenous full-turn completion, let `R_cell=1/sqrt(3)` be the exact current three-axis-slice cell radius, let `K_M` be the genuine finite Hamming/Krawtchouk integer-spectrum operator from #1159, and let

`B_M = K_M | span{g_p : p<=M prime}`

be its arithmetic prime-birth block. Let `P` be the native three-sector cycle matrix and `J=P^2-P`.

Then the current strongest prime extension is:

\[
\boxed{
\tau^2
=3!\lim_{M\to\infty}\det(I-B_M^{-2})^{-1}
}
\]

and, at standard Dirichlet weight-one analytic-completion strength,

\[
\boxed{
\frac{\tau R_{\rm cell}}3
=\prod_p\left(1-\frac{\operatorname{Tr}(JP^p)}{3p}\right)^{-1}.
}
\]

The first is the **prime-birth magnitude channel**; the second is the **native 120-degree orientation/chirality channel**.

## Finite exact meanings

- `prime p`: a new irreducible multiplicative direction born when the finite integer rotation spectrum first reaches `p`;
- `pi_P(M)`: rank of the arithmetic birth block;
- primorial: `det B_M`;
- exponent `2`: the first stable positive-integer Euler/holonomy completion order;
- `chi_3(p)`: exact native-slice chiral trace `Tr(JP^p)/3`;
- prime power `p^a`: repeated winding/occupation of one birth direction;
- composite integer: a finite multi-prime occupation vector.

## Factor `3!` is now realized in the same Hamming parent carrier

The naive hypothesis that the coefficient `6` comes from sixfold spatial degeneracy is refuted: sixfold eigenvalue repetition produces `Z_M(2)^6`, not `6 Z_M(2)`.

Current #1159 normalized coefficient gives

\[
\frac{\binom{M+1}{3}}{M^3}
=\frac1{3!}\left(1-\frac1{M^2}\right).
\]

In the same Hamming parent cube, set `m=M+1`. Shell 3 has exactly `choose(m,3)` endpoint supports. Each shell-3 endpoint is reached from the zero vertex by flipping three distinct coordinates, and those three coordinate flips commute. Therefore the six permutations in `S_3` are six distinct ordered shortest histories with one common endpoint.

Thus

\[
\boxed{
3!\binom{M+1}{3}
=(M+1)M(M-1)
}
\]

is literally the total ordered-distinct-three-flip history count, while `choose(M+1,3)` is the endpoint-support count. The `3!` factor is an exact Hamming provenance-fiber size inside the same parent carrier that produces the Krawtchouk spectrum.

A standalone main-based Lean PR #1228 formalizes the six ordering labels, generic pairwise-commuting endpoint recoalescence, fiber cardinality `6`, Hamming Boolean coordinate flips and their exact commutation. Its Lean workflow is nonblocking and was still in progress at this frontier capture; quality and bilingual-sync were already green. The independent reference-integrity red state is pre-existing control-path debt and unrelated to this theorem.

## Native/projective C3 intertwiner is closed at orientation strength

The current native sector cycle

\[
\rho(S_{12})=S_{23},\quad
\rho(S_{23})=S_{31},\quad
\rho(S_{31})=S_{12}
\]

is explicitly intertwined with the radius-selected projective action. For

\[
r=R_{\rm cell}=1/\sqrt3,
\qquad Q=T_{1/r},
\]

there is a three-point orbit

\[
r\to\infty\to-r\to r.
\]

The map

\[
\phi(S_{12})=r,\quad
\phi(S_{23})=\infty,\quad
\phi(S_{31})=-r
\]

satisfies

\[
\boxed{\phi\circ\rho=Q\circ\phi.}
\]

Hence the chiral trace matrix `P` is literally the permutation representation of both the native sector cycle and the radius-selected projective orbit. This closes the previous native-sector/projective-C3 gap at orientation-label strength without identifying the full native address space with a projective line.

## Target-free Wallis/Cauchy normalization

Define

\[
I_m=\int_0^\infty
\left(\frac{x}{\sqrt{1+x^2}}\right)^m\frac{dx}{1+x^2}.
\]

Then `I_1=1`, integration by parts gives

\[
I_m=\frac{m-1}{m}I_{m-2},
\]

and monotonicity gives, for the exact rational #1159 Wallis products `W_n`,

\[
W_n<I_0<W_n\frac{2n+1}{2n}.
\]

Since current Lean already proves `W_n -> wallisLimit`, this yields

\[
\boxed{
\texttt{wallisLimit}
=\int_0^\infty\frac{dx}{1+x^2}
}
\]

without using circumference, arctangent normalization or a primitive numerical pi. Thus internally

\[
\tau=2\int_0^\infty\frac{dx}{1+x^2}.
\]

Together with the radius-selected equal-third projective partition, this gives

\[
\boxed{
\sum_{n\ge1}\frac{\chi_3(n)}n
=\frac{\tau R_{\rm cell}}3
}
\]

without classical circle geometry as an input.

## Finite prime-winding partition geometry

For finite prime cutoff `M` and winding cutoff `K`, define

\[
\mathcal E_{M,K}
=\{e:\{p\le M\}\to\{0,1,\dots,K\}\}
\]

and

\[
w_2(e)=\prod_{p\le M}p^{-2e_p}.
\]

Then the total finite positive-rational branch mass is

\[
\boxed{
Z_{M,K}^{\rm wind}
=\sum_{e\in\mathcal E_{M,K}}w_2(e)
=\prod_{p\le M}\sum_{a=0}^{K}p^{-2a}.
}
\]

First `K->infinity`, then `M->infinity` gives

\[
\boxed{
\frac{\tau^2}{3!}
=\sum_{e\in\mathbb N_0^{(\mathbb P)}}\prod_p p^{-2e_p}
=\sum_{n\ge1}\frac1{n^2}.
}
\]

Thus `tau^2/3!` is the total quadratic mass of all finite winding configurations built from prime-birth directions. At finite `M,K` this is literally a finite positive-rational branch ensemble and is compatible with current Weighted-BRC typing.

A separate exact checker verifies the finite Cartesian-sum/product factorization, the closed geometric-sum formula, the `lcm(1,...,M)` maximal winding envelope, and pure prime-power single-direction occupation classification using only integers/Fraction; current status `PASS`.

## Distribution observables exposed by the geometry

The same exact occupation carrier gives:

\[
\pi(M)=\text{birth rank},
\]

\[
\vartheta(M)=\log\det B_M
\]

as a derived log readout, and

\[
\psi(M)=\log\operatorname{lcm}(1,\dots,M)
\]

as the derived log readout of the maximally saturated winding envelope.

The next asymptotic frontier is therefore the prime number theorem retyped as a statement about the growth of this saturated winding geometry, e.g. `psi(M)~M`. No PNT or RH claim is made in this frontier.

## Current boundaries

- the three-axis model remains only a research slice of P000 6D space;
- arithmetic holonomy directions are not spatial dimensions;
- the Eisenstein norm is not native Enterprise length;
- current BRC primitive periodic edge-word orbits are not identified with arithmetic primes;
- the projective coordinate is derived, not a primitive point address;
- the `s=1` Dirichlet Euler product is conditional analytic completion;
- external mathematical novelty is unverified;
- no Riemann-hypothesis consequence is claimed.

## Current next mother question

With local prime geometry substantially closed, the next mathematically discriminating question is:

> Can the prime-number-theorem scale `psi(M) ~ M` be derived from a finite Enterprise spectral/rotation invariant controlling the saturated prime-winding envelope, rather than imported as classical analytic number theory?

This is the correct next step before any attempt to interpret zeta zeros or the Riemann hypothesis geometrically.
