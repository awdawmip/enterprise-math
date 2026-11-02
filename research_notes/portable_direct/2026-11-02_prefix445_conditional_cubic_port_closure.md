# PREFIX-445 — Exact conditional BRC cubic-port closure and one-coordinate repair

Date: 2026-11-02 (Asia/Shanghai). Parent PREFIX-444 at commit 50f39522fa4c11961d41aa9f9e0b105117d0840b. Immutable scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Author proof/exact computation, not independently reviewed or admitted. Native task owner/CLAIM unavailable (CONTROL_QUOTA and read-only Site capability).

## Typed carrier and question

Within P000 signed native X6 Cell-torsor paths, select an auxiliary one-axis restricted subfamily of length-n ordered words in (+e1,-e1). This is a subset of the full six-axis world, not an independent lower-dimensional native world. Each k negative steps gives chart-relative endpoint x=n-2k and residue r=k mod 2. Count c_k is a nonnegative rational branch mass; for unit-weight witness word bags, c_k is an integer not exceeding binomial(n,k), with distinct ordered path identities. Positive rational alternative/serial branches have standard BRC semantics.

For j=0,1,2 let T_{r,j}=sum_{k mod 2=r} c_k x^j; let V_r=sum_{k mod 2=r}c_k x^3 and U3=V0+V1. PREFIX-444's seven-coordinate observer is

J=(T_{0,0},T_{0,1},T_{0,2},T_{1,0},T_{1,1},T_{1,2},U3).

Define a one-step positive rational typed kernel K_{a,b} conditioned on the **incoming** residue: a_r>0 weights the +e1 extension (x'=x+1, r'=r); b_r>0 weights the -e1 extension (x'=x-1, r'=1-r). All weights and branch counts are retained exactly. Put m_r=a_r+b_r.

## Theorem 445.1 (sharp closure criterion)

For all integers n>=7, the updated J(K_{a,b}(c)) is uniquely determined by J(c) for **all** admissible positive-rational source bags c if and only if

a0+b0 = a1+b1.

Sufficiency holds for all n>=0. Under the equality m0=m1=m, the full exact update is

T'_{s,j} = sum_{t=0}^j binom(j,t) [a_s T_{s,t} + (-1)^(j-t) b_{1-s} T_{1-s,t}], for s=0,1, j=0,1,2,

U3' = m U3 + sum_{r=0}^1 [3(a_r-b_r) T_{r,2} + 3m T_{r,1} + (a_r-b_r) T_{r,0}].

Proof: an old r-sector branch generates + and - contributions at residues r and 1-r respectively. Expand (x+1)^j and (x-1)^j binomially. The j<=2 update uses only retained lower moments. The cubic expansion gives (a_r+b_r)V_r plus its three displayed lower-degree terms. When m0=m1 the cubic contribution is m(V0+V1). At every future step the new J is determined, proving closure by induction for finite serial compositions. Positive alternatives add the same coordinates.

Sharp necessity: take the legal n=7 eight-word bags (entries are negative-step counts)
A=(0,3,3,3,4,4,4,7) and B=(1,2,2,2,5,5,5,6).
PREFIX-444 proved J(A)=J(B), and direct integer computation gives V0(A)-V0(B)=384, V1(A)-V1(B)=-384. For the same conditional kernel,

U3'(A)-U3'(B) = 384[(a0+b0)-(a1+b1)].

A nonzero sector-total imbalance thus separates the outputs of equal-J inputs. To obtain witnesses for every n>7, append n-7 common positive steps to each of the original 16 distinct words; residue and distinctness are preserved. The terminal x is translated by n-7; because within each residue lower moments through degree 2 already agree, its cubic difference remains exactly (384,-384). For n<=6, the inherited J reconstructs the endpoint histogram (PREFIX-444), so this necessity assertion is restricted to n>=7.

## Theorem 445.2 (optimal linear moment extension)

Retain the one extra rational cubic coordinate D3=V0-V1. It gives J+=(T_{0,0..3},T_{1,0..3}), equivalent to J plus D3, because V0=(U3+D3)/2 and V1=(U3-D3)/2.

For **arbitrary** positive rational a_r,b_r, including unequal m_r, the exact update closes on J+:

T'_{s,j} = sum_{t=0}^j binom(j,t)[a_s T_{s,t} + (-1)^(j-t)b_{1-s}T_{1-s,t}], s=0,1 and j=0,1,2,3.

Proof: the same positive branch expansion applies at each degree. Therefore arbitrary serial and positive alternative compositions preserve the eight coordinates. For the declared family of linear moment ports extending J, at least one additional coordinate of distinguishing information is necessary if all sector-conditioned kernels are admitted, by the explicit equal-J/different-future witness above; D3 is sufficient. This proves one-coordinate minimality for this declared port extension, not bit-optimality or universal compression of provenance.

At n=7, J+ has rank 8 and reconstructs all eight endpoint counts. At n>7 the port may coalesce distinct histograms, while remaining exact for its declared terminal observer and future language. The full one-axis endpoint histogram has n+1 rational counters, J uses 7, J+ uses 8. This compares scalar coordinate counts only; exact coefficient bit lengths, full branch provenance, and type metadata have separate costs.

## Explicit positive example and executed certificate

Choose a=(2/3,1/2), b=(3/5,1/3). Then (m0,m1)=(19/15,5/6), m0-m1=13/30, and U3'(A)-U3'(B)=832/5. As an exact positive safe example, choose a=(2/3,1/2), b=(3/5,23/30); then m0=m1=19/15, despite unequal conditional + and - weights. Both formerly indistinguishable sources have identical updated J.

The accompanying Python certificate uses only int and fractions.Fraction. It checks actual original six-axis endpoint multiplicities via the byte-verified unchanged frozen source experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py (Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176), and compares direct weighted branch propagation against the exact J+ update. The local exact run covers the A/B witness for every n=7..26; 3^4=81 rational positive conditional kernels, six source bags (n=7,9,14), each checked for two successive updates. The execution log reports 1052 exact J+ step checks, all PASS. This finite computation checks the implementation and examples; the displayed equations and infinite-length witness proof are analytic.

The ordinary upstream ControlPacket, EffectHistogram and MomentState implementations were read at the frozen source pin (brc_control_port.py blob 44def6b8ac787e798d3cc2c6be16f873f91bdb8, brc_transport.py blob be1debe367263931bd5e93fd750be3ed54624fe1); this run executed original signed_brc.py but did not directly import those three classes. This result precisely identifies an augmented, typed cubic state required when future sector-total masses can differ. It is an auxiliary BRC observation theorem, not an asserted native heartbeat physical update.

## Next PREFIX-446

Directly import the unchanged pinned ControlPacket/EffectHistogram/MomentState classes in a complete verified checkout. Exercise n=7 A/B and both conditioned kernels through source/target control state, exact evaluate, alternatives, then, and moment_action. Implement J+ as a separately typed additive cubic port, test legal state-conditioned serial/parallel composition, and measure wall cost, serialisation bits and future-observer closure against full endpoint histograms. Carry forward exact scientific pin, P000, active owner/CLAIM and independent review boundaries.
