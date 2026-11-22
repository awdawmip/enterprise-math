# EC49FWY — Relative-phase alias bifurcation and sharp two-channel observation costs

**Date:** 2026-11-22. **Frozen science pin:** `BRC16943` (unchanged). **Parents:** EC49FWW `61af64c051725e4caafd186efaeb6de7d23268ca`, EC49FWX `877375ab3e15d24d994bea046d534153fc2f6e67`. **Status:** AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Precise observer and provenance

This result concerns the **finite auxiliary** Farey/CRT Boolean observer, not native X6 time dynamics. The known reference is
\[
w(t)=\mathbf1_U(t\bmod10)\mathbf1_V(t\bmod11),\quad t\in\mathbb Z/110,
\]
where \(U\) is one of the 50 frozen P10 masks reconstructed from 72 primitive directions and \(V\) is full or missing one residue modulo 11. The two sensor words are
\[
L(t)=w(t-s_L),\qquad R(t)=w(-t-s_R),
\]
with independently sampled Boolean channel bits at each physical activation \(t\). Both **complete indexed reflection-defect spectra** are supplied; the reference \(w\) is known. We additionally know a prescribed admissible set \(D\subseteq\mathbb Z/110\) for the **relative phase**
\[
\delta=s_L-s_R\in D.
\]
This is the exact difference compatible with the displayed right-channel convention; switching to a different right-phase sign reverses its name, not the result. The layout is fixed before \(U,V,s_L,s_R\) are revealed (but may depend on the declared \(D\)); an adaptive layout is chosen after observing both spectra, known reference and \(D\). The target is the pair of full **observed membership words**, not the numeric phase, physical time, native X6 state, or Farey anchor identity. Required minimal Hamming distance of separately sampled channel bits is \(r\), \(1\le r\le20\). Thus \(r=1,2,3\) respectively mean exact recovery, tolerance of one known-channel erasure, and correction of one unknown channel-bit error.

Inherited EC49FWV/FWX spectral-alias result: for each side, exactly two distinct membership words remain; their relative phase representatives differ by \(55\) modulo \(110\). The half-turn disagreement row set \(D_U=\{i:U(i)\ne U(i-5)\}\) is a union of 1–4 opposite residue pairs \(P_i=\{i,i+5\}\), and frozen masks realize **one** such pair. By CRT, the missing modulo-11 column can be located arbitrarily. Every side's difference support has at least 20 positions.

## Theorem A — an exact 2-versus-4 candidate transition

Let one spectral-fiber representative pair be \((a,b)\) modulo 110, and put \(d=a-b\). Its four alias combinations are
\[
(a+55x,b+55y),\quad x,y\in\{0,1\},
\]
whose relative differences modulo 110 are \(d\) (when \(x=y\)) and \(d+55\) (when \(x\ne y\)), each occurring twice. Consequently:

* If neither \(d\) nor \(d+55\) belongs to \(D\), the spectra are inconsistent with the specified phase constraint.
* If exactly one belongs to \(D\), there are **exactly two** joint membership-word candidates. They differ by simultaneous half-turn aliasing of both sensor phases.
* If both belong to \(D\), there are **exactly four** candidates, i.e. all independently aliased channel combinations.

Call \(D\) *antipodal-free* if \(D\cap(D+55)=\varnothing\). An antipodal-free restriction has only two-state nonempty fibers, regardless of how many different offsets \(D\) contains. Admitting just **one** antipodal pair \(\{\delta,\delta+55\}\subseteq D\) creates actual four-state fibers. This is a discontinuous information threshold, not a smooth interpolation in the number of allowed offsets.

## Theorem B — sharp adaptive activation cost within each fiber

Let \(A\) and \(B\) denote the two side-specific half-turn difference supports, with \(|A|,|B|\ge20\), and write \(c=|A\cap B|\). In a **two-candidate** fiber, every activation within \(A\cap B\) contributes two differing channel bits; every activation in \(A\triangle B\) contributes one. Thus the exact minimum is
\[
\boxed{N_2(A,B;r)=\max\{\lceil r/2\rceil,\ r-c\}}\quad(1\le r\le20).
\]
Indeed, \(m\) activations supply at most \(2m\) bits and at most \(m+c\) differing bits, forcing both inequalities. To attain them, take \(\min(c,\lfloor r/2\rfloor)\) common sites and enough sites of \(A\triangle B\), or \(\lceil r/2\rceil\) common sites if available. The capacity \(|A|,|B|\ge r\) is sufficient; rounding handles odd \(r\).

