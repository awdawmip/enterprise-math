# Native filament coupled-selection theorem independent audit — return

Status: `FROZEN_INDEPENDENT_AUDIT_RETURN`

Date: `2026-08-25`

Research task: `RS-NATIVE-FILAMENT-COUPLED-SELECTION-INDEPENDENT-AUDIT`

Hard target: `NATIVE_FILAMENT_COUPLED_SELECTION_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

Final verdict: `PACKAGE_VERIFIED_WITH_NARROWING`

## 1. Audit metadata / input hash

- PR: `#631`
- Audit branch: `audit/native-filament-coupled-selection-20260825`
- Audit input head at acquisition: `719285f629358fcf15b014e594775bf2e323fb0c`
- Blind packet: `research_inputs/NATIVE_FILAMENT_COUPLED_SELECTION_BLIND_AUDIT_PACKET_20260825.md`
- Blind packet Git blob hash: `bce8b9ae6620f5c280e72656b0d22ff7063965c6`
- Taskbook: `research_tasks/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_20260825.md`
- Taskbook Git blob hash: `8ea053792a4209f1fa15f20e9f149ce25064267a`

Independence attestation: before freezing this return, the audit did **not** read PR #627, branch `research/native-filament-generalization-theorem-package-20260824`, source proofs, or any checker written specifically for that package. All finite checks described below were reconstructed independently from the blind statement packet.

## 2. Verdict matrix A1--I

| Row | Verdict | Core finding | PRIOR_ART_NOTE |
|---|---|---|---|
| A1 | `VERIFIED_EXACT` | Algebraic identity is exact on the inherited admissible side-position domain. | — |
| A2 | `VERIFIED_EXACT` | Central-seam formulas and odd gap `2h+1` are exact. | — |
| B1 | `VERIFIED_EXACT` | Window formula follows from the exact parity identity. | — |
| B2 | `VERIFIED_EXACT` | Alternating second difference and order-4 recurrence are exact. | — |
| C1 | `VERIFIED_WITH_NARROWING` | For `M>2`, the exact effective `R`-period is `L_(B,M)`; for `M=2` the effective period after fixing the intercept is actually `1`, not `2`. | Characteristic/quasi-polynomial viewpoint is standard. |
| C2 | `VERIFIED_EXACT` | `2` words for `M=2`; `M L_(B,M)` for every `M>2`, including even composite moduli. | — |
| C3 | `VERIFIED_EXACT` | Fixed chirality reduces exactly to affine evaluation words. | Reed--Solomon/MDS is classical. |
| D1 | `VERIFIED_WITH_NARROWING` | As written with only `Q_0,Q_1`, tangent identification is exact for `chi=+1`; for `chi=-1` odd indices require the opposite vertical shift. | Legendre/conic duality is classical. |
| D2 | `VERIFIED_WITH_NARROWING` | Mixed-parity obstruction is exact when the same-parity slope difference is a `q`-adic unit; without that distinct-slope condition there are counterexamples. | Arrangement determinant calculation is standard. |
| D3 | `VERIFIED_EXACT` | Under the inherited `q` odd, `q∤B` assumption and `q>k-1`, the two-chirality discriminant and fixed-chirality persistence depth are exact. | Arithmetic-arrangement discriminants are classical. |
| E1 | `VERIFIED_EXACT` | All local-factor formulas are exact, including `q=2,3` and `q|B`. | Quadratic character sums / order-2 cyclotomy are classical. |
| E2 | `VERIFIED_EXACT` | Universal breakers are exactly the stated subset of `{2,3,5}`; none occur for `q>=7`. | — |
| E3 | `VERIFIED_EXACT` | The four residue-class lists modulo `60` are exact. | — |
| E4 | `VERIFIED_EXACT` | Sharp breaker-coprime run capacities are `1,5,9`; for breaker `5`, extremal classes are exactly `H=0,2 mod 5`. | — |
| F1 | `VERIFIED_EXACT` | The two hit sets are exactly the negative Legendre-dual images. | Legendre transform is classical. |
| F2 | `VERIFIED_EXACT` | Image sizes and intersection formula are exact; `tau_B(q)=|I_0∩I_1|-1`. | Order-2 cyclotomic/quadratic-residue intersection formula is classical. |
| G1 | `VERIFIED_EXACT` | Exact CRT product. | CRT is classical. |
| G2 | `VERIFIED_EXACT` | Primorial extinction dimensions follow exactly from the first-breaker classification. | — |
| G3 | `VERIFIED_EXACT` | The claimed fixed-`B` asymptotic follows from the local factors, Mertens, and two nonprincipal quadratic characters. | Mertens/Dirichlet prime-sum theory is classical. |
| G4 | `VERIFIED_EXACT` | With the primorial metric made explicit below, the transparent product is compact, perfect, uncountable, Haar-null, and full Hausdorff dimension; the diagonal integer intersection is empty. | Tychonoff/product measure and Frostman/mass-distribution arguments are classical. |
| H | `VERIFIED_EXACT` | The scalar `3` is recovered in all three stated ways; for `B=3`, `2,3` are nonbreakers and `5` is the first breaker with E4 capacity `9`; `s=3` is the smallest odd sector count with latest possible finite first breaker. | — |
| I | `VERIFIED_EXACT` | All twelve displayed values are consecutive `F_15` values and are prime by an independent deterministic 64-bit Miller--Rabin replay. | Deterministic 64-bit Miller--Rabin base theorem is standard computational number theory. |

