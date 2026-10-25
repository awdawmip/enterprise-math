# Stage90 reproducibility

Finite auxiliary iid model; author-side exact rational proof, not native or independently reviewed.

Reproduce with Python stdlib in one directory containing derive90.py, crosscheck90.py and their exact prior-stage dependencies derive89.py / derive88.py. Those predecessor sources are available at stage89 commit 96e04e09dce8716acaecf3a69fb2dc8b0e845a80 and stage88 commit a08b0e41d583dabefe00b8116c89d97b4d0bdf65. Run: python derive90.py ; python crosscheck90.py.

These two scripts were locally run and exact certificate90.json agrees, but they share the predecessor stop-action map. Full offline author research package includes predecessor scripts, raw outputs and expanded proof. Retain two distinct statuses: Source publication and native Research Driver acceptance (pending). Global read SHA ad56c417... ; project initial SHA 94c79020... ; native owner/CLAIM unverified.