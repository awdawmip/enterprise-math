# EC49FWN supplement — Unknown hole count cannot be recovered from unsigned reflection defects

Date: 2026-11-22 (Asia/Shanghai). Scientific pin BRC16943. Follows the exact three-hole inverse in the same draft PR. Status: AUTHOR_PROVED / EXPLICIT_COUNTEREXAMPLE / NOT_REVIEWED.

**Proposition (universal complement ambiguity).** Let n,q be coprime positive integers and q odd >=3. Let G_n=Z/n, and let Z be any proper nonempty subset of G_q, of size r. Consider the two product supports W=G_n x (G_q\Z) and W'=G_n x Z. They are complementary subsets of G_(nq), so for every indexed reflection center c,

Delta_W(c)=|W triangle (c-W)|=|W' triangle (c-W')|=Delta_(W')(c).

To verify the middle equality, note (c-W')=(c-W)^c and A^c triangle B^c=A triangle B. Both supports satisfy the CRT product model with nonempty shorter factor U=G_n, but their unknown hole sets are respectively Z and G_q\Z, with distinct cardinalities r and q-r because q is odd. Thus the complete indexed unsigned reflection defect spectrum **cannot determine an unknown hole count** in the general class allowing an arbitrary number of excluded factor positions, even with U nonempty and known to be the full shorter group. In particular it cannot universally reconstruct the unknown hole convolution without another observation.

**Exact cyclic example:** n=10, q=11, Z={2,7}. First factor has V=G_11\{2,7}, i.e. 2 holes; second has V'={2,7}, i.e. 9 holes. Both use U=G_10. Their full 110-entry indexed defect spectra coincide, having only values 0,20,40. As a function of b=c mod11, the defect is [40,40,40,20,20,40,40,40,40,0,40], independent of a=c mod10. A direct independent integer calculation over all 110 positions gave exact equality of the two arrays.

**Sharp scope:** This counterexample addresses the *unknown-hole-count* model. It is not within the known-exactly-three-holes hypothesis of the main EC49FWN theorem, so does not contradict that theorem. Supplying the total size |W| distinguishes this particular complement pair, since its sizes are n(q-r) and nr. Whether (Delta_W,|W|) is sufficient for other unknown-hole-count classes remains open.

**Next:** Investigate collisions that preserve both the indexed defect spectrum and total support size, or derive a reconstruction result on a restricted family with known factor density. A real moving-Farey successor observer still requires its frozen update/observation source, not this auxiliary CRT calculation.
