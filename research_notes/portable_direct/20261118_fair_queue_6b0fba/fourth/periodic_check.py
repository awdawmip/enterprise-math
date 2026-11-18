"""Periodic avoidance certificate. python periodic_check.py [--emit periodic_tree.txt]"""
import argparse
import json
from collections import Counter
from math import gcd
from pathlib import Path

Q=65
CARD=((1,0),(-1,0),(0,1),(0,-1))
KING=CARD+((1,1),(1,-1),(-1,1),(-1,-1))
PARENT={(1,0):'E',(-1,0):'W',(0,1):'N',(0,-1):'S'}
DECODE={c:d for d,c in PARENT.items()}

def allowed(x,y):
    return gcd(x*x+y*y,Q)==1

def quotient(steps):
    vertices={(x,y) for x in range(Q) for y in range(Q) if allowed(x,y)}
    parent={}; pos={}; groups=[]; edges=0
    for root in sorted(vertices):
        if root in parent: continue
        parent[root]='*';pos[root]=(0,0);todo=[root];volt=set()
        for u in todo:
            for dx,dy in steps:
                X,Y=u[0]+dx,u[1]+dy
                v=(X%Q,Y%Q)
                if v not in vertices: continue
                edges+=1
                pred=(pos[u][0]+X//Q,pos[u][1]+Y//Q)
                if v not in parent:
                    parent[v]=PARENT.get((-dx,-dy),'x')
                    pos[v]=pred;todo.append(v)
                volt.add((pred[0]-pos[v][0],pred[1]-pos[v][1]))
        groups.append((len(todo),volt))
    rows=[''.join(parent.get((x,y),'#') for x in range(Q)) for y in range(Q)]
    return groups,edges//2,rows

def verify_tree(rows):
    assert len(rows)==Q and all(len(row)==Q for row in rows)
    owner={}; height={}
    for x in range(Q):
        for y in range(Q):
            assert (rows[y][x]!='#')==allowed(x,y)
            if not allowed(x,y): continue
            v=(x,y);seen=set();chain=[]
            while v not in owner:
                assert v not in seen
                seen.add(v)
                a,b=v;char=rows[b][a]
                if char=='*':
                    owner[v]=v; height[v]=(0,0);break
                dx,dy=DECODE[char];step=((a+dx)//Q,(b+dy)//Q)
                chain.append((v,step));v=((a+dx)%Q,(b+dy)%Q)
                assert allowed(*v)
            while chain:
                u,delta=chain.pop();owner[u]=owner[v]
                height[u]=(height[v][0]-delta[0],height[v][1]-delta[1]);v=u
    for x,y in owner:
        for a,b in CARD:
            X,Y=x+a,y+b; v=(X%Q,Y%Q)
            if not allowed(*v):continue
            assert owner[v]==owner[x,y]
            assert height[v]==(height[x,y][0]+X//Q,height[x,y][1]+Y//Q)
    return Counter(Counter(owner.values()).values())

def torus(period,steps):
    n=Q*period
    # Direct torus adjacency, no voltage data or tree certificates.
    available={(x,y) for y in range(n) for x in range(n) if allowed(x,y)}
    sizes=[]
    while available:
        start=available.pop(); queue=[start]
        for u in queue:
            for dx,dy in steps:
                v=((u[0]+dx)%n,(u[1]+dy)%n)
                if v in available:
                    available.remove(v);queue.append(v)
        sizes.append(len(queue))
    return Counter(sizes)

def horizontal_path():
    # heights at x=0,...,65, encoded by the start of each new run.
    changes={0:1,1:0,4:1,5:2,6:1,7:0,10:1,12:2,14:1,16:0,
             20:1,21:0,25:1,27:0,30:1,31:0,35:1,36:0,39:1,41:0,
             45:1,46:0,50:1,52:2,54:1,56:0,59:1,60:2,61:1,62:0,65:1}
    heights=[]
    for x in range(Q+1):
        heights.append(changes[x] if x in changes else heights[-1])
    assert heights[0]==heights[-1]==1
    assert all(allowed(x,y) for x,y in enumerate(heights))
    assert all(abs(a-b)<=1 for a,b in zip(heights,heights[1:]))
    return heights

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--emit',type=Path);a=parser.parse_args()
    base,edges,rows=quotient(CARD)
    if a.emit: a.emit.write_text('\n'.join(rows)+'\n')
    default=Path(__file__).with_name('periodic_tree.txt')
    actual=default.read_text().splitlines() if default.exists() else rows
    assert rows==actual
    sizes=verify_tree(actual)
    assert all(res<={(0,0)} for _,res in base)
    assert sizes==Counter(size for size,_ in base)
    large,edges2,_=quotient(KING)
    assert len(large)==1 and {(1,0),(0,1)}<=large[0][1]
    h=horizontal_path()
    torus_results={}
    for m in (1,2,3):
        a1,a2=torus(m,CARD),torus(m,KING)
        assert a1=={s:m*m*count for s,count in sizes.items()}
        assert a2=={2304*m*m:1}
        torus_results[str(m)]=[sum(a1.values()),max(a1),sum(a2.values()),max(a2)]
    print(json.dumps({'period':Q,'sieve':[5,13],'vertices':sum(s*c for s,c in sizes.items()),
        'unit_steps':{'edges':edges,'components':sum(sizes.values()),'max':max(sizes),
                      'full_size_histogram':dict(sorted(sizes.items()))},
        'steps_squared_at_most_two':{'edges':edges2,'components':len(large),
                   'span_witnesses':[list(v) for v in sorted(large[0][1])],
                   'horizontal_height_word':''.join(map(str,h))},
        'torus_sheet_side_component_count_and_max_unit_then_diagonal':torus_results},
        indent=2,sort_keys=True))

if __name__=='__main__': main()
