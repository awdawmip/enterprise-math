# RSA-270：BRC 关系层、special-q 边界与低成本路线收束

Progress-Event-ID: `rsa270-relation-layer-specialq-boundary-68d4a1`
At: `2026-09-06T08:51:09+08:00`
Scope: `enterprise-math / RSA-270 factor-blind factorization research`
Source: `ChatGPT project conversation / exact toy QS experiments / Enterprise Math factor-complexity artifacts / current public literature and GitHub search`
Kind: `HANDOFF`

## Event

Continued the RSA-270 parent objective after the shell/RNG routes were falsified or scale-limited. No RSA-270 factor was found.

### 1. Relation-level BRC is the correct semantic layer

The project-local factor-complexity audit was re-read. Existing PCF4/PCF7 results already close fixed finite N-independent gcd probe families as generic factoring routes and preserve the frontier of an N-dependent second observable. This motivated moving BRC from square-shell observables to smooth-relation valuation carriers.

For a quadratic-sieve relation `Q(x)=x^2-N`, the exact carrier retained prime valuations and relation provenance; parity was treated only as the dependency-detection observer. This obeys the BRC requirement that the mod-2 quotient not erase data needed to reconstruct the eventual square root.

On 30 generated approximately 41-bit semiprimes with adjacent factor bits and ratio near 2, a simple full-smooth-only QS was compared with a one-large-prime BRC interpretation: a partial relation with one large-prime boundary remained an open branch until another relation carrying the same large prime recoalesced, after which the large-prime valuation became even and the pair formed an effective full relation.

For the 29 cases where both full-only and passive one-large-prime variants factored within the common scan window:

- full-only first-factor candidate-index median: `3046`;
- one-large-prime first-factor candidate-index median: `1623`;
- median relative candidate-index reduction: `0.4682112069`;
- mean relative reduction: `0.4330324617`;
- one-large-prime earlier in `27/29`, equal in `2/29`, later in `0/29`.

One additional case factored only under the large-prime route within the 30,000-candidate window.

This is a useful BRC semantic calibration but NOT a new factoring method: it is the classical large-prime variant of QS/NFS.

### 2. Active recoalescence also maps to classical special-q

A further toy experiment did not passively wait for a second relation with the same large prime L. After observing a partial `Q(x)=L*smooth`, future candidates were targeted on the two residue classes `x' == +/-x (mod L)`, guaranteeing `L | Q(x')`, and the cofactor was tested for factor-base smoothness. Counting each targeted norm test as one relation test, on the same 30 toy semiprimes:

- passive large-prime median candidate tests: about `1637.5`;
- with 1 targeted candidate per residue progression: median tests `789.5`, median relative reduction `~0.4802`;
- with 2 targeted candidates: median tests `557`, median relative reduction `~0.6295`;
- with 4 targeted candidates: median tests `462`, median relative reduction `~0.7169`;
- targeted method beat the passive candidate-test count in `30/30` toy cases for each tested depth.

Prior-art audit immediately identifies this mechanism as Pollard lattice/special-q sieving: fix a prime q known to divide one norm and sieve a lattice of candidates whose norms remain divisible by q. CADO-NFS supports prime and composite special-q variants. Therefore the impressive finite toy gain is evidence that BRC has landed on the correct NFS relation-collection semantics, not evidence of a new asymptotic or practical RSA-270 shortcut.

The BRC correspondence is nevertheless exact and useful for future integration:

- partial relation = branch with open large-prime boundary;
- matching large prime / graph cycle = recoalescence;
- exact valuation vector = provenance-preserving carrier;
- parity vector = safe observer for dependency detection only;
- special-q lattice = active branch continuation conditioned on a retained boundary;
- multi-large-prime cycle graph / composite special-q = higher-order recoalescence already present in mature NFS practice.

### 3. Small-modulus construction scan found no third stable constraint

