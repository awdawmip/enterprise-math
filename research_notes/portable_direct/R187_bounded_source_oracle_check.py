#!/usr/bin/env python3
"""Exact finite source-oracle checks. Stdlib only; no package-native BRC claim."""
import itertools, functools, math, json

def states(k, fixed_r=None):
    rs=range(k+1) if fixed_r is None else [fixed_r]
    return [p for r in rs for p in itertools.permutations(range(k),r)]

def ask(s,U):
    return next((x for x in reversed(s) if x in U), -1)

def minimax(k, fixed_r=None):
    ss=states(k,fixed_r)
    queries=[(i,) for i in range(k)]+list(itertools.combinations(range(k),2))
    answers=[[ask(s,q) for s in ss] for q in queries]
    @functools.lru_cache(None)
    def solve(mask):
        if mask&(mask-1)==0: return 0
        best=len(ss)+1
        for qs in answers:
            groups={}
            left=mask
            while left:
                bit=left&-left
                i=bit.bit_length()-1
                z=qs[i]
                groups[z]=groups.get(z,0)|bit
                left^=bit
            if len(groups)<2: continue
            val=1+max(solve(g) for g in groups.values())
            best=min(best,val)
        return best
    return {"k":k,"r":fixed_r,"states":len(ss),"value":solve((1<<len(ss))-1)}

def reconstruct(s,k):
    comparisons=0
    def pair(x,y):
        nonlocal comparisons
        comparisons+=1
        return ask(s,(x,y))
    def merge_sort(xs):
        if len(xs)<2:return xs
        middle=len(xs)//2
        a=merge_sort(xs[:middle]); b=merge_sort(xs[middle:])
        i=j=0; out=[]
        while i<len(a) and j<len(b):
            if pair(a[i],b[j])!=a[i]:
                out.append(a[i]);i+=1
            else:
                out.append(b[j]);j+=1
        return out+a[i:]+b[j:]
    order=merge_sort(list(range(k)))
    if ask(s,(order[0],))!=-1:
        missing=0
    else:
        missing=1
        while missing<k and pair(order[missing-1],order[missing])==-1:
            missing+=1
    return tuple(order[missing:]),comparisons

def verify():
    out={"schema":"EM_R187_CHECK_V1","arithmetic":"exact integers","scope":"source-only last-occurrence quotient","sort":[],"minimax":[],"one_source":[]}
    for k in range(1,8):
        count=0;most=0
        for s in states(k):
            result,queries=reconstruct(s,k)
            assert result==s,(k,s,result)
            count+=1;most=max(most,queries)
        out["sort"].append({"k":k,"states":count,"max_pair_queries":most,"singleton_queries":1})
    for k in range(1,9):
        for b in range(1,k+1):
            worst=0
            for p in range(k):
                remaining=list(range(k));cost=0
                while len(remaining)>1:
                    U=remaining[:b];cost+=1
                    if p in U:break
                    remaining=remaining[len(U):]
                worst=max(worst,cost)
            expected=math.ceil((k-1)/b)
            assert worst==expected,(k,b,worst,expected)
            out["one_source"].append({"k":k,"b":b,"value":worst})
    for k in range(1,5):
        out["minimax"].append(minimax(k))
        for r in range(k+1):
            out["minimax"].append(minimax(k,r))
    out["total_sort_states"]=sum(e["states"] for e in out["sort"])
    out["minimax_cases"]=len(out["minimax"])
    out["result"]="PASS"
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=="__main__":verify()
