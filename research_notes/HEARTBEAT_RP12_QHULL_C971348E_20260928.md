# RP12-QHULL: the 19-dimensional Q16 hull and a one-bit newly generated defect

Progress-Event-ID: RP12-QHULL-C971348E-20260928
Date: 2026-09-28 Asia/Taipei
Status: AUTHOR_DERIVATION / STATIC_SOURCE_INSPECTION / LOCAL_VALIDATION_PENDING / UNREVIEWED / NOT_ADMITTED
Global read snapshot: 753bc40a5d365075c0bc60de68dc2f53ab59d9f1
EM read/publication preflight: b13cc16abc59707b719bab1c792704d4e89c34de
Parent derivation: c59a67def224fbf4ed4673be14d6e855288b0a1e:research_notes/HEARTBEAT_RP12_REPLICA_DIAGONAL_C971348E_20260928.md
Parent executed carrier: RP11-CLOSED, engine SHA256 120a8cd500711ac1b6a675e167a87547c6834e3370fe99b04ff0e5347f48430e.

This is a new proof checkpoint, not a new numerical experiment or formal Result. Container, analysis Python and visible Python each returned ClientError in this turn. No archive extraction, new BRC runtime call, machine-checked proof, timing, probability enumeration or raw-byte hash verification is claimed. All original files, P000, actual b12 gate identities, work-label semantics and schedules remain unchanged.

## 1. Exact source and the scope of the new result

The complete attached RP11_CLOSED_BankCertificate.json (file_000000008ba48211ab67c7941f25d025) was read through Files. It contains all thirteen 61-mode integer basis vectors E, their exact Gram, source pins and the previously executed restricted gate certificates. The basis is E=(e0,e1,f4,...,f14). The f_m are the published primitive tail vectors. Parent facts remain author-executed/not-independently-admitted facts.

RP12-REPLICA already identified U19={x: x_k=0 for k>20, x3=x2, x15=x14}, and its subspace U18 defined by the additional equality x17=2x14. These subscripts are zero-based INTERNAL MODE indices, not work labels or native spatial axes.

This note proves an exact new statement about the ORIGINAL common-shift, toward-zero Q16: U19 is the smallest fixed LINEAR space containing span(E) and closed under Q16 on EVERY finite dyadic input in that space. This is stronger than finding one failure of the scaled-copy relation, but it does not establish the minimal representation of only reachable histories or of arbitrary nonlinear codecs. Full-gate closure on U19 remains the separate source/runtime obligation described in section 7.

## 2. Static tail signatures from the complete certificate

Each row below is the vector of coordinate values across f4,f5,...,f14, in that order. The two grouped rows denote equal signatures. All omitted ambient coordinates above20 are zero. No floating tolerance or partial-state hash is used.

|mode(s)|signature|
|---|---|
|2,3|1,1,1,1,1,1,1,1,1,1,1|
|4|2,1,1,1,1,2,1,1,2,2,1|
|5|2,2,2,2,2,2,2,2,4,2,2|
|6|2,2,4,2,2,2,2,2,4,2,2|
|7|4,2,4,4,4,8,2,4,4,4,2|
|8|8,8,8,4,4,8,4,8,8,4,4|
|9|8,16,8,4,4,16,4,8,8,4,4|
|10|8,16,16,16,16,32,8,8,8,8,4|
|11|16,32,16,16,16,32,16,16,16,8,8|
|12|32,32,16,32,32,32,16,16,16,8,8|
|13|32,0,0,0,64,64,16,16,16,16,8|
|14,15|0,0,0,0,0,0,32,32,32,16,16|
|16|0,0,0,0,0,0,32,32,32,32,16|
|17|0,0,0,0,0,0,64,64,64,32,32|
|18|0,0,0,0,0,0,0,0,0,32,32|
|19|0,0,0,0,0,0,0,0,0,64,32|
|20|0,0,0,0,0,0,0,0,0,0,64|

Thus there are exactly seventeen distinct nonzero tail signatures. This is a direct comparison of source arrays, not seventeen new simulations. In particular, a scaled equality such as row17=2*row14 is NOT equality of signatures.

## 3. The Q16-closed linear hull theorem

Define Q_K on a finite dyadic vector x=n*2^e using the inherited common two-adic normalization, maximum magnitude bit length b, shift s=max(0,b-K), and q_i=sgn(n_i) floor(|n_i|/2^s). Its physical output is q*2^(e+s); exact post-normalization does not change this value. The map is sign-preserving truncation, not arithmetic right-shift of negative integers.

Theorem. Let V be a rational linear subspace of the 61-mode carrier containing S=span_Q(E), or a real linear subspace with the same containment. Suppose Q16(x) belongs to V for every finite dyadic x in V. Then U19 is contained in V. Conversely U19 contains S and is Q16-closed. Consequently the smallest such linear enlargement is exactly U19 and its dimension is19.

Proof.

