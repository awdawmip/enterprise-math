# Native tri-sector allocation: local curvature source predicts the global breaker phase

Status: `FREE_RESEARCH_EXACT_LOCAL_TO_GLOBAL_COROLLARY / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- native 7-Cell star Poisson invariant;
- odd-sector central-filament theorem;
- odd-curvature universal-breaker phase theorem.

## 1. Local Poisson source

For any internal Cell of the actual tri-sector allocation, let its label be `n` and the six nearest carrier-neighbor labels be `n_1,...,n_6`.

The frozen exact star identity is

`sum_i n_i - 6*n = 18`.

Define the normalized local source

`J=(sum_i n_i - 6*n)/6`.

Then identically

`J=3`.

This can be read from one unlabeled local star and is independent of shell, side position and allowed global side-orientation reversal.

## 2. The same number is the filament curvature coefficient

The abstract odd-sector shell calculation shows that a cyclic allocator with odd sector count `s` has central-filament values

`F_s(H,r)=H+(s*r^2+eps(r))/2`.

For the real native allocator `s=3`, the curvature coefficient is therefore

`B=3`.

Along the central filament the second differences alternate

`B-1, B+1`,

so in the native model they are

`2,4`.

Their presentation-stable mean is

`(2+4)/2=3`.

Thus the same scalar has three exact readings:

`SECTOR COUNT = 3`,

`MEAN FILAMENT CURVATURE = 3`,

`NORMALIZED STAR POISSON SOURCE = 3`.

## 3. Local-to-global breaker prediction

The odd-curvature phase theorem gives, for a positive odd coefficient `B`,

`5 is a universal long-filament breaker iff Legendre(B/5)=-1`,

provided channels2 and3 have not already broken the filament.

The native local star gives `B=J=3` without using a global sector label.

Now

`Legendre(3/5)=-1`.

Also the native coefficient satisfies

`3=3 mod4`, so channel2 is nonbreaking in the odd-curvature central-filament family;

`3|B`, so channel3 is nonbreaking.

Therefore one local star already determines the first-break phase:

`LOCAL STAR -> J=3 -> FIRST UNIVERSAL BREAKER = 5`.

## 4. Sharp capacity consequence

In the first-breaker-5 phase, the exact mod5 period is10 and the longest consecutive nonzero run is sharply9.

Therefore

`LOCAL STAR -> J=3 -> BREAKER5 -> SHARP CENTRAL-FILAMENT CAP9`.

Combined with the already-frozen native typed-Cell seam/no-branch theorem, the actual global prime-incidence graph realizes the corresponding sharp nine-Cell island cap.

So the global prime-incidence connectivity capacity is predictable from a prime-free seven-Cell local integer neighborhood.

## 5. Why this is stronger than a post-hoc prime fit

No prime test enters the extraction of `J`:

- the star Laplacian is prime-free;
- sector-count/curvature identification is prime-free;
- only after `J` is frozen is its quadratic character mod5 evaluated.

Thus the implication is not obtained by selecting a prime-rich pattern and then fitting a parameter. The parameter controlling the arithmetic phase is locally measurable before primality is considered.

## 6. Boundary

Discrete Laplacians, Legendre symbols and quadratic-character criteria are classical. The research-specific result is the exact native coupling

`one local star -> curvature/sector scalar -> global breaker phase -> sharp connectivity capacity`.

This is retained as a theorem-level corollary inside the experimental native allocation package, not as a coordinate-independent theorem about the classical primes.