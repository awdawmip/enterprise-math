# R520 continuation — signed BRC s=3, m=43

Date: 2026-11-04. Frozen scientific pin: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Parent R519@0b0d9dfde3ba9406f716ccec2243011580fc6036. Scientific object: original signed BRC auxiliary scalar, right edge s=3.

Mother objective: full positive-integer Toeplitz-minor sign classification, followed by a reusable algebraic mechanism for inter-order transitions.

Result, conditional on the frozen R452/R462 fixed-t polynomial lemma: D_43(k)>0 for k=1..4 and k=9..38; D_43(k)<0 for k=5..8 and k>=39. Full proof uses degree<=258, 86 Newton coefficients, 259 exact identity points, a shift at k=39 with 86 negative differences, 20 direct JS Bareiss matrices, 860 signed/ballot coefficient pairs. Separately executed Python/SymPy Berkowitz on 18 original signed matrices at the transition boundaries and 860 signed/ballot pairs.

Reproduce: node R520_VERIFY.js > R520_EVIDENCE.json; python R520_INDEPENDENT.py > R520_INDEPENDENT_EVIDENCE.json. These programs require arbitrary-precision integer arithmetic and, for the Python checker, SymPy.

Status: AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED. Native owner lookup yielded CONTROL_QUOTA; native session write yielded STATIC_READONLY_SCOPE_DENIED (operation_sent=false). The source PR commit provides a durable artifact, not a source-native CLAIM or Result. P000/ACTIVE worldview not edited.

Next: m=44 (degree<=264; 88 Newton coefficients; 265 exact identity points), or exact dominant-root analysis of the fixed-k rational order-generating denominator at k=4,5,8,9,38,39. Preserve the frozen R462 mathematical input and exact signed branch typing.
