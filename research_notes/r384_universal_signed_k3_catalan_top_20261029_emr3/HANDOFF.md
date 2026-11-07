# R384 portable handoff

2026-10-29; author-side exact BRC auxiliary research. Complete proof in R384_PROOF.zh-CN.md; executable stand-alone raw K/J checker in R384_verify.py.

For all integers r≥1 and all real θ>−1, changing only original signed K₃[t²] from −8 to −8(1+θ) gives Δ^r H_r=(6−16θ/5)^r and Δ^(2r)Q_r=Cat_r(30−16θ)^(2r). The proof extends the actual R348 formal y/z extraction at the parameterized kernel, using E₁(z)=z+θz². θ=15/8 alone forces top-degree loss for every r.

Finite independent raw-D evidence: 8 rational θ × 10 coranks r=1,2,3,4,5,6,8,12,15,16, 160 exact equalities; r16 at θ=15/8 has degree_H=8, degree_Q=16 and negative Turán indices 14,15. Run Python R384_verify.py to reproduce R384_EVIDENCE.json and R384_SUMMARY.json. The stronger half-degree rule for all r is an open conjecture; so is full r16 PF₂ phase classification.

Source pins: signed R346 Git Blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1; R348 PR#1599 commit 5347e506bd145028d7338e9f7993dcd2a2fed97c; R350 2e5d76989fbce6fef0aa891514bb5045008fe293; R383 786286050f4141ac6e278ab4a579ee2c68b6b5d7. Global main@22914f0903be04abde0f1c8cca91f737a31df4a8 and Enterprise Math main@ba18098a824b0306c55d6feb27415aaa801be71a.

Native session/CLAIM and Driver acceptance are not inferred from repository publication. Do not modify protected P000/ACTIVE. Next: prove the θ=15/8 general half-degree collapse through E₂ and higher order, or finish the r16 global PF₂ phase certificate.