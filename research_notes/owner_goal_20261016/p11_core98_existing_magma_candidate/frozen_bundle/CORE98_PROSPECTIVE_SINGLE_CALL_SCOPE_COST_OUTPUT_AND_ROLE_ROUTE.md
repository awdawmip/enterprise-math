# Fixed core (9,8): prospective one-shot existing-Magma experiment

Author and code proposer EM-DVR-F73673. Status: frozen LOCAL CANDIDATE for actual independent static review. No scientific script, wrapper, import, compilation, test, point search, FourDescent or pairing has been run. This is not a new Task publication or scientific authorization. The old fixed233 Task remains stopped with zero remaining preparation/invocation budget. All proposed work here concerns a different exact curve and the genuinely unknown higher mixed bit.

## Frozen executable inputs and interpretation

The Magma file core98_one_mixed_candidate.m is a fixed consumer of the existing TwoCover, FourDescent and mixed CasselsTatePairing APIs. It uses E=[0,-42050,0,418079809,0], P=161,Q=127, cubic roots in the order (0,25921,16129), d2=2-L0,d3=3-2L0 in the split cubic algebra. The elementary CRT proof fixes the two classes as U2 and U3. Actual all-place Selmer membership, full first-form zero, surjectivity of Sel4 to Sel2, and conditional interpretation are inherited only from their exact separately reviewed papers.

It requests exactly one ordinary FourDescent above U3, retains every local/real condition, selects the first returned valid lift and makes exactly one mixed evaluation against U2. It does not recompute abstract Sel4 or full Sel2, loop over parameters, search for points separately, call EightDescent or fall back to a different method. Internal work necessary to these existing routines remains part of the one invocation.

Required inherited mathematical Sources:
- 4090e063926e770103afc4628ea40c8a8949cedb, core98 full Sel2 and first form zero.
- a427759fc3dffd69c3d90ccf8440b6af8acf9e2a, abstract lift structure.
- a29ad230bfd4a94e305b9cdb4d3b046d7dcb88e6, precise conditional e=1 theorem and zero STOP.
- 5c9012200d6c271678416047a691da9d90deda20 / peer d6c4d3888165fb20b4de353977f858479a571c78, Fisher one-T0 bridge.
- 44488423c175820ccd07c6aa92509c97e7c08140, explicit U3 quartic plus conditional U2 readout; their two genuine 7CDA paper assessments are later distinct bindings, not automatic code approval.
- The separately frozen 9118B exact-Magma/CRT note and its genuine BFF6DC paper review; actual author Source is still pending at this candidate freeze. Its historical runtime-UNKNOWN text is not rewritten by the later actual service probe.

The direct exact API is official Handbook text/1570 (V2.29 footer): https://magma.maths.usyd.edu.au/magma/handbook/text/1570 .
The existing mixed evaluator takes a quadric intersection and a hyperelliptic two-cover of the same E/Q, both everywhere locally soluble, and returns an integer bit. Neither API description nor a nonzero norm proves these hypotheses. The full fixed papers supply the class-level hypotheses, while actual generated models/maps remain evidence to bind.

## Actual runtime availability and costs

A single CONTROL-only metadata request to the official XML endpoint really returned V2.29-10, GetMemoryLimit=400000000, GetNthreads=1, with matching nonce/end. Its full 381B response SHA256 is 2bb65d0b6a4a0a96dbc89112480b7ccf92582242ba241444fa07aeb6c2ad79c6. This queried version/settings only; it did not consume a scientific invocation or construct any mathematical object. The metadata binding lives at higher_descent_reference_intake/OFFICIAL_MAGMA_SERVICE_TRUE_METADATA_BINDING_AND_LIMITS.json.

The provider advertises and returned max_time=60 seconds and max_input=50000 bytes. It does not distinguish CPU from wall time in this field. The 400000000-byte setting bounds the Magma allocator, not proven total host RSS. This is a vendor service/version binding, not a local binary hash.

Proposed prospective caps for a NEW explicitly scoped execution unit:
1. One scientific POST, serial concurrency1, provider time cap60s, Magma allocator limit400000000 bytes and one thread. The script checks the exact version, allocator setting and thread count before mathematics. Version/settings mismatch stops the same invocation before curve construction.
2. Caller absolute wall90s, address space536870912 bytes and CPU20s. Raw response at most1048576 bytes; URLencoded source at most50000 bytes; parsed evidence sidecar at most2500000 bytes; invocation evidence at most4194304 bytes. No complete output means UNKNOWN.
3. Proposed author preparation cap1200s, to be explicitly approved in the new taskbook, not an extension/reset of fixed233. All future author mathematical/code/input/codec reading/design/editing and unclassified intervals are charged with one monotonic ledger. Before START, establish any execution-specific work the selected actor already performed and debit it conservatively; unknown unaccounted preparation means NO_START. Frozen reusable Driver papers/code are named inputs, not a claim that this actor performed no earlier work.
4. Static review and CONTROL publication time are recorded separately, never silently treated as zero actor mathematics. Owner may choose a different explicit prospective cap before publication; this candidate grants no cap or start itself.

