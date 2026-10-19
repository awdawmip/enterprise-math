# RSA-270 second-layer search and GNFS frontier

Progress-Event-ID: `rsa270-second-layer-nfs-frontier-4c8d2a`
At: `2026-09-06T09:02+08:00`
Scope: `enterprise-math`
Source: `ChatGPT project conversation / exact integer experiments / current public RSA-260 and RSA-270 disclosures`
Kind: `HANDOFF`

## Event

Continued the factor-blind RSA-270 semiprime-tree experiment from the 2026-09-05 neighbor audit. BRC observer discipline was retained: branch identities `(k,j)` and exact integer defects were preserved; low residuals were not promoted to factor evidence without an exact square/gcd witness.

1. Second-layer exact endpoint scans. For `x0=ceil(sqrt(4*k*N))` and `d_(k,j)=(x0+j)^2-4*k*N`, an exact square `d_(k,j)=y^2` would give `(x-y)(x+y)=4*k*N`. Exhaustive integer scans found no exact square endpoint for `j=0` over `k<=10,000,000`. The best normalized near-square point in `5M<k<=10M` was at `k=5,363,375` with error about `2.29e-8`, statistically compatible with an extreme among millions of generic trials and not a factor signal. Priority branches `k={1,10,18,20,47,52,62,5,363,375}` were scanned through `j<=5,000,000` with modular square filters: zero exact hits. After construction-family analysis singled out `k=2`, that branch was scanned through `j<=50,000,000`: zero exact hits. Small-k/small-j search was reclassified as a special low-denominator-ratio probe; generic useful denominators reach Lehman scale `k~N^(1/3)`.

2. Ratio-prediction falsifier. On 250 synthetic 895-bit semiprimes with hidden known factors, second-layer low-defect `k` branches (k<=5000, balanced divisor ratios) did not predict `q/p`: median best log-ratio error among the ten lowest-defect branches was worse than a random-ten control, and the low-defect set beat random only about 41.2%. Therefore second-layer near-square minima alone are not a deployable factor-ratio oracle.

3. Classical one-shot probes. Pollard p-1 stage 1 through B1=5,000,000 returned gcd 1. Williams p+1 across several Lucas parameters through B1=2,000,000 returned gcd 1. Multiple SymPy ECM batches (including B1=10k/B2=100k and B1=20k/B2=200k) returned no factor. Continued-fraction square-congruence sampling through 100,000 steps yielded no B=10,000 fully smooth relation and no repeated stripped large cofactor; peeling the best residuals with primes through 1,000,000 still left a best residual around 345 bits. No factor was obtained.

4. New construction-family out-of-sample evidence. RSA-260 was publicly factored on 2026-09-03. Its factors multiply back exactly, have bit lengths 431/431, both satisfy `2 mod 3`, and both begin with binary `11`. This is an out-of-sample confirmation of the 2026-08-31 construction-family study based only on solved original Challenge numbers through RSA-250. Applying the same documented/or observed family rules to 895-bit RSA-270 gives the plausible factor profile 447-bit x 448-bit, both `2 mod 3`, both starting `11`. Combining `N` with these high-bit intervals forces both first three bits to `111` and confines the factor ratio to roughly 1.765..2.266. This is a construction-family prior, not a theorem about the unknown factors.

5. Exact high-prefix branch entropy. Starting from `11 x 11` with the 447/448-bit allocation and pruning prefix-pair boxes whose product interval cannot contain exact RSA-270, the 3-bit pair is uniquely `111 x 111`; survivor counts then grow approximately by factor two per added paired bit: t=4:3, 5:7, 6:15, 7:31, 8:61, 10:241, 12:963, 16:15401, 20:246427, 23:1971413, 24:3942827. Thus the construction prior supplies a constant-size entropy reduction but does not make bitwise branch search tractable.

6. Public RSA-270 GNFS polynomial. A newly public degree-6 polynomial was transcribed and independently validated. Algebraic coefficients c0..c6 are:
`364247333275683342472365165550476120730693693328818157502991593984`,
`1153973715089888191946389898261544454239234565820467806984`,
`-236435216210702701902151548470267342947180119662`,
`-44103587181491086831987630081373613537`,
`4057688710924064290332793594`,
`118153186763991104`,
`240240`;
linear side `Y0=-99499021054511834692076135344701239177544641`, `Y1=6382870559300260766501`, skew `14627893992.01`.
The common modular root check passes; polynomial content is 1; the degree-6 polynomial is irreducible over Z; gcd(discriminant,N)=1; and the exact resultant `Res(f,Y1*x+Y0)` equals RSA-270 itself. Additional leakage checks found gcd 1 for `f(m)/N`, `(Y1*m+Y0)/N`, every nonzero univariate derivative through order 6, every nonzero homogeneous partial derivative through total degree 6, each of the seven resultant terms, all proper subset sums, and the full `{-1,0,1}^7` signed recombination family. No factor leakage was found.

7. Polynomial root-property comparison. Using projective root counts and Murphy alpha local terms, with ramified primes handled by explicit p^k root lifting until stable and an exact geometric tail, the truncated values through p<=1,000,000 are approximately `alpha_RSA260=-9.5870251` for the newly disclosed RSA-260 degree-6 polynomial and `alpha_RSA270=-12.7158059` for the public RSA-270 polynomial, a stable difference about `-3.12878`. The RSA-270 polynomial therefore has materially better root property on this common metric; the difference corresponds to an effective algebraic log-norm advantage factor `exp(3.12878)~22.9`, although RSA-270's size terms remain larger. This is not a full Murphy-E computation.

8. Current CADO-NFS has an experimental `parameters/factor/params.c270` with degree 6, `lim0=1071225238`, `lim1=2146644785`, `lpb0=38`, `lpb1=39`, `mfb0=109`, `mfb1=120`, `I=18`, and `qmin=1073322392`. The public polynomial can in principle be imported to skip polynomial selection. No public repository containing the poster's claimed GPU+CPU RSA-270 sieve pipeline was located in this turn.

## Artifacts

Prior durable audit: `journal/enterprise-math/2026-09-05/20260905T211800+0800-rsa270-semiprime-tree-neighbor-audit-7f31c2.md`.
Current exact computations were conversation-local Python; authoritative public/source repository parameters were read through connected GitHub/web sources. No RSA-270 factor was found.

## Next

Treat the validated GNFS polynomial plus current CADO c270 parameter scale as the main computational frontier. Apply BRC at the NFS relation layer: preserve rational/algebraic norm branch identity and test whether provenance-aware relation scoring/recoalescence can reduce relation collection or filtering cost without merely renaming standard lattice sieving. Continue monitoring for release of the claimed RSA-270 GPU+CPU sieve pipeline or relations. Do not resume blind linear expansion of small-k/small-j Fermat scans unless new factor-ratio information appears.
