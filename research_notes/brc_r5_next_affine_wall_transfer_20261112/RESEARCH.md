# R5 — first new signed affine walls after the previous parameter chambers

Date: 2026-11-12 Asia/Shanghai. Status: researcher-side exact rational finite computation and affine endpoint proof; formal Source Result/independent review pending. Domain: frozen *external* seven-likelihood-ratio P/Q–BRC Blackwell observer (not native X6 dynamics).

## Exact science and question

Preserve original immutable scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Original rational 28-vector, 15 labeled kernel moves, perturbation H and ray endpoint are fixed by [PR #2102](https://github.com/awdawmip/enterprise-math/pull/2102), [PR #2122](https://github.com/awdawmip/enterprise-math/pull/2122) and [PR #2123](https://github.com/awdawmip/enterprise-math/pull/2123); this new verifier copies the exact original frozen definitions from the full PR #2123 source.

Let x=155682221/25142124560000000, r=eta/x, X(r)=X+rxH and epsilon_max=9/115400000. For any nonempty atom-label subset S, put P_S=36 sum_(a in S) M_a, an integer vector of length 28. Its first-zero time is

tau_S(r)=min_{k:P_S[k]<0} [36(X[k]+rx H[k])/(-P_S[k])].

The already-established nearest signed minimizer-chamber endpoints were r=+1/2507 and r=-1/4945. We determine the first new minimizer switches and the legal ordering losses across them.

## Theorem 1: next two signed active-minimizer walls

On moving from r=0 outward:

- The first positive active-coordinate switch after +1/2507 is **r=+1/1265**; it changes from F_110 to Q_3 for precisely the seven masks 6516, 6714, 18788, 18986, 23214, 28732, 30846.
- The first negative active-coordinate switch after -1/4945 is **r=-1/2461**; it changes from Q_3 to F_107 when r decreases for precisely masks 10926 and 28966.

Here F_n=36x/n and Q_q=x(1-23r)/q. The wall equation F_n=Q_q gives

r=(n-36q)/(23n).

For (n,q)=(110,3), r=1/1265. For (107,3), r=-1/2461. Subsequent nearby walls are +5/5083 (F_442 meets Q_12) and -1/1633 (F_426 meets Q_12); these values delimit the following two additionally certified full intervals.

## Theorem 2: exact path-loss redistribution

A complete labeled order of 15 moves is feasible at epsilon iff all its 15 prefix masses are nonnegative. The integer recurrence W(empty)=1 and W(S)=1_{tau_S(r)>=epsilon} sum_(a in S)W(S without a) counts feasible complete orders over all 32768 masks. Phase loss equals the inclusive count minus the count excluding the equality boundary.

On increasing r through +1/1265, the pair of losses at F_110 and Q_3 is:

| r side | F_110 lost orders | Q_3 lost orders | Combined |
|---|---:|---:|---:|
| below | 216,738,876 | 12,939,867,720 | 13,156,606,596 |
| above | 193,333,788 | 12,963,272,808 | 13,156,606,596 |

Exactly **23,405,088** labels' orderings transfer from the fixed phase to the moving phase.

On increasing r through -1/2461 (more negative toward zero), the pair of losses at F_107 and Q_3 is:

| r side | F_107 lost orders | Q_3 lost orders | Combined |
|---|---:|---:|---:|
| below (more negative) | 126,633,932 | 12,847,872,840 | 12,974,506,772 |
| above (less negative) | 83,034,876 | 12,891,471,896 | 12,974,506,772 |

Exactly **43,599,056** orderings transfer toward the moving phase in increasing-r direction (the direction reverses moving farther negatively). At both walls the combined pair loss remains constant.

## Finite exhaustive certificate over four closed intervals

The complete interval certificate uses all 32,767 nonempty atom subsets and **all 28 transfer coordinates** and proves the four *closed* rational regions:

1. [1/2507, 1/1265].
2. [1/1265, 5/5083].
3. [-1/2461, -1/4945].
4. [-1/1633, -1/2461].

For each subset the checker selects at its interval midpoint the smallest eligible candidate from the fixed source2-target0 coordinate k7, source3-target0 coordinate k14, and source3-target1 coordinate k15. In the in-ray case it tests the same candidate against **every negative-component coordinate** at both rational endpoints, and verifies its time stays at most epsilon_max. The candidate difference between any two coordinates is affine in r, so endpoint dominance implies dominance on the **whole interval**, not only sampled parameters. In the out-of-ray case it proves the entire 28-coordinate terminal mass vector at epsilon_max strictly positive at both endpoints, hence the subset never enters the ray inside that interval. These are complete finite rational endpoint certificates under the fixed inputs.

Midpoint winning-coordinate census, in the above interval order:

1. k14=14,655; k15=11,004; k7=299; outside ray=6,809.
2. k14=14,648; k15=11,011; k7=299; outside ray=6,809.
3. k14=14,664; k15=10,995; k7=299; outside ray=6,809.
4. k14=14,666; k15=10,993; k7=299; outside ray=6,809.

At the positive new wall seven masks tie with P_S[14]=-110, P_S[15]=-108; at the negative new wall two masks tie with -107, -108. Initial positivity and equality of the maximal-ray endpoint were also checked at all four rational intervals' endpoints. Loss reallocation uses exact integer Boolean-lattice DP in the two open chambers immediately adjacent to each wall.

The published single-file verifier combines exactly the earlier frozen PR #2123 input construction with the new rational certificates. The numerical rows here reproduce actually executed equivalent local Fraction checkers. The newly combined published file has received remote byte-for-byte readback but has not yet been independently re-executed using its published bytes.

## Next research question

Extend the first-zero affine envelope and exact schedule loss transfer through +5/5083 and -1/1633. Report separately coordinate-minimizer changes, unique first-zero phase values and complete legal schedule losses; a new minimizer wall can reassign first-zero witnesses without adding a new numerical phase. Preserve original scientific pins and formal source/owner separation.
