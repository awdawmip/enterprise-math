# EC49FWH supplement — Exact collision of the complete reflection-defect spectrum

Date: 2026-11-22 (Asia/Shanghai).
Frozen input: BRC16943 four-fiber P10 decoder. Parent: EC49FWH all-center orbit theorem; scientific status EXACT_FINITE_COUNTEREXAMPLE / PARENT_DEPENDENT / NOT_REVIEWED.

## Statement

The **complete ten-coordinate reflection-defect vector** is not a lossless observer of the original binary certificate word, even when restricted to the frozen primitive rational-anchor directions.

Take the two reduced, proper rational anchors 1/11 and 3/5. Apply the source line
\[
(b-a)h_0-a n_0=-1\bmod10,\qquad
(h(t),n(t))=(h_0+at,n_0+(b-a)t),
\]
and let S consist of those t∈Z/10 whose coordinate belongs to the frozen P10 set. Direct exact evaluation gives

\[
A=S(1,11)=\{0,2,3,4,7\},\qquad
B=S(3,5)=\{0,1,3,4,6\}.
\]

These are two distinct five-site words, both of size five. Nevertheless, for **every** center c=0,...,9, the ten entries of
\[
\Delta_S(c):=|S\triangle(c-S)|
\]
agree:

\[
\boxed{\bigl(\Delta_A(c)\bigr)_{c=0}^9
=\bigl(\Delta_B(c)\bigr)_{c=0}^9
=(4,6,6,6,2,6,4,2,8,6).}
\]

Both therefore have the *same complete best-center set* C={4,7}, defect 2, orbit action K_C transitive on all ten sites (because 7−4=3 is invertible mod10), occupied orbit count 5, joint repair cost 5 and two minimum repairs.

Still **A and B are not related by any rotation t→t+d or reflection t→d−t modulo10**. Exact exhaustive checking of all twenty dihedral maps is an adequate finite proof.

This is a stronger information-loss witness than matching only (D,N), matching only C or matching orbit occupancy. The complete per-center unsigned defect spectrum plus the generated-group orbit occupancy also fails to reconstruct the original source word, even up to the ten-cycle dihedral group.

An immediate separating observable is the membership query at position t=1: 1∉A but 1∈B. Thus any subsequent operation which can query that original position must retain additional **signed/support** information. No claim about a specific moving-Farey next-height observable is made here; that needs the actual update/readout mapping.

## Reproduction

With the companion EC49FWH_ALL_CENTERS_ORBIT_VERIFY.py's functions loaded, the following is an exact certificate:

~~~python
A = source_word(1, 11, 10)
B = source_word(3, 5, 10)
assert A == {0,2,3,4,7} and B == {0,1,3,4,6}
def spectrum(S):
    return [len(S ^ {(c-t)%10 for t in S}) for c in range(10)]
assert spectrum(A) == spectrum(B) == [4,6,6,6,2,6,4,2,8,6]
assert all({(t+d)%10 for t in A} != B
           and {(d-t)%10 for t in A} != B for d in range(10))
assert 1 not in A and 1 in B
~~~

All claims use exact integer set operations on the stated finite domain. The P10 source model remains inherited under pin BRC16943. This witness is original-source position fidelity, not an assertion about general Farey asymptotics or native X6 observations.

## Next

Find a concrete frozen moving-height Farey readout or transition that distinguishes a pair of equal unsigned defect spectra, or prove that the requested readout factors through a finer observer retaining signed locations. A matching defect vector alone is now conclusively insufficient for arbitrary original-position queries.