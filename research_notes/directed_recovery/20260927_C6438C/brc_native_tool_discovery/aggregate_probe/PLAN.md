# Division-free aggregate factor probes: bounded execution plan

Status: CODE_PREPARATION_ONLY / NOT_EXECUTED / NOT_ADMITTED. The drafting agent may syntax-compile this source but does not import the scientific modules or run it. The coordinator supplies the current verified post-HBW activity guard and performs any later scientific execution. No earlier activity-record SHA is hardcoded as a new startup requirement.

## Fixed scientific contract

Inputs, frozen before this execution: `(N,a,t)=(437,2,1),(35,2,2),(19,2,1),(25,2,1)`. The algorithm receives only those integers. No expected factor, order, result classification or predicted residue is supplied to the arithmetic or classification functions. These are targeted finite fixtures, not random trials or evidence of a general success rate.

This is a new, unstopped certificate probe. It does not simulate the previous first-hit law and never absorbs the aggregate evolution on finding a factor. For `Q=2^t`, retain four residue registers `A=a^Q`, `G=G_Q(a)`, `H=G_Q(a^2)`, `q=Q mod N`. Initialize `(a,1,1,1)`. Every doubling uses the old A:

`A'=A^2`, `G'=G(1+A)`, `H'=H(1+A^2)`, `q'=2q`, all modulo N.

At the final horizon compute `D_minus=qH-G^2`, `D_plus=qH+G^2`, and `C_tilde=D_minus*D_plus`. Pay for and record all three gcds. Classify them from their computed gcd values only: UNIT, PROPER_FACTOR or SATURATED. Every proper factor has the existing typed division receipt. A unit result says only that this probe did not factor N; saturation is not a factor or an emptiness proof. No predicted outcomes are asserted.

The derivation is frozen in `AGGREGATE_WITNESS_PROBE_AUDIT.md`, SHA256 `c76465057ce793825916c3d22c85acc83703becfeb5154c05b362468dd5933fd`. It proves that the original unnormalized determinant `C=M0*M2-M1^2` equals `a^[-2(Q-1)] C_tilde`, so unit a implies exactly equal gcds. The aggregate production/readout uses no modular inverse and no order, full orbit or factorization input. Integer microscopic branch multiplicities are retained algebraically; q is their public-horizon parameter reduced modulo N. Metadata records Q symbolically as `2^t` rather than using untyped host scientific exponentiation.

## Native execution and accounting

Use the frozen `native_relative_port.Route` and actual typed `Arithmetic` for every scientific addition, subtraction, multiplication, modular reduction and gcd. Reuse only the standard-library `Work`, arithmetic wiring wrappers, setup and cost serializer from the frozen `hbw_marked_section.py`; do not call its run function. `Work` records a pending outer operation before entering the primitive. The original source binding verifies lazy arithmetic, gcd, histogram and native core dependencies. The unchanged full-adder catalog and every saved digit operation remain in the output evidence.

Each case has separate setup, production and readout Route ledgers. Setup pays the unit gcd of a. If that gcd is proper, record SETUP_FACTOR; if it is N, record NONUNIT_UNUSABLE. The inverse-free derivation applies only after gcd=1. The fixed fixtures are still classified by actual operations rather than supplied expected setup status.

Production retains every layer's old/new registers and operation links. It reuses the already paid A-square in H's multiplier. Readout computes all three probes even if an earlier probe already found a proper factor. It retains raw residues, gcd certificates and verified cofactors. Histogram evolution is not performed because this contract does not request it; no factor-probability statement is inferred.

## One additional paid validation, first case only

Only `(N,a,t)=(437,2,1)` receives an independent summary-level validation. It pays for a modular inverse b and the existing HBW regular setup `delta=a-b`, `k=a+b`, `M=[[0,1],[-1,k]]`. It checks regularity and the marked dual row `ell=(-b,1)`, including `ell M=a ell` and the initial marked value `L=ell(2,k)-delta=0`, through typed arithmetic.

In separate validation ledgers, propagate the original unstopped moments `(M0,M1,M2)` for one symmetric layer and the HBW marked moments `(h0,h1,h2)` for the affine alternatives

`L -> L` with multiplicity 2,

`L -> aL+delta(a-1)`, `L -> bL+delta(b-1)` with multiplicity 1 each.

This is a fixed three-moment contraction, not branch-state expansion. Starting from the single initial point, pay for and compare

`h0=M0`, `h1=delta(M1-M0)`, `h2=delta^2(M2-2M1+M0)`,

`h0*h2-h1^2=delta^2 C`, and `C=b^2 C_tilde` at Q=2.

Pay for the gcds of C and the marked determinant and compare them with the actual C_tilde gcd. These are summary-level identities and factor receipts, not a new independent raw-Cell simulation or proof that finite-field zero variance means support collapse. The HBW source is the already frozen marked companion/modular-observer implementation; raw Cell carries are not executed. The other three fixtures have no inverse/moment/HBW validation route.

## Evidence and execution lifecycle

Before any scientific import, require the supplied guard to allow this activity and persistence, have no sync debt, and match the explicit `--guard-record-sha256` argument. Record the full actual guard and its byte hash. Refuse any existing STARTED, successful result/summary or failure evidence, and exclusively create STARTED. A new current guard is an execution input, not a reason to rewrite the frozen science source or use the old guard.

Expected invocation, with the coordinator's real current values substituted:

`python -X utf8 aggregate_probe.py --guard-file CURRENT_GUARD_PATH --guard-record-sha256 ACTUAL_64_HEX_RECORD_SHA`

The source does not obtain the guard or perform remote writes. The draft preparation command is only `python -m py_compile aggregate_probe.py`.

Scientific failures preserve the available Work snapshot, route/digit records, native calls and incomplete outer wiring in `FAILED_EXECUTION.json.gz`. An unreturned primitive may not have appended its internal final record; this is not a promise of complete mid-operation recovery or resumability. A fallback plain-text failure file is attempted if serializing the richer failure evidence itself fails. Existing outputs are never overwritten.

Success writes `AGGREGATE_RESULTS.json.gz` and `AGGREGATE_SUMMARY.json`, with source/plan/guard bindings, all four inputs, complete registers, three classifications, validation identities, per-route costs, native calls and raw/compressed hashes. Source and guard bytes are checked again before success. A saved successful raw file remains preserved if a later summary write fails.

Frozen dependencies are the original `native_relative_port.py` (`0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8`), its original `EXPERIMENT_PLAN.md` (`931d7b7659c3e62707f10d20a2312cb03c945e6354f715c1ebda5d72fdb178a6`), the aggregate audit above, and `hbw_marked_section/hbw_marked_section.py` (`e2929468d9b430f9a0ef93a3412f132c692ce994c7b5061bece21a3960974851`). Earlier experiments are not rerun and their saved outcomes are not inputs to this classifier.

## Claim boundary and continuation

Digit counts include every recorded typed setup, production, readout and validation operation, including cached certificate construction once per relevant Route. Native catalog calls and digit replays are separate. General allocation, serialization and host control work are not a complete modeled runtime bill. No scaling, timing, random success-rate or general factorization claim follows from this small grid.

The purpose is to verify a cheap, lawful native factor-certificate interface and its HBW marked-section interpretation. Unknown-factor hit guarantees, repetition strategy, saturation recovery and total cost remain open. If the Shor endpoint demands an order, a valid order certificate is still required. Any authorized conversation can continue from the frozen sources and actual durable evidence; no particular host/persona is a research prerequisite. When execution is unavailable, further symbolic selection-law research can proceed without misreporting an execution result.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1
