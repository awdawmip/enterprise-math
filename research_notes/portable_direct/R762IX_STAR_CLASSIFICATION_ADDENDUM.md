# R762IX — independent ten-triangle classification addendum

Date: 2026-11-22. Frozen science pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.

For a ten-element family T of the 20 six-axis support triangles, form their union graph on all 15 Port vertices, retaining the isolated Port vertices when computing connected components. Define all-essential to mean that removing any single member of T strictly increases the component count.

The independent standard-library checker R762IX_TEN_TRIANGLE_CLASSIFY.py enumerates all C(20,10)=184,756 families, applies exact union-find to each family and its ten single-deletion subfamilies, and verifies precisely six all-essential families. Their 20-bit support masks, in lexicographic support order, are

    1023, 64527, 466033, 746898, 895652, 971592

These are exactly the six axis stars T_a={S:a∈S}, a=0,...,5. Actual local execution output:

    {"all_essential":6,"checked":184756,"domain":"all C(20,10) support families","star_masks":[1023,64527,466033,746898,895652,971592],"status":"PASS R762IX STAR CLASSIFICATION"}

Together with R762IX_STAR_TEN_TRIPLE_47_TO_45.md and its two exact integer certificates, this completes the all-essential ten-triple branch of the 47-event histogram (10 triples, 8 doubles, 1 singleton, 1 absence), including every realizable active set.

Scope: finite enumeration proof under the frozen composite Port–Euler observer. Mathematical status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. The general non-essential-triangle reduction relied on by earlier work remains a separate outstanding review obligation; this addendum does not assert a universal 46-event bound or a native signed P000 lift.

Next discriminating question: independently verify the R762IR non-essential-triangle reduction while preserving active Port set and positive support labels, then handle the remaining terminal histograms.
