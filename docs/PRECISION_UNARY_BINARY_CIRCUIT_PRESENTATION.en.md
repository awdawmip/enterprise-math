# Unary Binary-Power Circuit Presentation

Status: `RESEARCH BRIDGE / NONCANONICAL`

The literal macro-table Pareto is exact inside its own representation class, but it is not the global presentation frontier. A single repeated generator already gives a sharp counterexample: storing powers of two creates a sparse circuit-like presentation with logarithmic storage and logarithmic worst-case runtime.

## 1. Unary repeated-action language

Fix one exact transition A and a declared repetition horizon h.

The task must execute

`A^m`, `0<=m<=h`.

A contiguous literal d-macro table stores

`A,A^2,...,A^d`

and uses `ceil(m/d)` chunks in the worst case.

## 2. Binary-power presentation

Instead store only

`A^(2^j)`

for powers of two not exceeding h:

`A,A^2,A^4,A^8,...`.

The number of stored transition matrices is exactly

`P(h)=floor(log2 h)+1`,

equivalently the bit length of h.

## 3. Precomputation is also logarithmic

Starting from A, every next stored rule is obtained by one exact squaring:

`A^(2^(j+1)) = A^(2^j) A^(2^j)`.

Therefore after the generator itself, the full table needs only

`P(h)-1`

matrix multiplications to precompute.

No semantic law is added.

## 4. Exact runtime for one exponent

Write m in binary:

`m=sum_j epsilon_j 2^j`, `epsilon_j in {0,1}`.

Then

`A^m = product_(epsilon_j=1) A^(2^j)`.

The number of runtime macro applications is exactly

`popcount(m)`.

The executable layer verifies equality with literal repeated matrix multiplication for integer and rational matrices.

## 5. Exact worst-case runtime through horizon h

The maximum popcount among `1<=m<=h` is

`floor(log2(h+1))`.

Proof: let

`t=floor(log2(h+1))`.

Then `2^t-1<=h`, and that exponent has t one-bits. The smallest integer with t+1 one-bits is `2^(t+1)-1>h`, so no exponent through h needs more than t binary macros.

Thus binary presentation has

`storage = floor(log2 h)+1`,

`worst runtime = floor(log2(h+1))`.

Both are logarithmic.

## 6. Strict same-storage domination of contiguous macros

At the same stored-rule count P(h), a contiguous unary macro table can store only

`A,...,A^P(h)`

and has worst runtime

`ceil(h/P(h))`.

Binary powers can be strictly better.

The first strict horizon is h=13:

- both store4 rules;
- contiguous `{1,2,3,4}` needs4 chunks in the worst case;
- binary `{1,2,4,8}` needs at most3.

## 7. Large-gap example

At h=1024:

- both compared presentations store11 transition rules;
- binary powers have worst runtime10;
- contiguous depth11 macros have worst runtime94.

So the representation choice changes the Pareto frontier by nearly an order of magnitude in execution depth at the same rule storage.

## 8. Full table still occupies a different endpoint

The complete unary table

`A,A^2,...,A^h`

stores h rules and executes every requested power in one lookup/application.

Binary powers do not dominate this full-storage endpoint. They create a qualitatively different middle regime:

`O(log h) storage / O(log h) execution`

instead of

`O(h) storage / O(1) execution`

or

`O(1) storage / O(h) execution`.

## 9. Why this beats the literal contiguous family

The contiguous family spends storage on every short exponent, even though many can be composed cheaply from strategically chosen longer-scale generators.

Binary powers store a **basis for exponent construction**, not an interval of precomputed answers.

This is a presentation-level analogue of using circuits/DAGs instead of flat tables.

## 10. Representation-class minimality matters

The parent literal-macro theorems remain exact. The binary construction does not contradict them because it leaves that representation class.

It proves instead that phrases such as

`minimal storage for execution depth R`

are incomplete unless the allowed presentation technology is declared.

The same semantic future law has different Pareto fronts under:

- flat contiguous macro tables;
- binary-power circuits;
- general addition chains;
- arbitrary shared DAG/circuit presentations.

## 11. Scope boundary

This generation studies one repeated generator. Binary decomposition relies on

`A^r A^s=A^(r+s)`.

For multiple noncommuting generators, an arbitrary word cannot be summarized by one exponent and binary powers do not directly solve the presentation problem.

That multi-generator problem belongs to semigroup normal forms, rewriting systems, automata/circuit sharing and grammar-like presentations.

## 12. Stage131 bridge

The same binary-jump idea applies to a unary implication chain. Instead of storing only adjacent edges or every transitive edge, store power-of-two jumps from each chain position.

This creates an exact intermediate storage/depth point between Hasse adjacency and full transitive closure. The next generation derives that chain law explicitly.

## Owner-local assets

- `src/enterprise_math/unary_binary_circuit_presentation.py`;
- `tests/test_unary_binary_circuit_presentation.py`;
- `docs/PRECISION_UNARY_BINARY_CIRCUIT_PRESENTATION.{en,zh}.md`.

## Prior art / status

Binary exponentiation, repeated squaring and addition chains are standard prior mathematics/CS. The Enterprise Math value is the exact presentation-precision pressure test: representation class changes the storage/execution frontier.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.