# PREFIX-451 — Exact endpoint/history BRC support capacity in native X6

Date: 2026-11-03 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_INTEGER_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. Continues PREFIX-450. Scientific input is frozen at f42f2906d77f24085c123f3ccfe9667d41caa96d. Current rules and P000/ACTIVE X6 worldview were read separately at Enterprise Math main 8abe1a730a2fc95360c53738c63edab8e26cfd4c and global main 35f1c89412ea58b9cf48aa3d0bdf220558d89f34.

## Population and exact question

For integers q>=2, N>=0, let W_N be all ordered legal primitive signed X6 words of length N, steps among ±e_i for i=1,...,6. Endpoint x(w) is in the raw signed Cell-relative chart Z^6. A nonspatial control history sector is r(w) = number of occurrences of -e_1 modulo q. Define S_q(N)={(r(w),x(w)): w in W_N} and H_q(N)=|S_q(N)|. H counts potentially occupied joint endpoint/history bins, not labeled words, not an arbitrary actual sparse source, and not the original affine-effect action histogram.

## Theorem 451.1: Exact endpoint fiber and ordered-path multiplicity

For x in Z^6, m=sum_i |x_i|. If m>N or N-m is odd, x is unreachable. Otherwise T=(N-m)/2 and b1=max(-x_1,0). The exact set of attainable history residues at x is

R_q(N,x) = { (b1+t) mod q : 0<=t<=T },

with cardinality min(q,T+1).

Proof: write u_i,v_i for numbers of positive and negative steps along axis i. Every solution of u_i-v_i=x_i has unique parameters u_i=max(x_i,0)+t_i, v_i=max(-x_i,0)+t_i, t_i>=0. The common word length is equivalent to sum_i t_i=T, and #(-e1)=b1+t_1. Every 0<=t_1<=T is realizable by setting t_2=T-t_1 and all remaining t_i=0; six axes leave such an auxiliary axis. Thus the residues are precisely the indicated consecutive integers modulo q.

In fact, with a_i=max(x_i,0), b_i=max(-x_i,0), the number C_{N,q}(x,r) of distinct ordered words having endpoint x and sector r equals the exact integer sum

C_{N,q}(x,r) =
 sum_{t_1,...,t_6>=0; sum t_i=T; b_1+t_1 ≡ r (mod q)}
  N! / product_{i=1}^6 ((a_i+t_i)! (b_i+t_i)!).

This is a disjoint multinomial enumeration; summing over r recovers the original signed_brc.endpoint_multiplicity(N,x).

## Theorem 451.2: Exact full histogram support generating function

For m>=1 define

a_6(m)=sum_{j=1}^{min(6,m)} 2^j * binom(6,j) * binom(m-1,j-1), and a_6(0)=1.

This counts integer six-vectors with ℓ1 norm m: choose the j nonzero positions, their signs, and a positive integer composition of m. Consequently

H_q(N)=sum_{t=0}^{floor(N/2)} a_6(N-2t) * min(q,t+1).

The exact ordinary generating function is

SUM_{N>=0} H_q(N) z^N = (1+z)^4 (1-z^(2q))/(1-z)^8.

Equivalently, with binom(a,7)=0 when a<7,

H_q(N) =
 sum_{j=0}^4 binom(4,j)
 [binom(N-j+7,7)-binom(N-2q-j+7,7)].

For every fixed integer q>=2, H_q(N)=(2q/45)N^6+O_q(N^5).

Proof: The generating function for a_6 is ((1+z)/(1-z))^6. By Theorem 451.1 each endpoint at ℓ1 norm N-2t contributes min(q,t+1) different sectors. Moreover SUM_{t>=0}min(q,t+1)u^t=(1-u^q)/(1-u)^2; substitute u=z^2 and simplify to the rational function. Expand (1+z)^4 and (1-z)^(-8) for coefficient extraction. In the two shifted degree-seven binomials, the leading powers cancel and the surviving degree-six coefficient is 16*2q/6!=2q/45. Every equality holds for all q>=2, N>=0; no limit argument is used for the finite identities.

