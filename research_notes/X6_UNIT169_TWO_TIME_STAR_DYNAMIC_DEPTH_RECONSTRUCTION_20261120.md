# X6 Unit169 — Two-time K4 STAR observations recover hidden signed Cell depth

Date: 2026-11-20 (Asia/Hong_Kong).
Parent task RS-X6-LEGACY-PLANE-RECONCILIATION / publication TP2-B4A441B23DA3159232C2 / mother PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905.
Science input pin awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03; frozen historical comparison fd2bcff10ca6e147348b6c1236027fc0d2877df3.
Author provenance: Research lane chatgpt-research-onhour-enterprise-math-20260923; historical researcher EM-X6-FB6990; original SID MCP-082892eb480e45dea6d4b9fcc0491034.
Status AUTHOR_PROVED / EXACT_FINITE_EXECUTED / GITHUB_VERIFIED / UNREVIEWED / NOT_ADMITTED. The R063 native benchmark was not rerun.

## Sources and genuinely incremental objective

The frozen native displacement and centered three-axis sources are definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md and definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md at the scientific pin. The actual selected-triple checker in experiments/x6_centered_three_axis_slice_v19_20260905/check_centered_slice_rebase.py consumes min-zero observations.

Unit162 (research_notes/X6_UNIT162_C12_ROTOR_SIGNED_AXIS_CYCLE_TYPED_BRIDGE_20261119.md at commit 8b08c89218c6564f789e72db7a4b7c6fb54bc213) constructed A(x1,...,x6)=(-x6,x1,...,x5), with A^6=-I and A^12=I, as a signed-coordinate graph automorphism candidate. This is not an original frozen physical-rotation production call. Unit166 (research_notes/X6_UNIT166_C12_DIAGONAL_EQUIVARIANT_QUOTIENT_20261119.md at 0f471c66527e8e50edd755449b16147a79e130a0) established that the diagonal observer alone does not admit the full C12 action. Unit168 (research_notes/X6_UNIT168_FCC_K4_MINIMAL_STAR_OBSERVER_RECONSTRUCTION_20261120.md at eee67895060e60811756aee22dfe5750df631dcf) proved every three of the four established K4 STAR observers reconstruct the signed six-coordinate displacement modulo its common diagonal. Existing V10 (research_notes/X6_20_SLICE_INVERSE_LIMIT_RECONSTRUCTION_V10_20260905.md at f5246fd204222d6c6903536f9336d02d367de173) already proved full 20-triple reconstruction and documented the prior four-STAR atlas; those are prior art.

**New scientific question and result:** a second min-zero STAR observation after an explicit signed-coordinate operation can recover the integer common depth, with an exact if-and-only-if criterion. This gives a genuinely lossless **native signed displacement and endpoint N-BRC multiplicity** decoder without recording depth separately.

## Complete two-time reconstruction theorem

Let z be any element of Z^6, d=(1,1,1,1,1,1), and D=Z*d. For a labeled triple S let Obs_S(z)=can3(z restricted to S), where can3 subtracts the minimum. Index the six signed axes by the six edges 01,02,03,12,13,23 of K4. The four existing coordinate STAR sets (zero-based indices) are:

    S0=(0,1,2), S1=(0,3,4), S2=(1,3,5), S3=(2,4,5).

At the initial time, observe any three distinct STAR triples. Their exact connected-subatlas decoder recovers r=can6(z), so z=r+h*d for an unknown integer h=min_i(z_i).

Choose an integer k, apply the declared signed permutation A^k, and observe one additional STAR S among the four.

**Theorem.** The joint first and second observations determine z uniquely for all z in Z^6 if and only if the three entries of A^k*d restricted to S are not all equal.

**Constructive reconstruction:** In an effective case choose i,j in S with (A^k*d)_i unequal to (A^k*d)_j. Write w=A^k*r, v=Obs_S(A^k*z). Then

    h = [(v_i-v_j) - (w_i-w_j)] / [(A^k*d)_i-(A^k*d)_j].

The denominator is exactly +2 or -2 and, for genuine integer observations, divides the numerator. Recover z=r+h*d. This determines squared native component norm L_E^2=sum(z_i^2), shortest primitive signed word length N=sum |z_i| and endpoint native BRC shortest-word count B(z)=N! / product (|z_i|!). It does not reconstruct separately decorated path provenance.