1. Form the symbolic integer tail vector
   r=sum_(j=0)^10 128^j f_(j+4).
   Every signature digit is between0 and64, so base128 representation has no carries. Therefore r_i=r_j precisely when the two displayed signatures are equal. Because f14 is positive on every mode2..20, with L=128^10 we have L<=r_i<65L on those modes. Also r2=sum128^j is odd. These are exact algebraic consequences of the source entries; the large vector is not a claimed runtime artifact.

2. Use e0 as a scale-setting coordinate, with A=2^15. For a positive dyadic t<2/L put x(t)=A e0+t r. All tail magnitudes are below130<A, hence the anchor is the maximum coordinate. Write t=p/2^a in lowest terms; p is odd. Since r2 is odd, the common integer numerator (A*2^a,0,p*r2,...) has no common factor2. Its maximum bit length is16+a. The inherited Q16 therefore uses exactly shift a, and its physical quantization step is1. It follows that
   Q16(x(t))-A e0=(0,0,floor(t r2),...,floor(t r20),0,...)
   belongs to V. This uses the original data-dependent quantizer with a legal scale anchor, not an independently chosen replacement grid.

3. List the seventeen distinct positive r-values as a1>...>a17. Their first floor thresholds t=1/aj all lie inside (0,2/L). Around each threshold choose two dyadic numbers t_minus<t0<t_plus sufficiently close that the finite family floor(t r_i) crosses no other threshold except those exactly coincident with t0. Such dyadic choices exist. At t0=1/aj, the difference of the two floor vectors is the indicator of the aj block plus indicators of some larger-value blocks whose higher integer thresholds coincide. Smaller-value blocks have not yet reached their first threshold, so do not contribute.

4. Descending induction isolates the indicator of each of the seventeen signature blocks: the largest block is obtained first, and at each subsequent step previously isolated larger indicators are subtracted. Every indicator is in V by linearity. Together with e0 and e1 these are nineteen nonzero, disjoint-support vectors, hence independent, spanning U19.

5. U19 is itself Q16-closed because common-scale coordinate truncation preserves zeros and equal coordinates. It contains the displayed E. This proves both inclusion minimality and dimension minimality. QED.

This theorem concerns closure on ALL dyadic inputs of a fixed linear carrier. The synthetic anchored vectors and their linear combinations are not asserted to occur along a standard Shor measurement history. It is not a lower bound on stored bits, nonlinear encoding size, approximate-output algorithms, or general quantum/classical complexity. If one additionally requires a carrier to contain e0 and be invariant under the full gate bank, the RP11 linear minimality forces it to contain S; the theorem then supplies a19-dimensional lower bound after imposing all-input Q16 closure. It does not by itself prove a complete19-coordinate gate implementation exists.

## 4. The newly generated scaled-copy defect is exactly one discarded bit

Suppose an input is in U18, so its numerator triple at modes14,15,17 is (u,u,2u), with common exact exponent e. Let the ORIGINAL full-vector Q_K choose shift s>=1. Write
   a=floor(|u|/2^s),
   b=floor((|u| mod 2^s)/2^(s-1)) in {0,1},
   sign=sgn(u), q=2^(e+s).
The exact output triple is
   sign*q*(a,a,2a+b).
Therefore
   x'_17-2x'_14=sign*b*q.
For s=0 there is no new defect. This is integer division with remainder, not a stochastic or physical-noise assumption.

At this ONE boundary with ZERO incoming scaled-copy defect, eighteen representatives plus this carry bit, its required sign and common scale recover the old19-coordinate output exactly. When a=0, the sign cannot necessarily be inferred from the retained representative, so it must not be dropped.

This is NOT a claim that one bit persists for all later evolution. Once a nonzero defect is present, general signed arm addition, different dyadic scales, gates and later truncations must carry its actual value or a newly proved codec. In U19 a general triple can be written (a,a,2a+d), with exact norm 6a^2+4ad+d^2. The cross term is part of the actual norm. Treating the defect as an independent positive mass would be incorrect. No persistent carry sampler has been implemented.

## 5. A distinct new target: full-scale eighteen-coordinate repair

Define an unexecuted candidate Q18_FS,K only on U18 inputs. Choose the shift from the ORIGINAL full decoded21-coordinate maximum, run the original toward-zero truncation, and then discard the newly generated carry of section4. Equivalently, truncate all eighteen representative numerators at that SAME full-vector shift and decode with H18.

This differs from RP12's representative-maximum18 quantizer. For the interface input (3,3,6), K2, the original gives (2,2,6), the present full-scale repair gives (2,2,4), whereas the prior representative-maximum example can leave (3,3,6). They must not be mixed in probability or timing records.

For the triple in section4, the repair changes sign*q*(a,a,2a+b) into sign*q*(a,a,2a). Its EXTRA squared error relative to the original Q output is b*q^2, while its squared-norm loss is b*(4a+1)*q^2. Thus the repair error is bounded by its norm loss. Retaining the carry is exact; dropping it is a specifically declared approximation.