The V2 Python wrapper is frozen separately from the original8145B V1. V2 preserves HTTP rejection bodies and loads the exact Magma source relative to the bundle. V1 remains unchanged and was never imported/executed. The input V1 also remains unchanged. Neither revision was tested or sent to the service.

The wrapper encodes one input field, creates an exclusive durable original-attempt marker BEFORE its sole POST, keeps complete raw XML and headers, parses lines without dropping warnings, and never retries. A lost response, local deadline or interruption consumes the permitted attempt conservatively: UNKNOWN/NO_RESUBMISSION, even if it is unclear whether the server received or completed it. The UI Cancel is not a server kill; it must not be used as a claimed termination guarantee. The caller deadline is separate from the provider's stated limit.

## What must be exported, and what would still be UNKNOWN

The script prints the exact E, root-labelled cubic and d2/d3 polynomials; the actual two-cover models/maps; selected four-cover equations and symmetric matrices; its associated two-cover and returned map; the map to exact E; attempted polynomial map exports with individual actual flags; existing verbose output; one candidate bit; final settings; and a distinct final marker.

Some existing Map objects may print only an implementation rule or fail polynomial-equation export. Such output is retained as UNKNOWN, not replaced with invented equations. The wrapper's complete/version-bound candidate state is implementation evidence pending real review. It never asserts mathematical acceptance, Native completion or a complete portable certificate.

A portable pairing certificate additionally needs an actual cover/map identification above U3, local-solubility certificates at every necessary place, correct pushout/divisor data or a separately justified auditable implementation, and complete local support/readout or equivalent independently adequate evidence. No current public Handbook claim establishes that verbose output automatically exports these data. The new simple Hilbert formula still requires its real f, admissible local points and support.

e=1 can imply rank0 and Sha[2∞]=C4² only after the actual implementation/certificate has been bound and accepted at its true evidential strength by a genuine independent Driver. A raw printed1 is not that acceptance. e=0 stops this test and leaves rank in0..2; another lift/table/algorithm is not silently authorized. Empty lifts contradict the retained exact image hypotheses if they were computed correctly, so they trigger input/implementation integrity STOP rather than a fresh rank conclusion. Exceptions, warning-dependent assumptions, skipped local tests, incorrect model labels, oversized/truncated output, incomplete end marker or unverifiable version leave UNKNOWN.

## Exact role and Native route

The four project role contracts were freshly read as complete immutable bytes at Source44488423c175820ccd07c6aa92509c97e7c08140, retained under actual_policy with full raw responses. The current MCP README and ordinary-control/continuation protocols were read at server-repository Source228c94e37d707f1ab86ee404ee5eaf9adb6c5fec.

The role matrix explicitly permits RESEARCH_DRIVER -> TASK_RESEARCH by a typed transition, clearing Driver authority and resolving the genuine Researcher identity. It does not make a Driver verdict a research execution grant. Research Tasks require an actual Researcher session with native RA; Governance Tasks use actual Drivers with DA.

Recommended minimal route is to use a genuinely available current Researcher actor, retaining its own stable conversation, Source RA, prior work and NONBLIND contributions. The exact new taskbook and immutable V2 record must be canonically prepared/audited and atomically published before that actor can obtain execution authority. Existing new-task Native route is:
own successful task/continuation read -> prepare_exact(task_request_id) for a genuinely fresh no-prior-claim Task -> winning claim(prepare_request_id) -> open(claim_request_id) -> actual own run/generation/ER and full Source gate -> one admitted scientific invocation.
A prior owner/progress would instead require the typed actual continuation route, not fabricated fresh inputs. There is no old fixed233 claim/run reuse.

If this actual F73673 conversation is selected to execute instead, the service permits only one unclosed session per conversation: it must first durably hand off Driver responsibility and lawfully close the existing Driver session, then register its own RESEARCHER/TASK_RESEARCH session under the SAME real stable logical conversation with all contribution IDs and exposures, and obtain its native RA/prepare/claim/open. A close is not assumed possible: the ordinary protocol rejects pending requests, active claims or unpublished uploads, so the preserved old V1 staging history must be inspected through actual own status/typed recovery before deciding that path. No synthetic conversation or ID may evade those conditions. Current F73673 Driver/DA remain active because no transition or close has been requested.

The independent static code/input/codec/complete-cost gate blocks scientific invocation; it does not invent a requirement to have final code before lawful registration, task reading, prepare/claim/open. The wrapper's admission fields only bind recorded evidence; they cannot manufacture Native authority. No user reconfirmation is required by these contracts for the already authorized reversible preparation; Root coordinates actual Source windows and the true execution actor.

## Concrete next action

Independently preaudit this exact candidate bundle and its full output/evidence limits. Bind any findings by a new explicit version preserving these original files. Then finalize one new core98 task publication with true semantic lineage/Goal/current duplicate-owner checks, prospective clock/debit and exact service scope, and let the actual lawful Researcher claim/open it. The decisive reviewer must be a genuine nonauthor; F73673 authored these papers/code/plan and cannot vote its own Result. Until these concrete gates and source pins exist, current scientific state is NO_START and actual c3,f,e,rank remain UNKNOWN.

