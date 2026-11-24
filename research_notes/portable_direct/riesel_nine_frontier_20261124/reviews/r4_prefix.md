# Targeted check: every nine-cover on R4 contains the four-prime prefix

2026-11-24. Author-side collaborative check, not independent project Review.
This note uses the basic-pair theorem of `nine_prefix_v14/proof.md`, its
complete one-W theorem, and the fixed R4 definition of the companion spectrum
proof. No full nine-cover classification is assumed here.

The complete eight-budget observer is identically false on R4, so every
complete dictionary of size at most nine has size exactly nine and is
inclusion-minimal. The basic-pair theorem forces 5 and 13. A dictionary with
exactly one of 19 and 73 would, by the complete one-W theorem, contain all of
Z={29,43,1429,5419}; every one of these channels is inactive on R4. Hence that
case is impossible.

It remains to exclude a dictionary omitting both 19 and 73. After P,5,13 the
holes are n=8+12v, with

\[
A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod{35}.
\]

The two required fibers v=0 and v=1 modulo three each have A-mass normalized
to one. Their total required mass is two. At most seven other channels are
available.

## Channels meeting both fibers

Put f=ord_q(2^12). If 3 does not divide f, the channel can meet both fibers,
and its effective period in each is f. The coordinate change is invertible
modulo 35, so each fiber has the same incidence maxima for the gcd columns
1,5,7,35, namely 13,5,3,1.

All eligible f=7, f=8 and f=10 primes are inactive on R4. Explicitly:

* f=7 uses Z; other prime factors of the relevant orders are old.
* f=8 has base-two orders 32 and 96: old 65537 and the now-zero 193,22253377.
* f=10 has base-two orders 40 and 120: the now-zero 61681,4562284561.

The smaller eligible periods are old/basic/inactive by the inherited order
inventory. Therefore the following sufficient single-fiber bounds apply:

| gcd(f,35) | Sufficient lower f | Relative mass per fiber |
|---:|---:|---:|
| 1 | 11 | 1/11 |
| 5 | 20 | 5/52 |
| 7 | 14 | 3/26 |
| 35 | 35 | 1/13 |

Some candidates in the last two columns are also inactive on R4; leaving
them in is an upper-bound relaxation. Every entry is at most 3/26. Hence
the combined contribution of one such prime to both fibers is at most 3/13.
No independence between its two induced phases is assumed.

## Channels meeting just one fiber

If 3 divides f, a phase can meet at most one of v=0 and v=1 modulo three.
Its effective period there is h=f/3=ord_q(2^36). The R3 fixed small-order
inventory, after omitting both W primes, gives h>=6 on these two fibers.
In particular the other fixed active tail channels all have v=2 modulo three,
and every potentially useful h=5 channel is inactive.

The same four gcd columns now give sufficient single-fiber bounds

\[
1/6,\qquad5/26,\qquad3/13,\qquad1/13,
\]

with respective lower periods 6,10,7,35. Each is at most 3/13, and the other
fiber contributes zero. Thus this type also has combined mass at most 3/13.

## Conclusion and density normalization

Seven channels have combined mass at most 7*(3/13)=21/13<2. They cannot
cover both fibers. Each fiber has full-exponent density 13/(12*3*35)=13/1260,
so the remaining combined mass at least 5/13 gives the sufficient uncovered
density bound

\[
\frac{13}{1260}\frac5{13}=\frac1{252}.
\]

Consequently every complete supplementary dictionary of size at most nine
on R4 contains both W primes as well as 5 and 13:

\[
\boxed{Q_0=\{5,13,19,73\}\subseteq Q.}
\]

This is a prefix necessity statement. It does not require the subsequent
five-tail classification and makes no claim that all such dictionaries
contain the larger seven-prime fixed active prefix.