No row has `DEPENDENCY_GAP`. No row requires `REFUTED_COUNTEREXAMPLE` after the three explicit narrowings C1/D1/D2 are imposed.

## 3. Independent proofs / counterexamples

### A. Sector / curvature provenance

For odd `s`, with `sigma_*=(s-1)/2` and admissible `t=h+ceil(r/2)`, use

`ceil(r/2)=(r+eps(r))/2`.

Then

`N_s = 1+s r(r-1)/2 +(s-1)r/2 + h + ceil(r/2)`

`= h+1+(s r^2+eps(r))/2`.

Thus the abstract central-filament coefficient is exactly `B=s`. The inherited side-position condition is still required: `0<=t<=r-1` (equivalently `-ceil(r/2)<=h<=floor(r/2)-1`; if `h` is a nonnegative distance, `0<=h<=floor(r/2)-1`).

For even `s`, with `0<=h<=r-1`, direct substitution gives

`L=s r^2/2-h`,

`R=s r^2/2+1+h`,

hence `R-L=2h+1`. Two primes greater than `2` are odd and therefore cannot differ by an odd number. A2 is exact.

### B. Odd-curvature dynamics

The key exact parity identity is

`eps(R+j)=eps(R)+chi eps(j)`, with `chi=(-1)^R`.

It is checked by the two cases `R` even/odd. Substitution into `F_B` gives B1.

For B2,

`eps(j)-2eps(j+1)+eps(j+2)=-2(-1)^j`,

so the quadratic contribution has second difference `B` and the parity contribution has second difference `-chi(-1)^j`. This proves

`V_j-2V_(j+1)+V_(j+2)=B-chi(-1)^j`.

The fourth-order operator

`E^4-2E^3+2E-1=(E-1)^3(E+1)`

annihilates both the quadratic part and the alternating parity part, proving the second recurrence.

### C. Finite quotient code

Let `c=F_B(H,R)`. B1 gives

`V_j = c + B R j + (B j^2+chi eps(j))/2 (mod M)`.

Since `H` is arbitrary, `c` runs over all `M` residues for every fixed `R`.

Suppose two length-`k` words (`k>=3`) with the same first coordinate arise from `R,R'`. Equality at `j=1,2` gives, with `d=R-R'`,

`B d +(chi-chi')/2 = 0 (mod M)`,

`2B d = 0 (mod M)`.

If `chi!=chi'`, subtracting the doubled first equation from the second forces `M|2`. Therefore for `M>2` opposite chiralities never coincide. For equal chirality, equality is equivalent to

`M/gcd(B,M) | d`

plus equal parity, hence exactly

`lcm(2,M/gcd(B,M)) | d`.

This proves C1 and C2 for `M>2`.

