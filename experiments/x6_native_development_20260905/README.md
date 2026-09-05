# X6 Cell/path development research candidate

Read RESEARCH.md, followed by CHART_TRANSPORT_ADDENDUM.md. This is a conditional global packet/endpoint construction with exact algorithms, not a Foundation promotion or identification of the unique native X6.

Run from this directory:

```sh
python check_development.py
python check_reference.py
python check_chart_transport.py
```

Python uses the standard library for the model and SymPy==1.14.0 for the independent Smith-form/linear algebra check. Existing six_axis.py and atlas_brc.py are pinned, unchanged copies from source commit c53492f9e2946f2b10f8b1000fbf0d67da2db27a.

Key interfaces: Cell reduced endpoint normal form; PacketPath full events; Event exact positive weights; IncidenceVertex separate from Cell; FramedCell.reframe passive transport; FramedCell.active_rotate actual candidate-state action. Joint atlas relabeling is a separate operation because its passive-quotient kernel is V4.

Every claim retains its semantic boundary: counts are not native Cell addresses, FCC readout is not identity, operation inverses do not erase path events or branch weights, group rank is not spatial dimension, and passive coordinate transport does not determine native cross-chart returns.
