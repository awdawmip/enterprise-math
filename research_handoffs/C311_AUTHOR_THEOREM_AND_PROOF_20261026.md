# C311 — Composite-cofactor polynomial content certificates (2026-10-26)

**Classification:** author hand proof + two exact local implementations; **not** a native Source Result, independent Driver review, Working Truth or Foundation admission.

**Frozen sources:** GLOBAL_KNOWLEDGE_V1 main@`363cc21deb56c429a3d1304e62bde6fd4c35452e`; Enterprise Math scientific input main@`5ccb75b5ef5d57dfa75f379ec6425e54948a1e34`. Source is the C195/H168 auxiliary 79-branch scalar circuit with frozen C293 path records SHA256 `03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89`. Prior author C310: `0ea93a4cbd23994bc1f4323202922f54c8ab4785`. The complete proof, data, two programs, readme and logs are inside the linked `C311_AUTHOR_REPLAY_CAPSULE_20261026.tar.gz`; the combined frozen portable ZIP is separately available from the run artifact.

## Theorem (composite-cofactor content certificate)

Let `s>0` and `P,C,J_1,...,J_m ∈ Z[t]` satisfy `C P = Σ_a J_a` with `content(C)=1`. Let `L=gcd(s, content(J_1),...,content(J_m))`, `S=s/L` and `R=Σ_a J_a/L`. Then `R∈Z[t]` and

`gcd(s,content(P)) = L·gcd(S,content(R)).` (1)

Suppose `S=H Π_{q∈Q}q^{e_q}`, where every `q∈Q` is a distinct verified prime, its complete positive exponent is `e_q`, and `H≥1` is **not assumed prime**. Suppose `p∈Q`, `R≡0 mod p`, and `R≠0 mod p²`; for every `q∈Q\\{p}` a coefficient of `R` is nonzero modulo `q`; and for one integer `T`, `gcd(H,R(T))=1`. Then

`gcd(s,content(P))=L·p.` (2)

**Proof:** Every `J_a/L` has integer coefficients. Gauss's content lemma implies `L|content(P)` because `C` is primitive, and `R=C(P/L)` with `content(R)=content(P)/L`; this proves (1). The first modular condition says `v_p(content(R))=1`, and each nonzero coefficient witness rules out that other prime from dividing `content(R)`. Any prime factor shared by `H` and `content(R)` would divide `R(T)`, contrary to the stipulated gcd. Thus no prime factor of `H` contributes, whether or not `H` is factorized, and exactly one `p` remains in the gcd; (2) follows. QED.

**Zero-extra-content corollary:** if all primes in `Q` have nonzero coefficient witnesses and the same composite gcd test passes, `gcd(s,content(P))=L`.

## Exact 19-path application

Indices: `3,6,7,8,11,12,17,26,27,29,30,33,34,38,56,75,76,97,108`. Candidate `p=3` at four indices `3,8,38,56`; candidate `p=2` at the other fifteen.

All 19 exact factorizations `S=H Πq^{e_q}` obtained by trial division over primes below 10000 leave the same 250-bit integer

`H=1354520142208056835914840923242211064045022575104362006332341353239007546777.`

No primality of `H` is asserted or needed. For **every** path, `T=1` and the stored modular inverse witness prove `gcd(H,R(1))=1`. Verified totals: **154** excluded-small-prime nonzero polynomial coefficient witnesses; **19** full `R≡0 mod p` coefficient reductions; **19** nonzero `p²` coefficients; **19** composite modular inverse identities. A separate pure-Python implementation rechecked all **173** coefficient witnesses and **19** composite evaluations by a different arithmetic circuit, including exact `S` decomposition. Output lines:

`C311_ALL 19 PASS`

`C311_INDEPENDENT_ALL_PASS 19 coefficient_witnesses 173 composite_evaluations 19`

**Inference:** each of the 19 target coefficient-content gcds is now certified within the frozen author-level factorized circuit **without** using C306's complete Newton-content oracle as a premise. Historical oracle values were compared post hoc only.

## Authority, limits and next question

GitHub connected account: `awdawmip`, repository `admin`/push. Native `em_control_tasks` returned `CONTROL_QUOTA`; `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` and `operation_sent=false`. Active Source owner was not confirmed; **no CLAIM, Source Result, independent Driver admission or P000 change** occurred. C300's factorized numerator/cancellation identity remains an inherited author-level assumption, not independently source-audited.

BRC type: 79 individually labeled positive-rational auxiliary branches are retained in the input. The integer-content observer is a scalar quotient only; it does not erase native signed/phase, port, provenance, joint-relation or future-operation distinctions. No native GF(2)-BRC/X6 correspondence is claimed. Next unit C312: obtain the zero-extra-content corollary's **oracle-free certificates for the other 106 paths**, then independently audit C300's source identity.

Full replay capsule SHA256: `ed9ae0cd6594223e12d2ebbe91f4738271b3f139125a28bd6aa7a92a7897ba91`.
