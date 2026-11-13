# Scientific continuation after the first exact S23/AV jump

Date: 2026-11-08 Asia/Shanghai.
Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessors: PR #1777, especially `research_notes/brc_s23_av_universal_order_and_h30001_20261108_r1/`.
New author-side result: `N(H)=2455069` for all integers `510<=H<=380805`, the first increase occurs at `H=380806` with exact `N(380806)=4530352`, and the latter value persists through `H=649492`.
Source of proof and actual checker transcripts: sibling `PROOF.md`, `CHAIN_STREAM.cpp`, `VERIFY_PLATEAUX.py`, `RUN_EVIDENCE.txt`.

## First specific open research unit

Determine `N(649493)` and the first `H>649492` such that `N(H)>4530352`.

The fixed integer-order key `2074774*v-380295*j` has proven exact ordering at least through H649492 via `H*(2074774-r*380295)<1` with rational error certificates. Its simple certified guarantee does not extend to an arbitrary larger H. Begin by selecting a tighter continued-fraction convergent, proving an appropriate strict key-order enclosure for the new range, and checking whether the `w=(79,431)` chain boundary decomposition remains valid, perhaps by proving a cone-specific bound instead of global order. Reuse the nonenumerative rank/select and prefix-occupancy formulas from the earlier exact result, with their correctly sized certified convergent.

A decisive test is a newly adjacent future-threshold cell whose first-attainable prefix has length exceeding 4530352, or a complete higher-endpoint covering certificate. Describe exactly how to regenerate gap classes and verify each witness. Preserve the joint label-(1,4) count and label-3 padding.

## Other live independent questions

Map the auxiliary two-point S23/AV observer into the lawful six-source/ten-label mother experiment using an explicit observation and future-operation bridge; determine the exact four-observation minimax value `delta_4` under the full lawful parameters.

## Control

GitHub author-side PR publication persists research only. Native service authenticated Researcher-ID, active Owner/CLAIM, formal Result and independent mathematical review require separately verified source authority; none is asserted by this note. Do not recalculate already certified endpoint families without a new discriminating purpose.
