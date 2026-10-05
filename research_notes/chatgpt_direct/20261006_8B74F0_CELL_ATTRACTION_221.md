# 2×2×1: integer alignment does not force zero local response

Progress-Event-ID: EM-20261006-8B74F0-CELL-ATTRACTION-221
Status: PROVISIONAL_CANDIDATE_RESPONSE_MODEL / EXACT_BRC_CERTIFICATE / NOT_FORMALLY_ADMITTED
Global read snapshot: awdawmip/chatgpt-global-knowledge@9dfc309c47abf2c5c92734fab30f3e0f4bcef009.
Science Source snapshot: awdawmip/enterprise-math@fb325f11e26e6438f442312fd872c409b07f6c8c.
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0 (not platform-attested).
Own registered activity: RA-4089E16DFC891948C818A9B5; Researcher EM-DIRECT-091714; session MCP-c5a1b611a4d944d5a6062c3a1149cc2a.
Activity directly read back at 850b3ec12acc0255455904e04fac465885894652, research_activity_records/RA-4089E16DFC891948C818A9B5.json, blob 4e403c3fb15096f00a105a405f1898c04f19aee4. Registration grants no CLAIM, execution, review, or mathematical acceptance.

## User correction and scope

The user rejects n-floor(sqrt(n))^2 and square-shell/sieve reformulations for this question. Squares must not be assumed perfect geometric/energy landing points. Test the whole 2*2*1 using attractive Cell response and force-dependent positioning. Arithmetic 2*2*1=4 is unchanged; it does not determine a full joint configuration or force residue.

Existing Heartbeat contracts require joint material/field/boundary consistency, force inputs versus position outputs, and separation of structural and numerical residue. No settled specific attraction law was located in the targeted retrieval. The law below is therefore an explicitly NEW CANDIDATE constitutive choice, not a recovered old law, not a P000 consequence, and not established physics. This calculates the field and an effective directional drive at a declared initial configuration, NOT the final material position or a complete material heartbeat.

## X6 joint state and actual BRC law

Use all six native axes and twelve signed nearest-neighbor graph steps. Four labelled unit sources coexist at A=c, B=c+e1, C=c+e2, D=c+e1+e2. This is the declared 2-by-2-by-1 preparation inside X6, not an independent native plane or a claim that (2,2,1) is a displacement. Fixed coordinates restrict this source preparation only: response paths still use ALL six axes. Chart-relative signed displacements do not replace the final address codec.

Let mu be the sum of these four labelled unit sources. Choose 0<lambda<1/12, a decaying boundary at infinity, and

    chi = mu + lambda A_X chi,
    G(x) = sum_{ell>=0} N_ell(x) lambda^ell,
    chi(x) = sum_b G(x-z_b).

A_X sums twelve neighbors; N_ell counts ordered paths. Each path is a positive BRC response with weight lambda^ell, including loops and backtracks. Response weights are NOT physical mass, probability, energy or signed amplitude. Depth is not time or heartbeat count.

Define the CANDIDATE effective drive observer

    F[a,j] = lambda*(chi_without_a(z_a+e_j)-chi_without_a(z_a-e_j)).

The extra lambda is an actual BRC probe-return edge. Positive and negative ports retain separate positive CWM responses; only the final directional observer subtracts their total responses. Own-source contributions are symmetric and cancel only in this observer. This is not primitive native force, a two-force stability claim, or a supplied native triadic closure.

## Conditional theorem and proof

The four complete labelled effective drives are

    F_A=( f, f,0,0,0,0); F_B=(-f, f,0,0,0,0);
    F_C=( f,-f,0,0,0,0); F_D=(-f,-f,0,0,0,0),
    f=lambda*h(lambda),
    h=G(0)+G(e2)-G(2e1)-G(2e1+e2).

Reflect coordinate 1 after a path first reaches coordinate 1. This weight- and length-preserving bijection pairs paths ending 2e1 with paths ending 0 that hit coordinate 1, and paths ending 2e1+e2 with paths ending e2 that hit it. Thus h is EXACTLY the positive response of paths ending 0 or e2 that never have first coordinate positive. It contains the empty path and the one-step e2 path. Therefore

    h>=1+lambda>0, and f>0 for EVERY 0<lambda<1/12.

This is a graph-path reflection certificate, not a new native plane. Positive branch mass has not been treated as signed physical mass. All four sources have integer Cell addresses, and sum_a F_a=0, yet the labelled local-drive tuple is nonzero. Net observer cancellation is not complete-state erasure or local zero drive.