For `M=2`, after fixing the intercept the relative word is independent of `R`: if `B=1 mod4`, `F_B(H,r)=H+eps(r) mod2`; if `B=3 mod4`, `F_B(H,r)=H mod2`. Thus the minimal/effective `R`-period is `1`, while the total word set still has exactly two words. This is the C1 narrowing and confirms the C2 exception.

For C3, after subtracting `eta_j`, the word is

`c+(BR)j`.

At fixed chirality, `R mod q` still runs over all of `F_q` by CRT between parity and `mod q`; since `q∤B`, so does `BR`. Hence the packets are exactly all affine words `(a+bj)`. The condition `q>k-1` makes `0,...,k-1` distinct evaluation points, giving the standard `[k,2,k-1]` MDS code.

### D. Dual-parabola arrangement

For

`Q_delta(x)=x^2/(2B)-delta/2`,

the tangent at `x_0=-Bj` is

`y=-j x -(B j^2+delta)/2`.

Therefore the packet line

`y=-j x -(B j^2+chi eps(j))/2`

requires `delta=chi eps(j)`. If `chi=+1`, `delta` is exactly `0` or `1` and D1 is correct with the displayed `Q_0,Q_1`. If `chi=-1`, an odd `j` requires `delta=-1`, which is not one of the two defined parabolas.

Concrete sign check: modulo `5`, take `B=1`, `chi=-1`, `j=1`. The packet line is `y=-x`. At `x_0=-1`, the tangents to `Q_0` and `Q_1` have intercepts `2` and `4` modulo `5`, respectively, so neither is `y=-x`.

A uniform corrected formulation is

`Q_e^(chi)(x)=x^2/(2B)-chi e/2`, `e in {0,1}`,

with the line for local parity `e=eps(j)` tangent to `Q_e^(chi)`. Equivalently, D1 may be narrowed to `chi=+1` with the original `Q_e` definition.

For D2, write each line as

`j x + y +(B j^2+chi eps(j))/2 =0`.

If `u,v` have parity `e` and `w` the opposite parity, the exact determinant is

`(u-v)/2 * [B(w-u)(w-v)+chi(1-2e)]`.

Thus, when `q∤(u-v)`, the first two lines have a unique intersection modulo every `q^a`, and the three lines are concurrent iff

`q^a | B(w-u)(w-v)+chi(1-2e)`.

Without the unit-slope condition the stated iff fails. Counterexample:

- `q=3`, `a=1`, `B=1`, `chi=+1`;
- `u=0`, `v=6` (same parity), `w=1`;
- the `u` and `v` lines coincide modulo `3` as `y=0`;
- the `w` line is `y=-x-1` and all three meet at `(x,y)=(2,0)`;
- the displayed obstruction is `-4=2 mod3`, not `0`.

So D2 needs the distinct-slope hypothesis. D3's `q>k-1` condition automatically supplies it for distinct indices in a length-`k` window.

For three same-parity lines the determinant is

`B(u-v)(u-w)(v-w)/2`.

Hence in the distinct-slope range concurrency modulo `q^a` is equivalent to `q^a|B`, exactly as claimed.

For D3, define the fixed-chirality mixed obstruction

`O_(T,chi)=B A_T + chi(1-2e)`.

For odd `q`, union over the two chiralities is equivalent to

`(B A_T-1)(B A_T+1)=B^2 A_T^2-1 =0 (mod q)`.

Under the inherited `q∤B` assumption, all same-parity triples are generic, so a type change for at least one chirality occurs iff one mixed factor vanishes, equivalently iff `q|mathfrak D_(k,B)`. Since `q>k-1`, every slope-difference determinant factor is a `q`-adic unit. Consequently the exact fixed-chirality persistence depth is

`max_T v_q(O_(T,chi))`

