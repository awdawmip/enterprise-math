# Stage130 execution evidence and declared limits

This is **author-side local execution evidence** from one finite auxiliary iid N=14 Stage130 research unit. It is **not** a GitHub-hosted execution, independent Research Driver review, native CLAIM, native Result or P000/X6 theorem.

## Exact inputs and range

P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6); horizon14, all ordered histories. K=522693/802; L=244736/401. All calculations use Python stdlib fractions.Fraction, exact integer powers and finite DFS. No floating point estimates, empirical sampling, formal proof assistant, or physical calibration.

### Local commands that were actually run

```shell
python CHECKER_STAGE130.py
python INDEPENDENT_ORDERED_STAGE130.py
python SCAN_STAGE131.py
```

All three returned normally. Local outputs contained, respectively:

```
PASS STAGE130 PRIMARY
PASS STAGE130 INDEPENDENT INTEGER WORD DFS
PASS STAGE131 DUAL CANDIDATE
```

The two Stage130 programs were independently implemented by the same research author (not independent peer review). The first performs bottom-up 680-state Bellman and exact rational four-moment recursions; the second performs top-down Bellman and full literal ordered-word integer-product enumeration.

Exact Bellman stats: states=680; positive nonchosen gaps=1238; negative gaps=0; minimum strictly positive gap=517/28872; ties exactly B=(11,0,1) Q/C and T=(14,7,4) P/Q. Root=52838467869186182216021/117157274574869495808.

Actual first-hit ordered prefixes under B continue, T choose Q:

- B: 11 literal histories, P=107421875/1451188224, Q=107421875/725594112;
- T: 7593 literal histories, P=316375/50096498540544, Q=316375/53496602689536.

Four deterministic policy corners (w,v)=(0,0),(0,1),(1,0),(1,1) have exact prefix visit totals, respectively, **775522,775522,775390,775390**, and completed ordered histories **517015,517015,516927,516927**. Each of the four observer vectors is recorded verbatim in `certificate130.json`. The DFS and moment recursion agree exactly on all four, including the vanishing mixed difference.

Full-real endpoints agree with algebraic checker:

- alpha129=36696744060534746695/105616844785075617792;
- alpha130=36696744084893090695/105616844785075617792;
- V130=660257040358974188827/52808422392537808896;
- balanced randomization at v=1: w=23520936469043837/81438720000000000;
- tP-tQ positive at both endpoints.

The third code scanner proves only a **dual candidate** for Stage131: K131=3787884/5905, L131=3551272/5905, additional tie A=(12,7,3) P/C and retained B Q/C; 1238 strict positive gaps, min=13530313/2204029440. Stage131 primal proof is *not* claimed.

## Local versus remote source integrity

The following locally executed source Git blob SHA-1 values were checked against an immutable GitHub readback at commit `9e6c53848f361c461d45971e0921489945b1e33b`; all three match **exactly**, not merely by filename:

- `CHECKER_STAGE130.py`: dc4e15f64161dc5dbdb03f219f753324de3f3349;
- `INDEPENDENT_ORDERED_STAGE130.py`: 7a74f3c62f7da7a06659569eed04bed7bbe5fea3;
- `SCAN_STAGE131.py`: 426d31463b2698e7414b6c8913a602e2c6949292.

The published mathematical proof and machine certificate were also nonempty in immutable readback. The remote certificate was checked for its theorem endpoints and four exact corners. **Publication and readback are storage verification only.**

A local ZIP of the *expanded* proof, both actually executed programs, Stage131 scanner, raw output files, complete integer DFS evidence and SHA256 manifest was constructed and re-opened. Local archive name: `EM_R5_N14_STAGE130_EXACT_AFFINE_20261026.zip`, size=14559 bytes, SHA256=`f1a642ad8dfa94bd219d77a03885c9afe08ae18382bc16e9f9bbd21ca1ceb78b`. This archive exists in the research runtime; a GitHub link to it is **not** asserted unless explicitly uploaded separately.

## Authority and scientific limits

Fixed input GLOBAL_KNOWLEDGE_V1 main@363cc21deb56c429a3d1304e62bde6fd4c35452e, locked P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, verified Stage129 Source commit 6e879a2644d66fe73e03ebc178ee852d3416b3bf. GitHub actor was awdawmip. Native task inventory: `CONTROL_QUOTA`. Native Researcher session creation: `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. Therefore active native owner, winner CLAIM, Result publication and independent Driver review are unverified. No alternative Drive upload was used to bypass a native safety/permission restriction.

The only proved target is the declared **finite external iid sequential-test model** with unrestricted ordered-history policies. A mapping to the native P000, X6, Heartbeat state/observer, residual or temporal dynamics has not been built, and no native theorem promotion is claimed.
