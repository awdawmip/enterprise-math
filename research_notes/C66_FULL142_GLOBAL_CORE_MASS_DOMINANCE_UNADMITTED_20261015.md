# C66 — Global core-event mass dominance in the finite 142-face positive BRC auxiliary model

Status: UNREVIEWED / NOT_ADMITTED; author exact GF(2) proof and self-check only. This is neither a native Researcher CLAIM nor a Driver-accepted result, and is not an X6 Cell theorem.

Source pins (read-only): GLOBAL_KNOWLEDGE_V1 main@ae30c62e21132ac89cab0708a8fca475a1159b9e; Enterprise Math main@1c2913ac2c3b0412b3aedca30dfa9cf16ac8bee7. Ancestors C58-C65 provide the exact 156 original integer-edge / 142 exchange-face matrices and the genuine 156-edge complement witness x_star=0x854002244e384a429400c6cc8986.

**Claim.** Let Q_t(c)>0 be the *unnormalized complete core-event mass* in this finite positive-weight auxiliary model, with 48-bit core observation c, 66 core-determined faces and 76 noncore faces; let chi_83,chi_96 be the two named fixed-face characters. For 0<t<1 define W_+(t)=max_{chi_83=chi_96=+1} Q_t(c), W_-(t)=max_{chi_83=chi_96=-1} Q_t(c). Then

    W_-(t)/W_+(t) <= ((1-t)/(1+t))^2,

in particular W_-(1/2)/W_+(1/2) <= 1/9.

**Proof and exact finite audit.** Factor Q_t(c)=(1+t)^(66-w(c)) (1-t)^w(c) S_t(c), where w is the number of negative characters among 66 fixed faces and S_t>0 is the summed positive noncore partition, preserving exact fiber multiplicities. Reconstruct the 23-dimensional four-residual-preserving GF(2) gauge G0 and choose the 23-dimensional complement U in the 46-dimensional chi_83=chi_96=+1 core subspace: rank(G0)=rank(U)=23, rank(G0+U)=46. Each plus core lies in exactly one coset c(z)+G0, z in F_2^23.

The 66 fixed faces split into 33 pairs with identical G0 response. The special pair (83,96) is positive in every plus core; for each of the other 32 pairs choose (p_i,q_i), such that all 23 U-generators have chi_{q_i}=+1. This linear identity was checked for all 32*23=736 face/generator incidences; the full 736-equation GF(2) system admits the trivial section correction T=0 with 32 lambda_i=1, all 511 dual dependency tests, and independently reconstructed raw 156-edge witnesses. Put delta_i(z)=character-bit(p_i XOR q_i) on c(z), and d(z)=sum delta_i(z). The 32x23 disagreement map has rank23 and minimum nonzero weight2. For every g in G0, paired characters flip synchronously, so w(c(z)+g)=d(z)+2k(z,g), 0<=k<=32-d(z). The chosen canonical c(z) has k=0. Thus each positive G0 orbit O_z obeys m(O_z)=d(z), M(O_z)<=64-d(z); in particular m+M<=64 for every one of the 2^23 orbits.

The genuine C65 old-edge complement maps a positive orbit bijectively to its negative orbit, flips all 66 fixed face signs, preserves all 76 noncore faces, and hence keeps S_t exactly unchanged. Consequently its negative minimum is 66-M(O_z)>=d(z)+2. Since beta=(1-t)/(1+t) lies in (0,1), the ratio between maxima within the paired negative/positive orbits is beta^(m_minus-m_plus)<=beta^2. Taking the global maxima (and choosing the paired orbit of a negative maximum) gives the claimed uniform bound. A maximum mass bound is not a bound for the *total* mass or conditional four-residual feedback.

**Extra exact results.** Full enumeration of 8,388,608 positive G0 orbit labels gives 7,313,074 labels with a solvable stronger pair-flip equality certificate (exact orbitwise maximum ratio beta^2), and 1,075,534 without that certificate (all still satisfy the bound). The GF(2) code weight histogram was independently enumerated using raw old-edge reconstruction. One true 156-edge witness: plus c=0x110001, x=0x40a00180100000000010000000, w=8; minus c=0x1d0001, x=0x104800180100000000010000000, w=10; all76 noncore faces agree, so its paired orbitwise maxima have ratio 1/9 at t=1/2. This is not a claim that the global ratio attains 1/9.

**Local executable evidence (SHA-256).** c66_global_linear_section_exact_evidence.json: 7b6d8c98e98f8b579662b7a275462ad522c574d8a695ce18d053cf44965db558; c66_pairwise_exact_evidence.json: 1557153c7074bfcd89375f21b73d333657cfaef4e068fc94851fd291a37281ef; c66_independent_156_edge_evidence.json: 9b887cedde35f6c27367937266989ce6cafe37fcab2e9afd4aeff50bc91ede6d. The complete portable package EM_C66_FULL142_GLOBAL_MASS_DOMINATION_PORTABLE.zip has sha256 f2880c98e1083856c20b871a7ddeb8b6499fdd460a9b42614f39f369bf51d3ab; it contains 557 members incl. original C65 inputs, reproducibility scripts, SHA256 manifest and full proof. The source repository does not yet contain that binary package or independent Driver verification.

**Next smallest unit (C67).** Inspect the precise C46 2^24 competition observer and weights for a proof-preserving mapping to W_+/-; keep the independent full-negative-core conditional-feedback question separate; the native X6-to-three-dimensional-slice transport is unproved. Do not replay the now-resolved auxiliary m+M<=64 conjecture.

Publication intent: durable UNADMITTED draft evidence only, not admission or mathematical authority. Formal Source activity/CLAIM/Driver paths remain separate and require actual authorization and receipts.
