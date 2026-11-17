# X6 Unit88 — sharp finite-depth alias horizon for signed triadic events

Date: 2026-11-17. Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task RS-X6-LEGACY-PLANE-RECONCILIATION / publication TP2-B4A441B23DA3159232C2.

Status: **AUTHOR-EXACT / INDEPENDENT INTEGER EXECUTION / CURRENT SOURCE TYPED / UNREVIEWED / NOT_ADMITTED**.

## Source and operation type

Scientific inputs are frozen P000 V5 signed native Cell-displacement model on an affine torsor over Z^6 (P000 commit 59538f585d037d09ef687b28715c4bc1a3f9fe03), historical pin fd2bcff10ca6e147348b6c1236027fc0d2877df3 and native 12-step signed BRC source blob 300a96e3dc24bf6fff73743037a0347a8bc83176.

A **different, directly inspected current consumer**, experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py at blob 5d0f2cb88a0d4e437b5025e9050e3044f7831cd4, defines exactly 20 three-distinct-axis types times 8 sign assignments, i.e. 160 **labeled simultaneous triadic events**. Each event adds one signed unit on three distinct axes. The event is a composite word-operation, not a new primitive spatial axis and not automatically an admissible stable physical-force configuration.

Define for this exact event alphabet the ordered length-L word multiplicity A_L(z). Let rho(z)=z-min(z)*1 and C_m(z)=(rho(z),min(z) mod m) for every positive integer m, where 1=(1,1,1,1,1,1). Define the cover return R_m(L)=sum over C_m(z)=C_m(0) of A_L(z), and the exact Cell return R_0(L)=A_L(0). The full primitive signed 12-operation BRC remains a separate operation language with a distinct clock.

## New theorem: first separating event count for every positive modulus

For all integers m>=1 and event lengths L>=0:

- R_m(L)=R_0(L) for 0<=L<2m.
- R_m(L)=R_0(L)=0 for every odd L.
- The first positive difference occurs exactly at L=2m, with

  R_m(2m)-R_0(2m)=2 E_m,

  E_m = [x_1^m ... x_6^m] (sum_{S subset {1,...,6}, |S|=3} prod_{i in S} x_i)^(2m) > 0.

**Proof.** C_m(z)=C_m(0) iff z=km*1 for some integer k. Each event moves exactly three coordinate units, so reaching the nonzero diagonal endpoint km*1 requires at least 6|km| atomic axis changes, hence at least 2|k|m composite events. No extra cover endpoint can contribute for L<2m. At equality, the only nonzero diagonal endpoints that can contribute are +m*1 and -m*1. The bound is saturated only by all-positive, respectively all-negative, sign assignments. The ordered list of unsigned triad supports must contain each named axis exactly m times, counted by the stated coefficient E_m. At least one such list exists (repeat a complementary pair of three-axis supports m times). Finally, each event changes the parity of the total coordinate sum by one: 3L has the same parity as L; a diagonal endpoint sum 6km is always even. Thus odd-length event words cannot reach any cover return. QED.

**Operator-clock consequence.** Under the original 12 signed primitive axial operations, Unit86 first separates at 6m **primitive steps**. This current 160-type triadic-event language first separates at 2m **composite events**, with separate multiplicity 2E_m. Relating the two return statistics requires retaining the event decomposition, axis/sign labels and observation scope; merely equating tick numbers is invalid.

## Exact new finite execution

Independent Python checked the E_m coefficients via a bounded six-axis degree-vector DP and performed separate 160^2 direct signed-event enumeration at L=2, plus a two-event convolution to exactly count all 160^4 possible four-event words at L=4.

| m | first separating event count | E_m for each sign | additional event words |
|---:|---:|---:|---:|
| 1 | 2 | 20 | 40 |
| 2 | 4 | 1,860 | 3,720 |
| 3 | 6 | 297,200 | 594,400 |
| 4 | 8 | 60,871,300 | 121,742,600 |
| 5 | 10 | 14,367,744,720 | 28,735,489,440 |

Direct results: R_0(2)=160, R_1(2)=200. At four composite events, R_0(4)=460,320, R_2(4)=464,040; the convolution table contains 3,477 distinct two-event signed endpoints. All exact checks passed. Three runs with ordinary Python, -O and -OO produced byte-identical JSON.

Portable artifacts saved separately in:
- research_checks/X6_UNIT88_TRIADIC_SIGNED_COVER_FIRST_ALIAS_CHECK_20261117.py (local exact executed SHA256 30015bff94e6bddc5dd4f65021182f77425e7f1894ef956d2c9e49c1e9eb842a).
- research_checks/X6_UNIT88_TRIADIC_SIGNED_COVER_FIRST_ALIAS_RESULTS_20261117.json (local output SHA256 f78276dc0aae8ecafe864776d4f9a7711cef09f1ed1a4fd5500f6a69ad01cf83).

This check uses the actual 160-event source alphabet but does not rerun or substitute for native R063/Helly benchmarks. The existing triadic source continues to correctly report its own 20/1860 underlying degree counts. No wrong production caller was established from this scoped read, so no existing source was patched.

## Control boundary and genuine next unit

Original X6 author provenance: Research conversation chatgpt-research-onhour-enterprise-math-20260923, SID MCP-082892eb480e45dea6d4b9fcc0491034, CLAIM MCP-579c8e23625448582b421831, RUN RUN-fb25028676f9692ab1bacaee, Activity RA-5E3FE1E761E4963EC461A892 (last verified 106 events). The account-level GitHub Chat recovery receipt #6994 currently projects a different D25 SID. The exact continuation receipt #6995 is SUCCEEDED as a read but execution_authorized=false, with the typed predecessor route. This evidence is a scientific portable author continuation, not a current authenticated X6 Source PROGRESS/CLAIM/Result.

Parent open work: LP011/LP019 precise historical source:line attribution or independent Driver REQUEST_REVISION; remaining 28-LP real downstream consumer graph; original-X6-authenticated Native semantic publication and Activity; independent review/admission. **Next exact step:** inspect an unreviewed real downstream call that mixes triadic composite event counts with native signed primitive BRC or finite-depth return, preserving its actual caller path/line, inputs and output observer. Patch only a demonstrated current defect; keep unlocated historical blame as UNRESOLVED_PROVENANCE.

No scheduler, notifications, task-selection, P000, Source scientific pin, or unrelated owner work was changed.