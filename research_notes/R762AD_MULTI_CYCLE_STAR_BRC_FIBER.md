# R762AD — Exact multi-cycle shortest BRC mass for the two-slot X6 star

Date: 2026-11-14. Scientific status: **AUTHOR-SIDE CONDITIONAL THEOREM; REPRODUCIBLE EXACT COMPUTATION; NOT_REVIEWED; NOT_NATIVE_ADMITTED**.

Parent: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / `TP2-8B7E13C5904A2D6F1142`.
Author-side continuity: `EM-X6-3050F6`; historical CLAIM `MCP-e4b33a56e2686c66e7cd5ca2`, RUN `RUN-53ab7d7bffccaaf2c0af47a4`. Source control at the last read had the same CLAIM as current owner but a read-only packet does not authorize protected progress. This note does not claim a new native checkpoint.
Frozen P000 and X6 science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Extends, rather than repeats, R762AC `research_notes/R762AC_X6_STAR_BUFFER_FORCE_SOURCE_RESIDUAL.md@ff7f13951e13d2b50134e6139e9493c2659a22f2`.

## Model, observation, and one-step recurrence

Let a star have \(n\) named, capacity-one outer ports and an initially empty, capacity-two hub \(c\). One distinguishable token begins at each outer port. A primitive step moves one token between its outer port and \(c\), in either direction, respecting capacities. The completed target is a permutation \(\pi\) of the original token-to-port attachments. Write \(S=\{i:\pi(i)\ne i\}\), \(m=|S|\), and let \(\ell_1,\ldots,\ell_r\ge 2\) be the lengths of the \(r\) nontrivial disjoint cycles of \(\pi\). Fixed-port tokens remain stationary in every length-\(2m\) optimal trace. This follows from R762AC's lower bound of two moves for every moved token and its attaining construction.

In such a shortest trace, each moved token \(i\) must enter the hub exactly once (operation \(I_i\)) and leave exactly once into port \(\pi(i)\) (operation \(O_i\)). If \(A\) is the subset of tokens whose ingress has occurred, and \(D\subseteq A\) the subset whose egress has occurred, then legal transitions are exactly

\[
(A,D)\xrightarrow{I_i}(A\cup\{i\},D) \quad (i\notin A,\ |A\setminus D|<2),
\]

\[
(A,D)\xrightarrow{O_i}(A,D\cup\{i\}) \quad (i\in A\setminus D,\ \pi(i)\in A).
\]

The destination \(\pi(i)\) is empty precisely after its original occupant entered the hub, provided \(i\) has not already exited; because \(\pi\) is a permutation, no other exiting token targets that port. Therefore the recurrence \(F(A,D)\) obtained by summing these legal successors, with \(F(S,S)=1\), counts exactly all labelled shortest serializations. This is a direct, finite BRC path-count carrier, not an approximation.

## AD1. Closed formula for any permutation's shortest trace count

**Theorem.** For \(m\ge2\), the number of labelled shortest \(2m\)-step serializations in the two-slot star is

\[
\boxed{\ N_2(\pi)=r!\,2^{m-1}\prod_{j=1}^r\ell_j.\ }
\]

For \(\pi=\mathrm{id}\), the only shortest trace is empty, so \(N_2(\mathrm{id})=1\). If \(m=1\), no permutation exists.

**Proof.** A nontrivial cycle cannot start using one hub token while some *other*, unfinished cycle has a token in the hub whose destination is still occupied: two ingresses from distinct cycles fill the hub, but neither token can exit because neither target port is yet empty. Thus a cycle in progress must be advanced until its last ingress before any other cycle can begin. More precisely, after the final ingress of a cycle, the remaining hub tokens can leave to their now-empty destinations. A different cycle can begin at the single interface after the penultimate departure, when one ready-to-exit token from the previous cycle remains in the hub. Its first ingress may occur either immediately before or immediately after the previous cycle's final departure; no second ingress can overtake that departure because the hub would then be full and both tokens of the newly started cycle would still have occupied destinations. Consequently every admissible shortest serialization determines a unique total order of its nontrivial cycles, and, for each consecutive pair, exactly one of two interface placements (no overlap, or the one-token overlap). Removing these optional adjacent interchanges yields a unique concatenation of individually legal shortest cyclic traces.

R762AC proved that an individual directed \(\ell\)-cycle has exactly \(\ell2^{\ell-1}\) shortest traces, for every \(\ell\ge2\). There are \(r!\) possible cycle orders, \(2^{r-1}\) interface toggles, and independently \(\prod_j \ell_j2^{\ell_j-1}\) internal traces. Their product is
\[
r!\,2^{r-1}\prod_j\ell_j2^{\ell_j-1}
=r!\,2^{m-1}\prod_j\ell_j.
\]
The decomposition and reconstruction above are mutual inverses, establishing exactness. QED.