In a **four-candidate** fiber, comparing pairs differing solely on the left or solely on the right requires at least \(r\) hits in each of \(A,B\). Hence the inherited exact formula is
\[
\boxed{N_4(A,B;r)=2r-\min\{r,c\}}.
\]
The frozen CRT overlap structure of EC49FWX has \(c=0\) or \(c\ge18\). For the full range \(1\le r\le20\), the two-state formula therefore specializes to
\[
N_2=\begin{cases}r,&c=0,\\\lceil r/2\rceil,&c>0.\end{cases}
\]
A literal one-bit activation saving becomes a two-channel distance saving only under the declared two-state coupling. No assertion about correlated physical errors is made.

## Theorem C — exact universal fixed-installation and worst-case adaptive optima

Define
\[
h(r)=\begin{cases}r+1,&1\le r\le10,\\r+2,&11\le r\le20.\end{cases}
\]

**C1. Known relative offset.** For **every fixed \(\delta\in\mathbb Z/110\)**, if \(D=\{\delta\}\), the optima are
\[
\boxed{N_{\mathrm{fixed}}(\{\delta\};r)=\left\lceil\frac{5h(r)}2\right\rceil},\qquad
\boxed{N_{\mathrm{adaptive,worst}}(\{\delta\};r)=r}.
\]
The first formula extends EC49FWW's \(\delta=0\) mirror-coupled theorem to **all even and odd phase offsets**. It yields 5, 8 and 10 fixed activations for \(r=1,2,3\); the adaptive worst cases require 1, 2 and 3.

**C2. An antipodal phase pair suffices to recover the independent worst case.** For every nonempty \(D\) containing **some** \(\{\delta,\delta+55\}\), the exact universal optima are
\[
\boxed{N_{\mathrm{fixed}}(D;r)=5h(r)},\qquad
\boxed{N_{\mathrm{adaptive,worst}}(D;r)=2r}.
\]
Even \(D=\{\delta,\delta+55\}\), only two possible relative offsets, attains this complete loss of the mirror-coupling savings. For \(r=1,2,3\), fixed costs jump to 10, 15, 20 and adaptive worst costs to 2, 4, 6.

**C3. General antipodal-free \(D\).** Every nonempty observed fiber has exact adaptive cost \(N_2\) above and worst-case \(r\). A universal layout obeys
\[
\left\lceil5h(r)/2\right\rceil\le N_{\mathrm{fixed}}(D;r)\le5h(r).
\]
For general multi-offset antipodal-free sets this report does **not** assert a sharp fixed-cost formula: the actual constraint hypergraph depends on \(D\), even though the per-spectrum candidate count stays two.

### Proof of C1

Fix \(\delta=s_L-s_R\). Then identically \(R(t)=L(\delta-t)\). The map \(t\mapsto\delta-t\) permutes the five opposite residue-pair blocks \(P_i\), acting on block indices by \(i\mapsto\delta-i\pmod5\). This involution has precisely one fixed block \(P_{i_0}\), where \(2i_0=\delta\bmod5\), and two swapped block pairs. Its action on columns modulo 11 has precisely one fixed column \(j_0\) and five exchanged column pairs.

An authentic half-turn difference concentrated on either swapped block gives at most one differing channel bit per physical activation in that two-block orbit. If the orbit has \(m\) installed sites, one of the 11 possible missing columns deletes at least \(\lceil m/11\rceil\) such bits. To guarantee distance \(r\), \(m-\lceil m/11\rceil\ge r\), i.e. \(m\ge h(r)\). Each of two swapped orbits therefore requires \(h(r)\).

For the one central block, each activation contributes at most two differing channel bits. Across all 11 columns, one column has at least \(\lceil2m/11\rceil\) of those, so \(2m-\lceil2m/11\rceil\ge r\) implies \(m\ge\lceil h(r)/2\rceil\). This proves the total lower bound.

