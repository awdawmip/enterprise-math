# Adjacent-shift proof review

Verdict: PASS within the stated scalar, adjacent-bit, supplied-modulus contract. Shared-context independent derivation review; not independent mathematical admission and not an executed checker. No scientific import, host numeric example, provider query, or remote write was used.

Reviewed complete source: `../ADJACENT_SHIFT_REDUCTION.md`, SHA256 `96757c3624c69bf3ec1e313504f56bb6099d1a79e47032813084b19340c272ad`. Also reread the complete frozen `sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md`, SHA256 `c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf`.

The sign identity s(x)=f(x+V) follows from bit carry into k=ell+1. Periodic extension is legitimate for the proof and requires no negative-index bit computation in an implementation. Writing the interval length as n=L-d, the translation difference is the difference of prefix sums at n+V,n,V,0. Hence the two boundary intervals are correct even for n<V; their overlap cancels algebraically. Because P divides L and f(t)=1 on 0<=t<V, the correction is exactly the stated sum f(t-d)-f(t+d). This also gives zero at the empty endpoint d=L.

The four forward-window pieces yield the three correction pieces with the stated signs, including all junctions at 0,V,2V,3V,P. An independent symbolic collection verifies formula (4): put d=Pq+z, Qa=q+a, Qb=q+b, where a and b are the two threshold indicators. Since P=4V, all terms involving q cancel, leaving

    -2z + 4(z-V)a - 4(z-3V)b.

This is precisely the hinge form (3). Formula (5) then follows by replacing each sum d*Q with b*T[0,1]+R*T[1,1]; no higher or mixed floor product remains. Each correction table needs only degree two, so the existing degree-three backend is sufficient.

Both modular orientations are necessary. Residue zero has heads 0 and R, so the zero displacement is counted once; at a half-modulus residue identical heads must remain duplicated. A head at or beyond L is empty and needs no table. The original raw denominator 4^g is unchanged. At most four top-level ordinary tables per nonempty orientation (two old single-bit plus two corrections), or eight per query, is a correct upper bound. It is not an operation count or a savings measurement.

The symbolic polynomial-bit conclusion uses the paid integer scale sizes and the established fixed-degree Euclidean table algorithm; it is not polynomial in the bit length of the exponent g alone. The extension is arbitrary R and arbitrary ell but fixed adjacent bit gap. It does not acquire unknown order/address information, compress general separated masks, or reorder matrix products.

No substantive correction is required before a separately reviewed implementation/checker stage. This verdict binds only the proof hash above and asserts no new actual arithmetic evidence.

Global-Knowledge-Sync: main@52978d9 / GLOBAL_KNOWLEDGE_V1