Actual first nine h coefficients are [1,1,11,30,332,1370,15255,80010,896364]. For lambda=1/48, retaining depths 0..8 gives

    803068977083/37572373905408 <= f <= 803072958395/37572373905408.

The exact interval width is 1/9437184. Positivity gives a lower approximation; the omitted paths are a subset of all twelve-branch paths. The actually executed one_state_recurrent_cwm([lambda]*12) yields the tail certificate

    0<=f-f8<=lambda*(12*lambda)^9/(1-12*lambda)=1/9437184.

The interval is an uncalibrated MODEL RESPONSE, NOT a material displacement. The positive drive and the truncation tail are different residual types.

## Further consequences and limitations

For m>=1 and v_j=0, reflection after first hitting coordinate m proves

    G((m-1)e_j+v)-G((m+1)e_j+v)>0.

An exposed minimum-coordinate component of any finite positive-source aggregate with nonzero span along j consequently has strictly inward drive. Thus this pure-attraction model does NOT single out squares, composites or primes; it fails to supply an unconstrained noncollapsed all-local-drives-zero aggregate. Occupancy/contact/exclusion, material constraints and native triadic response are genuinely needed to ask for a final material state. This is not a force-derived motion solution, stability proof or prime criterion.

Colocating four labelled sources gives zero coarse drive by symmetry, provided co-occupancy is considered; this does not establish its physical admissibility or full-state zero residue. Same total count4 is insufficient to determine the observer.

The full four-point response field cannot equal that of 4 delta_z at any single Cell: applying I-lambda A_X would imply equality of the distinct source measures. Reducing the joint configuration to a scalar4 or net-zero observer loses future field queries. This is a scoped injectivity result, not an unrestricted compression claim.

Integer occupation with stress is distinct from off-Cell position. The present proof establishes neither inevitable off-Cell landing nor nonzero residue for every possible square configuration. A Heartbeat may have nonzero acceleration; stationarity is a separately chosen question.

## Actual execution, reuse and provenance

Unchanged source: src/enterprise_math/brc_weighted.py, Git blob 3f205696709e847909958a153f8fe10d3f6b70f0, 9635 bytes, SHA256 4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f. Complete fetched bytes were Git-blob verified. AST loading removes only unused relative imports brc_logarithm and exact_arithmetic; CWM/closure function bodies are unchanged, and no log functions are called.

Branch carrier retains source, ordered steps, depth and signed observation port. Aggregation by source/depth/endpoint/killed-policy is safe for the declared homogeneous history-blind future extensions because outgoing transfer depends only on endpoint and CWM propagation distributes over recoalescence. Source labels and signed ports remain available. This does not license history-dependent, phase-sensitive or general physical reductions.

Final executed assertions: 202998. Actual core calls: cwm_edge=3, one_state_recurrent_cwm=1, cwm_propagate=498438, cwm_recoalesce=528515. Checks include all depth0..8 endpoint CWM states, realizability, unrestricted scalar closure, killed-domain states, reflection coefficient identities, four-source drive pattern, net zero, same-count colocated comparison, and 68 explicit path reflections with per-edge BRC weight replay. They are checks of one implementation, not independent experiments. Earlier development runs are not independent replication.

Conversation archive files:
- check_model.py: 11680 bytes; SHA256 26fb24e816f3e98efd539c255fbf6427e2988455a47fade0b3f47443af426091.
- evidence/results.json: 20768 bytes; SHA256 0a101891e1f702c04d7492d4f8e334b8b767bb90a584f6d9bfd33c20e04910f3.
- evidence/run_log.txt: 473 bytes; SHA256 07971040dd47b389fbfe49ab52d1c37be03513b6b6921294e6a7155d28e702a5.
Run python check_model.py with the byte-pinned source in sources/. No classical pi, square-root, trigonometric, matrix-exponential or reference-solver run was used. This Source note preserves the theorem/proof/validation frontier; the full execution archive is delivered in the conversation, not claimed uploaded here.

General adjacency-path/Green-function methods have prior art: A.J. Guttmann, Lattice Green functions in all dimensions, arXiv:1004.1435 (2010); only its abstract was read for general attribution. No literature-wide novelty claim.

This is same-author direct continuation, not independent review. Earlier contribution file_00000000a010820b8411c84d1797a06f was disclosed in registration. Neither a formal Task/CLAIM nor a Driver review was performed. The RA is verified but its checkpoint array was empty at readback; this note does not pretend the control registry has linked this scientific checkpoint.

Next scientific unit: specify an admissible non-primality-tuned occupancy/material/triadic BRC closure and derive joint successor positions rather than prescribing final positions. Preserve this positive-path proof and the full-field noncollapse certificate; do not redo square-shell screening.
