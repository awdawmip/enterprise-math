# Nollm Hecke tree layers -> zeta(2) thickness bridge

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
At: `2026-09-08T21:55+08:00`
Scope: `enterprise-math <-> nollm cross-project synthesis`
Parent: `research_notes/nollm_hecke_radix_multiplicative_field_sync_20260908.md`
Related EM frontier: `research_notes/1162_alias_prime_valuation_thickness_semigroup_20260908.md`
Source snapshots: `enterprise-math@8e8f2232e99b0271d9bc89a336f63fc9e0d63edc`, `Nollm@91bd14ab394e87931b45baaaa87671f30fcfd706`

## 1. Change of observer: Hecke correspondence as a regular tree

Fix a prime p and quotient rank-2 lattices by homothety. The local index-p Hecke geometry is the `(p+1)`-regular Bruhat-Tits tree. Let `A_s` denote the formal sphere of vertices at tree distance s from the base homothety class.

Sphere cardinalities are

- `|A_0|=1`;
- `|A_s|=(p+1)p^(s-1)` for `s>=1`.

An actual index `p^r` sublattice L of `Z^2` has Smith exponents `(a,b)`, `0<=a<=b`, `a+b=r`. Factor

`L = p^a L_prim`.

After removing the common scalar `p^a`, the primitive homothety class lies at tree distance

`s=b-a=r-2a`.

Thus every index-`p^r` branch has two exact typed coordinates:

- **homothety thickness** `J=a`;
- **primitive shape distance** `S=r-2J`.

This is the Hecke analogue of a skeleton/thickness decomposition. The same integer exponent r does not determine J; J is branch-dependent and therefore cannot be recovered after Boolean support/provenance collapse.

## 2. Exact layer decomposition

Let `T(p^r)` be the formal sum of all index-`p^r` sublattices. Then, stratified by common scalar content,

`T(p^r) = sum_(j=0..floor(r/2)) p^j * A_(r-2j)`

where `p^j * A_s` denotes the actual lattices obtained by multiplying primitive representatives in tree sphere s by the common scalar `p^j`.

Counting gives

`#T(p^r)=1+p+...+p^r=sigma_1(p^r)`.

For a noncentral shell (`r-2j>0`),

`N_(r,j)=(p+1)p^(r-2j-1)`.

Successive inward shells therefore satisfy the exact ratio

`N_(r,j+1)/N_(r,j)=p^(-2)`

until the even-depth central boundary is reached.

### Concrete p=5 layers

- r=0: distance `0`: `1`
- r=1: distance `1`: `6`
- r=2: distances `2,0`: `30 + 1 = 31`
- r=3: distances `3,1`: `150 + 6 = 156`
- r=4: distances `4,2,0`: `750 + 30 + 1 = 781`
- r=5: distances `5,3,1`: `3750 + 150 + 6 = 3906`
- r=6: distances `6,4,2,0`: `18750 + 750 + 30 + 1 = 19531`
- r=7: distances `7,5,3,1`: `93750 + 3750 + 150 + 6 = 97656`
- r=8: distances `8,6,4,2,0`: `468750 + 18750 + 750 + 30 + 1 = 488281`

The factor 25 between successive noncentral p=5 shells is exact.

## 3. New exact bridge: deep Hecke thickness has the zeta(2) prime-valuation law

Choose uniformly from the index-`p^r` sublattices and let J be homothety thickness.

For `j<r/2`,

`P_r(J=j) = (p+1)p^(r-2j-1) / sigma_1(p^r)`

which simplifies to

`P_r(J=j) = ((1-p^(-2)) p^(-2j)) / (1-p^(-(r+1)))`.

If r is odd, `r=2m+1`, there is no special center shell and this is an exact truncated geometric distribution for every `j=0..m`:

`P_(2m+1)(J=j)=((1-p^(-2))p^(-2j))/(1-p^(-2m-2))`.

Hence, as odd depth tends to infinity,

`P(J=j) -> (1-p^(-2))p^(-2j)`.

This is exactly the prime-valuation law in the existing EM inverse-square / Basel carrier:

`P(v_p(K)=j)=(1-p^(-2))p^(-2j)`.

Therefore the same local law has two exact coordinate interpretations:

1. EM alias/zeta carrier: exponent of prime p in an inverse-square distributed integer;
2. Nollm-Hecke field: common p-adic homothety thickness of a uniformly chosen deep index-p^r lattice branch.

This is a project-level synthesis, not a novelty claim about the classical components.

## 4. Odd-prime product recovers the EM antiperiodic alias distribution

Take independent local deep Hecke layers over odd primes and let

`G_odd = product_(p odd) p^(J_p)`.

The limiting local laws are independent geometric laws. Therefore, for odd positive integer n,

`P(G_odd=n) = [product_(p odd)(1-p^(-2))] n^(-2)`

and the existing EM normalization gives

`P(G_odd=n)=8/(pi^2 n^2)`.

Thus the odd inverse-square alias variable in `#1162` is distributionally identical to the odd homothety-thickness content of the deep Hecke product field.

A finite exact approximant is already available: choose a finite prime set S and odd local depths `r_p=2m_p+1`. Then on integers `g=product_(p in S)p^(j_p)` with `0<=j_p<=m_p`,

`P(G_S=g)=C_(S,m) g^(-2)`

exactly, with

`C_(S,m)=product_(p in S) (1-p^(-2))/(1-p^(-2m_p-2))`.