(and, if one algebraically extends the same-parity determinant outside the section's `q∤B` hypothesis, also `v_q(B)`). The union discriminant must not be confused with a fixed-chirality depth.

Boundary guard: the leading `B` factor in `mathfrak D_(k,B)` must not be used to extend D3 across `q|B` without rechecking `k`; for `k=3,4` there is no three-same-parity index triple. This does not affect the stated D3 because Section D assumes `q∤B`.

### E. Transparency / breaker classification

For odd `q`, parity and residue modulo `q` are independent, because adding `q` flips parity. Therefore the hit sets are

`I_0={-B x^2/2 : x in F_q}`,

`I_1={-(B x^2+1)/2 : x in F_q}`.

If `q|B`, these are the two singleton classes `0` and `-1/2`, giving `tau_B(q)=q-2` (including the special value `1` at `q=3`).

If `q∤B`, each image has `(q+1)/2` elements and F2 below gives

`|I_0∩I_1|=[q+1+(B/q)+(-B/q)]/4`.

Thus

`tau_B(q)=q-|I_0 union I_1|`

`=[q-3+(B/q)+(-B/q)]/4`.

For `q=2`, direct reduction modulo `4` gives:

- `B=3 mod4`: `F_B(H,r)=H mod2` for all `r`, so exactly `H=1` is transparent;
- `B=1 mod4`: even/odd shells alternate the two residues, so no transparent class exists.

This proves E1.

For `q>=7`, if `q|B` then `tau=q-2>0`. If `q∤B`:

- for `q=3 mod4`, `(−B/q)=−(B/q)`, so `tau=(q-3)/4>=1`;
- for `q=1 mod4`, `tau=(q-3+2(B/q))/4`, whose minimum for primes `q>=7` occurs from `q>=13` and is `(q-5)/4>=2`.

Hence no breaker occurs at `q>=7`. At `q=3`, the breaker condition is exactly `3∤B`; at `q=5`, because `(-1/5)=1`, the breaker condition is exactly `(B/5)=-1`; together with the `q=2` calculation this proves E2.

Sorting odd residues modulo `60` by the first applicable condition gives exactly the E3 lists.

For E4, a generic odd breaker `q` has shell-residue period `2q`. A universal breaker forces at least one zero in every such period, so a breaker-coprime run has length at most `2q-1`. The bounds are attained:

- `q=2`: alternating residues give `1`;
- `q=3`: an appropriate tangency class has exactly one zero in a six-shell period, giving `5`;
- `q=5` in the nonresidue phase: `H=0` and `H=-1/2=2 mod5` each have exactly one zero in a ten-shell period, giving `9`.

The two `q=5` classes are therefore exactly the normalized extremal classes stated in E4.

### F. Legendre-dual value sets

For the algebraic Legendre transform over `F_q`, the stationary point for

`p x-Q_e(x)`

is `x=Bp`, and

`Q_e^*(p)=B p^2/2+e/2`.

Hence

`-Q_e^*(p)=-(B p^2+e)/2`,

which is exactly the `H` class hit by a shell of parity `e`. This proves F1.

Let `S` be the set of quadratic residues including zero. After scaling by the nonzero factor `-B/2`, the intersection problem is equivalent to counting `z in S` with `z-B^(-1) in S`. The standard order-2 residue identity (with zero included) is

`|S intersect (S+c)|=[q+1+(c/q)+(-c/q)]/4`, `c!=0`.

With `c=B^(-1)`, the two character values equal `(B/q)` and `(-B/q)`. Therefore

`|I_0|=|I_1|=(q+1)/2`,

`|I_0 intersect I_1|=[q+1+(B/q)+(-B/q)]/4`.

Since two subsets of size `(q+1)/2` in a `q`-element universe have overlap at least `1`, and

`tau_B(q)=|I_0 intersect I_1|-1`,

universal breaking is exactly minimal overlap `1`. F2 is exact.

### G. Finite wheel / profinite basin

For squarefree `M`, the condition at a prime `q|M` depends only on `H mod q`. CRT therefore gives the direct product bijection and

`Theta_B(M)=product_(q|M) tau_B(q)`.

G1 and G2 follow immediately.

For G3, fix a no-break `B`, so `B=15,39,51 mod60`. For all primes `p∤2B`, put

`chi_+(p)=(B/p)`, `chi_-(p)=(-B/p)`.

Then

`tau_B(p)/p = (1/4) [1+(-3+chi_+(p)+chi_-(p))/p]`.

All primes dividing `2B` contribute only a finite positive correction. Because `B=3 mod4`, positive `B` is not a square, so the quadratic character associated to the squarefree kernel of `B` is nonprincipal. The character associated to `-B` is also nonprincipal. Therefore the prime sums

`sum_p chi_+(p)/p`, `sum_p chi_-(p)/p`

converge (equivalently from standard Dirichlet `L(1,chi)` theory), while Mertens gives

`sum_(p<=x) 1/p = log log x + M + o(1)`.

The quadratic error from `log(1+u)` is absolutely summable. Hence, with `x=p_d`,

`log(Theta_B(P_d)/P_d) = -d log4 -3 log log p_d + C_B' + o(1)`

for a finite real `C_B'`, and positivity of every no-break local factor makes `C_B=exp(C_B')>0`. Thus

`Theta_B(P_d)/P_d ~ C_B 4^(-d)/(log p_d)^3`.

No PNT is needed for this exact fixed-`B` product asymptotic in the displayed `d,p_d` variables; PNT is used below to compare `d` with `log P_d` for Hausdorff dimension.

For G4, define the primorial ultrametric on

`S_sq=product_i F_(p_i)`

by

`rho(x,y)=0` if `x=y`, and otherwise

`rho(x,y)=P_n^(-1)`

where `n` is the largest index for which `x` and `y` agree at every prime `p_1,...,p_n` (`P_0=1`). A depth-`n` cylinder has diameter at most `P_n^(-1)`.

The ambient space has exactly `P_n` depth-`n` cylinders. Uniform Haar measure assigns mass `P_n^(-1)` to each, so the ambient Hausdorff dimension is exactly `1` (upper bound from the cylinder covers; lower bound from the mass-distribution estimate).

For no-break `B`, every `T_B(p)` is nonempty. Moreover `tau_B(p)>=2` for all sufficiently large primes (indeed for every `p>=11`): if `p|B`, `tau=p-2`; if `p∤B`, the E1 formula gives at least `2`. Hence the infinite product `Tcal_B` is compact, has no isolated point, and has continuum cardinality.

Its Haar measure is

`lim_d Theta_B(P_d)/P_d =0`

by G3.

For the Hausdorff lower bound, place the uniform product probability measure `mu` on `Tcal_B`. A nonempty depth-`d` cylinder has

`mu(C)=1/Theta_B(P_d)`.

G3 gives

`log Theta_B(P_d)=log P_d-d log4-3 log log p_d+O(1)`.

By PNT, `log P_d=theta(p_d)~p_d` and `d=pi(p_d)~p_d/log p_d`, so `d=o(log P_d)`. Thus for every `s<1`, eventually

`Theta_B(P_d)>=P_d^s`,

and hence every sufficiently small primorial ball satisfies

`mu(B_r)<=r^s`.

The mass-distribution/Frostman bound gives `dim_H Tcal_B>=s`; letting `s` increase to `1` and using the ambient upper bound proves

`dim_H Tcal_B=1`.

Finally, under the diagonal embedding, no ordinary integer lies in `Tcal_B`. For any integer `H`, choose `|r|` large enough that the integer `F_B(H,r)>1`; any prime divisor `p` of that value witnesses that `H mod p` is not transparent. Conversely every finite set of transparent coordinates has an ordinary integer lift by CRT. Hence every finite subsystem is solvable while the full diagonal integer intersection is empty.

### H. Native tri-sector selection corollary

Using only the frozen inputs:

`sector count=3`,

`mean curvature=(2+4)/2=3`,

`normalized Poisson source=18/6=3`.

For `B=3`, E1 gives

`tau_3(2)=1`, `tau_3(3)=1`, `tau_3(5)=0`,

because `3=3 mod4`, `3|B`, and `(3/5)=-1`. Therefore `5` is the first breaker and E4 gives the sharp **breaker-coprime** filament run capacity `9`.

Scope guard: the E4 conclusion is a divisibility/nonzero-run capacity. It must not be silently promoted to an unconditional prime-run theorem for the unrestricted integer `(H,R)` family, because the breaker value itself may equal the prime `5`; for example `B=3,H=5,R=0` gives the ten primes

`5,7,11,19,29,43,59,79,101,127`.

This does not contradict H as the stated E4 breaker-coprime corollary, and `r=0` is outside the native shell domain `r>=1` from the packet's allocator.

For the final selection claim, any finite universal breaker is in `{2,3,5}` by E2, so the latest possible first breaker is `5`. Avoiding `2` requires `s=3 mod4`; avoiding `3` requires `3|s`; breaking at `5` requires `(s/5)=-1`. The smallest positive odd `s` satisfying all three is `s=3`.

### I. Finite prime control witness

Direct substitution with

`B=15`, `R=610`, `H=977767522784021`

reproduces the twelve packet values exactly for `j=0,...,11`:

| `j` | `F_15(H,610+j)` | deterministic MR64 |
|---:|---:|---|
| 0 | 977767525574771 | PASS |
| 1 | 977767525583929 | PASS |
| 2 | 977767525593101 | PASS |
| 3 | 977767525602289 | PASS |
| 4 | 977767525611491 | PASS |
| 5 | 977767525620709 | PASS |
| 6 | 977767525629941 | PASS |
| 7 | 977767525639189 | PASS |
| 8 | 977767525648451 | PASS |
| 9 | 977767525657729 | PASS |
| 10 | 977767525667021 | PASS |
| 11 | 977767525676329 | PASS |

All twelve are 50-bit integers. The independent deterministic primality replay uses the standard theorem that, for `n<2^64`, strong Miller--Rabin testing at bases

`2, 325, 9375, 28178, 450775, 9780504, 179526502`

is deterministic. Each candidate was first screened by small-prime division, written as `n-1=2^s d` with `d` odd, then passed every strong test in this fixed base set. No package-specific primality checker was read.

SHA-256 of the newline-separated twelve-value vector (with a final newline):

`31100dd156785bb57edfa3ed191f8e82b976620e22caaa6d1304a0bd3a54260c`

Thus I is independently verified.

## 4. Pressure-test log

Independent finite checks were reconstructed from scratch and used only as supporting evidence for the proofs above.

1. **A/B algebra grid**: odd `B<=99`; `H=-20,...,20`; `R=-10,...,10`; `j=-10,...,10`; no mismatch in B1/B2. A1/A2 were checked over small sector/shell grids with only admissible side positions.
2. **C quotient grid**: every odd `B<=99`, every `2<=M<=60`, every `3<=k<=10`; C2 cardinalities matched exactly. This includes `M=2` and all even composite moduli. The same grid isolated the C1 minimal-period exception: `M=2` has period `1`; every `M>2` has exact period `L_(B,M)`.
3. **Prime grid E/F**: every odd `B<=99` and every prime `q<=101`; E1 and F2 matched exactly, including all `q|B` cases.
4. **D distinct-slope grid**: odd `B<=99`, primes `q<=101`, `k<=10`, both chiralities, and `a=1,2` where the relevant same-parity slope difference is a `q`-adic unit; no mismatch with D2. The explicit `q=3,k=7` collision above demonstrates the necessity of the narrowing.
5. **D3 union grid**: for `q>k-1`, `q∤B`, odd `B<=99`, primes `q<=101`, and `3<=k<=10`, the union-over-chirality concurrence condition matched the product factors `B^2 A_T^2-1` exactly.
6. **G1 CRT grid**: odd `B<=99`, every squarefree `M<=60`; direct counts of transparent `H mod M` matched `product tau_B(q)`.
7. **Mandatory special `B` values**, reporting `(tau(2),tau(3),tau(5))`:
   - `B=1`: `(0,0,1)`;
   - `B=3`: `(1,1,0)`;
   - `B=5`: `(0,0,3)`;
   - `B=7`: `(1,0,0)`;
   - `B=15`: `(1,1,3)`;
   - `B=27`: `(1,1,0)`;
   - `B=39`: `(1,1,1)`;
   - `B=51`: `(1,1,1)`.
8. **E4**: across odd `B<=99`, every first-breaker phase had the asserted maximum `1`, `5`, or `9`; the first-breaker-5 classes (`B=3,27 mod60`) had extremal `H` classes exactly `{0,2}` modulo `5`.
9. **Negative/zero `H`**: included in the B-grid; modular transparency depends only on residue class, so no hidden positivity assumption enters E/F/G. G4's diagonal-integer exclusion was proved for all signed integers.
10. **`k=3,4` versus `k>=5`**: C is already rigid at `k=3`; D3 remains exact under its inherited `q∤B` assumption. The leading `B` factor must not be used to extend D3 to `q|B` for `k=3,4`, where no same-parity triple exists.
11. **Ordinary integer versus profinite**: finite coordinate systems lift by CRT; the full diagonal integer intersection is empty by the prime-divisor argument in G4.
12. **Tiny prime exceptions**: `q=2` and `q=3` were handled separately in E1; C3 excludes `q=2`; D's slope-collision example already occurs at `q=3`; H is retained at the exact breaker-coprime strength and is not promoted to an unrestricted prime-run claim.
13. **Witness I**: all twelve values reproduced exactly and passed the deterministic 64-bit primality replay.

## 5. Witness-I primality certificate / replay description

Replay procedure:

1. Compute the twelve values directly from `F_15(H,610+j)` using integer arithmetic.
2. Confirm each is `<2^64` (all are 50-bit).
3. Reject divisibility by the standard small primes through `37`.
4. For each remaining `n`, write `n-1=2^s d`, `d` odd.
5. Apply the strong Miller--Rabin test to the fixed deterministic 64-bit basis set
   `2,325,9375,28178,450775,9780504,179526502`.
6. All seven bases pass for all twelve numbers; by the deterministic `<2^64` basis theorem, every displayed number is prime.

This replay is independent of the withheld package checker.

## 6. Dependency graph

- `A1 -> abstract B=s provenance`.
- Frozen native `sector=3`, `{2,4}` curvature, and `18/6` source, together with `E2/E4 -> H`.
- `B1 -> B2` and supplies the normalized affine form used by `C1/C2/C3` and the line model in `D`.
- `C1 -> C2`; `C3` additionally uses `q>k-1` and `q∤B`.
- `D1` is geometric interpretation; `D2` is the determinant identity; `D2 + q>k-1 -> D3`.
- `F1/F2 -> generic odd-prime hit/intersection formula -> E1` (E1 was also derived directly).
- `E1 -> E2 -> E3/E4`.
- `E1 + CRT -> G1`; `G1 + E2 -> G2`.
- `E1 + Mertens + nonprincipal Dirichlet character prime sums -> G3`.
- `G1/G3 + product topology + PNT + mass-distribution -> G4`.
- `B definition + deterministic 64-bit primality theorem -> I`.

No verification row depends on a withheld source proof.

## 7. Exact list of narrowed statements

### N1 — C1 (`M=2` effective-period exception)

Replace the unqualified exact-period reading by:

- if `M>2`, the exact/minimal `R` period after the intercept is fixed is
  `L_(B,M)=lcm(2,M/gcd(B,M))`;
- if `M=2`, the exact/minimal effective `R` period is `1`.

C2 remains unchanged.

### N2 — D1 (chirality-dependent parabola shift)

Either restrict the original `Q_e=x^2/(2B)-e/2`, `e=0,1`, tangent statement to `chi=+1`, **or** replace it uniformly by

`Q_e^(chi)(x)=x^2/(2B)-chi e/2`, `e=0,1`.

The latter recovers both chiralities without changing the line family.

### N3 — D2 (distinct-slope / unit condition)

For a mixed triple with `u,v` the common-parity pair, require

`q∤(u-v)`

(or the stronger finite-window condition `q>k-1` for distinct indices). Then and only then the displayed obstruction alone is an iff criterion modulo every `q^a`.

D3 already imposes `q>k-1`, so its stated finite-window use is unaffected.

## 8. Final verdict

`PACKAGE_VERIFIED_WITH_NARROWING`

The blind packet is mathematically sound after the three explicit statement-strength repairs C1/D1/D2 above. All other audited rows A1--I are verified at their stated strength, with H kept at the exact E4 breaker-coprime capacity meaning and without promoting it to an unrestricted prime-run theorem.

Hard target achieved:

`NATIVE_FILAMENT_COUPLED_SELECTION_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`
