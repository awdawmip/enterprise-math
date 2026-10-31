# R421 research handoff — 2026-10-31

Full theorem/proof: R421_PROOF.zh-CN.md. Regenerator: r421_cert.py. Independent signed-convolution verifier: r421_independent.py. Actual eight-batch SHA256, byte counts, and validation totals: R421_EVIDENCE_SUMMARY.json.

From immutable R420 d4659e227a1a1a5fd0f35db5476ba1b87ec915c2 and frozen GLOBAL_KNOWLEDGE_V1 d310c5f090bd5883e89df4c5827468959073541b / EM main e4da8741fc91c6b584de6a61a9c8cd6b7ae1ed66: exact finite polynomial certificates prove D_(s+m,s)>0 for every s>=3 and each m=193..256; additionally, for *each* fixed m>=1, lim s^2 D/W_s^2=4^m/(m+1)>0. Polynomial degree 4m+5 and universal leading coefficient 2^(2m+1). 57,856 exact positive coefficients checked. Independent verifier: 960 direct signed-delta checks and 320 cross-products.

Reconstruction: run python r421_cert.py --low 193 --high 202 --full; repeat ranges 203..212, 213..222, 223..231, 232..239, 240..245, 246..251, 252..256. Next run python r421_independent.py R421_EVIDENCE_193_202.json R421_EVIDENCE_203_212.json R421_EVIDENCE_213_222.json R421_EVIDENCE_223_231.json R421_EVIDENCE_232_239.json R421_EVIDENCE_240_245.json R421_EVIDENCE_246_251.json R421_EVIDENCE_252_256.json. Compare raw JSON byte hashes to summary.

Native Site control authority not granted; active Source owner query returned CONTROL_QUOTA. This is author-side portable scientific preservation, not a CLAIM, Result, official Research-Activity, independent Driver review or mathematical admission. Do not impersonate an earlier session, reviewer or owner. Next proof question: a uniform coefficientwise m-induction on P_m, or an explicit S(m) for the analytic tail; alternatively certify m=257..320. P000 and ACTIVE worldview unchanged.
