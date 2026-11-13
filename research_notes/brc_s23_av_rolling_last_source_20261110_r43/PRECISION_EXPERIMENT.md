# R43 follow-up: finite decimal-precision certification

Additional exact experiment on the same rolling-source theorem. For `theta=sqrt(2)-1`, `m=16`, `J=10^9`, `N=10^8`, `K=32`, form the nested enclosure `lo=isqrt(2*10^(2d))/10^d-1`, `hi=(isqrt(2*10^(2d))+1)/10^d-1`, integer `d=1,...,15`. Try the R42 initialization plus all R43 incoming integer owner certificates. Verify the first passing candidate by 33 independent Euclidean Floor Sum source vectors.

Actual run 2026-11-10 (Python Fraction/int/isqrt): digit lengths 1 and 2 are UNCERTIFIED at the historic order constraint; 3 through 10 are UNCERTIFIED at a source boundary; 11 passes initial scanning but is UNCERTIFIED on an incoming source; **12 is the first certified precision within this tested sequence**, with `Q=2*10^12` (41 bits), 33 exact independent vectors and zero repairs.

This is a finite selection result for the declared decimal ladder, indices and interval; no claim that twelve digits is minimal across all possible rational enclosures. The actual test source `PRECISION_R43.py` and literal `PRECISION_LOG.txt` are included in the standalone research bundle. The strict failure diagnostics give a direct refinement target for R44. Source pin remains `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; observer-only scope and P000 unchanged.
