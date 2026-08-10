# R004 precision genesis — Supplement 12: kernel-only semantic reconstruction no-go

Status: `PROVED_WIP + EXECUTABLE_CHECKED + NEGATIVE_BOUNDARY + FOUNDATION_FEEDBACK_CANDIDATE`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_11.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

The Representation Compiler has progressively converted future kernels into structured states: p-adic tries, product kernels, quotient modules, relation matrices, exponent profiles and integer determinant relations.

This supplement records a limit on that program. A bare equivalence kernel determines the quotient **set**, but not the typed operations, relations or witness semantics that the future language requires on that set.

Therefore the canonical compiler input cannot be only `exact carrier + kernel`. It must retain the typed future language as semantic input; the kernel is an intermediate representation.

## 1. Smallest exact example: parity quotient

Take exact state

`X=Z/4Z`

and current observation

`q(x)=x mod 2`.

The kernel partition is

`{{0,2},{1,3}}`.

Now consider two exact binary operations on the same carrier.

### Addition

`x+y mod 4` descends through parity because parity of a sum depends only on input parities.

The induced quotient table on `{0,1}` is XOR:

`0+0=0`, `0+1=1`, `1+0=1`, `1+1=0`.

### Multiplication

`x*y mod 4` also descends through parity because parity of a product depends only on input parities.

The induced quotient table is AND:

`0*0=0`, `0*1=0`, `1*0=0`, `1*1=1`.

The quotient carrier and equality kernel are exactly the same in both cases, but the descended operation semantics differ.

Hence a compiler receiving only the partition `{{0,2},{1,3}}` cannot infer whether the required quotient operation is XOR, AND, both, or neither.

## 2. R004-COMP-C01 — kernel semantic underdetermination

A finite equivalence relation `E` determines the quotient set `X/E` up to relabeling.

It does **not** determine additional structure on that quotient unless that structure is included in the input language and proved to descend.

In particular, the same kernel can support different:

- binary operation tables;
- order or metric structures;
- relation/witness semantics;
- action families and composition laws.

Therefore there is no general kernel-only procedure that reconstructs the intended typed future semantics uniquely.

This is a semantic identifiability boundary, not a claim that quotient operations cannot be computed. They can be computed once the exact operation/future language is supplied.

## 3. Correct compiler interface

The research target must therefore be written as

`Exact Carrier + Typed Future Language`

`-> Future Kernel IR`

`-> Structured Gates / Minimal Safe Carrier`

`-> Descended Typed Operations / Relations / Witness Semantics`.

The future kernel is useful because it captures exact future equality and class minimality. But it is only one intermediate representation.

This sharpens P023's existing operation-family rule: safe equality and safe operation semantics are related but not identical payloads. The compiler must preserve the declared operation family rather than discarding it after the kernel is computed.

## 4. Consequence for A3/A4 fallback

Supplement 11 proved that some noncongruent kernels can still be represented by integer linear-lift relations and that the A3 weighted relation field is exactly a rank-one determinant/exterior token.

However, even when a kernel admits multiple mathematically valid coordinates, the kernel alone does not tell the compiler which coordinate semantics are required by the original future task.

Therefore the transition into A3/A4 must be driven by typed requirements such as:

- preserve a weighted relation field and its closure law;
- preserve witness identity under composition;
- preserve MAY/MUST support;
- preserve a declared common-target relation;
- preserve a specific action algebra.

A bare partition is insufficient evidence for choosing among these structures.

## 5. Architecture correction

The earlier slogan

`future kernel -> minimum representation`

is correct only if "representation" means an unlabeled quotient set for the declared equality language.

For the actual project goal, the stronger and correct contract is:

`typed future language -> minimum typed representation`.

The compiler may use the kernel internally to minimize equality classes, but every operation/observable/relation that matters after compression must have an explicit descent/factorization certificate.

This prevents two symmetric errors:

1. retaining exact state detail that no future operation can use;
2. compressing to an equality partition and then silently inventing quotient operations that were never certified.

## 6. Executable witness

`precision_kernel_semantics_nogo.py` records the `Z/4Z -> parity` example.

It mechanically verifies:

- addition modulo 4 descends through parity;
- multiplication modulo 4 descends through parity;
- both use the same parity kernel;
- the descended quotient tables are XOR and AND respectively;
- the tables are distinct.

This is a minimal executable counterexample to kernel-only semantic reconstruction.

## 7. Revised compiler state machine

The compiler architecture after Supplements 06–12 is now:

### Semantic input

`Exact finite carrier + typed observations/actions/relations/witness requirements`.

### Equality IR

Compile the declared deterministic/future outputs into a future signature and kernel.

### Structured carrier gates

Attempt, where justified:

1. p-adic translation trie;
2. product factorization;
3. modular relation factorization;
4. additive quotient module / exponent profile;
5. integer linear-lift determinant relation;
6. A3 rank-one exterior specialization;
7. richer A3/A4 state only when required.

### Semantic output

For every required operation/relation/witness structure, emit an explicit descended implementation/certificate on the chosen safe carrier.

Thus the compiler output is not only a class identifier. It is a typed finite state machine whose retained detail and operations are both justified by the declared future language.

## 8. Next frontier

The remaining Foundation-level problem can now be stated without ambiguity:

> **Define the minimum typed representation object and compiler interface that preserves both future equality and the declared algebra/relation/witness operations, while selecting the weakest available structured carrier rather than an opaque partition.**

The equality component is substantially covered by P023/FQ-004 and the R004 compiler specializations. The unresolved design boundary is how the project should expose typed descended structure across functional, A3 relation and A4 witness/correspondence layers without promoting any one coordinate system to a universal primitive.

R004 should hand this interface question back to Foundation/A3/A4 rather than inventing a competing mother layer.
