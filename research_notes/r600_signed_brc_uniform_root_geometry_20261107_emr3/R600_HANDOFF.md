# R600 research handoff — 2026-11-07

Mother objective: signed BRC with P000 native X6 and preserved provenance/joint relations. Local auxiliary input is frozen R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f and R599 commit 139d0646e12739be79f710851377bb7eb2421dc7.

Scientific increment (author-side analytic proof): exact factorization F(z)=3(sinh(w)-w)(sinh(w)+w)/w^4, w^2=-2z, yields F(x)>0 for real x. Every complex zero zeta satisfies |zeta|>2 and |F'(zeta)|>=1/(sqrt(2)*|zeta|^(3/2)); any two distinct zeros have distance >sqrt(2*max(|zeta1|,|zeta2|))/8. Exact proof: R600_PROOF.zh-CN.md.

Reproduce: python R600_VERIFY.py. 101 exact rational coefficient identities and strict rational bound checks, actual output in R600_EVIDENCE.txt. All-parameter result uses analytic argument, not finite enumeration.

Status: AUTHOR_SIDE_ANALYTIC_PROOF / DRIVER_UNREVIEWED / NOT_ADMITTED. Current GitHub actor awdawmip, repository admin. Native em_status and em_control_tasks: BACKEND_IDENTITY_OR_VERSION_MISMATCH / operation_sent=false. Native owner, session, Researcher/RA and CLAIM remain unconfirmed.

Next: combine R590 moving-disk error with R600 derivative and spacing to derive uniform local modulus bounds and finite F_k root matching on a growing disk, then a controlled sum over the matching auxiliary roots and a separate spectral-tail bound. Maintain the auxiliary/native observer distinction and the V_k=O(k^(-1/2)) candidate status.
