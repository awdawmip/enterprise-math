# R327 HANDOFF — BRC Newton positive forward-difference cone through q=640

Research activity: RA-EMR3-20261027-R327-1025 (GitHub main), logical researcher EM-DIRECT-EMR3-R327-1025. Native Source session denied STATIC_READONLY_SCOPE_DENIED; em_control_tasks denied CONTROL_QUOTA; no official CLAIM, authenticated Source Result, Driver review, or Foundation admission.

## Verified frontier
For the R325 BRC ordered-source 12-term integer transfer, R326 proves for every fixed q>=0 a polynomial Phi_q(s) of degree <=q and [t^q]B_s(t)=2^s Phi_q(s) for s>=q. R327 defines N_(q,u)=2^(q-u)[t^q]B_(q+u) for 0<=u<=q and positive integers D_(q,k)=Delta_u^k N_(q,0). Then Phi_q(q+u)=2^(-2q)*sum_(k=0)^q D_(q,k)*binom(u,k) for all integer u>=0. For any j<=q, Delta^j Phi_q(q+u)>0 follows from D_(q,k)>0 and the binomial identity.

Exact Python integer verification of 205761 D entries establishes strict positivity for all 0<=q<=640, hence all s>=q in these 641 unbounded strips, with positive forward differences up to order q. Independently, all 821121 triangle entries 0<=s<=1280, 0<=q<=s are strictly positive. R325 full-triangle SHA256 prefix through 1024 matches; R326's 2145 monomial-coefficient SHA256 reconstructed by independent rational basis conversion matches.

Evidence: R327_EXACT_EVIDENCE.json (actual execution summary, full local output SHA256 included); R327_verify_newton_difference_cone.py (complete self-contained executed code); R327_NEWTON_DIFFERENCE_CONE_AUTHOR_PROOF.zh-CN.md (algebra and scope). SHA256 of newly checked D list: ace585095c2606cb7e5c07d54640a8fe586fe669ae8d37503e2d6042ea9fb2ec. All-row triangular hash: fd37e0fe67867da8ba63c44999e92ee83a4e1ceabfd7e32e2780381b9cd536b9.

Source pins: GLOBAL_KNOWLEDGE_V1 main@7b33f8066e9993e7c941959a9d738ed405248eb8; Enterprise Math main@95be22f0181d18b7cc7d6df9db4024e8d85e34dd; R325@2c62f1502e640d1aed2db6f72956abc6a22ca2d5; R326@e5478b005efd75971c31ea8468d725d4c50ea26f.

## Next precise unresolved unit
The only remaining triangle positions, combining the two exact certificates, are s>=1281 and 641<=q<=s. Seek structural positivity or an exact negative D_(q,k) at q>=641; a negative forward-difference numerator would invalidate this sufficient cone but would not by itself falsify domain coefficients. Keep off-domain signed tail in the full polynomial recurrence; K_2(t) has a negative coefficient. Preserve positive source provenance vs signed Newton observation semantics. No native heartbeat/6D physical implication. D_d(n)>0 and N_peak=81 remain unresolved. Next formal Owner/Driver review must independently assess source, arithmetic and 205761 sign assertions.

Research branch is research/r327-newton-difference-cone-640-20261027-emr3; always resolve its actual immutable HEAD and file blobs before announcing durable success. Author-side only, NOT_ADMITTED.
