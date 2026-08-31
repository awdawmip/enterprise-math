# Native Enterprise C3 shell-unit identity fiber and parity selection

Status: `FREE_RESEARCH_EXACT_SELECTION_LEMMA / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_SHELL_RESIDUE_COLLAPSE_INVARIANT_20260823.md`

## 1. Identity fiber

In shell-residue coordinates, define the shell identity fiber by

`rho = 1 in Z/rZ`.

For the fixed monotone tri-sector allocation, there is exactly one such folded fiber in every shell because `t -> rho` is a bijection.

Its geometric side location depends only on the parity of `r`.

### Odd shell

If `r` is odd, `rho=t+1 mod r`. Therefore

`rho=1 <=> t=0`.

So the shell identity is the C3 orbit of the three positive-axis boundary states.

### Even shell

If `r=2m`, `rho=t+m+1 mod 2m`. Therefore

`rho=1 <=> t=m=r/2`.

So the shell identity is exactly the equal-coordinate C3 midpoint orbit

`(m,m,0), (0,m,m), (m,0,m)`.

Freeze:

`ODD SHELL: UNIT IDENTITY -> AXIS FIBER`.

`EVEN SHELL: UNIT IDENTITY -> EQUAL-COORDINATE MIDPOINT FIBER`.

This is an exact axis/bisector parity duality of the chosen native allocation.

## 2. Prime-compatible parity selects the midpoint

Every nonexceptional fully-prime C3 fiber `{c-r,c,c+r}` has even common difference `r`; otherwise parity forces an even composite member.

The stronger universal C3 prime gate already gives `6|r` for labels greater than 3.

Therefore, whenever the canonical shell identity fiber is considered inside the full-prime regime, the parity requirement automatically places it on the equal-coordinate midpoint rather than on the axes.

Selection chain:

`SHELL MULTIPLICATIVE IDENTITY rho=1`

`+ FULL-PRIME PARITY r even`

`=> EQUAL-COORDINATE MIDPOINT`.

Thus the midpoint does not need to be selected first by visual symmetry.

## 3. Exact shell-unit recoalescence

For even `r`, the identity/midpoint center is

`c = 3r^2/2 + 1`.

Hence the three labels are

`M_-(r)=3r^2/2-r+1`,

`M_0(r)=3r^2/2+1`,

`M_+(r)=3r^2/2+r+1`.

Each satisfies the stronger exact congruence

`M_-(r) == M_0(r) == M_+(r) == 1 (mod r)`.

So the earlier observation that a fully bright midpoint on `210|r` recoalesces to `1 mod 210` is only a shadow of the stronger shell theorem:

`IDENTITY MIDPOINT RECOALESCES TO 1 MOD THE ENTIRE SHELL INDEX r`.

Every prime divisor of `r` is therefore automatically harmless to this fiber.

## 4. Relation to the 210 gate

The `210|r` condition does not create the residue-1 recoalescence. The recoalescence is already exact for every even shell.

Instead, the 210 gate says that for the identity fiber to have all three labels prime, the initially saturated local obstructions from `2,3,5,7` force those primes into the shell index itself:

`2*3*5*7 | r`.

Once a prime q is absorbed into `r`, the identity fiber is automatically safe from q because every member is `1 mod r` and hence `1 mod q`.

This separates two mechanisms cleanly:

1. `rho=1` gives universal shell-divisor safety;
2. the small-prime root-slot saturation forces `2,3,5,7` to become shell divisors.

## 5. Minimality

Within one shell, `rho=1` is unique by the residue bijection.

Within the even-shell monotone geometric presentation, `t=r/2` is therefore the unique folded fiber whose three labels all reduce to the multiplicative identity modulo the full shell index.

This gives an arithmetic characterization of the equal-coordinate midpoint independent of counting how many primes happen to lie on it.

## 6. Boundary

The congruence calculations are elementary. The Enterprise-specific research content is the selection route

`C3 shell fold -> shell residue ring -> multiplicative identity -> parity switch -> equal-coordinate midpoint`.

Current verdict:

`EQUAL_COORDINATE_MIDPOINT = PRIME-COMPATIBLE GEOMETRIC REALIZATION OF THE SHELL UNIT IDENTITY`.
