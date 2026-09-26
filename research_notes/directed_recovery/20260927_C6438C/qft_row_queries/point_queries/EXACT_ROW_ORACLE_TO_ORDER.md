# One exact native prefix-row query suffices for modular order

Status: AUTHOR_DERIVED_AND_BOUNDED_EXECUTED / SHARED_CONTEXT / NOT_ADMITTED.
Activity: RA-CAAAC604CB513AEA8BBC1DFC. This is a reduction identifying the
strength of the proposed generic query interface, not an efficient oracle,
an impossibility theorem, or a lower bound on typical sampler trajectories.
The algebra was independently checked by a second shared-context author.

Let N>=3 and gcd(a,N)=1. Put n=ceil(log2 N), t=2n and i=t-1. Consider the
actual recorded prefix h=0^i in the existing native two-H4 instrument.
Every history-controlled feedback is the identity for this prefix,
regardless of the other certified phase words in the bank. Its first i
work multipliers are a^(2^(t-1)),...,a^2. Set Q=2^i and s=ord_N(a^2).

Expanding the two actual arms from the standard initial work label 1 and
internal vector e0 gives

    v_h(w) = (1/Q) #{0<=j<Q : a^(2j)=w mod N} e0.

This is a raw, unnormalized complete row, not the normalized conditional
state or a branch probability. In particular,

    alpha = v_h(1)_0 = C/Q,       C=ceil(Q/s).

The prefix has nonzero probability, so this is an eligible prefix query.
No order is assumed available to evaluate it: obtaining alpha is exactly
the oracle call whose difficulty this reduction exposes.

## Recovering s from alpha

Write r=ord_N(a). Then s=r/gcd(r,2). The group of units has even order
phi(N) for N>=3 and r divides phi(N). If r is even, s=r/2<=phi(N)/2.
If r is odd, phi(N)/r is a positive even integer, hence s=r<=phi(N)/2.
Thus s<2^(n-1), while Q=2^(2n-1), in particular Q>s(s-1).

For s=1 the result below is immediate. For s>1, C>=Q/s yields Q/C<=s.
Also C<Q/s+1 and Q>s(s-1) yield C(s-1)<Q. Therefore

    s-1 < Q/C <= s,
    s = ceil(Q/C) = ceil(1/alpha).

Finally compute a^s modulo N. If it is 1, r=s; otherwise r=2s. This is
one exact complete-row query, one exact rational reciprocal/ceiling and
one modular exponentiation. The implementation also verifies a^r=1 as an
extra check, and performs the integer division and modular powers using
the inherited actual typed full-adder transducers.

The elementary facts about orders are Lagrange's theorem and the kernel
formula for the square map in a cyclic subgroup. They are used to prove
the recovery formula; phi(N) and the factors of N are never computed.

## Consequences and precise limits

A uniform polynomial-time exact oracle for arbitrary legal prefix rows of
this instrument would already supply polynomial-time modular order finding,
and hence the usual randomized factoring route. It would be a major result,
not a bookkeeping optimization hidden behind the phrase 'two row queries'.

This does not show that order finding is impossible, that polynomial-time
classical factoring cannot exist, or that the present sampling objective
requires exact worst-case point queries. In particular:

- The single walker need not visit this all-zero prefix on a typical run.
  Its probability can be small. A distribution-specific or approximate
  query guarantee need not answer this adversarial exact query efficiently.
- Replacing alpha by a normalized amplitude loses the displayed formula.
- An arbitrary additive-error answer cannot be inserted into the ceiling
  operation without a separate precision and rounding proof.
- An oracle specialized to typical sampled prefixes, or a direct sampler
  avoiding arbitrary row queries, remains a valid research direction.

This makes the next research target sharper: exploit average-case
trajectory structure with a proved global sampling-error bound, or solve
the exact modular fibre sum itself. Do not assume the latter is cheap.

## Bounded actual execution

`check_order_reduction.py` used the exact checkpoint oracle and the admitted
full-D61 bank, with default width t=2 ceil(log2 N). It queried the complete
row at label 1 once per case, then performed typed recovery:

| N | a | t | Recovered order of a^2 | Recovered order of a |
|---|---:|---:|---:|---:|
| 15 | 2 | 8 | 2 | 4 |
| 21 | 2 | 10 | 3 | 6 |
| 21 | 4 | 10 | 3 | 3 |
| 35 | 2 | 12 | 6 | 12 |
| 143 | 2 | 16 | 30 | 60 |

All five matched separately enumerated actual typed modular orbits. Orbit
enumeration happened only in the checker, after recovery, and was never
passed into the algorithm. The run used 307 BRC core calls in total; full
adder digit work, row-oracle work, typed traces, complete rows and source
hashes are retained. Wrong prefix depth and a nonzero history bit were
rejected. No ideal-QFT reference was executed and no fast factoring
performance claim follows from these small bounded checks.
