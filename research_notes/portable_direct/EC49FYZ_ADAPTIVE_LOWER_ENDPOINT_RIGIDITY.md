# EC49FYZ addendum — two exact lower-endpoint prefix types across all phases

Date 2026-11-24. Same frozen BRC16943 auxiliary Boolean observer and parent hypotheses as EC49FYZ_EXACT_PACKED_BLOCK_ALL_PHASES.md at b0134fad8dc42d5da5edf016ae1bc12e92b36aea. Reuse FYU unique deficient support lemma and FYX all-phase weighted distinct-column bound. Let h>=4, c=ceil((15h+6)/11), k=h-4, t=11c-15h-6 (0..10), z=(k-8t)/11 (integer; can be negative). Thus h=11z+8t+4, c=15z+11t+6, d=h+c-1=26z+19t+9. Proposed minimum endpoint m0=28h-19c+10=23z+15t+8. Let S=(1,2,3,4,8,16,64,128,144,192,256,512), n=(3z+2t,2z+t,3z+2t,4z+3t,z+t,z,z,2z,t,t,3z+2t,3z+2t) as in companion note.

## Rigid classification

If m0>h and a winning tree on m0 columns of depth m0+c exists, its zero path reaches exactly d probes, with every column touched, no repeated query, all masks in S, and exactly one deficient support U*, either 394 or 673, with b(U*)=h-1 and all other b(U)>=h.

Proof: use FYX's prefix argument, stopping at earlier complete saturation or depth d. The weighted distinct hit sum is >=47h-9 by FYU, and <=N+19L<=m0+19d=47h-9. All inequalities must be equalities. Earlier complete saturation is impossible (weighted sum >=47h). There is exactly one deficiency of one unit, and its weight must be maximal 9, so it is 394 or 673. Equality forces N=m0,L=d and no repeat, every used mask dual-tight, and each positively weighted support exactly at h except U*. The same determinant-1 matrix A of companion note has a unique solution for each right-hand side (h-1 at U*, h at the other ten weighted supports, and d queries). Explicitly it is n+D_U* with
D_394=(1,0,1,1,0,1,1,1,0,0,1,1),
D_673=(1,1,1,2,1,0,0,0,0,0,1,1).
Each D contains 8 physical columns and 9 probes. These are algebraic residual vectors; they need not cover h=4 as standalone prefixes.

For U*=394, nonnegative multiplicities and all required support coverages are equivalent to z>=max(1,t-1). For U*=673 they are equivalent to z>=t+1. Necessity follows from support 299 (slack z-1) and 211,243 (slack z-t+1) in the former; 211,243 (slack z-t-1) in the latter. Sufficiency follows by the following exact symbolic coefficient check, including the multiplicities. These conditions characterize a feasible all-zero static prefix, not the feasibility of every positive branch of a decision tree. In particular when t>=1 and z=t only the 394 type can attain the lower endpoint. When t>=2 and z=t-1 the 394 type is already feasible although exact static full-cover equality of the companion theorem has not yet begun. If neither prefix type is feasible, M_h cannot equal m0; consequently M_h>=m0+1 (if m0<=h the same follows directly from M_h>h).

## Executed exact check

Use F, S, w, z, t, n and A from the companion note, with h=11*z+8*t+4:
```python
for u,delta in [(394,[1,0,1,1,0,1,1,1,0,0,1,1]),(673,[1,1,1,2,1,0,0,0,0,0,1,1])]:
    x=[v+b for v,b in zip(n,delta)]
    assert A*sp.Matrix(x)==sp.Matrix([h-int(v==u) for v in w]+[26*z+19*t+9])
    print('u',u,'sum',sum(delta),'queries',sum(s.bit_count()*v for s,v in zip(S,delta)))
    slacks={v:sp.expand(sum(a for s,a in zip(S,x) if s&v)-h+int(v==u)) for v in F}
    print('slacks',sorted(map(str,set(slacks.values()))))
    print('bad at z=t',[(v,str(a)) for v,a in slacks.items() if a.subs(z,t).subs(t,0)<0])
    print('thresholds',[(tt,min(zz for zz in range(-20,30) if all(a.subs({z:zz,t:tt})>=0 for a in slacks.values()) and all(sp.sympify(a).subs({z:zz,t:tt})>=0 for a in x))) for tt in range(11)])
```
Exact output:
```
u 394 sum 8 queries 9
slacks ['-t + z + 1', '0', '2*t + 3*z', '2*t + 3*z + 1', '2*t + 4*z + 1', '2*z + 2', '3*t + 4*z', '3*t + 4*z + 1', '3*t + 4*z + 2', '3*t + 5*z + 1', '4*t + 6*z + 1', '4*t + 6*z + 2', '5*t + 8*z + 2', '5*t + 8*z + 3', '6*t + 9*z + 3', 't + 2*z', 't + 2*z + 1', 't + 3*z + 2', 't + z', 'z', 'z - 1']
bad at z=t [(299, 'z - 1')]
thresholds [(0, 1), (1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)]
u 673 sum 8 queries 9
slacks ['-t + z - 1', '0', '2*t + 3*z + 1', '2*t + 3*z + 2', '2*t + 4*z + 1', '2*z - 1', '3*t + 4*z + 1', '3*t + 4*z + 2', '3*t + 5*z + 2', '4*t + 6*z + 2', '4*t + 6*z + 3', '5*t + 8*z + 2', '5*t + 8*z + 3', '6*t + 9*z + 3', 't + 2*z', 't + 2*z + 1', 't + 3*z', 't + z + 1', 'z', 'z + 1']
bad at z=t [(211, '-t + z - 1'), (243, '-t + z - 1'), (721, '2*z - 1'), (753, '2*z - 1')]
thresholds [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)]
```
The full slack expressions supply the unbounded proof; finite thresholds are a crosscheck only. As all displayed slacks other than the identified constraints are nonnegative under the stated conditions, no asymptotic extrapolation is used.