For attainment in each swapped orbit, install \(h(r)\) sites in one designated row-pair block, distributing their *logical* modulo-11 columns as evenly as possible: at most one per column for \(h\le11\), at most two for \(h\ge12\). Each activation then covers the designated block through one channel and its reflected block through the other. The worst missing-column deletion leaves \(\ge r\).

In the central block, there are five nonfixed column pairs, each admitting two mirror-related activation positions with one bit in each member column, plus two physical sites in the fixed column with two bits each in that same column. This incidence statement holds also for **odd \(\delta\)**: when the reflection has no fixed *site*, it interchanges the two fixed-column sites, without changing their per-column bit counts. For \(m\le5\), select \(m\) distinct nonfixed column pairs; for \(6\le m\le10\), double \(m-5\) of the five pairs; for \(m=11\), double all five and add one fixed-column site. Their worst-column deletions leave respectively \(2m-1\), \(2m-2\), or \(20\) bits, attaining \(r\) at \(m=\lceil h(r)/2\rceil\). Any larger frozen mask disagreement contains one or more \(P_i\), so distances can only increase. This proves C1 fixed.

For the adaptive worst case, every two-state pair needs only \(r\) activations by Theorem B, and the frozen mask \(U=299\) has a single difference pair. For any prescribed \(\delta\), choose \(s_L\bmod5\) so that the left difference pair \(P_{a+s_L}\) and reflected right pair \(P_{\delta-a-s_L}\) are disjoint. This is possible because it excludes only one of the five choices modulo 5. Then \(c=0\) and \(N_2=r\), proving sharpness.

### Proof of C2

For a chosen \(\delta\) with both \(\delta,\delta+55\in D\), each relevant fiber admits a **left-only** half-turn alias change with right held fixed; this changes relative phase by 55 but remains in \(D\), and preserves both indexed spectra. Thus for every opposite row-pair block \(P_i\) and arbitrary one missing column, the left channel **alone** must produce distance \(r\). The EC49FWX occupancy argument forces \(h(r)\) physical installations in each of the five blocks: total at least \(5h(r)\). A universal installation putting \(h(r)\) equally column-distributed sites in every block attains \(r\) in both channels for *every* phase relation, so the bound is sharp even if \(D\) has additional offsets.

Adaptive cost is at most \(2r\) by independently selecting \(r\) hits in each side's difference support. For a frozen one-pair mask such as \(U=299\), choose phases with \(s_L-s_R=\delta\) and disjoint left/right difference blocks as in C1. Then \(A\cap B=\varnothing\); all four alias combinations remain permitted since \(D\) contains the antipodal pair, forcing \(r\) independent hits per channel, i.e. \(2r\). This proves C2.

## Exact finite verification and limits

Adjacent `EC49FWY_RELATIVE_PHASE_VERIFY.js` independently reconstructs the 72 primitive directions and 50 P10 masks, confirms gap histogram \(\{2:10,4:26,6:10,8:4\}\), explicitly constructs the optimal fixed layout for **every one of 110 relative offsets**, and for every \(r=1,\dots,20\) checks every one-pair disagreement block \(i=0,\dots,4\) against every excluded column \(j=0,\dots,10\): **121,000 exact integer distance checks, all PASS**. These single-pair cases are sufficient because every actual gap is a union of such blocks and each is realizable by the frozen family. It additionally checks the two/two alias parity identity for all 110 offsets. JSON output is saved beside the verifier. The proof is analytical for the specified finite auxiliary family; there has been no independent proof review, formal verification or native X6 temporal simulation.

**Next specific problem:** determine \(N_{\mathrm{fixed}}(D;r)\) exactly for structured **antipodal-free multi-offset** classes, beginning with parity-only uncertainty \(D=2\mathbb Z/110\) and finite offset intervals; then test same-anchor Farey trajectory constraints on physically reachable \(D\), retaining signs, affine seeds, height and complete joint-residual provenance.

**Authority:** independent portable scientific continuation. Original `RS-EC49AS` at the current checked Source pin has no canonical publication directory; no Task CLAIM, Result, Review or promotion asserted. Existing native researcher/session/Activity provenance is reused without asserting execution authorization.