Examples: cycle types \((4)\) and \((2,2)\) both cost eight transfers but respectively admit **32** and **64** shortest serializations. Types \((6)\), \((2,4)\), \((3,3)\), \((2,2,2)\) give **192**, **512**, **576**, **1536**, respectively. Thus the final per-spoke transfer ledger cannot even determine shortest BRC path mass when source permutations differ.

## AD2. Fibonacci identity for the full terminal-ledger fiber

At a completed macro boundary every moved spoke \(i\in S\) records exactly one inward and one outward matched inter-Cell V29 TRANSFER, irrespective of \(\pi\). Fixed spokes record zero. Under the R762AC boundary-only coupling, V29's terminal nonnegative ledger, \(u=0\), \(\Omega=0\), and fixed-frame V39 signature \((j,h)=(0,\mathrm{id})\) are identical for **all permutations with the same moved support**. We do not infer equality of the ordered microstep traces, source-to-port map, or any future source-sensitive observable.

For \(|S|=m\), admissible source maps are precisely the derangements of \(m\) tokens, in number
\[
!m=m!\sum_{k=0}^m(-1)^k/k!.
\]
A fixed-length lossless repair coordinate restoring the final source permutation therefore needs exactly \(\lceil\log_2(!m)\rceil\) bits when \(!m\ge1\) and the map is unrestricted within this fiber.

**Theorem (aggregate BRC mass).** Summing *labelled shortest traces* across every permitted derangement for the same nonzero transfer support yields
\[
\boxed{\ C_m=\sum_{\pi\in D_m}N_2(\pi)=m!\,2^{m-1}F_{m-1}\quad(m\ge2),\ }
\]
where \(F_0=0,F_1=1,F_{k+1}=F_k+F_{k-1}\).

**Proof.** For cycle multiplicities \(a_\ell\ge0\) (\(\ell\ge2\)) satisfying \(\sum_\ell \ell a_\ell=m\), let \(r=\sum_\ell a_\ell\). There are \(m!/\prod_{\ell\ge2}\ell^{a_\ell}a_\ell!\) permutations of that cycle type. Multiplying by AD1 gives \(m!\,2^{m-1}r!/\prod_\ell a_\ell!\). The remaining multinomial factor counts all orderings of the \(r\) cycle lengths, i.e. compositions of \(m\) into parts at least two. Their count obeys the Fibonacci recurrence and has ordinary generating function \(z^2/(1-z-z^2)\), hence equals \(F_{m-1}\). QED.

| Moved support \(m\) | Final source maps \(!m\) | Shortest-trace mass \(C_m\) | Min repair bits |
|---:|---:|---:|---:|
| 2 | 1 | 4 | 0 |
| 3 | 2 | 24 | 1 |
| 4 | 9 | 384 | 4 |
| 5 | 44 | 5,760 | 6 |
| 6 | 265 | 115,200 | 9 |

Here \(!m\) is a **Boolean fiber size**, while \(C_m\) is a **positive BRC chronology multiplicity**. Neither is a signed cancellation amplitude. The 3-port \(m=3\) result is compatible with P000's primitive triad *arity*. The larger \(m>3\) counts are strictly auxiliary nonprimitive multi-source combinatorics and do not assert that a four-, five-, or six-force configuration is a primitive stable event; P000 requires triadic decomposition for populations greater than three.

## Verification, boundaries and next obligation

The accompanying `R762AD_VERIFY.py` uses independent bitmask recurrence and explicit token-position breadth-first counting. Exhaustive checks cover every derangement on \(m=2,\ldots,6\) labelled moved ports, with independent BFS for \(m\le4\), plus three representative disjoint-cycle families at \(m=8,9,10\). All assertions passed with Python exact integers. See `R762AD_EVIDENCE.json` for cycle-type counts and SHA-256 of the tested local files in the run record if separately supplied; no SHA-256 value is asserted by this note.

This is a precise extension of R762AC's **conditional star-buffer model**. The native P000 `TRIADIC_CLOSURE_E` incidence/legality and its V29 internal PASS coupling remain unestablished; under a different coupling the V29 observer fiber may split. Nothing here changes P000, the ACTIVE worldview, the task's frozen scientific pins, original owner rights or formal Result/Driver acceptance.

**Next discriminating question:** determine from an actually admitted Cell/Link/Port macro event whether a hub passage is recorded as boundary TRANSFER alone, boundary TRANSFER plus internal PASS, or a more detailed source-typed event. Then restrict \(D_m\) and the AD1 recurrence to that event alphabet; calculate the resulting smallest operation-safe BRC repair and actual V17/V39 frame transport instead of promoting the auxiliary model to native dynamics.