So the inverse-square law is visible before any infinite limit as a finite product of uniform Hecke-layer thickness laws.

## 5. Why exponent 2 appears geometrically

The `p^(-2)` ratio is not inserted by a probability ansatz. Moving inward one homothety unit replaces primitive index `p^s` by `p * (primitive index p^(s-2))`; a scalar p in a rank-2 lattice consumes index `p^2`. Therefore every inward thickness step costs exactly two powers of p.

This gives a geometric reason that the local thickness law is zeta exponent 2 in rank 2. A higher-rank analogue may replace 2 by ambient rank/dimension, but that generalization has not been established here.

## 6. Important measure distinction: arithmetic layer != sequential local walk

Do not confuse a uniform `T(p^r)` layer with the r-step path measure `T(p)^r`.

For p=5 and r=8, the arithmetic layer has shell populations

- distance 8: `468750`
- distance 6: `18750`
- distance 4: `750`
- distance 2: `30`
- distance 0: `1`

(total `488281`).

By contrast, all `6^8=1,679,616` sequential local paths end with masses

- distance 8: `468750`
- distance 6: `675000`
- distance 4: `402000`
- distance 2: `121080`
- distance 0: `12786`.

The per-vertex path multiplicity is respectively

`1, 36, 536, 4036, 12786`.

Thus local uniform walking massively overweights backtracking/recoalescence compared with the arithmetic uniform-index layer. This is a direct BRC witness that support and path multiplicity are different carriers.

A correct exact sampler for a uniform Hecke layer is instead:

1. sample thickness J with the exact shell weights above;
2. set primitive distance `S=r-2J`;
3. sample a nonbacktracking path uniformly on sphere S: first edge among `p+1`, then p outward choices per step.

This separates thickness from primitive shape and avoids accidental random-walk bias.

## 7. Correction to the earlier inert-prime recurrence picture

The p=5 eight-step exact return should be separated into two recurrences.

### p-adic/Hecke shape recurrence

At every even r, `T(p^r)` contains the unique central homothetic branch `p^(r/2) Z^2`. Therefore return to the same homothety class is universally available at even depth. At r=2 it is simply one step out and one step back.

### archimedean/hex conformal recurrence

Returning to the same homothety class does not guarantee a desired complex rotation, low local Beltrami defect, or spatial discrepancy. The earlier p=5 eight-step loop selected the r=8 central homothety branch while additionally closing to the Eisenstein unit rotation `625*omega` with a bounded-distortion matrix path.

Therefore one recurrence integer must not encode both effects. Keep separately:

- Hecke tree distance / homothety thickness;
- archimedean hex rotation / anti-conformal phase holonomy.

The earlier `r_p=2p` schedule remains a finite angular-load-balancing candidate, not a fundamental p-adic return period.

## 8. Adelic-style conservation law for the sqrt(n) radial rule

For the ideal 2D similarity associated with positive integer n,

`det(T_n)=n` when the isotropic linear scale is `sqrt(n)`.

Prime valuations give the rational product formula

`n * product_p p^(-v_p(n)) = 1`.

Therefore the 2D archimedean area expansion is exactly balanced by the product of local p-adic contraction factors. This gives a second structural justification for the radial law `sqrt(n)`: it is the unique isotropic 2D scale whose determinant equals the ordinary absolute value of n and therefore fits the rational product formula exactly.

This is an interpretation/synthesis, not a new proof of the product formula.

## 9. Secondary finite observation: finer inert-prime hex defect spectrum

Define `delta_hex(p)` as the minimum exact conformal defect `Delta(M)=N(B(M))` over integer axial matrices with determinant p. Split/ramified primes admit `delta_hex=0`; inert primes have `delta_hex>0`.

An exact finite matrix search over the 338 inert primes below 5000 found only

`{1,3,4,7,12,13,16,21,25}`

as minimum defect values, with frequencies

- 1: 78 primes
- 3: 49
- 4: 138
- 7: 26
- 12: 18
- 13: 16
- 16: 11
- 21: 1
- 25: 1.

This shows that inertness has a finer arithmetic nonconformality spectrum beyond the binary mod-3 obstruction. No asymptotic bound or distribution theorem is claimed. It is a candidate canonical cost for future Hecke-branch selection, to be compared with angular low-discrepancy cost.

## 10. BRC resolution and new candidate primitive

`COMPOSE_APPLIED` with the existing prime-valuation/skeleton-thickness interface.

For a local p^r layer retain

`(r, J, primitive_shape_endpoint, path_multiplicity, radix_digits, archimedean_defect_phase)`.

Do not collapse to tree distance alone, total branch count, normalized mass, or `Delta=N(B)` if future composition is allowed.

The strongest new exact relation in this note is

`uniform deep Hecke homothety thickness <-> zeta(2) prime-valuation geometric law`.

## 11. Next

1. Treat the primitive Hecke shape sphere as the geometry layer and homothety J as an explicit thickness coordinate in the Nollm research model.
2. Test finite bounded quotients of the `(p+1)`-regular tree as shape atlases. Arithmetic Ramanujan graph quotients are a natural candidate because they preserve the local Bruhat-Tits geometry while offering near-optimal spectral expansion; this is an architectural hypothesis, not yet an implementation decision.
3. Investigate whether the EM alias/Basel boundary can be reconstructed directly from finite odd-depth Hecke products, providing an exact finite combinatorial bridge between the two research programs.
4. Keep p-adic return and archimedean conformal holonomy as separate recurrence coordinates.