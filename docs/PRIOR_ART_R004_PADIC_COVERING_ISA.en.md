# Prior art — R004 p-adic precision-native covering ISA

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

Supplement 36 does not claim linear codes over finite chain rings, projective Hjelmslev geometry, or modular-code covering radii as new mathematics.

## Sources

### SRC-R004-CHAIN-RING-CODES-HONOLD-LANDJEV-2000

Honold and Landjev, *Linear Codes over Finite Chain Rings*, Electronic Journal of Combinatorics 7 (2000), R11. This develops linear coding over finite chain rings geometrically and establishes the code/projective-Hjelmslev connection.

### SRC-R004-HJELMSLEV-ARCS-2024

Honold, Kiermaier and Landjev, *New Results on Arcs in Projective Hjelmslev Planes over Small Chain Rings*, arXiv:2409.02099. The paper works with projective Hjelmslev planes over finite chain rings, explicitly defines points as free rank-one submodules, and discusses the connection to linear codes over the ring.

### SRC-R004-MODULAR-COVERING-GUPTA-2012

Gupta and Durairajan, *On the Covering Radius of Some Modular Codes*, arXiv:1206.3038. This is prior work on covering radii for codes over `Z_(2^s)`. Its stated metric is homogeneous distance, so it is only a broad ring-covering prior, not a source for R004's Hamming-specific formulas.

## R004-local package

The project-local claims under test are limited to interpreting p-adic precision cap K as a changing primitive-ISA alphabet in the typed compiler; exact monotonicity under reduction `K+1 -> K`; the free-projective-line formula for one-step primitive storage; the full-support repetition null-line optimum for one redundant primitive; the explicit precision phase-change `L_(2,1)(3,2)=4` versus `L_(2,2)(3,2)=6`; and the fail-closed reminder that ring and field algebras of the same cardinality are different typed worlds.
