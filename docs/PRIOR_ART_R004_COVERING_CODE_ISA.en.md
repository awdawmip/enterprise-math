# Prior art — R004 covering-code primitive ISA bridge

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

Supplement 35 is a compiler bridge. It does not claim covering codes, covering radius, covering density, length functions, parity-check matrices, projective saturating sets, or their optimization as Enterprise Math inventions.

## Primary prior sources

### SRC-R004-COVERING-CODE-DAVYDOV-2025

Davydov, Marcugini and Pambianco, *New upper bounds for binary linear covering codes*, arXiv:2511.02542 (2025).

The paper states the q-ary Hamming-ball volume, the syndrome/column characterization of covering radius, and the length function `ell_q(r,R)` as the smallest code length at fixed codimension and covering radius. It also records the one-to-one correspondence with saturating sets and provides modern infinite-family upper bounds.

R004 consumes these structures as the unrestricted additive primitive-ISA backend.

### SRC-R004-SATURATING-DAVYDOV-2018

Davydov, Marcugini and Pambianco, *Classification of minimal 1-saturating sets in PG(v,2), 2<=v<=6*, arXiv:1802.04214 (2018).

This gives exhaustive small binary radius-2 / 1-saturating classifications used to bound historical novelty of the small exact staircase.

## R004-local package under test

R004 only claims the following project-specific interpretation:

1. parity-check columns are primitive additive instructions;
2. the code kernel is the null-program space;
3. covering radius is worst-case semantic readout depth;
4. covering density becomes average short-program multiplicity;
5. the standard length function becomes the primitive storage/readout Pareto backend;
6. this bridge is rejected when typed instruction order, side effects, witness identity or history-sensitive legality make code-kernel words semantically non-null.

The one-redundant repetition-line formula and normalized small enumerations are elementary/specialized checks, not claims to have created covering-code theory.
