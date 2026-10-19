# RSA-270 continuation: at most four weighted local traces per odd-prime-power lift

Status: `RESEARCH NOTE / EXACT TRACE-COMPRESSION THEOREM + PORTFOLIO CONSEQUENCE / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T01:08:00+08:00`  
Parents:
- `research_notes/RSA270_ODD_PRIME_POWER_CHARACTER_ATLAS_20260908.md`
- `research_notes/RSA270_EXPLICIT_TERNARY_TRACE_DECODER_20260906.md`

No RSA-270 factor is obtained.

## 1. Goal

The odd-prime-power atlas proved that an `l`-adic lift has exactly l product-compatible ordered branches. A naive generalization of the ternary decoder might appear to require O(l) separately returned Ramanujan traces.

This note proves a stronger statement: **the complete local Ramanujan trace vector can be packed into at most four exact integer linear functionals, independently of l.**

The coefficient magnitudes of the packing weights grow with l, so this is a width theorem, not a claim that large-l arithmetic is free.

## 2. Local extreme packet

Let

`m=l^e`, `n=l^(e-1)`, `e>=2`,

with l odd prime. After subtracting the N-only and previous-level-determined packets, the normalized new factor packet has the form

`Z = zeta^tp - zeta^-tp + zeta^tq - zeta^-tq`,

where `zeta=zeta_m` and `tp,tq` are the positive normalized exponents determined by the current factor residues.

Modulo n, the four signed exponents lie in the known previous-level base fibers

`{+tp0,-tp0,+tq0,-tq0} mod n`.

Hence there are at most four occupied base fibers.

For an occupied base b and digit position `j=0,...,l-1`, put

`r_j=b+j n`

and define the integer Ramanujan trace

`L_(b,j)(Z)=Tr_(Q(zeta_m)/Q)(zeta_m^(-r_j) Z)`.

For prime-power modulus m,

`Tr(zeta_m^k) = (l-1)n` if `k=0 mod m`,
`=-n` if `k` is a nonzero multiple of n modulo m,
`=0` otherwise.

## 3. One base fiber is a signed digit histogram

Inside one fixed previous base b, write the signed current exponents as

`t_s = b+d_s n`, `d_s in {0,...,l-1}`, `epsilon_s in {+1,-1}`.

Define the signed digit counts

`C_j = sum_(s:d_s=j) epsilon_s`.

There are only four signed monomials globally, so

`C_j in {-2,-1,0,1,2}`.

Let

`Ctot=sum_j C_j`.

Then exactly

`L_(b,j)/n = l C_j - Ctot`.

Thus the entire l-component trace vector on one base fiber is equivalent to the signed histogram `(C_0,...,C_(l-1))`.

## 4. Pack one complete fiber into one integer functional

Choose any integer base `B>=6`; for definiteness take `B=10`.

Define the weighted local trace

`W_b(Z)=sum_(j=0)^(l-1) B^j L_(b,j)(Z)`.

Since `Ctot` and the set of signed terms occupying b are known from the previous-level state,

`W_b/n
 = l sum_j B^j C_j - Ctot sum_j B^j`.

Therefore W_b determines

`sum_j B^j C_j`.

This code is injective on all possible signed histograms with `C_j in [-2,2]`: if two histograms differed, their difference digits would lie in `[-4,4]`; for B>=6 the highest nonzero digit term strictly dominates the total possible contribution of all lower digits.

Hence **one weighted integer trace reconstructs the full ordinary Ramanujan trace vector on one occupied previous fiber.**

## 5. At most four weighted traces separate every product-compatible lift

There are at most four occupied previous base fibers, so at most four weighted functionals `W_b` reconstruct all Ramanujan traces that can possibly see a difference between candidate lift packets.

Why do these traces separate distinct product-compatible unordered factor lifts?

- all lower/intermediate packets are fixed by the previous factor residue state and cancel in a candidate difference;
- if two candidate extreme packets produced the same trace on every occupied base fiber, their difference would pair to zero with every cyclotomic monomial trace that can see its support, hence the extreme packets would be equal in `Q(zeta_m)`;
- applying the faithful primitive-character projector would then give the same twisted coefficient `A_(l,e)(N)`;
- N already fixes the product of the two faithful character values;
- equal sum + equal product fixes the same unordered character pair, and faithfulness fixes the same unordered factor residues modulo `l^e`.

Contradiction.

Therefore:

**Theorem (four-trace local compression).** At every odd-prime-power lift level `e>=2`, the l-way product-compatible branch can be selected using at most four explicitly constructed weighted integer Ramanujan-trace functionals, given the previous unordered factor residue pair.

For l=3 under the RSA Challenge H2 sector separation, the earlier unweighted 2--4 trace decoder remains simpler; this theorem is the uniform odd-prime generalization.

## 6. Finite verification

The attached verifier exhaustively constructs local candidate sets from random unit factor residues and checks weighted-signature injectivity for

`l in {3,5,7,11,13}`,

`e in {2,3,4}`,

200 random states per `(l,e)` pair.

All candidate lift signatures are distinct using B=10 and at most four occupied base fibers.

This is verification of the implementation/model; the theorem itself is the exact argument above.

## 7. Mixed-radix cost consequence

Because the number of returned weighted trace integers can be bounded by four per prime-power level, increasing l does not necessarily increase **output count** linearly with l. It does increase coefficient size and the complexity of evaluating each weighted functional from the product side.

Using the equal-depth mixed-radix examples from the atlas and counting at most four weighted traces per unresolved level gives the rough uniform upper bounds:

| towers | common terminal depth E | unresolved levels | <= weighted traces | final CRT candidates |
|---|---:|---:|---:|---:|
| `{3}` | 141 | 140 | 560 | 2 |
| `{3,5}` | 58 | 115 | 460 | 4 |
| `{3,5,7}` | 34 | 101 | 404 | 8 |
| `{3,5,7,11}` | 22 | 87 | 348 | 16 |
| `{3,5,7,11,13}` | 17 | 84 | 336 | 32 |
| `{3,5,7,11,13,17}` | 13 | 77 | 308 | 64 |
| `{3,5,7,11,13,17,19}` | 11 | 76 | 304 | 128 |
| `{3,5,7,11,13,17,19,23}` | 9 | 71 | 284 | 256 |

For a fixed number of towers, the final `2^k` CRT pairing factor is a constant and each candidate can be sent to the divisor-in-residue-class/Coppersmith handoff once the combined modulus exceeds `N^(1/4)`.

This table is **not** a runtime claim. It counts only branch-observable outputs. Product-side evaluation cost may grow substantially with l and is still the unresolved bottleneck.

## 8. Updated preferred question

The output-width objection to mixed prime bases is now weaker: even an l-way lift can be compressed to <=4 exact integer functionals.

The decisive unresolved issue is therefore the **input-side cost** of one weighted trace:

`W_b = sum_j 10^j Tr(zeta^(-(b+jn)) Z)`.

The next experiment should push this combined functional directly through the BRC product/Cartier representation and measure the minimal state required to evaluate **only W_b at one target N**, rather than the globally nonautomatic full twisted coefficient sequence.

If target-adaptive W_b admits polylogarithmic state while the full coefficient does not, that would be the first genuine opening left by the finite-state no-go.
