# A3 opposite-edge resonant forcing: half-shell variance and cross-helicity decomposition

Status: `RESEARCH_NOTE / DURABLE_FRONTIER / EXACT_RESONANT_FORCING_ESTIMATE / NOT_PROMOTED / NOT_MILLENNIUM_PROOF`
Researcher-ID: `EM-FREE-7N3K2A`
At: `2026-09-07T17:38:00+08:00`
Parent: `research_notes/ns_a3_resonant_core_normal_form_walsh_20260907.md`
Authority immediately before write: `enterprise-math main@f08c57ea73d06f4a487fa39be583f397dc4be0dd`.

## 1. Resonant operator

Let `c` be a smooth divergence-free periodic field supported on the exact A3 root rays and decompose into helical sectors

`c=c^+ + c^-`.

Let `R_res(c,c)` denote the part of `P[(c·grad)c]` whose two input root directions are orthogonal K4 opposite-edge lines, equivalently `p·q=0`. This is exactly the quadratic parabolic resonant root-root operator identified in the parent note.

For one orthogonal pair with magnitudes `P=|p|`, `Q=|q|`, output magnitude

`L=|p+q|=sqrt(P^2+Q^2)`.

The generalized helical/Walsh formula implies:

- same-helicity input coefficient is bounded by `C |P-Q|` times the product of helical amplitudes;
- opposite-helicity input coefficient is bounded by `C (P+Q)` times the product of amplitudes.

The output representation multiplicity is uniformly finite because there are only three opposite-edge line-family pairs and finitely many signed orientations.

## 2. The correct radial variance at H^{-1/2} forcing level

For one helicity sector `s`, define radial moments

`E_s = sum_p |c_s(p)|^2 = ||c^s||_2^2`,

`J_s = sum_p |p|^(1/2)|c_s(p)|^2 = ||c^s||_{Hdot^{1/4}}^2`,

`H_s = sum_p |p||c_s(p)|^2 = ||c^s||_{Hdot^{1/2}}^2`.

When `E_s>0`, define the half-shell variance

`W_s^(1/2) := H_s - J_s^2/E_s >=0`,

and set it to zero for the zero sector.

The exact pairwise identity is

`boxed:`

`E_s W_s^(1/2)`
`= E_s H_s-J_s^2`
`= (1/2) sum_{p,q}`
`  (sqrt(|p|)-sqrt(|q|))^2`
`  |c_s(p)|^2 |c_s(q)|^2`.

This is the variance of `sqrt(|p|)` under the sector L2 mass distribution.

## 3. Why the half-shell variance matches the resonant output norm

For orthogonal inputs,

`L=sqrt(P^2+Q^2)`.

The same-helicity resonant coefficient at Hdot^{-1/2} level carries the squared radial weight

`(P-Q)^2/L`.

But

`P-Q=(sqrt(P)-sqrt(Q))(sqrt(P)+sqrt(Q))`

and

`(sqrt(P)+sqrt(Q))^2/L`
`<= 2(P+Q)/sqrt(P^2+Q^2)`
`<=2sqrt(2)`.

Hence

`boxed:`

`(P-Q)^2/L`
`<= 2sqrt(2) (sqrt(P)-sqrt(Q))^2`.

Therefore the Hdot^{-1/2} forcing sees exactly a half-power shell dispersion rather than the higher critical variance `D_s-Z_s^2/H_s` used for Hdot^{1/2} mass production.

This is a norm-matching principle: the radial observer changes with the Sobolev level of the forcing being estimated.

## 4. Same-helicity resonant forcing estimate

Using the finite output multiplicity and the pairwise identity,

`boxed:`

`||R_res(c^s,c^s)||_{Hdot^{-1/2}}`
`<= C_A3 sqrt(E_s W_s^(1/2)).`

This term vanishes when the helicity sector is supported on a single radial shell, exactly as required by the Beltrami/shell-commutator null structure.

