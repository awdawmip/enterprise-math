# R₄ exact eleven: global minimum and density

The least positive \(a\in R_4\) with \(\delta_P(a)=11\) is \(A_4+105257386702317\,S_4\) (368 decimal digits), with unrestricted total cost \(\tau(a^2)=31\). This is smaller than the least exact-nine and exact-ten roots on the same fiber (371 and 375 digits). The relative natural density of exact cost eleven on \(R_4\) is between \(2.4892508568010196\cdot10^{-14}\) and \(2.4892508568010290\cdot10^{-14}\). The exact rational expression has only the prime factorization of the order-5040 carrier left symbolic.

## The least root and unrestricted cost

Use the [873-term eleven-budget theorem](https://github.com/awdawmip/enterprise-math/blob/5c489fc73fef7d1fe5b4545bc6c393ce7cc0ac77/research_notes/portable_direct/riesel_r4_eleven_observer_20261125/REPORT.md) and the [42 ten-budget terms](https://github.com/awdawmip/enterprise-math/blob/86964457e4281ad88df72b6abc222d95dd0c8736/research_notes/portable_direct/riesel_r4_ten_exact_20261125/REPORT.md). A slot \(h:b\) is fulfilled by a prime of effective order \(h\) at a root \(a\equiv\pm2^{-16-18b}\pmod q\). Slots within one group are disjoint for each prime. Choose a distinct prime and a sign for each slot and solve by CRT for \(k=(a-A_4)/S_4\). Descendants of a partial class \(k\equiv j\bmod m\), \(0\le j<m\), have minimum at least \(j\); prune only once \(j\) is at least the incumbent. At each full class test its representatives below the incumbent against the full ten-budget predicate. A term identical to a ten-budget term contributes no exact-eleven roots, so it can be dropped.

Both traversal orders give \(k=105257386702317\) via \(15:5,15:8,15:11,12:0\), using respectively \(541,811,271,209924353\). There is a separate exact exclusion for all 91 terms using group \(h=140\), which is the only place with unfactored primes: they all require both \(20:0\) and \(20:8\). The 80 signed CRT assignments to these two slots have minimum \(k=351939035706001\), which already exceeds the winner. This exclusion is valid even if the group-140 slots are granted for free. The full-carrier gcd check independently confirms that the winning four slots give the only satisfied eleven-budget term at the winning root.

Keep the original \(P\) and add \(5,13,19,73,38737,246241,487824887233,541,811,271,209924353\). This covers all 60,480 indices in a full common period. The 31 listed indices give actual terms \(a^2 2^n-1\), each with a proper dictionary divisor; all 465 pairs of terms are relatively prime, with largest index 3488. Any prime can cover at most one of these 31 terms, so even a fully replaced dictionary needs 31 primes.

## Density, including the unresolved layer

The prime inventory reconstructs all 46 order carriers, fully factoring 45 into 142 distinct known primes. Sources of primality include the [Cunningham main table](https://homes.cerias.purdue.edu/~ssw/cun/pmain1126.txt), [its primes appendix](https://homes.cerias.purdue.edu/~ssw/cun/appa1126.txt), and the [inherited order certificates](https://github.com/awdawmip/enterprise-math/blob/aa1cd83afdfad7a5912df77df1e8cc6a410188c1/research_notes/portable_direct/riesel_r2_exact_nine_density_20261125/replay.js). The replay rechecks products, distinctness, and exact orders; it relies on these primality sources rather than issuing fresh primality proofs for all 142 primes.

For one prime \(q\) with \(k\) relevant phases, each phase has probability \(2/q\) and the remaining outcome has probability \(1-2k/q\). Prime outcomes are independent by CRT. The weighted decision diagram counts the union of all 873 terms. It conditions on the eight possible masks of the three \(h=140\) phases. Probabilities for masks of equal cardinality agree exactly. Let \(y_0,\ldots,y_3\) be these conditional probabilities, and let \(P_j=\prod_{q\text{ in group }140}(1-2j/q)\), including all unknown prime divisors. Expansion by occupancy gives
\[
\rho_{=11}=y_3+3(y_2-y_3)P_1+3(y_1-2y_2+y_3)P_2+(y_0-3y_1+3y_2-y_3)P_3-\rho_{\le10}.
\]
The exact coefficient numerators and common denominator are in the replay output. Group masks were checked by both categorical convolution and Boolean-lattice Möbius inversion; an independent rational evaluation of this polynomial gives the same two endpoints and checks the subtracted probability against the pinned ten-budget result.

The order-5040 carrier is a 347-digit composite. Every prime divisor is \(1\bmod5040\), and a scan of all 19,841,269 candidates through \(10^{11}\) found none. A base-3 compositeness witness and exact power checks show that it has at least two distinct prime divisors. Its size and the least possible divisor 100000000801 bound the number of distinct divisors by 31, giving total minimal observer support between 144 and 173 primes. The lower probability drops this carrier, while the upper probability uses 31 independent dummy channels, each with the maximal possible per-phase weight \(2/100000000801\). Coupling an activation uniform variable and a phase label for each channel gives pointwise containment of phase availability and hence of the covering event. The same exact at-most-ten probability is subtracted on both sides.

The entire gain from the order-5040 layer is therefore positive by the preceding observer theorem and less than \(9.224\times10^{-29}\), under \(3.71\times10^{-15}\) of exact-eleven roots. This is the sharp worst-case observation order even though it affects a tiny fraction of roots on this fiber.

## Replay

In this directory run:
```sh
node minimum.js >minimum.json
node density.js >density.json
python3 audit.py
```

The last script checks the full-carrier gcd predicate at the winner, independently recomputes the signed period-20 bound, and verifies the symbolic density expression against both rational endpoints and archived budget-ten input. The supplied README-level claims are computed proof results using the pinned phase-theorem input, not formal Lean verification or a separate project Review.

Next: separate budget twelve into its prefix-normalization question and its eight-slot tail. An exact factorization of the remaining order-5040 carrier would close the exact eleven rational and prime count; it is not needed for the minimum, density interval, or the next budget's combinatorics.
