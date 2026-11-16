# R762CC — Exact BRC observer-safety hierarchy and sharp signed triad license-query complexity

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS · immutable task publication: TP2-8B7E13C5904A2D6F1142 · 2026-11-16.
Status: AUTHOR-PROVED CONDITIONAL FINITE MODEL; EXACT FINITE CENSUS PASSED; INDEPENDENT REVIEW NOT_REVIEWED.

## Scientific sources and boundary

Frozen task science: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\` P000 V5; taskbook \`research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\` Git blob \`218bf9ce05fd2dd79f477ac269fc3590f83f482e\`. Prior exact candidate classifications: R762CA, PR #2551 @ \`7530269499c7f799e65cb20b50a0f5c698b4b1c7\`; based-return formula: R762CB, PR #2554 @ \`e0724e29612a5c5252f425d876e65ad2ef36f06a\`. Read V17 at \`research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md\` (blob \`42b810a8f82c504833027da17884cc4fb2943e5b\`), which explicitly states that its shared-axis slot inheritance is *conditional*, not native event permission.

All results here are restricted to the **conditional** \`S6 × C3\` sign-only three-Port model at a selected Cell of the six-dimensional X6 spatial world. P000 retains six signed primitive axes, pairwise \`PERP_E\` / 120° native orthogonality, minimum primitive nonzero stable force arity 3, and mandatory triadic lifting of apparent two-force readouts. No classical force-vector sum, extra spatial direction, native two-dimensional plane, or physically established \`TRIADIC_CLOSURE_E\` event is assumed. Cell/time, signed force amplitudes, Link provenance and ordered branch histories remain separately typed.

Three named Ports 0,1,2 carry a directed Link cycle \`0→1→2→0\`, an injection of three occupied native axis labels into six, and signs \`s∈{+,-}³\`. C3 rotates Port/sign positions; S6 relabels axes. The sign-only closure predicate \`C(s)\` and rooted Port permission \`g(s,p)\` are respectively invariant and covariant; \`g(s,p)≤C(s)\`. The four C3 sign orbits are +++, ---, exactly one minus, and exactly one plus, of sizes \`(1,1,3,3)\`. Their independent rooted permission-bit counts are \`r=(1,1,3,3)\`. At each orbit the candidate law has either EXCLUDED (closure 0; all permissions 0), or CLOSED(mask) (closure 1; arbitrary mask of r rooted permissions). Hence exactly \`(1+2)^2(1+2^3)^2 = 729\` coherent laws.

## Theorem 1 — Four non-equivalent observer quotients

Define four *law-level* observers (not full BRC branch records):

* **A**: the complete aggregate based-return count sequence \`N(m)\`, summed over closed sign words at every \`m≥0\`, as defined in R762CB.
* **S**: all eight sign-word-resolved based-return count sequences \`N_s(m)\`.
* **E**: all eight independent rooted, C3-covariant binary event permission bits \`g(s,p)\` (a total candidate-law query, including nonadmitted sectors).
* **J**: four C3 closure bits together with eight rooted event permission bits.

The exact image sizes and minimal arbitrary fixed binary class indices are:

| Observer | Distinct classes | Minimum binary index |
|---|---:|---:|
| A: aggregate all-length spectrum | 90 | 7 bits |
| S: sign-resolved all-length spectra | 225 | 8 bits |
| E: rooted event table only | 256 | 8 bits |
| J: closure + rooted event table | 729 | 10 bits |

Exact fiber-size census (fiber size : number of fibers):

* A: \`1:9, 2:18, 4:9, 6:18, 9:6, 12:18, 18:9, 36:3\`.
* S: \`1:81, 3:108, 9:36\`.
* E: \`1:49, 2:112, 4:78, 8:16, 16:1\`.
* J: \`1:729\`.

**Proof.** Each homogeneous C3 sign orbit has 3 possibilities (EXCLUDED or CLOSED with one of two masks). Each mixed size-three orbit has 9 possibilities (EXCLUDED or CLOSED with one of eight masks), and the four choices are independent. For every admitted sign word with \`k\` enabled Ports, its return sequence is \`B_k(m)\` from R762CB; for excluded sectors it is zero. The pair \`(N_s(0),N_s(2))\` equals \`(1,3k)\` for a closed sector or \`(0,0)\` for an excluded sector, since \`B_k(0)=1\` and \`B_k(2)=3k\` for \`k=0,1,2,3\`. Consequently S retains 3 possible statuses for each homogeneous orbit and 5 for each mixed orbit: \`|S|=3²·5²=225\`. Fiber sizes are products of the relevant \`binom(r,k)\` rooted mask counts.

The E table consists of eight independent binary bits, each possible since all closures may be set to 1, so \`|E|=2^8=256\`. A zero rooted mask has two compatible closure statuses (EXCLUDED or CLOSED(0)); a nonzero mask forces closure 1, giving the stated E fibers. J is the original coherent law, hence injective and of size 729. A has 90 exact classes by the four-variable census polynomial proved in R762CB,
\`F(u0,u1,u2,u3)=(1+u0+u3)^2(1+u0^3+3u1^3+3u2^3+u3^3)^2\`.
Its 90 exponent vectors give distinct aggregate spectra by the invertible four-return-count matrix of determinant 324. The companion verifier independently enumerates all 729 policies and counts every fiber size. QED.

**Observation preservation.** S refines A because summing sign-resolved counts gives aggregate N. But S and E are incomparable. E cannot distinguish closure EXCLUDED from CLOSED(0) when gates vanish, whereas S can at m=0. Conversely, switching which named Port is enabled while retaining its count k changes E but leaves every sign-resolved return sequence unchanged. Therefore the 90-class or 225-class spectrum quotient is NOT future-event-safe when the future can ask rooted Port permissions, and the 256-class E quotient is NOT closure-safe when closure itself is observable.

## Theorem 2 — Explicit same-spectrum, different-future witness

Consider two coherent laws P and Q: both admit exactly the three sign words with **one minus**, and exclude all other words. In P the unique enabled Port is the Port with that minus sign. In Q the unique enabled Port is the immediately preceding Port along the directed Link cycle. The two choices are S6-invariant and C3-covariant, have precisely one enabled Port for every admitted sign word, and have identical sign-resolved spectra and thus identical aggregate spectra for **every** path length:

\`N_P(m)=N_Q(m)=3 B_1(m)\`, \`n=(0,3,0,0)\`, \`(N(0),N(4))=(3,63)\`.

For sign word \`(+,+,-)\`, P enables Port 2 whereas Q enables Port 1. At frame \`(1,2,3)\` with vacant native axis 4, the *candidate* switch \`(Port 2, axis 4)\` is legal for P and illegal for Q. Both laws have the same size-one holonomy subgroup S1. Thus even the entire sign-resolved return spectrum plus holonomy group size loses information needed for a named-Port future. The witness proves an **observer-safety obstruction in this candidate model**, not that either event is physically licensed by native P000. QED.

## Theorem 3 — Exact worst-case limited-query costs

Suppose a deterministic interrogation protocol has only two types of **single Boolean model-law questions**:
\`Q_C(i)\` gives the closure bit of one of the 4 C3 sign orbits;
\`Q_g(i,j)\` gives one rooted permission bit of that orbit, \`j=1,...,r_i\`.
No integer return-count oracle, arbitrary group test, or native execution in an excluded sector is assumed. These are logical law-interrogation queries.

Then identifying E takes **exactly 8** worst-case Boolean questions, adaptive or nonadaptive. Identifying J takes **exactly 12** worst-case questions, adaptive or nonadaptive (4 closure + 8 rooted gate questions).

**Proof.** Sufficiency is the explicit exhaustive set of 8, respectively 12, questions. For necessity consider the *single baseline policy* in which all four sign sectors are closed and every rooted gate is zero. If any rooted bit j is not queried along the baseline transcript, its value could independently be changed to 1, producing a coherent alternative with identical responses to every question asked but a different E. Consequently every rooted bit must be queried, forcing 8. If a closure bit at some orbit is omitted, changing only that orbit from CLOSED(0) to EXCLUDED produces a coherent alternative with all previous answers unchanged but a different J. Hence every closure bit must also be queried, forcing 12 on the same baseline. Adaptivity cannot improve these worst-case bounds. QED.

The 10-bit minimum *unrestricted fixed policy code* and the 12 restricted pointwise binary queries are different optimization problems.

## BRC relevance, exact check and outstanding work

The distinction A/S/E/J gives a **scope-typed information-loss hierarchy for policy laws**. It does not erase the BRC ordered path/branch source, Cell, Link, time, signs or internal rotation state. If a later operation depends on such data, J itself is not a full-state compression theorem. Valid redundancy requires the declared future to factor through the proposed quotient (Joint Relation Observer Preservation).

The Python/JavaScript companion verifier uses only exact integers and exhausts the finite 729-policy universe; its output includes the four class counts, four full fiber histograms, two explicit incompatibility witnesses and the 12-bit baseline query adversary. There is no extrapolation from finite checks to actual native dynamics. The general all-length spectral identity used here is the already saved R762CB graph-spectral proof.

**Next actual mother-objective task:** obtain the true signed \`TRIADIC_CLOSURE_E\` Cell/Link/Port predicate and the legal event-to-V17/V29/V39 transducer at frozen pins. Check whether the permitted event family really factors through sign-rooted masks. If not, enlarge the candidate space to Cell, Link, time or provenance dependent licensing before repeating observer-quotient computations. Do not identify current candidate policy-law observations with physical event legitimacy, acceptance, or Foundation status.
