# Collaborative check of the gap-one dyadic witness geometry

2026-11-24, Researcher `EM-DIRECT-970E1C`, Activity
`RA-D2EC212845B63844081F9A14`. Shared-context mathematical checking, not
independent project Review or formal proof acceptance.

Inspected `nine_gap_v15/verify_gap_spectrum.py`, `base_geometry.json`, and
the saved certificate structure. The complete frozen
`nine_gap_v15/proof.md` has now also been read, together with the seed
progression argument in Section 5 of `nine_one_min_v15/proof.md`. This
review covers the general fixed-prime incidence mechanism, collision
CRT, and the written theorem for every k>=1, with the separate s=9
seed linkage. No large integer examples were rerun.

## Parent class and old witnesses

The parent prime 1429 has zero class n=68 modulo 84. The retained base
has 27 primes: nineteen from P, with 113 omitted, and eight supplements.
Each retained old witness avoids n=12 modulo 28. Every new prime order
is divisible by 28 and its zero phase is 12 modulo 28, so no new prime
hits an old witness.

The new orders D_j=84*2^j and T_k=28*2^k are pairwise distinct: equality
across the two groups would require a power of two to equal three times
a power of two. For j>=1, none equals an order in the retained base or
fixed 43 coordinates; the low cases 56,112,168 are explicitly absent,
and all later orders exceed the fixed maximum 180. Thus primitive-prime
selection gives new, mutually distinct ordinary primes without requiring
two primes of one specified order.

On n=68+84i, the new zero classes are the shifted binary classes
i=3+2^(j-1) modulo 2^j, and the terminal i=3 modulo 2^k. They partition
the full parent class. The T order also has precisely that effective
period on the parent class because gcd(3,2^k)=1. Its extra hits outside
the parent class cause no witness collision, by the modulo-28 exclusion.

## The fixed-prime obstructions are separated

Every new witness additionally imposes i=21 modulo 45, equivalently
i=3 modulo nine and i=1 modulo five. This condition is coprime to every
binary modulus, so it can be imposed at every level.

For n=68+84i under this condition, no old P prime, 5,13,73,19 or 246241
hits. The finite incidence table and period divisibilities establish the
same fact for all such i, not just the first four checked levels. In
particular, 19 would require a different i modulo three, and 246241 would
require i=0 modulo nine.

The fixed 38737 channel hits exactly when i is even. Only D_1 has that
parity. The fixed 487824887233 channel hits exactly when i=1 modulo four
after i=0 modulo three is imposed. Only D_2 has that class. For j>=3,
all D_j have i=3 modulo four. Every terminal witness has the same class,
because the construction explicitly uses modulus 2^max(k,2); the extra
modulo-four condition on T_1 is necessary and correctly included.

Among retained old witnesses, the witness assigned to 649657 has the
fixed extra factor 19. It is the only such old witness. Since every new
witness avoids 19, this does not obstruct mutual coprimalization. The
fixed 38737 and 487824887233 factors occur respectively only at the new
D_1 and D_2 witnesses. The general fixed-prime incidence is therefore
at most one chosen witness per fixed prime.

## Exact costs after coprimalization

The eight retained supplemental witnesses are P-free; the k+1 new
witnesses are also P-free. Thus there are s=9+k P-free witnesses among
28+k total witnesses. If the collision CRT makes all total witnesses
pairwise coprime, it simultaneously proves delta_P>=9+k and tau>=28+k.
The constructed cover supplies the corresponding upper bounds.

The collision identity is exact:
gcd(F_n,F_m)=gcd(F_min(n,m),2^abs(n-m)-1).
For the lcm of these difference values, saturating away all prime powers
dividing the phase modulus is legitimate because each fixed or selected
prime hits at most one witness. The structural primes 2 and 3 are also
harmless: all witnesses have positive indices and hence odd F_n, while
every R3 root is zero modulo three and hence F_n=-1 modulo three.
Setting a=0 modulo the remaining coprime collision cofactor kills every
other possible common prime. No factorization or primality assertion
about that cofactor is needed.

All roots in the resulting CRT progression preserve both the cover and
these gcd exclusions. This supports the general s>=10 construction.
The s=9 seed is separate: its already verified 28 coprime witnesses
persist on a suitable finite congruence class, giving infinitely many
roots with the same exact costs. No infinite-cost root is inferred.

No fixed-prime collision obstruction was found in the corrected binary
shift-three construction. The earlier ternary construction's collision
with fixed 19 is genuinely avoided by the new choice.

## Follow-up on the complete general proof

The all-k claim is supported by the formulas, not by the illustrative
first four levels. The first binary position at which i differs from
three assigns exactly one D_j, unless i is in T_k. The indicated root
residues therefore cover the whole parent progression. The distinct
orders 84*2^j and 28*2^k give distinct new primes for every k, using only
the stated primitive-prime-divisor input. Their exact effective orders
on n=68+84i are 2^j and 2^k. The terminal's extra full-sequence hits have
n=12 modulo 28; the alternatives n=0 and 4 modulo twelve are already
covered by 13 and 7. No extra old witness is hit because all 27 old
exponents avoid n=12 modulo 28.

Equations (9)--(10) impose the same i=21 modulo 45 condition at every
level. Together with the explicit binary residues, they keep the fixed
19 collision only at the old 649657 witness, the fixed 38737 collision
only at D_1, and the fixed 487824887233 collision only at D_2 when it
exists. The fixed 246241 channel hits none. This checks the exact
fixed-prime incidence needed for the entire family, including the k=1
terminal boundary case. All new witnesses are P-free, so the count of
P-free mutually coprime terms is exactly 8+(k+1)=9+k.

The structural factor three is a consequence of the actual R3
constants, not an additional restriction on the constructed roots.
Direct reduction of the A3 and S3 integers embedded in
`nine_gap_v15/verify_gap_spectrum.py` gives

```text
A3 mod 6 = 3
S3 mod 6 = 0
```

The source also checks S3=6*product(fixed 43 primes). Hence every
a=A3+S3*j is 3 modulo six, in particular a=0 modulo three, and every
F_n(a) is -1 modulo three. The structural factor three in the fixed-fiber
modulus is thus accounted for directly from the defining constants.

The saturation step accounts for every possible common prime of any
two full integer witnesses: either it divides the coprime remaining
cofactor and is killed by a=0 there, or it divides M0 and is excluded
by the fixed/selected incidence argument, with two and three treated
as above. No prime-size bound is introduced. The resulting progression
preserves R3 and all covering phases. Removing finitely many initial
roots makes every chosen divisor proper while leaving infinitely many
ordinary roots. Thus the proof supplies

\[
\delta_P(a)=9+k,\qquad\tau(a^2)=28+k
\quad\text{for every integer }k\ge1.
\]

For s=9, the companion seed proof fixes all selected phases and the
complete false budget-eight predicate, and takes its progression step
divisible by every witness difference value 2^|n_i-n_j|-1. The exact gcd
identity then preserves its 28 pairwise-coprime full terms. This is a
valid separate seed step within the author proof and completes all
s>=9, without applying the dyadic construction at k=0.

Combining this family with the cited inherited (s,s+20) family on
R4 contained in R3 gives the two asserted joint finite-cost values for
each s>=9. This review checks that implication and its scope; it does
not independently re-prove the inherited family. It also does not
classify all joint costs, establish any infinite-cost root, or assert
that the large constructed roots are minimal. No necessary correction
to the frozen general proof was found.
