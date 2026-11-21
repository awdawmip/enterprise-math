"""Independent direct-menu verification of the 54-edge DAG and rigidity.

Uses all 250 common-transform menus, without the binary forbidden-triple file.
The history triples are typed readouts of the original native program.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations,product
import json,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
POINTS=list(product(range(5),repeat=3))
MENUS=[]
for d,start in product((1,3),POINTS):
    row=[]
    for point in POINTS:
        active=sum(1<<j for j in range(3)if (point[j]-start[j])%5 in (0,d))
        target=sum(point[j]*5**j for j in range(3)if active>>j&1)
        row.append((active,target))
    MENUS.append(row)

@lru_cache(None)
def evaluate(points):
    price=0
    for menu in MENUS:
        cells={}
        for p in points:
            active,target=menu[p]
            targets,count=cells.setdefault(active,(set(),0));targets.add(target)
            if len(targets)>2:return None
            cells[active]=(targets,count+1)
        price+=sum(count for targets,count in cells.values()if len(targets)==2)
    return price

def main(output=None):
    start=time.monotonic()
    initial=json.loads((HERE/'initial.json').read_text());rows=initial['groups'];prices=initial['costs']
    assert len(rows)==12 and sorted(sum(rows,[]))==list(range(125))
    assert prices==[evaluate(tuple(r))for r in rows] and sum(prices)==9996
    graph=json.loads((HERE/'exchange_graph.json').read_text());dag=json.loads((HERE/'exchange_dag.json').read_text())
    labels=[None]*125
    for c,row in enumerate(rows):
        for p in row:labels[p]=c
    assert labels==graph['labels']
    edges=[];tested=0
    for c,row in enumerate(rows):
        for removed in row:
            for added in range(125):
                if added in row:continue
                candidate=tuple(sorted(set(row)-{removed}|{added}));tested+=1
                price=evaluate(candidate)
                if price is not None:edges.append([removed,added,price-prices[c]])
    assert edges==graph['edges']==dag['edges'] and len(edges)==54
    order=dag['topological_order'];assert sorted(order)==list(range(125))
    rank={p:i for i,p in enumerate(order)};assert all(rank[x]<rank[y]for x,y,c in edges)
    adjacency=defaultdict(list)
    for x,y,c in edges:adjacency[x].append(y)
    # Independent forward-path enumeration followed by a Cartesian product.
    # Discovery used reverse paths and a recursive selection tree instead.
    receipts=[]
    discovery=json.loads((HERE/'single_exception_result.json').read_text())['classes']
    for exceptional,old in enumerate(rows):
        choices=defaultdict(list)
        def walk(path,used):
            for y in adjacency[path[-1]]:
                if labels[y]==exceptional:
                    choices[y].append(path+[y])
                elif labels[y] not in used:
                    walk(path+[y],used|{labels[y]})
        for p in range(125):
            if labels[p]!=exceptional:walk([p],{labels[p]})
        assert sum(map(len,choices.values()))==discovery[exceptional]['incoming_paths']
        balanced=legal=0
        for options in product(*[[None]+choices[p]for p in sorted(choices)]):
            paths=[p for p in options if p is not None]
            if not paths:continue
            support=[labels[x]for path in paths for x in path[:-1]]
            if len(support)!=len(set(support)):continue
            balanced+=1
            candidate=tuple(sorted(set(old)-{p[-1]for p in paths}|{p[0]for p in paths}))
            assert len(candidate)==len(old)
            if evaluate(candidate)is not None:legal+=1
        assert legal==0==discovery[exceptional]['legal_nontrivial_selections']
        receipts.append({'exceptional_class':exceptional,'paths':sum(map(len,choices.values())),'balanced_nontrivial_selections_checked':balanced,'legal':legal})
    result={'all_direct_menus':250,'original_cost':9996,'single_replacements_tested':tested,'legal_edges':54,'dag':True,'one_exception_verified':True,'exceptions':receipts,'seconds':time.monotonic()-start}
    if output is not None:Path(output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main(HERE/'exchange_verification.json')
