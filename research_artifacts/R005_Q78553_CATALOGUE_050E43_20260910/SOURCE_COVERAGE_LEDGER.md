# Source and coverage ledger

The required object is every exact-916 consecutive-prime gap whose start is in
[1291005053866735,1294364244470160]. Sources have distinct evidence roles.

| Route / source | Actual observation | Coverage role and boundary |
|---|---|---|
| [TOS gaps](https://sweet.ua.pt/tos/gaps.html), [numeric table](https://sweet.ua.pt/tos/gaps/t0.txt.gz) | Downloaded exact data; it states a test range through 4e18, with a double-tested range through 4e17. Gap 916 has first start 1189459969825483 and aggregate count 107483. | A complete global computation is described, but this published first-position/count projection does not locate every repeated 916-gap in the task band. It was not used as the local catalogue. |
| [TOS pi values](https://sweet.ua.pt/tos/primes.html), [numeric table](https://sweet.ua.pt/tos/primes/1d12.txt.gz) | Fully downloaded and hashed; five exact original rows were extracted for 1291e12 through 1295e12. All four resulting count differences matched the constructed prime sequence. | Independent aggregate count check of four full cells; not by itself a positional-gap completeness proof. |
| [Nyman–Nicely 2003](https://cs.uwaterloo.ca/journals/JIS/VOL6/Nicely/nicely2.html) | The primary publication describes first-occurrence and maximal-gap searches over 1e15 through 5e16. | First-occurrence coverage is not the required list of every repeated 916-gap. No local absence was inferred. |
| Official [primesieve 2.3.0 distribution](https://pypi.org/project/primesieve/2.3.0/) | Matched official wheel hash, loaded unchanged C++ library 7.5, passed independent adapter checks, then completed the full 4e12 interval. | Actual constructive catalogue route. Complete block coverage, all-pair stitching, independent counts and separate witnesses provide the finite certificate. |
| Canonical R005 scanner / DSI | Accepted byte pins and source review were consumed. The final scanner execution is logged and returns zero failures. | Accepted reduction and final candidate interface; no scanner repair or DSI proof replay. |

Transport and execution recoveries were kept distinct from mathematical results:

- The web reader could not decode the TOS gzip content type. A direct Python
  HTTPS attempt also reported a certificate-chain error. Default Windows
  Invoke-WebRequest certificate validation succeeded, and the original bytes
  were preserved and hashed. Neither earlier failure established unavailable data.
- The host Python 3.14 had no installed primesieve binding, and the requested
  native compiler commands were not found on PATH. An isolated compatible
  official Python 3.9 / primesieve / NumPy environment executed the existing
  implementation. This was an execution-environment mismatch, not a new
  mathematical capability gap.
- A 1e8 pilot and a 1e9 pilot established feasibility. They were not presented
  as full coverage. The billion-integer block was reused exactly as block 0;
  the smaller overlapping pilot was not counted again.
- The bare runtime authorization CLI hit an unrelated raw publication fork.
  The documented canonical bootstrap then authorized the same real claim.
  Both actual runs remain in the immutable startup evidence; no control
  quarantine, task, dependency or accepted result was edited.

The completed construction replaces the unresolved catalogue obligation with
an auditable finite source. This ledger makes no claim that every possible
external archive was exhausted or that no other complete catalogue exists.

