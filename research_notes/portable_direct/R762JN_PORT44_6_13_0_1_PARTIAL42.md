# R762JN — (6,13,0,1) 44→42 Port–Euler compression on 17 inactive-Port types

Status: AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED. Date: 2026-11-23 (Asia/Shanghai). Model: six-axis **composite Port–Euler observer**, not the native signed P000 dynamics.

## Statement
Take six axes, the 15 pair-Ports as vertices, and the 20 three-axis supports as event labels. Every support supplies three possible local Port–Port edges. A legal configuration is a connected multigraph on its exact declared active Port set, with all active degrees positive and even, all inactive degrees zero and prescribed support multiplicities. Such a configuration admits a closed Euler trail starting at **any** chosen active Port.

For any missing support z, any six triple-multiplicity supports T among the other 19, and the remaining 13 double supports, set n_z=0, n_S=3 if S∈T, n_S=2 otherwise (44 total). Let M be either empty or one of the 16 **nonmatching** inactive Port sets that are locally eligible: no positive triple support has two inactive local Ports. Then there is j∈T and a legal 42-event configuration with counts n−2e_j, **the same exact active Port set**, the same positive support labels, parity of each support count, and arbitrary prescribed Euler start. This construction exists for every such (z,T,M), independently of the premise that the 44-event Euler circuit already exists; adding two parallel j edges to the 42-event certificate gives a valid 44-event witness.

The 92 locally eligible inactive sets for each z split into 76 matchings and 16 nonmatchings, with counts by |M|=0..4 of 1,15,48,25,3 (R762JM). This result covers the empty set and **all 16 nonmatching sets**. The other 75 nonempty matchings remain to be solved for this histogram.

## Finite complete classification and constructive proof
S6 acts transitively on z. Fix z={0,1,2}; its stabilizer S3×S3 has 36 members, dividing the binomial(19,6)=27,132 possible T into precisely **885** orbits. For each orbit representative T, inspect each of the 17 admissible M in the stated domain. Moving an arbitrary labelled (z,T,M) into the representative T transports M to another one of these same 17 sets, so the coverage requires no assumption about a representative's residual stabilizer.

A direct certificate specifies j∈T and exactly 60 nonnegative integer edge counts a[S,e]∈{0,1,2,3}; check for every support S: sum_e a[S,e] = n_S−2·[S=j], that the total is 42, that precisely the complement of M has positive even degree, and that its positive edge graph is connected. These integer assertions imply existence of the required Euler circuit. Axis permutations preserve all assertions. The standard-library independent checker in this research batch recomputes the 885 orbit representatives and all 92 locally eligible M, then checks every certificate, without relying on SciPy/HiGHS candidate solver status.

- M=empty: **885/885 PASS**, raw record SHA256: 52ccee2fab77f0b8ff343cffbebbe2833dc3fe2f10bc5fa963c0412e22a4a738.
- M nonmatching: **14,160/14,160 PASS**, raw record SHA256: a255c9a3fc95d4d578a99243c68171d114db7bef038b3fc28b2035b037d5e512.
- Total exact integer certificates: **15,045**; full labelled coverage: **20×27,132×17 = 9,224,880** configurations. Independent checker: PASS. Archived records are binary 16-byte records, LZMA compressed, then Base64 encoded. Byte 0 is the removed support; the next 15 bytes contain 60 two-bit local edge multiplicities. The full certificate archives are in the conversation's R762JN research ZIP; they are not contained in this small GitHub publication. The compact checker can validate them without requiring the original candidate-generation implementation.

The SciPy/HiGHS MILP run was used only for *candidate discovery*, not as the proof oracle. A second independent exact Python checker reconstructed the finite domain, checked all graph constraints, and reproduced the above two raw SHA256 values. The statement is computer-assisted, author-checked and not independently mathematically reviewed.

## Continuation and scope
R762JM (Draft PR #2972) proved a different 44-event class (5,14,1,0) and the 92-local-inactivity lemma. This R762JN result advances (6,13,0,1), but **does not yet settle the complete class**; next: 75 nonempty matching Port sets (15+45+15), and independently (6,12,2,0). The previous author-side global k=0 upper bound **remains 44**, without upgrading earlier unreviewed R762IR/R762JK dependencies. Native signed P000 Cell/Link, triadic closure and BRC provenance are separate research obligations. The active X6 formal task's owner and protected PROGRESS are not inferred from this independent scientific note.

## Reproduction
Full independent checker: R762JN_CHECK_INDEPENDENT.py (next to this document). Run it with the two LZMA/Base64 certificate text files from the attached complete research ZIP. Supporting generator scripts and candidate MILP code are included in that ZIP; they allow regeneration where SciPy is available. Certificate verification uses only Python's standard library.