# PREFIX-892 — Dyadic-complement two-flip collision certificate

Date: 2026-11-18 (Asia/Shanghai). Scientific model: frozen pin \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Predecessors: PREFIX-887 (axis collision), PREFIX-889/891 (zero/flip multiplicity and endpoint criterion), PREFIX-883 (complete FF collisions). Author research continuation; mathematical status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED**. Independent BRC observation auxiliary result, not an assertion of X6 native time-dynamics execution or possession of a shared CLAIM.

## Model and the new question

Let p>=2, N=2^p, b=2^(p-1), and q1,q2>1 odd. Legal **named directed** trajectories are (x,x) or (x,x xor 2^i), 0<=x<N, 0<=i<p, each with its actual named source and ordered first/second time ports. The observation is Phi(s,t)=(s mod q1,t mod q2). We seek constructive FF collisions that are outside the previously counted single-axis and zero/flip (ZF) families. The method preserves the source name, XOR legality, temporal port order and explicit witness, rather than quotienting distinct trajectories by a bare numerical difference.

## Theorem 892-A (dyadic positive-completion obstruction)

For arbitrary p>=2 and odd q1,q2>1, the existence of **positive integers** k,l with

  k*q1 + l*q2 = 2^p

is sufficient for a collision of **two distinct** legal one-source-flip trajectories, both flipping the **same named highest bit p-1**. In fact it supplies the following explicit witnesses.

Put a=k*q1, c=l*q2, b=2^(p-1), so a+c=2b and 0<a,c<2b. Since q1,q2 are odd and >1, neither a nor c can equal b.

* If a>b: X=(0,b), Y=(a,a-b).
  Both toggle bit p-1 (0 -> 1 and 1 -> 0). First observations agree because a=k*q1. Second observations agree because (a-b)-b=a-2b=-l*q2.
* If a<b (so c>b): X=(b,0), Y=(c-b,c).
  Both toggle bit p-1 (1 -> 0 and 0 -> 1). First observations agree because (c-b)-b=c-2b=-k*q1. Second observations agree because c=l*q2.

Every endpoint lies in [0,2^p), the trajectories are distinct, and the named source and both time ports are explicit. This is a general **sufficient collision theorem**, not a claimed equivalence with all FF collisions. The positive-completion predicate is equivalent to existence of a collision **in the displayed construction family**.

For odd q1,q2, positive completion also forces gcd(q1,q2)=1: their odd gcd must divide 2^p, hence is 1.

## Theorem 892-B (constant-candidate exact CRT test)

Assume q1*q2>N; in particular this holds when p=32 and both moduli have exactly 19 bits. Set K=floor((N-1)/q1). If gcd(q1,q2)>1, no positive completion is possible. Otherwise let

  k0 = (N * (q1 inverse modulo q2)) mod q2,  1<=k0<q2.

Then positive completion exists **if and only if**

  k0*q1 < N.

Proof: any solution has k*q1<N<q1*q2, so 0<k<q2. Reduction modulo q2 forces k=k0. Conversely, k0*q1<N makes l=(N-k0*q1)/q2 a positive integer; the congruence guarantees exact divisibility. Thus one modular inverse and one bounded candidate suffice. The test is **complete for the positive-completion family**.

## Theorem 892-C (all lower-bit zero-anchored same-source FF collisions shadow ZF)

Take any i in [0,p-2] and a legal collision of the special zero-anchored pair

  X=(0,2^i), Y=(a,a xor 2^i),

where bit i of a is 1. Then a=k*q1 with k>=1 and q2 divides a-2^(i+1). Necessarily gcd(q1,q2)=1. Moreover k<=K, and the least positive solution r_(i+1) of

  r_(i+1)*q1 = 2^(i+1) (mod q2)

obeys r_(i+1)<=k<=K. By the PREFIX-891 downward-endpoint criterion, a ZF collision already exists with named bit i+1. Therefore **the only bit index capable of adding new exclusions through this particular zero-anchored same-source FF family beyond ZF is the highest bit p-1**. At that bit, the congruence becomes q2 | (a-2^p), precisely the positive-completion identity of Theorem 892-A.