At q=3,d=2,N=4 (the PREFIX-450 sharp full quadratic rank duration), all 84=q*binom(8,6) quadratic sector coordinates are linearly independent, while H_3(4)=912+2*72+3*1=1059 endpoint/history bins are attainable. Among the 396 ordered four-step returns to x=0, the sector counts are exactly (270,120,6). The 84 versus 1059 figure compares fixed-degree rational moment coordinate count with dense full joint-histogram support capacity; practical byte costs depend on sparsity, magnitudes and serialization.

## Theorem 451.3: Earliest future-detectable history residual

For all q>=2, the least duration at which two native legal words have the same endpoint and different history sectors is N=2. Explicitly, (+e2,-e2) has r=0, whereas (+e1,-e1) has r=1, and both finish at x=0. Under a future positive-rational BRC control kernel assigning a +e2 effect with weights 1 and 2 on control states 0 and 1 respectively, the resulting endpoint coincides while the total masses differ. At N=0 only the empty word exists; at N=1 the endpoint determines the unique signed native step and hence the history sector. This is a minimal concrete witness of failure of the endpoint-only quotient under the stated future language.

## BRC transport and exact execution

For each history r and primitive signed step v, choose lambda[r,v]>0 in Q; the next sector is s=(r+1_{v=-e1}) mod q. For homogeneous 7x7 quadratic matrices Q_r=sum_x mass(r,x)[x;1][x;1]^T, the existing typed BRC affine law is

Q'_s = SUM_{r,v with target s} lambda[r,v] H_v Q_r H_v^T,
H_v = [[I_6,v],[0,1]].

This retains 28 independent symmetric entries per control sector and is closed under finite weighted alternatives and serial steps. REUSE_APPLIED: frozen brc_transport.py (Git blob be1debe367263931bd5e93fd750be3ed54624fe1), frozen brc_control_port.py (Git blob 44def6b8ac787e798d3cc2c6be16f873f91bdb8). REUSE_EXECUTED: unmodified pinned signed_brc.py endpoint_multiplicity implementation (Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176).

Exact certificate prefix451_joint_support_certificate.py executes standard-library integer/Fraction dynamic programming for q in {2,3,4,7}, all 0<=N<=7, comparing joint support counts to BOTH closed forms, source word count to 12^N, and endpoint multiplicities to 2,220 direct calls of the original pinned signed_brc.endpoint_multiplicity. It verifies the (270,120,6) return example and two consecutive exact positive-rational quadratic BRC moment transfers against independent full joint-histogram propagation, in q=3 sector states with input/output support sizes 316->1059->2984. All assertions passed. Execution stdout is preserved in PREFIX451_EXACT_EXECUTION.log. The program's repo-root invocation is python research_notes/portable_direct/prefix451_joint_support_certificate.py; on a detached evidence archive set EM_PINNED_BRC_PATH to the original verified source copy. The script explicitly checks that source's Git blob.

The original upstream ControlPacket / EffectHistogram / MomentState classes are the next direct-import integration target; this run directly executed frozen signed_brc and independently evaluated the exact affine moment law. The theorem concerns an X6 chart and declared BRC observation language, not a new physical heartbeat dynamic or full labeled path-state reconstruction.

## Next scientific unit and real authority

Next: import the unchanged pinned upstream ControlPacket, EffectHistogram and MomentState classes, instantiate the q=3,d=2,N=4 selected full-rank words and the two-step hidden-sector witness, compare direct effects with moment_action, then benchmark actual sparse/dense serialization bytes and Fraction bit lengths against endpoint/history histograms. Also study dependence on the specific history-count definition before replacing it by more general path functionals.

GitHub authenticated login awdawmip has admin/push permission. Native Site gateway reported research_authority_granted=false and native task listing returned CONTROL_QUOTA. Active Owner, native Researcher-ID and CLAIM therefore remain unconfirmed. This is an author-side durable research frontier only: neither formal Result/Review nor mathematical Admission or Foundation promotion was performed.

Sources: prior PREFIX-450 @84cb80025bd64c7d66f84b4634217416439474a1; frozen scientific source f42f2906d77f24085c123f3ccfe9667d41caa96d; current Enterprise Math canonical control 8abe1a730a2fc95360c53738c63edab8e26cfd4c; current global canonical entry 35f1c89412ea58b9cf48aa3d0bdf220558d89f34; docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context and docs/PORTABLE_RESEARCH_PROTOCOL.md; ACTIVE P000 / Heartbeat X6 / residual fidelity, current math/code/output/BRC rules.
