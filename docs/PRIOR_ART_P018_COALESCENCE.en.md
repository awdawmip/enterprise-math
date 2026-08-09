# Prior Art — P018 Coalescence Time and Ultrametric Structure

Status: `ACTIVE PRIOR-ART NOTE`  
Scope: P018 Supplement 14  
Primary source IDs: `[SRC-MURTAGH-CONTRERAS-2010-HIERARCHY-ULTRAMETRIC]`, `[SRC-FOUTEL-RODIER-2018-COALESCENT-ULTRAMETRIC]`

## 1. Boundary that must be preserved

Hierarchical merge structures and ultrametric descriptions are established mathematics. Murtagh and Contreras explicitly review hierarchy together with ultrametric topology, while Foutel-Rodier, Lambert, and Schertzer study coalescent processes through ultrametric spaces and nested partitions.

Therefore Enterprise Math does **not** claim as novel:

- dendrogram or hierarchy-to-ultrametric constructions;
- the general association between coalescence/genealogical merging and ultrametric spaces;
- the strong triangle inequality as a characteristic ultrametric law.

## 2. Enterprise Math-specific research interface

P018 studies a narrower deterministic finite-state interface:

1. State Pair / kernel logic is already present before any metric is chosen;
2. for one deterministic endomap, first common-iterate time is defined entirely by entry of a pair into the diagonal;
3. P020 gives finite stabilization on well-founded monotone reductive dynamics;
4. this makes eventual coalescence equivalent to equality of canonical stabilized states and gives an explicit finite bound from stabilization steps;
5. P011 collision spectra can then be shown to saturate after a finite observation-dependent time.

The novelty of this integrated interface is `NOVELTY_UNVERIFIED`. It must be treated as a project-specific synthesis unless a dedicated historical search establishes otherwise.

## 3. Source use

`[SRC-MURTAGH-CONTRERAS-2010-HIERARCHY-ULTRAMETRIC]` is used only to mark hierarchy/ultrametric structure as prior art.

`[SRC-FOUTEL-RODIER-2018-COALESCENT-ULTRAMETRIC]` is used only to mark the broader coalescent/ultrametric connection as prior art.

Neither source is evidence for the Enterprise Math P020 stabilization theorem or the exact deterministic kernel identities proved in this repository.
