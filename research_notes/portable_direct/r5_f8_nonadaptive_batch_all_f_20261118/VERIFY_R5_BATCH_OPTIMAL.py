#!/usr/bin/env python3
"""R5 all-f fixed-batch theorem; exact standard-library certificate."""
import json,hashlib,itertools,pathlib,sys
SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L=25845652773852463277015040000
U=58182461585441404127941754880
K=range(214,315)
W=[
 ((16,32),set(range(296,313)),296),
 ((0,64),set(range(223,291)),223),
 ((0,1),set(range(214,222)),213),
 ((1,2),{214,*range(216,222)},1),
 ((2,8),set(range(215,222)),2),
]
def verify(path):
    src=pathlib.Path(path).read_bytes()
    assert hashlib.sha256(src).hexdigest()==SHA
    data=json.loads(src)
    assert data["mask_count"]==256
    table=data["counts_and_cohorts"]
    assert sorted(map(int,table))==list(K)
    N={k:tuple(map(int,table[str(k)]["counts"])) for k in K}
    assert all(len(N[k])==256 for k in K)
    for (a,b),expected,w in W:
        for t in [L,U-1]:
            actual={k for k in K if abs(N[k][a]-N[k][b])>t}
            assert actual==expected,(a,b,t,sorted(actual^expected))
    assert sum(w for pair,s,w in W)==735
    tight=[k for k in K if sum(w for pair,s,w in W if k in s)==k]
    assert tight==[214,215,216,223,296],tight
    for k in K:
        assert sum(w for pair,s,w in W if k in s)<=k
    q=(216,223,296)
    counts={1:0,2:0,3:0}
    for a,b in itertools.combinations(range(256),2):
        d=sum(abs(N[k][a]-N[k][b])>U-1 for k in q)
        assert d>=1,(a,b)
        counts[d]+=1
    assert counts=={1:2448,2:12192,3:18000}
    assert sum(counts.values())==32640
    assert 17*sum(q)==12495
    print(json.dumps({"domain":"256 x 101","input_sha256":SHA,
      "checked_pairs":32640,"covered_by_budgets":[216,223,296],
      "separation_multiplicity_distribution":counts,
      "dual_weights":[296,223,213,1,2],"dual_tight_budgets":tight,
      "unique_optimal_batch":"(2*f+1) copies of each 216,223,296",
      "all_f_cost":"735*(2*f+1)","f8_batch_cost":12495,
      "f8_adaptive_interval":[8335,8343],
      "f8_saving_interval":[4152,4160]},sort_keys=True,indent=2))
    print("PASS_R5_256_FIXED_BATCH_ALL_F_FIBER_CERTIFICATE",file=sys.stderr)
if __name__=="__main__":
    assert len(sys.argv)==2,"usage: VERIFY_R5_BATCH_OPTIMAL.py input.json"
    verify(sys.argv[1])
