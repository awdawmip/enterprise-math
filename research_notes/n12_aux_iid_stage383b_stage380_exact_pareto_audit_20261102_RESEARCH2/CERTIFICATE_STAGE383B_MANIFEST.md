# Stage383-B exact reproducibility manifest

Scientific frozen pins: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Parent Stage382-B ad1aefb5ec5053cdde6ce7a2496ff4b5f641078f.

Run `python REPRO_STAGE383B.py` using only the Python 3 standard library in this directory. The program regenerates CERTIFICATE_STAGE383B_EXACT.json and prints the marker STAGE383B_STAGE380_LOCAL_PARETO_AUDIT_PASS.

Actual executed and repeated local output was byte-identical to REPRO_STAGE383B_EXECUTED_STDOUT.txt. The generated certificate contains all 32 original cost audit signs, eight residual interval bounds, exact source cost polynomial coefficients, and strict boundary/one-sided perturbation margins.

Expected certificate: 4786 UTF-8 bytes, SHA256 c4e96b331fcbb5772423d36112e8106439e946e608774fdbee3d550928d82e0b.

This is an author-side algebraic audit of Stage380-B **conditional on Stage379-B localization**. It does not constitute an independently admitted Driver review, a new native result, or a P000 X6 mapping.