## 5. Cross-helicity resonant forcing estimate

For `s != t`, the strong resonant coefficient is `O(P+Q)`. After the Hdot^{-1/2} output weight, the squared branch weight satisfies

`(P+Q)^2/L <= C(P+Q)`.

Therefore

`boxed:`

`||R_res(c^+,c^-)+R_res(c^-,c^+)||_{Hdot^{-1/2}}^2`
`<= C_A3 (E_+ H_- + E_- H_+).`

Consequently

`||R_res,cross||_{Hdot^{-1/2}}`
`<= C_A3 sqrt(E_+H_-+E_-H_+).`

This is nonzero on equal-shell opposite-helicity data and is therefore irreducible by radial shell variance alone.

## 6. Combined resonant forcing theorem

### Theorem R1

For every smooth divergence-free exact A3 root-ray field `c`,

`boxed:`

`||R_res(c,c)||_{Hdot^{-1/2}}`
`<= C_A3 [`
` sqrt(E_+ W_+^(1/2))`
`+sqrt(E_- W_-^(1/2))`
`+sqrt(E_+H_-+E_-H_+) ].`

No absolute-value aggregation is taken before the exact same/cross-helicity split; output collisions are handled only after coherent summation at each Fourier frequency.

### Null loci

R1 reproduces the exact structural boundaries:

- one helicity sector absent + remaining sector single-shell -> zero resonant forcing;
- same-helicity single-shell opposite-edge pairs -> zero;
- opposite-helicity equal-shell opposite-edge pairs -> generally nonzero;
- shell variance alone cannot control cross-helicity resonance;
- helicity purity alone cannot control same-helicity multi-shell resonant velocity forcing, although homochiral critical Hdot^{1/2} production remains zero by a separate identity.

## 7. General Sobolev-level variance ladder

The half-shell observer is one member of a broader family. For `0<=sigma<1`, a same-helicity resonant branch measured in `Hdot^{-sigma}` has radial factor

`|P-Q| L^{-sigma}`.

Since `L~max(P,Q)`, the mean-value theorem gives comparison with

`|P^(1-sigma)-Q^(1-sigma)|`.

Thus the natural pairwise positive observer at that forcing level is the variance of `|p|^(1-sigma)` under L2 branch mass:

`E_s M_{2(1-sigma),s}-M_{1-sigma,s}^2`
`= (1/2)sum_{p,q}`
` (|p|^(1-sigma)-|q|^(1-sigma))^2`
` |c_s(p)|^2|c_s(q)|^2`.

At `sigma=1/2` this is exactly the `sqrt(|p|)` variance above. At the endpoint `sigma->1`, the natural limiting coordinate becomes logarithmic shell separation rather than a power difference.

This hierarchy is a derived observer family inside the present resonant analysis; it is not proposed as a new global toolbox item.

## 8. Relation to the normal-form reduction

The complete root-ray quadratic forcing now splits into

`NONRESONANT dot ±1 pairs`
`+ RESONANT opposite-edge pairs`.

The nonresonant part has a one-derivative smoother quadratic normal form because the denominator is exactly `2nu p·q` with no small divisors.

The surviving quadratic resonant part is controlled by R1. Therefore the quadratic root-ray problem has been reduced to two positive dynamic coordinates **after signed branch resolution**:

1. sectorwise half-shell dispersion;
2. cross-helicity mass coupling.

The next question is whether these two coordinates can be propagated by viscosity strongly enough to remove the high-minimum-frequency hypothesis in the structured full-NS theorem. No such propagation result is claimed here.

## 9. BRC resolution

Keep before aggregation:
- opposite-edge line pair;
- radial magnitudes P,Q;
- helicity signs;
- Walsh characters / complex amplitudes;
- output frequency.

After the exact same/cross-helicity split, the positive half-shell variance is an admissible BRC observer for the same-helicity resonant forcing. It is **not** admissible as a replacement for the cross-helicity term.