All 36 known prime factors of the 18 solved original decimal-labelled Challenge moduli were scanned for additional low-bit/small-modulus structure beyond the established binary prefix `11` and `p mod 3 = 2` constraints.

Tests included residue distributions modulo powers of two and small odd primes, plus pair-level same-residue relations. The smallest unadjusted signal in the examined family was the modulo-16 residue-distribution chi-square `p ~= 0.04052`; after Holm correction across the tested family it became approximately `0.7293`. The next pair-level signal, same residue modulo 13, had unadjusted `p ~= 0.05733` and adjusted `p ~= 0.9747`. No reliable third small-modulus construction constraint was found.

The documented `p,q == 2 (mod 3)` condition still implies the Fermat midpoint consequence `A^2-N=((q-p)/2)^2 == 0 (mod 9)`, but this is a derived rule and provides only standard quadratic-residue/Fermat sieve pruning, not independent factor information.

### 4. Additional cheap classical probes

Williams p+1 stage-1 was added to the earlier cheap-method audit. Ten Lucas parameters were tested to `B1=100,000`; five parameters were further tested to `B1=300,000`. All terminal gcds were 1 and no factor was found. Earlier stages had already tested low-million Pollard p-1, small ECM, bounded Fermat/Lehman-style windows, and second-layer square-endpoint scans without a factor.

### 5. RSA-260 method/code-leak search

Current web reporting still states that Eric Lu's RSA-260 algorithm, software, hardware and runtime are undisclosed; GNFS is presumed and Lu has publicly said there was 'no silver bullet'. Public GitHub code search for `RSA-260`, the modulus, the newly published factor, `penlume`, `cado`, and `nfs` found result mirrors, news ingestion, educational/independent factor attempts, and post-announcement experiments, but no authenticated Eric Lu parameter file, CADO job artifact, relation dataset, script, or method commit.

Status: `NO_RSA270_FACTOR / BRC_RELATION_LAYER_VALIDATED_AS_RIGHT_SEMANTIC_LAYER / LARGE_PRIME_AND_ACTIVE_RECOALESCENCE_MATCH_CLASSICAL_NFS_SPECIAL_Q / NO_THIRD_SMALL_MOD_CONSTRAINT / CHEAP_CLASSICAL_PROBES_NEGATIVE / RSA260_METHOD_STILL_UNDISCLOSED`.

## Artifacts

- Enterprise factor-blind no-go evidence: `research_artifacts/PRIME_COORD_FACTOR_BLIND_PADIC_GCD_BRIDGE_20260827/evidence.json`.
- Enterprise complexity frontier: `research_artifacts/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION/PCF7_COMPLEXITY_FAILURE_CERTIFICATE_V1.json`.
- Prior RSA-270 checkpoints:
  - `journal/enterprise-math/2026-09-06/20260906T083741+0800-rsa270-second-layer-rng-provenance-4c8e2d.md`
  - `journal/enterprise-math/2026-09-06/20260906T084423+0800-rsa270-rsaref-gap-falsifier-91e6b4.md`
- Toy QS/BRC and low-mod computations were conversation-local exact Python experiments; no Enterprise source artifact was created.

## Next

The current chat/runtime cannot mount the multi-thousand-core-year GNFS-scale relation collection required for an 895-bit general RSA modulus. Do not spend further cycles on linear Fermat-j extension, fixed public gcd probes, exact-RSAREF MD5 state recovery without provenance, or renaming large-prime/special-q NFS mechanics as a new BRC factor method.

Resume immediately if one of the following changes: (1) Eric Lu publishes the RSA-260 algorithm/parameters/implementation; (2) authenticated RSA DSP prime-generation/random-source provenance appears; (3) externally available RSA-270 GNFS relation/polynomial/sieving data can be consumed; or (4) a genuinely N-dependent BRC observable is derived whose output is not isomorphic to standard NFS relation valuation/parity/special-q/filtering data and whose cost advantage survives a matched end-to-end benchmark.