For K>=2 a nonzero complete input row remains nonzero after full-scale repair. If a maximum-magnitude coordinate is not17 its own retained representative survives. If17 is maximal, its representative14 has at least2^(K-2) units after the common shift and therefore survives. Every decoded physical mantissa at the common output scale has at most K magnitude bits: in particular |2a|<2^K. Exact common normalization cannot increase that bound. This is stronger than the K+1 possible decoded width of the independent representative-maximum rule. It still does not bound exponents, temporary gate products, probabilities, labels, audit objects or total RSS.

Let W18 have weights2 at representative2,6 at representative14, and1 on the other16 representatives. Its sum is24. Both the original-to-repaired coordinate magnitude decrease and the weighted identity a^2-b^2-(a-b)^2=2b(a-b)>=0 imply
   Q(Q18_FS,K(x))<=Q(x),
   Q(x-Q18_FS,K(x))<=Q(x)-Q(Q18_FS,K(x)).
If a nonzero shift is used, each representative error is less than2^(e+s). The original full norm contains its largest coordinate, of magnitude at least2^(e+b-1). Hence
   ||x-Q18_FS,K(x)||/||x|| < sqrt24 * 2^(1-K) < 5*2^(1-K).
If shift0 is used the error is zero. There is no fitted radial factor, trial Gram search, or unknown order/factor in this rule.

Subject to the still-pending exact gate closure on U18, the same fixed b12 library, preserved work labels and coherent arm order, the inherited whole-attempt mass-correction proof applies to this NEW target. Rejecting a random mass correction ends the entire attempt; it is not local retry at the current label. With eta_K=5*2^(1-K)<1, all-history TV to the same-bank unquantized evolution is at most min(1,(t-1)*eta_K), and survival is at least(1-eta_K)^(2(t-1)). Initial-model/bank error remains separate. These are symbolic conditional bounds, not newly measured probabilities. Even error certification does not prove that repairs are worthwhile in wall time or that the target finds factors efficiently.

## 6. What can and cannot be concluded

Established here as author derivations from the declared exact source:
- the exact19-dimensional quantizer-closed linear hull, including a scale-anchor/threshold proof;
- the exact one-bit freshly generated scaled-copy defect, with sign/scale requirements;
- the full-scale18 repair contract, its norm-loss certificate and decoded K-bit property;
- a sharper separation of same-target representation, changed-target approximation, and non-linear residual encoding.

Not executed here: parent ZIP extraction/hash, any new scientific BRC call, intertwiners on all18/19 carrier vectors, new quantizer code, finite output laws, timing or time-to-factor comparison. The17 signature classes are static source facts, not17 tests. No generic minimal nonlinear carrier or memory lower bound is asserted.

The old13-column gate certificate does not establish action on the ambient complement. A sufficient full-gate condition remains im(T-I) subset S, or the exact documented reflection decomposition with normals in S and first-two-mode coordinate operations. The actual installed FixedRotor source could not be extracted in this turn. One GitHub symbol search and a REST code search returned no matches; the latter explicitly reported incomplete_results=true. This is NOT evidence that source does not exist. No unsupported numerical replacement was used.

## 7. Provenance, antecedents and continuation

The exact prior RP12 note and complete RP11 certificate are the scientific sources. The quantizer semantics are those recorded in RP11-CLOSED/RP3 and the prior RP12 note. BRC-only and residual-faithful constraints were read at the declared snapshots; this is a typed integer/linear identity derivation, not new non-BRC simulation or a change in P000.

External antecedents were read at official abstract/metadata scope only: Nijholt/Sieben/Swift, arXiv:2206.00094v2; Neuberger/Sieben/Swift, arXiv:2411.10904v2. Equal/opposite-coordinate (polydiagonal) invariant subspaces are prior art. Their network/matrix results are not asserted to prove this specific common-bit-length Q16 hull theorem. No full-text novelty-completeness review or worldwide-first claim is made.

Current control status request status-rp12-qhull-c971348e-20260928-01, private issue2563, returned matching SUCCEEDED/0.6.8 as transport only. Request SHA256 c8b744897d1b3011c8ece22c43d8e7e9a046b556f7b8d35e58c5e6473c33550a. The existing logical conversation and original start binding remain chat-stage101-c971348e64294a5882dfc50fcc8217f1 / stage101-session-c971348e-02. research_authority_granted=false; no new session, RA, CLAIM, run or formal Result is asserted. Native admission, durable publication and Drive mirroring are separate facts.

Next executable unit: obtain the exact full gate source or an authenticated complete carrier-action packet; bind H19/H18 intertwiners and the denominator/sign convention; implement the same-target19 quotient and the separately named full-scale18 repair; compare decoded full rows/tapes for the exact path and full probability/bit/cost records for the changed target. The new19 lower bound should not be rerun as a numerical discovery; its synthetically anchored proof can be independently audited. Runtime results remain pending.
