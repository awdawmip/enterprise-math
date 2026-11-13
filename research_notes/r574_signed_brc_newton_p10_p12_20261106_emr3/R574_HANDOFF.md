# R574 continuation · 2026-11-06

Parent: frozen signed BRC R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; prior author-side R573@a7d13b34f83c0d72ca053cccc038fcc520aec96c.

New exact theorems: p10 degree20 with p10(2..4)>0, p10(k)<0 for all integers k≥5 (21 strictly negative coefficients of p10(5+u)); p12 degree24 with p12(2..4)>0, p12(5..10)<0, p12(k)>0 for k≥11 (25 strictly positive coefficients of p12(11+u)). The global spectral lower-growth exponent improves to 23/12, with constant (3710099603382272/25508120926983929364990234375)^(1/12).

Files: R574_PROOF.zh-CN.md (complete proof and certificate construction), R574_VERIFY.py (actual local executed verifier), R574_EVIDENCE.txt (stdout from exact run), this handoff.

Checks: exact SymPy polynomial/shift coefficients, independent integer-Catalan and Fraction recurrence for all 999 integers k=2..1000; PASS. Source is a frozen auxiliary scalar; no native X6 or theorem admission changes. Researcher/Source-native activity, owner status and independent Driver review have separate receipts/status.

Next: test p14/p16 and analytically study leading-coefficient generating function for fixed m and possible uniform-in-m estimates; use existing R462 frozen definitions. Do not repeat the verified p10/p12 computation merely as continuation.