The ZF shadow statement is about this named zero-anchored FF family, not arbitrary two-flip transitions.

## Exact strict-19-bit panel experiment

Declare Q={262145,262147,...,524287}, |Q|=131072. Hold q1 successively at

  262147, 280001, 300001, 320003, 340007, 360007, 380003, 400009,
  420001, 440003, 460001, 480007, 500383, 510007, 520001, 524285.

Each q1 is outside PREFIX-887's A_32 single-axis family. Scan **all** q2 in Q, hence exactly 2,097,152 ordered pairs. Apply the complete PREFIX-891 ZF endpoint criterion separately; determine membership of q2 in A_32. An explicit exact modular inverse tests positive completion; each positive result is checked against the actual two named XOR trajectories.

| Exhaustive panel category | Ordered pairs |
|---|---:|
| Full specified panel | 2,097,152 |
| ZF collisions, PREFIX-891 | 1,308,292 |
| Positive-completion FF collisions | 59,405 |
| Positive-completion, already ZF | 49,019 |
| **New beyond BOTH single-axis and ZF** | **10,386** |
| Positive completion using a>b orientation | 29,623 |
| Positive completion using c>b orientation | 29,782 |

The 10,386 pairs have q1 and q2 outside A_32 and fail the ZF endpoint criterion; this is **non-overlapping coverage relative to those two earlier predicates**. They may overlap other previously constructed FF collision families. The 16 separate q1 rows are disjoint; the row counts and canonical first witness for each row are in \`PREFIX892_R6_DYADIC_COMPLEMENT_RESULTS.json\`.

One new example: q1=262147, q2=263307, k=3715, l=12613, a=973876105, c=3321091191. Check k*q1+l*q2=4294967296 and c>b=2147483648. Then

  X=(2147483648,0),
  Y=(1173607543,3321091191)

are two distinct legal top-bit XOR flips with identical observations. This pair is outside both A_32 and ZF.

## Reproduction and evidence boundaries

* \`PREFIX892_R6_DYADIC_COMPLEMENT_CHECK.py\`: Python3, exact integer operations only, exhaustive 16 x 131072 scan, extended independently from prior PREFIX-891 endpoint implementation; rechecks every constructed pair's XOR rule and both modular observations.
* \`PREFIX892_R6_DYADIC_COMPLEMENT_CENSUS.cpp\`: C++17, independently coded extended Euclid and same-domain scan. The two full-panel implementations agreed on all 16 row records and totals. The C++ checker also compared CRT exact existence against direct integer-k enumeration in 12,362 small q1/q2/p cases (p=2..10, q1/q2 odd 3..79, q1*q2>2^p); zero discrepancies. A separate Python independent modular-inverse and witness check reverified the full q2 domain for q1=262147,400009,524285.
* The complete arithmetic and row-level certificate is \`PREFIX892_R6_DYADIC_COMPLEMENT_RESULTS.json\`. Its \`small_crt_brute_cases\` refers to the C++ crosscheck. Source integers are exact, no floating point.
* Theorem 892-A/B/C are deductive mathematical arguments; the finite computation confirms the declared panel and does not enlarge the theorem to the full 19-bit pair domain. No formal proof assistant or independent mathematical peer review is claimed.

## Next unfinished unit

Form the exact remaining ordered-pair predicate excluding A_32 on both ports, PREFIX-891 ZF, and this positive-completion family. On its survivors, use the general PREFIX-882 modular-inverse search and PREFIX-883 exact witness counter with both named source indices (including mixed indices), maintaining one witness per excluded parameter pair and an exhaustive, non-overlapping coverage manifest. The wider frozen scientific objective remains B_fix,odd(32) in {19,20}; the actual value remains open at this stage. The X6 native time Task retains its separate owner and frozen-event/admission frontier.
