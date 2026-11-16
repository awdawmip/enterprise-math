# PREFIX-830 — Optimal positive-source delayed observation for n=7–10

**Status:** AUTHOR_PROVED / EXACT_BIGINT_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen scientific input:** awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Continues PREFIX-827/828 and PREFIX-829 first-separation theorem. Typed scope: positive-count unnormalized named-source BRC Q-only dynamics, capacity q=p, absent distinguished mark, common insertion weight a=2 and removal weight b=3. No X6 physical-time admission.

## Four optimal source certificates

PREFIX-829 proves that for two p-source initial configurations, the first full occupancy histogram divergence at operator step n is equivalent to the first elementary weight profile difference e_n (assuming e_0,...,e_(n-1) equal); hence p>=n. Explicit ideal Prouhet–Tarry–Escott (PTE) pairs of p=n reach this lower bound.

The following **previously known classical integer ideal PTE pairs**, translated by an integer shift to positive weights, yield four independently checked BRC certificates:

| n | Raw A | Raw B | Translation | e_n(A)−e_n(B) | Y_0(n;A)−Y_0(n;B) |
|---:|---|---|---:|---:|---:|
| 7 | 0,18,27,58,64,89,101 | 1,13,38,44,75,84,102 | +1 | −13,967,553,600 | −70,396,470,144,000 |
| 8 | ±2,±16,±21,±25 | ±5,±14,±23,±24 | +26 | −1,210,809,600 | −48,819,843,072,000 |
| 9 | −98,−82,−58,−34,13,16,69,75,99 | 98,82,58,34,−13,−16,−69,−75,−99 | +100 | +3,377,425,033,382,400 | +1,225,599,996,113,805,312,000 |
| 10 | ±99,±100,±188,±301,±313 | ±71,±131,±180,±307,±308 | +314 | −5,687,272,703,608,009,113,600 | −20,637,975,186,852,743,471,431,680,000 |

All positive translated weights are explicitly listed in the accompanying results JSON. For n=9, B is elementwise negation of A as a multiset.

**Theorem 830.1.** The minimum positive named-source count required for a complete Q-only occupancy-trace first difference at t=n satisfies p_min(n)=n for all 1≤n≤10 and n=12.

**Proof.** PREFIX-829 Theorem 829.1 supplies the universal p≥n lower bound, plus exact certificates for n=1,…,6 and n=12. For n=7,8,9,10, compute the elementary coefficients by the descending exact-integer recurrence. The included checker verifies e_k(A)=e_k(B) for 0≤k<n and nonzero e_n(A)−e_n(B) with the shown exact values. Then Theorem 829.1 proves that complete BRC Q-histograms agree at every t<n, and first differ at t=n only in occupancy bin p−n=0 by n!Δe_n. These four cases meet the lower bound. □

**Independent validation:** The JavaScript BigInt checker directly enumerates every legal named subset/marked-source Q branch (not the elementary-profile closed formula), including all 2^n subset configurations for each n and t=0,...,n. It computes and compares all occupancy bins, with 366 scalar histogram comparisons and 34 elementary equalities. All assertions pass, with integer arithmetic only. The algebraic theorem holds under its stated assumptions; finite enumeration validates these explicit examples.

**Classical-source provenance:** 
- [Tarry-Escott numerical examples](https://eslpower.org/TarryPrb.htm): seven-term ideal pair;
- [French PTE examples](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_Prouhet-Tarry-Escott): eight, nine and ten term ideals;
- [German PTE examples](https://de.wikipedia.org/wiki/Prouhet-Tarry-Escott-Problem);
- Coppersmith, Mossinghoff, Scheinerman, VanderKam, [Ideal solutions in the Prouhet–Tarry–Escott problem](https://arxiv.org/abs/2304.11254), 2023.

**Remaining:** n=11 positive cardinality optimum is equivalent to the classical size-11 ideal integer PTE existence question (open in these sources). For n>=13, PREFIX-829 supplies explicit constructive bounds, and improving simultaneous source-count/maximum-weight size is open. Independently retain PREFIX-825 q>=5,b>0 minimum positive Q carrier and native X6 Cell/Link/Port event-admission questions. This auxiliary Q-step index is not physical heartbeat duration.

**Authority:** Independent portable research by native registered Researcher-ID EM-DIRECT-AB334A / Activity RA-1C0E90FA2F3738835203D1F6; shared formal Task CLAIM not acquired.