"""Independent exact p=4 graph census for at most one multiport residual."""
from collections import defaultdict, deque
from itertools import product

def dictionary(p):
    raw=defaultdict(dict)
    for i in range(p):
        for j in range(1,p):
            for s in (-1,1):
                c=(1<<i)-s*(1<<j)
                if c:
                    raw[c][j]=raw[c].get(j,0)|(2 if s<0 else 1)
    return dict(raw)

def graph_cyclic_and_longest(word, dic, p):
    states=[(ph,x) for ph in range(4) for x in range(1,1<<p,2)]
    edges={a:[] for a in states}
    indeg=dict.fromkeys(states,0)
    for ph,x in states:
        for j,m in dic[word[ph]].items():
            if m & (1<<((x>>j)&1)):
                b=((ph+1)%4,x^(1<<j))
                edges[(ph,x)].append(b)
                indeg[b]+=1
    queue=deque([v for v in states if indeg[v]==0]); n=0
    longest={v:0 for v in states}
    best=0
    while queue:
        u=queue.popleft();n+=1
        for v in edges[u]:
            longest[v]=max(longest[v],longest[u]+1)
            best=max(best,longest[v]); indeg[v]-=1
            if indeg[v]==0:queue.append(v)
    return n!=len(states),best

if __name__=='__main__':
    d=dictionary(4);s=[c for c,z in d.items() if len(z)==1];multi=[c for c,z in d.items() if len(z)>1]
    count=cyc=mx=0
    for w in product(s,repeat=4):
        r,b=graph_cyclic_and_longest(w,d,4);count+=1;cyc+=r
        if not r:mx=max(mx,b)
    for pos in range(4):
        for w3 in product(s,repeat=3):
            for v in multi:
                word=list(w3);word.insert(pos,v)
                r,b=graph_cyclic_and_longest(word,d,4);count+=1;cyc+=r
                if not r:mx=max(mx,b)
    print({'p':4,'words':count,'cyclic':cyc,'max_finite':mx})
