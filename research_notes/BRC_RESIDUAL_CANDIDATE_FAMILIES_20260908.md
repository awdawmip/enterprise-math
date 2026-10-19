# BRC: fixed square corrections to separate D and U residuals

Researcher-ID: EM-HME-0CE4FD / TASK_RESEARCH  
Global-Knowledge-Sync: main@e5a0861 / GLOBAL_KNOWLEDGE_V1  
Canonical snapshot: e5a086173024bde6e59782df4c68427bbe24e3ef  
Project parent: a93a0a74d2aefea45ef27954fdab34895230e076

Three additional candidate branches extend the preceding center-difference study: D uses a small square added to its downward remainder, U uses a small square removed from its completion gap, and either state can first remove a fixed odd coefficient. Each branch has a constructive positive family. Its query constructs candidates from N and a fixed table, without the construction parameters p, q or the factor-ratio parameter a.

The prescribed experiment contains 124 positive constructed composites, with 62 D states and 62 U states. The complete coefficient packet succeeds on all 124. In this same positive corpus, 90 have center gcd equal to 1; coefficient removal adds 67 successes beyond the unit-coefficient packet. These are coverage distinctions on prescribed positive families, not population hit rates or public RSA results.

No public input is queried in this checkpoint. The earlier public-position count remains 312, with its previously recorded outcomes unchanged. No multiplier positions, adaptive horizon, factor enumeration or fallback are added.

## Coordinates and three branches

For odd nonsquare N greater than 2, retain

\[
J=\lfloor\sqrt N\rfloor,\qquad R=N-J^2,\qquad A=(J+1)^2-N.
\]

D means R is at most J; U means R is greater than J. The following fixed packet uses b in {1,3,5,7}, D offsets c in {1,2,3}, and U offsets c in {2,3,4}.

| Branch | Candidate h | Admission |
| --- | --- | --- |
| D square correction | R+c^2 | 1<h<N and h divides N |
| U square correction | A-c^2 | 1<h<N and h divides N |
| Fixed odd coefficient removal | (R+c^2)/b in D; (A-c^2)/b in U | The numerator is divisible by b, then the same proper-factor check |

The third branch uses b=3,5,7; b=1 is the first two branches. Every returned factor receives exact divmod and product verification. These are occasional sufficient candidate branches; exhausting the fixed packet does not establish primality or the absence of factors.

There are twelve (b,c) pairs per state. Odd N requires odd h, and b is odd, so even corrected numerators are rejected exactly. Among each state's three offsets, at most two survive this parity check. Therefore at most eight candidates reach a possible full N division; nonintegral quotients are discarded earlier. No table enlargement follows a miss.

The construction stage of a prepared D query receives R and the D label; its U counterpart receives A and the U label. It does not read J or the other residual. N is still required for factor verification. A complete N-only call pays for the native integer root, residual preparation and state classification. A supplied state label is not claimed to follow from a single residual alone.

## Positive families, without a ratio search

Let b be a positive odd integer, a an even integer with a>b, c a positive integer, and p an odd integer greater than c^2. Primality is not assumed. Consider two separate constructions:

\[
N_D=p(a^2p+2ac+b),\qquad N_U=p(a^2p+2ac-b).
\]

For D, write x=ap+c. Then

\[
N_D=x^2+(bp-c^2).
\]

The remainder is positive. Since a>b,

\[
bp-c^2\le ap+c=x.
\]

Consequently x is the exact floor root, the state is D, and

\[
\boxed{J=ap+c,\qquad R=bp-c^2,\qquad (R+c^2)/b=p.}
\]

For U, write y=ap+c. Here

\[
N_U=y^2-(bp+c^2).
\]

Because (a-b)p>c^2-c, the positive completion gap is strictly less than y. Thus y is the exact ceiling root, the state is U, and

\[
\boxed{J+1=ap+c,\qquad A=bp+c^2,\qquad (A-c^2)/b=p.}
\]

Both cofactors are odd and greater than one, so p is a proper divisor in each family. These statements hold for every even a>b. The query never estimates or enumerates a: only the fixed small b,c values are used. The actual prescribed checks choose a=b+1; the general a statement follows from the inequalities above, not a finite enumeration.

This is a derivation from elementary integer product identities within the existing BRC coordinate family. No claim of a new general factoring complexity result or independent globally novel algorithm family is made. Classical square-based factoring context is described in the authors' [Handbook of Applied Cryptography, Chapter 3](https://cacr.uwaterloo.ca/hac/about/chap3.pdf); it does not establish these measured costs or their applicability rate.

## Optional root gate and its information boundary

There is also a sufficient short-remainder gate. In D set E=J and in U set E=J+1. For a candidate h formed above,

\[
N=(E-c)(E+c)+bh\quad\text{in D},
\]

\[
N=(E-c)(E+c)-bh\quad\text{in U}.
\]

Therefore

\[
E\bmod h\in\{c\bmod h,\ -c\bmod h\}\quad\Longrightarrow\quad h\mid N.
\]

This gate reads a root endpoint, so it is explicitly a different prepared observer from the single-residual route. It saves full N divisions on candidates rejected by a smaller-operand remainder, while still paying for divmod and product verification on an admission. The complete query includes preparation of that endpoint.

For composite h the gate is sufficient and may omit a divisor whose prime-power components split between E-c and E+c. It is not an equivalent rewrite of direct divisibility for all candidates. Both variants find a proper factor on all 124 prescribed cases, but their first returned factors are identical on only 99 cases. The other 25 pairs contain two valid certificates. Timings are reported as the cost of finding some proper factor on this cohort, not equal-value comparisons or universal route dominance.

## Fixed examples and executed checks

