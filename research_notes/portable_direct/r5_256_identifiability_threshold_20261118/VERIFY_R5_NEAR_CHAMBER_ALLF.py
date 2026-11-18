#!/usr/bin/env python3
"""Exact all-f disjoint witness certificate for the R5 last noise chamber."""
import hashlib,itertools,json,pathlib,sys
SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
T=1876919155234970890319953920000
D=1882951873548292168718745600000
W=[((11,14),list(range(217,218)),217),
   ((4,10),list(range(218,220)),218),
   ((0,64),list(range(224,291)),224),
   ((16,32),list(range(298,312)),298)]
QUERY=(217,218,224,298)
def check(file):
    raw=pathlib.Path(file).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA
    data=json.loads(raw)
    assert data["mask_count"]==256
    K=range(214,315)
    N={k:tuple(map(int,data["counts_and_cohorts"][str(k)]["counts"])) for k in K}
    for (a,b),expected,lower in W:
        for tau in (T,D-1):
            actual=[k for k in K if abs(N[k][a]-N[k][b])>tau]
            assert actual==expected,(a,b,tau,actual)
        assert expected[0]==lower
    assert all(not(set(x[1])&set(y[1])) for x,y in itertools.combinations(W,2))
    freq=[0,0,0,0,0]
    for a,b in itertools.combinations(range(256),2):
        n=sum(abs(N[k][a]-N[k][b])>=D for k in QUERY)
        assert n>=1,(a,b)
        freq[n]+=1
    assert freq==[0,560,2576,11984,17520]
    assert sum(QUERY)==957 and 957*17==16269
    print(json.dumps({"count_table_sha256":SHA,"chamber":[str(T),str(D)],
        "exact_fixed_batch_all_f":"957*(2*f+1)",
        "unique_optimal_multiset":"q=2*f+1 copies each of 217,218,224,298",
        "witness_pairs":[list(w[0]) for w in W],
        "separation_sets":[w[1] for w in W],"coverage_histogram":freq,
        "f8_exact_cost":16269,"unordered_pairs_checked":32640,
        "review":"NOT_REVIEWED"},indent=2))
    print("PASS_R5_LAST_CHAMBER_ALLF_UNIQUE_FIXED_BATCH",file=sys.stderr)
if __name__=="__main__":
    if len(sys.argv)!=2:raise SystemExit("Supply frozen input JSON path")
    check(sys.argv[1])
