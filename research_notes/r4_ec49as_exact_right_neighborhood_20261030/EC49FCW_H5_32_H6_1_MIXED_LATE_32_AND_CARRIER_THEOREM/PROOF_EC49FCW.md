# EC49FCW — 32 exact five-slot minima and the H8 two-carrier elimination theorem

Date: 2026-11-07 Asia/Shanghai
Status: AUTHOR_FINITE_EXACT_PROOF / DUAL_REPRESENTATION_EXECUTED / UNREVIEWED / NOT_ADMITTED
Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab

## Frozen object and sources
Use the original 24 designated observation/signature slots, nine-state trap-excluding DFA, ordered signed primitive-step prefix language, and fixed BRC multiset cache keys L=(4,2,1) for H2-H5 and M=(7,3,2) for H6-H9. The primitive prefix set P(w) contains every nonempty literal signed prefix of a legal word w. The total cost is the size of the union of P(w) over all original/replaced paths. The original witness costs 158 edges.

The exact source model is frozen_model.py, Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859. The bitset/literal exact search code is VERIFY_EC49FCS_EARLY2_H7H8H9.py, Git blob 6403b576ea415646d80aa8971d75a7facc20af85, both previously published on this PR in EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256. Preserve these model/source bytes; this is not a replacement scientific pin.

## Theorem A — H8 two-carrier elimination for any selected-slot set
Let D = {2:16, 3:16, 5:16, 2:32, 3:32, 5:32} in the original 24-slot witness. The following original words are signed *primitive-prefixes* of the original words in each of their two H8 carrier slots:

| Original redundant slot | Word | Two H8 carrier slots |
| --- | --- | --- |
| 2:16 | fe | 8:2 and 8:4 |
| 3:16 | feg | 8:2 and 8:4 |
| 5:16 | feggf | 8:2 and 8:4 |
| 2:32 | ge | 8:1 and 8:8 |
| 3:32 | gef | 8:1 and 8:8 |
| 5:32 | geffg | 8:1 and 8:8 |

Here the prefix relation is checked on the complete literal signed primitive expansion, not simply operator strings; the executed VERIFY_EC49FCW_CARRIER_LEMMA.py tests all 12 relations.

Choose ANY set S of original slots to replace simultaneously by legal candidate words of their respective frozen signature languages, provided at most ONE slot of H8 = {8:1,8:2,8:4,8:8} is selected. Put R=S∩D. Define OPT(S) to be the minimum cardinality of the union of all 24 signed primitive prefix sets when words in S may change and other slots remain original.

Then, as an exact theorem of this frozen model:

    OPT(S) = OPT(S \ R).

Proof. Fix arbitrary legal replacements for the slots S\R. For every d∈R there are two distinct original H8 slots carrying all prefixes of the original word at d. Because S replaces at most one H8 slot, at least one carrier for each d is unchanged and already contributes P(w_d) to the union. Replacing d by its own original legal word therefore contributes zero new edges. Every other legal replacement at d only adds a set to the union and cannot lower its size. Apply this to all d∈R simultaneously, then minimize over choices at S\R. This proves the equality. QED.

This is a genuine search-dimension elimination theorem for ALL selected-slot sets with at most one altered H8 slot. It requires no claim that the wider unrestricted problem is rigid.

## Theorem B — 32 finite exact minima
Select five slots (5:32, 6:1, 7:u, 8:v, 9:z), where u and v each range over {1,2,4,8} and z over {16,32}. Their global frozen enumeration indices are exactly 1120 through 1151 inclusive. In every one of these 32 cases the exact minimum is 158 distinct nonempty signed native prefix edges.

Finite exact proof: Write F for the prefix union of the other 19 original words and c=158-|F|. For each selected slot enumerate its full frozen multiset/DFA final-signature candidate pool; form residuals P(w)\F. Each candidate residual of size >=c cannot belong to a strict improvement. In each pool and each intermediate union stage retain only inclusion-minimal residual masks: A⊆B entails A∪T⊆B∪T for every future choice. For a remaining suffix of candidate pools let I_j be the intersection of all options in pool j. Every completion contains ⋃I_j; if |U∪(⋃I_j)|>=c for partial union U, delete U. Both reductions preserve every possible strictly improving completion. The final residual antichain is empty in all 32 cases. The original 158-edge witness is a feasible bound, proving the exact minimum.

Actual execution: 32/32 integer-bitset exact searches and 32/32 direct frozenset-of-literal-signed-prefix representation cross-checks. The two implementations share the pinned generator, but use separate prefix set representations. All per-row fixed counts, strict caps, stage antichain counts, and improvement flags agree. Bitset stage-union tests total 1,930,268; max intermediate antichain 84; unpruned Cartesian candidate product sums to 30,725,775,360,000 (domain size, not executed loops). Full per-row canonical JSON is losslessly stored in EC49FCW_FULL32.json.gz.b64 (base64 -> gzip -> UTF-8 JSON); its uncompressed SHA-256 is e139eb9f36312795b8033979290769a4be8fdd923a58974796d893e1b2f2e96a.

Theorem A also proves each of the 32 EC49FCW five-slot minima equals the corresponding four-slot minimum for (6:1,7:u,8:v,9:z). The previously computed EC49FCV 32-slot family choosing 5:16 instead of 5:32 reduces to that same four-slot problem. An additional exact certificate comparison showed identical 32 per-row bitset result objects between the EC49FCV and EC49FCW variants. This is a structural consequence of the pinned redundant H5 words, not a claim about arbitrary cache arrangements.

## Reproduction, evidence scope, next question
From the existing EC49FCS source directory, execute the immutable checker over disjoint index ranges covering 1120..1151 with --literal set to the number of rows. The completed runs used individual rows for harder indices 1120..1135 and two eight-row runs for 1136..1151. To check the new analytic carrier lemma, run PYTHONPATH=../EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256 python VERIFY_EC49FCW_CARRIER_LEMMA.py from this directory. Use VERIFY_EC49FCW_CERT.py to expand and validate the committed canonical 32-row certificate. All operations are exact integer/string/set computations.

Prior author-side five-slot row count 8,252; this disjoint 32-row extension gives 8,284. Prior early-two + H7,H8,H9 mixed-family evidence 320/1440; this extension gives 352/1440. Those counts are author-side finite certificates, not formal Source Result or independent mathematical admission. The nine-window 93-edge target remains open.

Control observation: native EM service returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Current native Researcher-ID, active owner, CLAIM, Result, and independent Driver review are not established by this GitHub write. P000 and ACTIVE worldview were read and unchanged. The next discriminating unit is in NEXT_EC49FCX.md.
