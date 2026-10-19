# RSA-270 continuation: PCF/fast-product branch oracle is already a classical factoring route

Status: `RESEARCH NOTE / CROSS-ROUTE CLASSIFICATION / NEGATIVE FOR NEW SPEEDUP / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T01:30:00+08:00`  
Parents:
- `research_notes/RSA270_WEIGHTED_LOCAL_TRACE_COMPRESSION_20260908.md`
- PCF5 restricted-support frontier as independently audited in PR #1361/#1377.

No RSA-270 factor is obtained.

## 1. Exact N-only residue-class branch oracle by products

Let `N=pq` with p the smaller factor, so `p<=sqrt(N)<q`. Suppose a previous step has identified

`p ≡ r (mod M)`

with `gcd(M,N)=1`.

To lift one digit in an odd prime base l, put

`M'=lM`.

The l child classes are

`r_j = r+jM (mod M')`, `j=0,...,l-1`.

For each child define the bounded candidate set

`C_j={ x : 2<=x<=floor(sqrt(N)), x≡r_j (mod M') }`

and the product-gcd observer

`G_j = gcd(N, product_(x in C_j) x)`.

Exactly one child contains p. For that child the product is divisible by p; it cannot be divisible by q because every candidate is below q. Hence

`G_j=p`.

All false child products are coprime to N unless they accidentally contain another multiple of p, which cannot occur outside p's residue class modulo M'.

Therefore this construction is an exact N-only branch oracle.

But it is stronger than a branch bit: the first successful gcd already returns the factor p itself.

## 2. Why this does not solve the low-cost BRC problem

Across all l children, the candidate sets partition the previous residue class up to sqrt(N). Their total size is approximately

`sqrt(N)/M`.

At the public H2 starting modulus M=6 this is still `Theta(sqrt(N))` candidates.

A naive product is therefore trial-division scale. Fast polynomial/factorial methods can batch the arithmetic progression products. This is precisely the classical Strassen/Pollard-Strassen family of product-polynomial, multipoint-evaluation and gcd machinery already identified in the PCF5 prior-art audit.

The PCF5 audit explicitly freezes its own table/block batching as classical machinery and rejects a factoring-speedup interpretation.

For a progression of K candidates, baby-step/giant-step fast-factorial/product methods can bring this style of search to roughly square-root-in-K work, so with K on the order of sqrt(N) the classical exponent-1/4 regime reappears. This is an **upper-bound implementation route**, not a lower bound.

Moreover the current rigorous general deterministic factoring frontier is stronger: Harvey's 2021 exponent-one-fifth algorithm, with the Harvey--Hittmeir 2022 log-log refinement, factors a general N in `N^(1/5+o(1))` bit operations.

Thus using PCF/fast-product machinery merely to instantiate the BRC residue branch is not competitive with the best known deterministic general-purpose baseline.

## 3. Cross-route conclusion

`PCF5 BLOCK VISIBILITY + BRC RESIDUE FIBER`

does provide an exact N-only selector, but only because the block product directly contains the unknown factor. It does not furnish the missing cheap observable whose cost is materially below factoring.

This is an important distinction:

`EXACT BRANCH ORACLE EXISTS`

does not imply

`CHEAP BRANCH ORACLE EXISTS`.

The research target in the character/BRC line remains specifically a product-side computation of the **weighted local trace** without multiplying over the candidate factor interval and without invoking a general-purpose factoring routine.

## 4. Relation to the multiplier route

The same correction applies to the earlier multiplier/Fermat near-collision route. Modern deterministic factoring improvements of Hittmeir and Harvey already combine Lehman/Lawrence rational-approximation geometry with fast polynomial arithmetic and beat the old N^(1/4) deterministic exponent.

Therefore neither

- a multiplier near-collision scan, nor
- a PCF block-product residue scan

should be presented as a new factorization mechanism unless the BRC layer supplies a genuinely cheaper N-only selector than those classical engines.

## 5. Route disposition

`PCF_FAST_PRODUCT_BRANCH_ORACLE -> REUSE_IDENTIFIED / NO_NEW_SPEEDUP / ROUTE_CLOSED_FOR_CURRENT_LOW-COMPUTE_GOAL`.

Do not spend further effort enlarging candidate products, PCF tables, or multiplier blocks on this RSA-270 line.

The only unresolved direction still outside the classical route is:

`TARGET-ADAPTIVE WEIGHTED LOCAL TRACE`
` -> direct BRC product/Cartier evaluation`
` -> no explicit factor-interval product`
` -> no full primitive-character expansion`.

That is now the unique high-value gap left by this salvage continuation.
