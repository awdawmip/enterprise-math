# Coverage clarification — sector conservation check

Applies to the proof at enterprise-math@000f4ec351da312c052f8a04ff9a06496cb37a4e,
research_notes/chatgpt_direct/20261009_EULER_SECTOR_CONSERVATION_SHARED_FIELD.md.

Section 7's wording “four field-dependent positive NB policies” means one implemented
field-dependent nonbacktracking policy, tested from four different initial fields,
through eight edges. The code assigns weights 1/3 and 2/3 based on current field data.
It does not execute four different policy definitions or a history-dependent selector.
The theorem for arbitrary state/history-dependent selections follows from the
pathwise invariant proof, rather than those four executions.

The 40,750-assertion final run and all mathematical conclusions are unchanged.
This is a verification-coverage wording clarification, not an additional experiment.
