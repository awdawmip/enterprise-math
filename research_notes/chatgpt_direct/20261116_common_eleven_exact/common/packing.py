"""Exhaust all large color classes and prove ten common-map messages insufficient."""
from collections import Counter
from itertools import product
P=list(product(range(5),repeat=3))
def no_ten(edges):
    def indices(mask):
        while mask:
            bit=mask&-mask;mask^=bit;yield bit.bit_length()-1
    n=125;full=(1<<n)-1;bad=[[0]*n for _ in P]
    for a,b,c in edges:
        for i,j,k in [(a,b,c),(b,c,a),(c,a,b)]:bad[i][j]|=1<<k;bad[j][i]|=1<<k
    anchored=[];nodes=0
    def enum(ch,can,forb,size):
        nonlocal nodes
        if size+can.bit_count()<12:return
        nodes+=1;order=[];un=can;level=0
        while un:
            level+=1;cl=un
            while cl:
                bit=cl&-cl;v=bit.bit_length()-1;order.append((v,level));un^=bit;cl&=un&forb[v]
        for v,lev in reversed(order):
            if size+lev<12:return
            bit=1<<v;can^=bit;d=can&~forb[v];add=ch|bit
            if size+1>=12:anchored.append(add)
            if size+1+d.bit_count()>=12:
                enum(add,d,{w:forb[w]|bad[v][w] for w in indices(d)},size+1)
    enum(1,full^1,bad[0],1)
    shifts=[[25*((x+i)%5)+5*((y+j)%5)+(z+k)%5 for x,y,z in P] for i,j,k in P]
    sets=set()
    for s in anchored:
        ix=list(indices(s));sets.update(sum(1<<d[v] for v in ix) for d in shifts)
    big=sorted(s for s in sets if s.bit_count()==13);small=sorted(s for s in sets if s.bit_count()==12)
    assert len(big)+len(small)==len(sets)
    dis=[sum(1<<j for j,t in enumerate(big) if not(s&t)) for s in big]
    dis12=[sum(1<<j for j,t in enumerate(small) if not(s&t)) for s in big]
    counts=Counter();max_avail={5:0,6:0};fail=False
    def walk(used,rest,compatible,depth):
        nonlocal fail
        counts[depth]+=1
        if depth in (5,6):
            max_avail[depth]=max(max_avail[depth],compatible.bit_count())
            if depth==5:
                # Exactly five large classes: the remaining 60 points need five 12-classes.
                union=used
                for j in indices(compatible):union|=small[j]
                if union==full:fail=True
            else:
                # Six large classes leave 47 points, forcing three 12-classes and one 11-class.
                if compatible:fail=True
        while rest:
            bit=rest&-rest;rest^=bit;j=bit.bit_length()-1
            walk(used|big[j],rest&dis[j],compatible&dis12[j],depth+1)
    for j,s in enumerate(big):
        if s&1:walk(s,dis[j],dis12[j],1)
    assert max(counts)==6 and not fail
    return {'anchored_threshold_search_nodes':nodes,'anchored_classes':len(anchored),'size12_classes':len(small),'size13_classes':len(big),'anchored_disjoint_packings_by_count':dict(sorted(counts.items())),'largest_family_of_still_available_12_classes_after_5_or_6':max_avail,'ten_messages_feasible':False,'minimum_messages_at_least':11}