The main family consists of 24 prescribed (state,b,c) combinations at five p sizes: p=127 and p=2^e-19 for e in {127,511,1023,4095}. The cofactor always comes from the displayed formula with a=b+1. This gives 120 constructed composites. They are not asserted to be semiprimes.

Four additional examples have explicitly prescribed p values and receive the existing exact small-prime checker. Both factors in each row pass that bounded checker:

| State | N | J | Selected residual | Candidate | Verified prime pair |
| --- | ---: | ---: | --- | --- | --- |
| D | 583 | 24 | R=7 | R+2^2=11 | 11 times 53 |
| U | 767 | 27 | A=17 | A-2^2=13 | 13 times 59 |
| D | 4811 | 69 | R=50 | (R+1)/3=17 | 17 times 283 |
| U | 6023 | 77 | A=61 | (A-4)/3=19 | 19 times 317 |

The preceding full center gcd, gcd(N,abs(J-R)), equals 1 in all four examples. This demonstrates new positive coverage relative to that particular branch; it is not a comparison against the entire library of classical methods.

Across the complete prescribed corpus:

| Observation | D | U | Total |
| --- | ---: | ---: | ---: |
| Constructed positive cases | 62 | 62 | 124 |
| Unit-coefficient packet hits | 28 | 29 | 57 |
| Complete coefficient packet hits | 62 | 62 | 124 |
| Positives whose prior center gcd is 1 | 35 | 55 | 90 |

The 67 additional coefficient successes are within these same 124 cases. Neither those successes nor the four small prime-pair checks support an infinite prime-pair claim, a random-semiprime hit-rate estimate, or a public RSA success claim.

All executed floor/ceiling inequalities, D/U labels, corrected-residual identities, assigned factors, returned products, parity bounds and complete/prepared representation checks pass. AST parsing passes. No production source or production test is changed. The earlier 46-test result remains historical validation of the unchanged native-root change and is not represented as a fresh test run here.

## Costs and replay contract

The experiment uses nine rotated paired rounds, four repetitions per timed batch, and four variants: complete residual, complete root-gated, prepared residual, and prepared root-gated. Complete calls receive N alone and include exact root preparation, both residuals, D/U selection, fixed candidate construction, small-coefficient division and factor verification. Source checks, fixture construction, primality checks, imports, warmups and output serialization are outside query timers.

The following ranges are the minimum and maximum per-case median costs within the named positive group, in microseconds. They are not worst-case guarantees:

| State and actual N bits | Cases | Complete residual | Complete root gate |
| --- | ---: | ---: | ---: |
| D, 1024-1028 | 12 | 5.825-11.225 | 6.075-9.900 |
| U, 1024-1028 | 12 | 6.100-14.375 | 6.475-10.325 |
| D, 2048-2052 | 12 | 11.000-21.900 | 11.875-16.775 |
| U, 2048-2052 | 12 | 11.500-22.675 | 12.650-17.525 |
| D, 8192-8196 | 12 | 90.775-195.350 | 100.225-122.075 |
| U, 8192-8196 | 12 | 89.200-190.625 | 106.375-119.325 |

Small prime-pair examples cost 1.825-2.475 microseconds through the complete residual route; the extra gate is slightly more expensive on those four cases. The root gate narrows the range of larger-case costs here, but it does not preserve every composite candidate or dominate every case. All raw timing arrays and per-case counters are retained in the certificate. Repetitions are cost replays, not new independent successes.

The cohort checks and timing loops took 0.6289711 seconds inside the measured local run. No public challenge arithmetic was run. This checkpoint consequently has no new public miss/hit timing and leaves the prior public observations unchanged.

## Reuse and durable evidence

The chosen carrier retains state, selected residual, fixed branch identity (b,c), returned factor certificate and source provenance. Unit and coefficient branches are alternative candidates; their results are not treated as independent modular information. State and branch labels survive aggregation in the certificate. The optional root endpoint is explicitly recorded when consumed. No hidden p+q moment or p,q input is used by a query.

The current local tool lookup is recorded in [the coverage packet](../experiments/brc_residual_shortcut_coverage_20260908.json). Resolution is COMPOSE_APPLIED within T0_BRC and an extension of the preceding root/residual audit. The exact native integer_nth_root implementation is REUSE_EXECUTED at core blob 2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07. The exact bounded prime helper is reused at blob 65f06c03038b2c95a875436c099f50f008700af3 for the four small pairs only.

The square-gap prefilter, neighbor-square lift and opportunistic-prefix interfaces are relevant existing families, but their squarehood/multiplier queries are not the present corrected-residual divisibility test. Their established identities and scope boundaries are retained; those APIs are not claimed to have been executed in this checkpoint. The broad lexical matches concerning Bellman closure, Morse complexes, incidence and finite symmetry are NOT_APPLICABLE to this scalar integer query. A lookup match alone is not counted as tool execution or a new capability theorem.

No new general-purpose production API, arbitrary-target command-line interface, task registration, Driver review, Foundation promotion or Working Truth status is created. This is direct TASK_RESEARCH provenance on the existing draft branch. The geometry/worldview contract is unchanged; all displayed derivations are ordinary integer arithmetic.

Companions:

- [Prescribed synthetic checker](../experiments/brc_residual_candidate_families_20260908.py)
- [124 certificates and raw measurements](../experiments/brc_residual_candidate_families_20260908.json)
- [Prior root-endpoint identities](BRC_ROOT_ENDPOINT_GCD_AUDIT_20260908.md)

The raw certificate's serialization was compacted after the arithmetic run. Parsing the compact encoding reproduces the complete original document exactly; no observations or timings were rerun or replaced by that packaging change.

The remaining mathematical question is how to choose additional useful fixed residue corrections from structure available in N, without enlarging a search after a miss. This checkpoint proves and verifies the displayed positive families; it does not answer their frequency on unstructured semiprimes.
