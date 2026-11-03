# D25: original 216–2304 weighted bridge, terminal units and precision boundary

Date: 2026-11-03 (+08). TASK_RESEARCH author-side, logical research lane `chatgpt-research-onhour-enterprise-math-20260923`; never maintenance lane. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING; no native claim/run/checkpoint. Consumes existing D24 first-digit and source-aligned reflected R interface. D25 mother remains OPEN.

## Original objects and directly relevant comparison

In Z_(p), p>3, set
```
b_k=(2k)!(3k)!/((k!)^5*216^k)
c_k=(4k)!/((k!)^4*2304^k)
W_p=sum_(k=0)^(p-1)(6k+1)b_k
S_p=sum_(k=0)^(p-1)(8k+1)c_k.
```
Guo–Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), 329–358, arXiv:1803.01830, proved for all p>3 that `S_p = p*(-3/p) (mod p^3)`, using exactly this 2304 coefficient, original weight, and p-1 truncation. The frozen D25 source-port alignment previously gave `Delta_p-R_p = (W_p-p)/p^2 (mod p)` for target primes p=13 or 19 (mod24). Hence an all-target proof of the explicit **candidate** `W_p=S_p (mod p^3)` would prove the D25 scalar LIFT target. This bridge is not proved here. The existing signed-216 numerical generalization remains a conjecture; independent 2304 proof does not turn that conjecture into a theorem.

## Theorem A (PROVED): valuation mismatch in original coefficient fibers

For each prime p>=5, and 0<=k<p,
```
v_p(b_k)=floor(2k/p)+floor(3k/p);
v_p(c_k)=floor(4k/p).
```
Legendre's factorial formula proves both exactly: denominators are p-units and all factorial arguments are <4p. For every p>=7, choose k_*=ceil(p/4), so p/4<=k_*<p/3. Then v_p(b_{k_*})=0 but v_p(c_{k_*})=1. No **index-preserving multiplication by p-adic units** can identify the entire coefficient arrays. This excludes that specific transfer; it does not obstruct a two-index WZ/creative microscoping or parameter-dependent normalized transfer.

## Theorem B (PROVED): exact universal terminal discrepancy

For every prime p>=5,
```
b_(p-1)/p^3 = c_(p-1)/p^3 = -1 (mod p).
W_p-W_(p-2) = 5*p^3 (mod p^4)
S_p-S_(p-2) = 7*p^3 (mod p^4)
(W_p-S_p)-(W_(p-2)-S_(p-2)) = -2*p^3 (mod p^4).
```
All p-divisions are performed in Z_(p) after showing exact valuation three. Proof by disjoint p-block factorials and Wilson:
```
(2p-2)!/p  = (p-1)!(p-2)! = -1       (mod p).
(3p-3)!/p^2 = 2*(p-1)!^2*(p-3)! = -1 (mod p).
(4p-4)!/p^3 = 6*(p-1)!^3*(p-4)! = -1 (mod p).
```
Here (p-1)!=-1, (p-2)!=1, (p-3)!=-1/2, (p-4)!=1/6 mod p. Also the two bases to p-1 power are +1 mod p and denominator (p-1)!^5=-1, (p-1)!^4=+1. Hence the terminal coefficient units are both -1; multiplying by native weights 6p-5 and 8p-7 proves the three assertions. The ordinary 216 terminal +5p^3 was known; the exact *cross-model* -2p^3 mismatch is an immediately usable precision check. It does not imply a full p^4 bridge fails for every p.

## Executed finite falsification/probe

Companion checker generates the original two sums via exact modular recurrences,
```
b_k/b_(k-1)=(2k-1)(3k-2)(3k-1)/(36k^3)
c_k/c_(k-1)=(4k-3)(4k-2)(4k-1)/(576k^3).
```
It independently checks 10 selected primes against factorial/binomial coefficients. All 301 primes 5<=p<=2000 (including all 77 target primes p=13,19 mod24) satisfy the *unproved* mod-p^3 bridge, and the full mod-p^4 difference is nonzero for 300/301. Finite agreement is no all-prime proof.
- p=13: mod 28561, W=19786, S=24180, W-S=24167=11*13^3 (an **exact counterexample** to the *stronger* mod-p^4 bridge inside the target domain).
- p=19: mod 130321, W=82327, S=41173, W-S=41154=6*19^3.
- p=373: mod 19356878641, W=11832087049, S=5916043711, W-S=5916043338=114*373^3.
This all-source precise third-versus-fourth-digit boundary informs the next transformation candidate.

## Next exact scientific action and BRC application

Construct a *terminating* two-index/parameter-dependent 216–2304 WZ or creative-microscoping identity, with original weights, p-1 endpoint, parity and sign/derivative orientation. Validate a candidate against k_*=ceil(p/4), terminal -2p^3 modp^4, and p13,p19,p373; prove its mod-p^3 specialization uniformly before feeding the already proved 2304 comparator to original frozen Delta-R. BRC COMPOSE_APPLIED: preserve integer coefficient labels, exact valuations, signed difference and cutoff fibers. Positive-mass/termwise collapse cannot replace this signed observer; no native X6 coordinate retyping is implied.

Native p373 same-original-class H0/B0 divided-power benchmark #1559 remains NOT_EXECUTED/PENDING_OWNER: [X]U mod139129, rank, real semilinear Frobenius, eta, original odd signed observer and independent reproduction missing. Ordinary integer checks are not the benchmark. Research Source writing unavailable: Sites status read 2026-11-03T04:26Z reports research_authority_granted=false, write_relay_enabled=false, executor_binding_configured=false and 5/5 active control jobs. Original request `research-onhour-20261031-0205-dispatch-r15` / bridge #6633 is COMPLETE/FAILED/UPSTREAM_CODE_REVIEW_REQUIRED; do not replay. Session/CLAIM/run not established for this unit, no admitted Result or Source checkpoint. Control support #1558. Schedule and notifications unchanged.
