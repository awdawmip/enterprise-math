# Collaborative check of the global R3 minimum and its native execution

Checked on 2026-11-24 against `eight_minimum_v13/proof.md`, `verify_minimum.py`, `minimum_certificate.json`, and the proof, calculator and certificate in `eight_native_v13`. This is shared-context mathematical assistance, not an independent project Review.

## The smaller-root exclusion proves the stated global minimum

The conditional four-prefix classification exhausts 320 signed CRT descriptions. Each describes positive roots in a fixed congruence progression. Its least positive representative is the minimum in that progression, so comparing all 320 representatives minimizes the entire retained-prefix branch even when progressions overlap.

The prefix dichotomy leaves only the zero-W alternative. Its proved requirement that all four primes 29,43,1429,5419 be active is sufficient for the exclusion method; no lower bound on the final two primes and no enumeration of that branch's 451584 signed descriptions is needed.

For each compulsory prime q, the exact active-root categories on n=8+12v are the fourteen residues formed by the seven sign pairs ±2^{-(4+6c)}, c=0,...,6. They cover every possible phase because the effective v-order is seven. Allowing c=0 and c=6, which do not meet the residual A-set, only weakens the necessary condition. Therefore failing this relaxed simultaneous-four-activity test safely excludes every zero-W cover.

The chosen CRT residue A3 lies strictly between zero and S3. The candidate has exact progression index 63706. Hence the roots with k=0,...,63705 are every positive R3 root below it; there are no positive negative-index roots omitted from the sweep. The saved histogram sums to 63706, and its four-active bin is zero. This excludes the entire other branch below the candidate, completing the global R3 minimum proof.

## The new native root and phases agree

The minimum calculator and the native certificate contain the same 146-digit root. Its new residues are 885 modulo 1153 and 63 modulo 193. They satisfy 885=2^{-16} modulo 1153 and 63=2^{-88} modulo 193, producing w=0 and w=4 modulo eight on n=32+36w. In particular, the u-phase 88 at 193 is interpreted modulo ord_193(4)=48; it is valid without treating 88 as the least representative.

The common covering period lcm(210,4,12,18,9,72,144,288,96) is 10080. The reported 453600 individual readouts and 433440 fixed-coordinate comparisons are exactly 45 and 43 times that period. The separately stated 60480 residue-value period is not claimed to have been executed by this native run. The retained final integer agrees exactly with a^2 2^10080−1 and has 11047 bits.

The coverage route, root minimality and total covering cost retain separate evidence: the native run checks the explicit route and lossless readouts, the classification plus finite exclusion proves minimality, and the compact root's unrestricted total count is only bounded above by 28. No total-count equality is inferred from private witnesses alone.

## Checks performed for this review

The arguments and full calculator control flow were read. Small consistency checks verified the root's progression index, positive-base range, phase inverses, histogram total, minimum among the saved 320 starts, operation-count products and saved final integer formula. The 63706-root sweep and the native trajectory were not rerun. No correction to the reviewed minimum or native proof was required.
