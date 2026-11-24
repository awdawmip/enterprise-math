# The basic pair is forced through supplementary budget eight

Date: 2026-11-24. This is a new author-level continuation of the fixed-square-Riesel analysis, obtained during collaborative checking of the seven-prime classification. It is not an independent project Review. The task keeps the fixed X6 anchor, the full integer register, and the positive singleton BRC update \(x\mapsto2x+1\); exponent fibers and prime channels are arithmetic observations of that state.

## Statement and reused input

Use \(F_n(a)=a^2 2^n-1\), the old twenty-prime dictionary \(P\), and the root family \(R_1\) of the seven-cover source. Explicitly, \(a\equiv a_*\pmod{6M}\), where

\[
a_*=690786768637635218740714348513373826260012289,
\qquad M=1397394912916194098609132326092145093313722687204526281,
\]

and the fixed residues at primes \((5,13,11,61,331,19,37,73,109)\) are \((3,1,0,0,0,6,0,37,0)\). The inherited even-index holes are \(u\in H\pmod{105}\), where \(n=2u\) and

\[
\begin{split}
H=\{&0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,\\
&55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100\}.
\end{split}
\]

The fixed phases of \(5,13,19,73\), in that order, are \(u=1\bmod2\), \(u=0\bmod6\), \(u=4\bmod9\), \(u=1\bmod9\). Primes 3,11,61,331,37,109 are inactive.

**Theorem.** For every \(a\in R_1\), every complete supplement \(Q\subseteq\mathbb P\setminus P\) of at most eight distinct primes contains both 5 and 13. More quantitatively, any supplement of at most eight primes that omits at least one of these two primes leaves full-exponent uncovered density at least \(1/2520\).

The density bound is a sufficient obstruction; it is not asserted optimal.

The proof reuses the all-prime incidence formula and the exact small-period inventories in the seven-cover source `basics/proof.md`, which are themselves based on the five-cover global proof. The new arithmetic exclusion is effective parity period eight, and the new obstruction uses compulsory overlap.

## 1. Omitting both basic primes

Outside old/basic/inactive primes, the original H-incidence bound is \(1/9\), with only 43 at capacity \(7/36\) and the two fixed channels 19,73 at capacity \(13/108\) above this bound. Thus eight channels omitting 5 and 13 cover at most

\[
\frac{21+13+13+5\cdot12}{108}=\frac{107}{108}<1
\]

of H. Since H has full-exponent density \(6/35\), the remaining density is at least \(1/630\).

## 2. A sharper all-prime bound on either parity fiber

Suppose exactly one basic prime occurs. It misses one whole u-parity. On that parity write \(u=\epsilon+2z\). Its old-hole density is \(3/35\) among the original exponent indices. An active prime gives one z-class of effective period

\[
e=\operatorname{ord}_q16.
\]

With \(g=\gcd(e,105)\), relative coverage is bounded by \(K_g/[36(e/g)]\), where

\[
(K_1,K_3,K_5,K_7,K_{15},K_{21},K_{35},K_{105})
=(36,23,11,7,6,4,2,1).
\]

The inherited inventories exclude e=1,...,6 outside the basic/old/inactive channels; e=7 permits only 29 and 43; e=9 permits 19,37,73,109, of which only the fixed 19 and 73 are active; e=10 permits only 61681; e=12 and e=15 are unavailable. In addition,

\[
2^{32}-1=3\cdot5\cdot17\cdot257\cdot65537
\]

excludes e=8: its factors are all old/basic/inactive.

After removing \(29,43,61681,19,73\), all remaining prime channels have relative capacity at most \(1/9\). The complete gcd-column bounds are

| g | Lower bound on remaining e | Capacity bound |
|---:|---:|---:|
| 1 | 11 | 1/11 |
| 3 | 18 | 23/216 |
| 5 | 20 | 11/144 |
| 7 | 14 | 7/72 |
| 15 | 30 | 1/12 |
| 21 | 21 | 1/9 |
| 35 | 35 | 1/18 |
| 105 | 105 | 1/36 |

The exceptional capacities are

\[
c_{29}=c_{43}=\frac7{36},\qquad c_{61681}=\frac{11}{72},
\qquad c_{19}=c_{73}=\frac{13}{108}.
\]

These statements include inactive primes as zero-contribution channels and cover every multiplicative order.

## 3. The apparent excess forces a nonzero overlap

There are at most seven further slots on the missed parity. Their largest possible sum of capacities is

\[
U=2\frac7{36}+\frac{11}{72}+2\frac{13}{108}+2\frac19
=\frac{217}{216}.
\tag{1}
\]

If any one of the five exceptional primes is absent, its replacement has capacity at most \(1/9\). The smallest possible loss is

\[
\frac{13}{108}-\frac19=\frac1{108}.
\]

Hence the union has relative density at most \(215/216<1\). We may therefore restrict attention to the case in which all five exceptional primes occur.

If 29 or 43 fails to occupy a maximal seven-point H-class modulo 7, its contribution is at most \(6/36\); its loss from (1) is at least \(1/36\), already giving an upper bound \(211/216<1\). Thus a potentially complete dictionary requires both of their classes to be maximal.

The maximal H-classes modulo 7 are exactly 0,1,2. Each contains seven H-residues, exactly three of which are in

\[
H_1=\{h\in H:h\equiv1\pmod3\}.
\]

Consider the channel 29, which has one such maximal class on the chosen parity, and the fixed channel 19. For each compatible H-residue in \(H_1\), the lifts on this parity run through the three residue classes modulo 9 compatible with \(u\equiv1\pmod3\). Exactly one is the fixed 19 phase \(u=4\bmod9\). Therefore their intersection has relative density

\[
\frac3{36\cdot3}=\frac1{36}
\]

inside the parity's old holes. This calculation is unchanged by the affine z-coordinate. Equivalently it can be checked on the full u-period \(\operatorname{lcm}(105,2,9)=630\): the parity has 108 old-hole positions and the intersection has three.

For any finite family of sets, the union is at most the sum of their sizes minus the size of one specified pairwise intersection. Subtracting this compulsory intersection from (1) gives

\[
\mu(\text{union})\le\frac{217}{216}-\frac1{36}
=\frac{211}{216}<1.
\]

All cases consequently have union at most \(215/216\), so the original exponent density left uncovered is at least

\[
\frac3{35}\left(1-\frac{215}{216}\right)=\frac1{2520}.
\]

Together with Section 1, this proves the theorem.

## 4. Reproducible arithmetic and claim scope

`verify_eight_basic_pair.py` checks the new exact factorization and factor primalities, the gcd-column rational bounds, the maximum-incidence classes, both parity restrictions, both fixed W phases, every required overlap on a complete period, and the rational exclusion margins. The all-prime result rests on the stated incidence bounds and complete inherited inventories; the calculator does not approximate it by a finite prime search.

This theorem is an additional necessary condition for eight-prime completion in R1 and its subfamilies. It does not classify all eight-prime dictionaries. The source seven-prime prefix and tail theorems retain their original budget-seven scopes.

## Immutable dependencies

- `awdawmip/enterprise-math@a88e3e001275269cae93c40d77e6984b1ef2970f:research_notes/portable_direct/riesel_seven_cover_20261124/basics/proof.md`.
- `awdawmip/enterprise-math@b1de1acbdc97b5e51d486127abd1fadd24babd99:research_notes/portable_direct/riesel_five_cover_20261123/global/proof.md`.