## FYY recovery, exact original source preservation

The four earlier local files were restored to this same branch with exact original Git blob match and content readback:
- EC49FYY_pack.py, commit 3308cedaca57a94d0b54579b12d6d9a4295b03c8, blob b00bef9b36f3c3012bbda34a5f5bb20d32ec9573.
- EC49FYY_pack.out, commit 3c1f6b95ce10dec1e3dbb5889689073149bb8228, blob 7a666b8009f7f32e444c31d5e1d5dd7eacf257b4.
- EC49FYY_terminal.py, commit 3e7eaa5cb388ff6df282dfb1ebb9fc654b11966b, blob a13981ac9a419661c35a4b44420b1fb4a2cc483e.
- EC49FYY_last.py, commit 813baec19fc3c82890076e610ecdaffc187f7823, blob cb65296d1d2921d749f1f34bf0c75654648bc677.
Replayed the terminal program solely to obtain the missing raw terminal log:
```
1 394 31 30 17 True 59
1 673 31 31 17 True 61
2 394 54 41 29 True 81
2 673 54 41 29 True 81
3 394 77 53 41 True 105
3 673 77 53 41 True 105
4 394 100 65 53 True 129
4 673 100 65 53 True 129
```
No new search of earlier positive branches; M15 remains 31 or 32.

## Additional static block witnesses (new numerical optimization with exact integer feasibility check)

Run the preserved FYY_pack.py with range(12,23) and time_limit=3.0 instead of its original settings. Actual output columns: k,L,N,list of (mask,multiplicity), optimizer status, reported dual bound.
```
12 29 21 [(1, 2), (2, 1), (3, 3), (4, 3), (6, 1), (17, 1), (40, 1), (64, 1), (128, 1), (144, 2), (256, 3), (512, 2)] 0 20.999999999999996
13 31 24 [(1, 4), (2, 2), (3, 2), (4, 4), (8, 1), (144, 2), (192, 2), (256, 3), (320, 1), (512, 3)] 0 24.0
14 34 24 [(1, 2), (3, 4), (4, 2), (6, 2), (48, 2), (64, 2), (128, 2), (144, 2), (256, 4), (512, 2)] 0 24.000000000000007
15 36 27 [(1, 3), (2, 3), (3, 3), (4, 6), (9, 3), (144, 3), (256, 3), (512, 3)] 0 26.999999999999776
16 38 31 [(1, 4), (2, 2), (3, 4), (4, 5), (8, 2), (16, 1), (64, 1), (128, 1), (132, 1), (144, 1), (192, 1), (256, 4), (512, 4)] 0 30.99999999999998
17 41 30 [(1, 3), (2, 1), (3, 5), (4, 5), (6, 1), (8, 1), (9, 1), (48, 1), (64, 1), (128, 1), (144, 3), (256, 4), (512, 3)] 0 30.0
18 43 33 [(1, 3), (2, 2), (3, 5), (4, 6), (8, 2), (17, 1), (64, 1), (128, 2), (144, 2), (256, 3), (257, 1), (320, 1), (512, 4)] 0 32.99999999999976
19 45 38 [(1, 5), (2, 3), (3, 5), (4, 7), (8, 2), (16, 1), (64, 1), (128, 2), (144, 1), (192, 1), (256, 5), (512, 5)] 0 38.000000000021714
20 48 36 [(1, 4), (2, 4), (3, 4), (4, 8), (9, 4), (144, 4), (256, 4), (512, 4)] 0 35.99999999999976
21 50 40 [(1, 5), (2, 3), (3, 5), (4, 7), (8, 1), (9, 1), (12, 1), (16, 1), (64, 1), (128, 2), (144, 2), (192, 1), (256, 5), (512, 5)] 0 40.0
22 52 46 [(1, 6), (2, 4), (3, 6), (4, 8), (8, 2), (16, 2), (64, 2), (128, 4), (256, 6), (512, 6)] 0 46.00000000000214
```
Every rounded witness was checked against all 50 exact support inequalities and exact query count by the preserved program. Separate run with range(331,342), time_limit=5.0 produced N=(680,689,679,688,697,687,696,705,695,704,713); these all meet 47k-19L, and the exact symbolic proof now certifies them and their uniqueness. The small-range optimization reports are not all independent exact infeasibility certificates.

## Next

Determine whether either rigid prefix admits a full winning adaptive tree; exploit its small fixed defective vector D, rather than enumerate all column placements. Investigate a finite lower-endpoint base strategy which transports across exact packed blocks. Original terminal replay survives; M15=31 remains unresolved. AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED. Historical researcher EM-DIRECT-23537B; current authenticated writer/owner binding not established.