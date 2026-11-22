# EC49FWW — Sharp activation cost for paired mirrored Farey phase observers

**Date:** 2026-11-22. **Frozen scientific pin:** `BRC16943`. **Parent:** EC49FWV at `e2a255177cb437976b356e1a6ba21f3a4fb862e0`. **Scientific status:** AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Statement, quantifiers and observer

Use precisely the frozen EC49FWV P10 family: 50 Boolean masks $U\subseteq\mathbb Z/10$ from 72 primitive directions, and $V\subseteq\mathbb Z/11$ either full or missing one residue. For any known reference word $w(t)=1_U(t\bmod10)1_V(t\bmod11)$, consider an unknown phase $s\in\mathbb Z/110$:
$$
L_s(t)=w(t-s),\qquad R_{-s}(t)=w(-t-s)=L_s(-t).
$$
Here the right trace is indexed from the **negated left seed** as in EC49FWT, so that mirror alignment is exactly $t\mapsto-t$. The left/right sensor drifts are opposite and linked. This theorem assumes this coupling; independent drifts and a different unknown coordinate alignment are different problems.

Both complete indexed reflection-defect spectra are supplied. For a known $w$, EC49FWV proves that each spectrum leaves exactly two distinct membership words; the right spectrum is a deterministic relabeling of the left. A fixed hardware activation at $t\in\mathbb Z/110$ returns **two separate Boolean channel samples**, $L_s(t)$ and $R_{-s}(t)=L_s(-t)$. The installed set of activation locations is chosen before $U,V,s$ and the spectra are seen. Repeated channel values at $t=-t\pmod {110}$ count as two separately sampled channel bits, including for a single arbitrary channel-bit error; no extra independence of underlying membership is asserted. A decoding code must separate the two spectrum-equivalent *pair-response vectors* by Hamming distance at least $r$, uniformly over all 50 masks, 12 V types and phases.

**Exact theorem.** Put
$$
h(r)=\begin{cases}r+1,&1\le r\le10,\\ r+2,&11\le r\le20.\end{cases}
$$
Then the least number of fixed paired activations is
$$
\boxed{N_{\mathrm{paired}}(r)=2h(r)+\lceil h(r)/2\rceil
=\lceil5h(r)/2\rceil,\quad 1\le r\le20.}
$$
This is exactly the ceiling of half the EC49FWV single-site optimum $5h(r)$. In particular **five** activations suffice and are necessary for error-free decoding ($r=1$); **eight** tolerate one known-channel erasure ($r=2$); and **ten** correct one unknown erroneous channel bit ($r=3$). The output is the complete *observed left/right membership word*, not necessarily the numeric unobservable phase or a native X6 state.

## Proof of lower bound

For each of the five opposite ten-residue row pairs $P_i=\{i,i+5\}$, $0\le i\le4$, the frozen family contains a mask with half-turn disagreement of cardinality two. By varying $s\bmod10$, that disagreement can occupy *any* $P_i$; by CRT varying $s\bmod11$, the single missing column can be *any* $j\in\mathbb Z/11$, independently. These are legitimate spectrum-alias pairs from EC49FWV, not invented external masks. Thus every $P_i$ imposes its own minimum-distance requirement.

The mirror $t\mapsto-t$ permutes these row pairs as $P_0\mapsto P_0,\ P_1\leftrightarrow P_4,\ P_2\leftrightarrow P_3$. All activation locations split disjointly into **three** orbit blocks: central $P_0$, swapped $P_1/P_4$, and swapped $P_2/P_3$. For a disagreement concentrated in either member of a swapped block, one activation supplies *at most one* differing channel bit (the other lies in the opposite row pair). With $m$ activations, and one adversarial missing mod-11 column, the distance is no greater than $m-\lceil m/11\rceil$: among 11 columns, at least (\lceil m/11\rceil) of these potentially differing samples share some column. Therefore each swapped block needs at least $h(r)$ activations for $1\le r\le20$.

For a disagreement on central $P_0$, every activation yields *at most two* differing samples, distributed across 11 columns; the missing-column adversary removes at least $\lceil2m/11\rceil$ of those if all $2m$ could differ, and a smaller initial support only reduces the distance. Hence the minimum possible distance is at most $2m-\lceil2m/11\rceil$. For $1\le r\le20$, the least $m$ satisfying $2m-\lceil2m/11\rceil\ge r$ is $\lceil h(r)/2\rceil$. The three disjoint blocks give
$$
N\ge2h(r)+\lceil h(r)/2\rceil.
$$
This reasoning permits even repeated activation positions; no efficiency claim is obtained by silently equating the two mirrored channels with one bit.

## Attaining layout

For each swapped block $P_1/P_4$ and $P_2/P_3$, install $h(r)$ activations whose designated first-side samples lie in $P_1$, respectively $P_2$, across mod-11 columns with occupancies at most one when $h\le11$, at most two when $h>11$. For example use row 1 (respectively 2) in the first 11 columns; then row 6 (respectively 7) for the extra $h-11$ columns. Its mirror automatically supplies the opposite row-pair sample. After any column deletion there remain at least $r$ differing readings whenever the half-turn disagreement includes that pair.

For central $P_0$, the mirror pairs nonzero columns $c\leftrightarrow-c$. There are ten distinct nonzero-column activation orbits: two rows (0 and 5) times the five unordered nonzero column pairs; there are also two mirror-fixed activations at $t=0,55$, both in column zero. For $m\le5$, select $m$ distinct nonzero column pairs, obtaining $2m-1$ surviving bits after any missing column. For $6\le m\le10$, use both row choices as necessary, with a maximum occupancy of two per column, obtaining $2m-2$. At $m=11$, take all ten nonzero-column orbits and one mirror-fixed activation; the worst distance is 20. Selecting (m=\lceil h(r)/2\rceil) attains $r$ for all stated $r$. A fixed activation at a mirror-fixed index reports two separate channel measurements of the same underlying site, as declared.

Every frozen mask's half-turn disagreement is a nonempty union of the $P_i$, so any actual alias pair contains at least one of the three covered blocks. The entire paired response thus has distance at least $r$. This matches the lower bound, proving the theorem.

## Verification, provenance, limits and next unit

`EC49FWW_PAIRED_MIRROR_VERIFY.js` rebuilds 72 primitive directions and the 50 masks using the frozen P10 slope/parity predicate. It independently enumerates 4,096 central-orbit subsets and 177,147 swapped-block column-occupancy vectors, checks all 20 optimal costs, then directly computes the two-channel difference at the installed activation sites for all 50 masks, 12 factors and 110 phases (66,000 witness states times 20 target distances = 1,320,000 layout checks). Exact integer assertions show equality to the claimed bound and actual attainment of worst-case distance. `EC49FWW_PAIRED_MIRROR_OUTPUT.json` is the direct executable output.

The pair-mirror phase relation derives from EC49FWT; the underlying phase alias / 50-mask census are inherited from the pinned EC49FWV. All calculations concern these exact finite auxiliary rational Farey trace observers. No claim of an already validated native-X6 temporal evolution, independent right/left drift theorem, or formal scientific admission is made.

**Next research question:** when left and right sensor phases drift **independently**, classify the joint indexed-spectrum fiber (up to four bit words), then optimize paired activation cost under the actual coupled-anchor constraint. Determine which signed seed, phase and height-origin provenance must accompany any compressed future-neighbor observer.

**Control/authority:** independent portable scientific note. Original `RS-EC49AS` task observation is a source-directory absence only, not a global active-owner projection or a CLAIM; native researcher Activity association awaits verification of this conversation's own identity. No formal Result/Review is asserted.