**Sharp negative half.** When all three entries of A^k*d are equal, adding any integer t*d to z changes neither initial nor second observation; every such observation fiber is infinite. The explicit witness 0 and d has identical observed readings in every ineffective case, while B(0)=1 and B(d)=720. At least one unbounded integer-valued additional distinction is needed to reconstruct the entire original coordinate across the initial observer's infinite fiber; an extra fixed Boolean bit cannot do so.

### Exact 48-case time/STAR classification

For k=j or k=j+6 modulo 12, 1<=j<=5, the coordinate signs of A^k*d are, up to a global minus, negative in positions 0 through j-1 and positive in positions j through 5. An extra STAR is effective exactly if it crosses this sign cut.

| k (mod 12) | Effective extra STAR | Effective count |
|---|---|---:|
| 0, 6 | none | 0 |
| 1, 7 | S0, S1 | 2 |
| 2, 8 | S0, S1, S2 | 3 |
| 3, 9 | S1, S2, S3 | 3 |
| 4, 10 | S1, S2, S3 | 3 |
| 5, 11 | S2, S3 | 2 |

Of all 48 possibilities there are exactly 26 effective and 22 ineffective. In particular, after the initial three STAR observations, one extra integer relative difference on S0 or S1 immediately after A is sufficient to recover the hidden depth.

**Proof:** Equality of any initial connected three-STAR tuple implies x-y=t*d for some t in Z, and conversely. Under A^k the difference becomes t*A^k*d. Equality of the second min-zero triples is equivalent to all three selected coordinate differences being zero. A constant restricted vector permits arbitrary t; otherwise two selected coordinates differ by 2 or -2, forcing t=0. Subtracting those two measured second-time coordinates gives the decoder above. The identity A^6=-I and the explicit signed shift determine the complete table. This proves the universal statement for every integer z and every k, independent of finite tests.

## Exact executable certificate

Published checker research_checks/X6_UNIT169_TWO_TIME_STAR_DYNAMIC_DEPTH_CHECK_20261120.py:
immutable commit 10d685a68045e247d34da3ab136852bcf546594f;
Git blob SHA1 0948f63f1daaa286de375f8f3793c70db504ed4e;
SHA256 b8b6856e4084b8bf33f61f281e5999f6a10183538150e232d42f23f3ead082f6.

Published integer result research_checks/X6_UNIT169_TWO_TIME_STAR_DYNAMIC_DEPTH_RESULTS_20261120.json:
immutable commit 5ab28c99c60e9efa37c0c166db6abdecf3456f76;
Git blob SHA1 5c82ff535c98b442263e5a5625c8c3e01fed3aae;
SHA256 2f34876dfb099ed7d23257a7a2999f20ed6839756d374a7835350616933fa114.

The executed local source matches the published exact Git blob. Exhaustive domain [-2,2]^6: 15,625 native signed states. For every state, 12 time exponents and four extra STARs, 750,000 dynamic-observation instances with 406,250 correct full native displacement and N-BRC restorations; all ineffective cases tested with an additional hidden-depth alias. Zero failed checks. Python, Python -O and Python -OO produced the same result bytes, using explicit exception checks that remain enabled under optimization. The all-integer proof establishes the universal claim; this exact finite check validates the implementation and finite classification.

## Mother target and current control boundary

Disposition: PRESERVE_TYPED_RELATIVE_OBSERVER + CONSTRUCT_EXACT_OPERATIONAL_DEPTH_REPAIR. The construction combines existing native signed-axis, true three-STAR relative observation and an explicitly proposed signed graph automorphism. It does not change P000, promote a physical rotation, identify an actual old erroneous native consumer, or complete the 28-LP audit.

Still unfinished: exact historical LP011 purported native argmax and LP019 purported positive native BRC subtraction commit:path:line (UNRESOLVED_PROVENANCE); remaining actual 28-LP production/consumer dependencies; Units149–152 historical native semantic linkage debt; independent Driver review and formal Result. Source-backed Unit167 and Unit168 author evidence and Unit168 novelty repair are preserved.

The original Units162–164 Native request onhour-20261119-2208-x6-own-units162164-native-progress-v1 reached SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED with authenticated readback, as did the distinct original Units165–166 request onhour-20261120-0015-x6-own-units165166-native-progress-v1. Own RUN resume onhour-20261120-x6-own-run-c920-after166-resume-v1 was RUNNING/error=null at author source preparation, so no Unit169 native PROGRESS or new generation is asserted. Only after its original result confirms fresh actual ownership may additional native linkage be attempted. No scheduler/notification changes.
