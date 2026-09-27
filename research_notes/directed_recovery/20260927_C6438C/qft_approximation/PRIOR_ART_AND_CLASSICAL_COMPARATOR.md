# Prior art and an input-matched classical comparator

Status: shared-context author analysis and bounded execution, not admitted.
Activity RA-CAAAC604CB513AEA8BBC1DFC. Existing prior-art/cache intake from
EM 951cc16cb09635fae9f93230d96030fdaa2035b3 remains applicable. No new
professional provider query was submitted in this continuation.

## Primary-source scope check

Yoran and Short, *Classical simulability and the significance of modular
exponentiation in Shor's algorithm*, [full text](https://arxiv.org/html/0706.0872v1),
was read through its simulation definition, conditional measurement
construction and tensor-contraction discussion. Its reduction requires
access to conditional measurements in the required product bases, not just
an ordinary modular-power function. The implication is a useful audit of
our own work: cheap preparation-label samples do not supply coherent native
rows or arbitrary conditional measurement probabilities.

Aharonov, Landau and Makowsky, *The quantum FFT can be classically simulated*,
[version 2](https://arxiv.org/html/quant-ph/0611156v2), was opened in full HTML;
the abstract, introduction and section routing were examined. Its headline
is explicitly accompanied by limitations when joining the Fourier stage
to the rest of Shor's circuit. No claim here rests on an unverified
assumption that our modularly prepared input has the required small width.
This is a scope comparison, not a new proof or a full theorem audit of that
paper. Earlier BGL sampling and robustness sources remain cited in the
individual error-contract notes.

A search also found Coppersmith's original small-root paper and an IACR
weak-prime-factor preprint. The latter full PDF fetch failed; no theorem
from that uninspected PDF is used. The following elementary comparator is
derived directly and does not require a lattice theorem.

## A classical benefit of exactly the same arithmetic witness

Either the primitive power-sum witness or a verified modular root witness
`b^(2^(ell-1)) = -1 mod N` forces every prime divisor p of odd N to satisfy
`p = 1 mod m`, where `m=2^ell`. This statement does not need the Jacobi
condition used to transfer an order lower bound to the chosen Shor base a.

If N is composite, a prime divisor is at most sqrt(N). Testing candidates
`1+m, 1+2m, ... <= sqrt(N)` therefore finds a factor after at most
`floor((sqrt(N)-1)/m)` typed divisions. There is no supplied factor or order.
Certificate construction/replay and each actual division remain charged.
This is a simple structure-aware trial division, not a new general-purpose
factoring complexity result, and it does not reproduce the QFT output law.

`observer_contracts/check_classical_congruence_comparator.py` actually
executed this comparator on the same input family:

| N | ell | factor pair found | candidate divisions | scan adder digits |
|---|---:|---|---:|---:|
| 65 | 2 | 5, 13 | 1 | 111 |
| 4097 | 3 | 17, 241 | 2 | 459 |
| 4294967297 | 6 | 641, 6700417 | 10 | 8237 |

The digit counts are scan arithmetic only. Full construction and replay
receipts are retained separately in `CLASSICAL_COMPARATOR_RESULTS.json.gz`;
the single primitive-core call in this run is cached primitive admission,
not a claim that all scan arithmetic costs one operation. A one-candidate
budget correctly returns PARTIAL instead of claiming a factor or primality.
Payload SHA256: `687e1e003775704f33008e52d4269ae9b8ceac88ed472b29dc653420f255ef0e`.

For a balanced semiprime N=pq with p,q both 1 mod m, a further symbolic
comparison follows by writing p=1+mu, q=1+mv:

    p+q = N+1 mod m^2.

If, for example, 1/2 <= p/q <= 2, then `2sqrt(N) <= p+q < 3sqrt(N)`.
One can enumerate that congruence class in this interval and test whether
`S^2-4N` is a square, using exact integer arithmetic. There are
`O(1+sqrt(N)/m^2)` candidates. This paragraph is an elementary symbolic
comparison only: no balanced-semiprime promise, square-root implementation
or execution is imported into our actual sampler.

## What counts as an improvement

Skipping ell certified terminal rounds genuinely removes their native row
queries. It does not establish a better general factoring algorithm. For
the *integer equality* power-sum witness, one of u,v is at least 2, so
`N >= 2^(2^(ell-1))+1`: ell is at most O(log log N). A modular root witness
can certify a longer suffix, but finding it is an additional cost and it
reveals the same stronger classical congruence information above.

With a binary-tree point-query implementation, shortening the queried
depth by ell may reduce its exponential upper bound by a factor involving
2^ell; an exact checkpoint implementation has a different depth tradeoff.
Neither expression is an observed universal speedup, and both must include
witness discovery, verification, bank admission, precision and fallback.
Any later complexity claim must compare against a classical method given
the *same* public witness, not against an uninformed baseline.
