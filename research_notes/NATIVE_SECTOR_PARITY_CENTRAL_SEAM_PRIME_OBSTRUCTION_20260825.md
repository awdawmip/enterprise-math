# Cyclic shell allocators: sector-parity bifurcation and the even-sector central-seam prime obstruction

Status: `FREE_RESEARCH_EXACT_COMBINATORIAL_CONTROL / NOT_CANONICAL_HIGHER_SECTOR_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

This is an abstract shell-allocation comparison. Only s=3 is the current native Enterprise geometry.

## 1. General cyclic shell allocator

Take s cyclic blocks on shell r, each with r side positions.

The shell base is

`B_r^(s)=1+s*r*(r-1)/2`,

and the label is

`N_s(r,t,sigma)=B_r^(s)+sigma*r+t`.

## 2. Odd s: one central block

If s is odd, there is a unique central block

`sigma_*=(s-1)/2`.

The half-step zigzag

`t=h+ceil(r/2)`

cancels the linear shell drift and produces

`N_s(r)=h+1+(s*r^2+eps(r))/2`.

Thus odd sector count creates the parity-curvature family studied in the master theorem.

## 3. Even s: the center is a seam

Let s be even.

The two central blocks are

`sigma_L=s/2-1`,

`sigma_R=s/2`.

Take positions at equal combinatorial distance h from their common seam:

left: `t_L=r-1-h`,

right: `t_R=h`,

with `0<=h<r`.

Their labels simplify exactly to

`L_s(r,h)=s*r^2/2-h`,

`R_s(r,h)=s*r^2/2+1+h`.

Therefore

`R_s-L_s=2h+1`.

This gap is always odd.

## 4. Prime obstruction

If both labels exceed2 and are prime, both must be odd. Their difference must then be even.

But the reflected central-seam gap is always odd.

Therefore:

`NO EVEN-SECTOR CENTRAL REFLECTION PAIR CAN CONTAIN TWO PRIMES >2`.

The only possible double-prime exceptions must involve the prime2 and hence occur only at bounded tiny labels.

This is an exact parity obstruction independent of any density heuristic.

## 5. Geometric selection consequence

The central symmetry type of the shell allocator bifurcates by sector parity:

- odd s -> a unique central block and one parity-curvature trajectory;
- even s -> a central seam whose reflected Cell pairs have opposite parity and cannot both be nonexceptional primes.

Thus any cyclic shell allocation seeking a nonexceptional reflection-centered prime filament must use an odd sector count.

The smallest positive odd count is1, which is a degenerate one-sector allocator. The smallest nontrivial cyclic multi-sector count is therefore3.

## 6. Combined selection of s=3

The odd-sector breaker theorem further shows:

- s=3 is nonbreaking at channels2 and3;
- s=3 breaks at5;
- no finite breaker can occur later than5 in the whole odd-curvature family.

Hence s=3 is simultaneously

1. the smallest nontrivial sector count with a central block rather than a seam;
2. the smallest sector count not killed by the even-seam prime-pair obstruction;
3. the smallest odd coefficient attaining the latest possible finite first-breaker channel5.

This strengthens the current tri-sector selection principle without claiming that abstract s-sector allocators for s!=3 are canonical Enterprise geometries.

## 7. Boundary

Parity of prime numbers and the combinatorics of block centers are elementary. The research-specific value is the way this control family isolates why the actual three-sector allocation supports the native parity-curvature prime filament while even-sector analogues fail at the central-symmetry level.