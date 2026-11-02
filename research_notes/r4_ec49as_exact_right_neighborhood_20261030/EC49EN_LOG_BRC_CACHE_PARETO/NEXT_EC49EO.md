# EC49EO — Three-resource native-X6 / BRC Pareto optimization

**Parent:** EC49EN (also EC49EI, EC49EJ, EC49EM). Scientific pins remain GLOBAL_KNOWLEDGE_V1 773d538180bfb49e24cffeb35c3ee75eb0628e2e, EM fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. P000/ACTIVE worldview and typed positive BRC-only path remain unchanged.

**Completed analytic facts:** All H>=2: M_min(H)=ceil(log2(H+1))-1 and M_if_S4(H)=ceil(log2 H). Exact nondominated (M,S): (j,4) for H=2^j; (j,6),(j+1,4) if 2^j<H<2^(j+1). Independently, E_min=4H+30 at H>=5. EC49EN witness schedules have verified native prefix costs but have not been optimized conditional on M or S.

**Next smallest executable exact question:** For H=3,4,5 enumerate legitimate same-p rank-nine word sets and solve for least distinct signed primitive-prefix edges E subject to M=M_min(H), and separately S=4. Produce exhaustive or exact integer-program lower-bound certificates, attaining word lists, true nine-history transfer rank, actual two-channel positive-BRC monomials and independent recheck. Determine true non-dominated (E,M,S) triples. Extend to H=6 upon successful finite classification.

Do not treat word/path count, BRC arithmetic count, observer block count and native edge count as interchangeable. Preserve original word identity, A/B seam, cached p-vector, and native operation path. Store in existing Draft PR #1730 with immutable readback. Formal native Result/Driver review remains subject to authenticated role and ownership.