"""Exhaust every repartition with one exceptional old class and <=1 deletion
in each of the other old classes, under a size-preserving correspondence.

The complete one-point replacement graph is acyclic. Every nontrivial balanced
reassignment in this family therefore consists of label-disjoint directed paths
ending in the exceptional class, together with its joint replacement.
"""
import argparse,itertools,json
from collections import defaultdict
from functools import reduce
from pathlib import Path
HERE=Path(__file__).resolve().parent

def run(obs):
    source=json.loads((HERE/'initial.json').read_text());rows=source['groups'];prices=source['costs']
    graph=json.loads((HERE/'exchange_graph.json').read_text());labels=graph['labels']
    rev=defaultdict(list)
    for x,y,c in graph['edges']:rev[y].append((x,c))
    raw=obs.read_bytes();pair=[[int.from_bytes(raw[32*(i*125+j):32*(i*125+j+1)],'little')for j in range(125)]for i in range(125)]
    bad=[[0]*125 for _ in range(125)]
    for off in range(125*125*32,len(raw),3):
        for i,j,k in itertools.permutations(raw[off:off+3]):bad[i][j]|=1<<k
    def cost(cl):return sum(reduce(int.__or__,(pair[i][j]for j in cl),0).bit_count()for i in cl)
    summaries=[];winners=[]
    for c,old in enumerate(rows):
        choices={a:[]for a in old}
        def paths(v,mask,price,path):
            for x,delta in rev[v]:
                bit=1<<labels[x]
                if mask&bit:continue
                p=[x]+path
                choices[path[-1]].append((p,mask|bit,price+delta))
                paths(x,mask|bit,price+delta,p)
        for a in old:paths(a,1<<c,0,[a])
        ends=[a for a in old if choices[a]]
        count=nodes=0;best=None;bestpaths=None
        def select(i,mask,used,delta):
            nonlocal count,nodes,best,bestpaths
            nodes+=1
            if i<len(ends):
                select(i+1,mask,used,delta)
                for path,support,d in choices[ends[i]]:
                    if (support^(1<<c))&mask:continue
                    select(i+1,mask|support,used+[path],delta+d)
                return
            if not used:return
            removed={p[-1]for p in used};new=sorted(set(old)-removed|{p[0]for p in used})
            assert len(new)==len(old)
            m=sum(1<<v for v in new)
            if any(bad[x][y]&m for x,y in itertools.combinations(new,2)):return
            count+=1;d=delta+cost(new)-prices[c]
            if best is None or d<best:best=d;bestpaths=list(used)
        select(0,1<<c,[],0)
        summaries.append({'exceptional_class':c,'incoming_paths':sum(map(len,choices.values())),'selection_nodes':nodes,'legal_nontrivial_selections':count,'minimum_cost_change':best,'best_paths':bestpaths})
        if bestpaths:
            result=[set(r)for r in rows]
            for path in bestpaths:
                result[c].remove(path[-1]);result[c].add(path[0])
                for x,y in zip(path,path[1:]):result[labels[x]].remove(x);result[labels[x]].add(y)
            result=list(map(sorted,result));assert sorted(sum(result,[]))==list(range(125))
            winners.append({'exceptional_class':c,'cost':9996+best,'groups':result})
    out={'scope':'one exceptional class, all other corresponding classes lose and gain at most one point; every corresponding class keeps its size','classes':summaries,'winners':winners}
    (HERE/'single_exception_result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(summaries,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--obs',type=Path,required=True);run(p.parse_args().obs)
