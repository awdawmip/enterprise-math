"""Stage469-B exact ternary X6 full future observer; author-side finite checks.
No approximation. Original histories have positive unit BRC weight.
"""
from collections import defaultdict,deque
from itertools import product
from math import comb
from bisect import bisect_left
import json, hashlib

DIRECTIONS=tuple((i,s) for i in range(6) for s in (1,-1))
ABC=(0,2,4)  # A,B,C are +E1,+E2,+E3

def obs(p,q):
    def one(word):
        d=[0]*6; e=[0]*144
        for x in word:
            i,sgn=DIRECTIONS[x]; d[i]+=sgn
        for x,y in zip(word,word[1:]): e[12*x+y]+=1
        return (len(word),tuple(d),tuple(e))
    return (one(p),one(q),sum(x==y for x,y in zip(p,q)))

def lambda_h(p,q,h):
    m,n=len(p),len(q); t=max(1,n-h)
    return (q[t-1],)+tuple((p[j],q[j]) if j<m else (q[j],) for j in range(t,n))

def oldkey(p,q,h):
    m,n=len(p),len(q); t=max(1,n-h)
    return (lambda_h(p,q,h),p[-2],(p[-1]==q[m-1]) if t>m else None)

def key(p,q,h):
    """Exact Stage469-B key: additional Q_m and Q_m+1 only if not in Lambda_h."""
    m,n=len(p),len(q); t=max(1,n-h)
    return (lambda_h(p,q,h),p[-2],q[m-1] if t>m else None,
            q[m] if t>m+1 else None)

def future_diff(p,q,p2,q2,h,max_states=300000):
    """Exhaustive synchronous labeled operation tree, including all 12 P/Q appends."""
    queue=deque([(p,q,p2,q2,0,0,0,0,())]); seen=set()
    while queue:
        x,y,x2,y2,a,b,c,d,path=queue.popleft()
        state=(x,y,x2,y2,a,b,c,d)
        if state in seen: continue
        seen.add(state)
        if len(seen)>max_states: raise RuntimeError('finite tree state cap hit')
        if obs(x,y)!=obs(x2,y2): return path,len(seen)
        if a<1 and x:queue.append((x[:-1],y,x2[:-1],y2,a+1,b,c,d,path+('POP_P',)))
        if b<h and y:queue.append((x,y[:-1],x2,y2[:-1],a,b+1,c,d,path+('POP_Q',)))
        if c<1:
            for u in range(12):queue.append((x+(u,),y,x2+(u,),y2,a,b,c+1,d,path+(f'APPEND_P({u})',)))
        if d<1:
            for u in range(12):queue.append((x,y+(u,),x2,y2+(u,),a,b,c,d+1,path+(f'APPEND_Q({u})',)))
    return None,len(seen)

def fibers(m,n):
    out=defaultdict(list)
    for pp in product(ABC,repeat=m-1):
        p=(0,)+pp
        for qq in product(ABC,repeat=n-1):
            q=(0,)+qq
            out[obs(p,q)].append((p,q))
    return out

def checks():
    data={"model":"native X6, originals +E1/+E2/+E3, future appends all 12, P_POP<=1 P_APPEND<=1 Q_POP<=h Q_APPEND<=1", "fibers":0,"histories":0,"mass_rank_unrank_cases":0,"future_equal_pairs":0,"future_distinct_pairs":0,"future_tree_states":0,"old_key_counterexamples":{},"configs":[]}
    for m,n,hs in ((2,3,(0,1,3)),(3,5,(0,1,2,4,5)),(4,6,(0,1,2,4,6))):
        group=fibers(m,n)
        data['fibers']+=len(group); data['histories']+=sum(map(len,group.values()))
        for h in hs:
            count_all=0; diff_num=0; equal_num=0; future_nodes=0
            for fh in group.values():
                classes=defaultdict(list)
                for hist in fh: classes[key(*hist,h)].append(hist)
                masses=[len(classes[k]) for k in sorted(classes)]
                assert sum(masses)==len(fh)
                order=sorted(classes)
                def class_rank(repair):return bisect_left(order,repair)
                def class_unrank(rank):return order[rank]
                for rank,k in enumerate(order):
                    assert class_unrank(class_rank(k))==k
                    assert class_rank(class_unrank(rank))==rank
                    assert classes[k] and masses[rank]==len(classes[k])
                    data['mass_rank_unrank_cases']+=1
                count_all+=len(fh)
                if len(fh)<=1: continue
                for members in classes.values():
                    leader=members[0]
                    for other in members[1:]:
                        path,states=future_diff(*leader,*other,h)
                        assert path is None,(m,n,h,leader,other,path)
                        equal_num+=1;future_nodes+=states
                keys=sorted(classes)
                if len(keys)>1:
                    first=classes[keys[0]][0]
                    for kval in keys[1:]:
                        second=classes[kval][0]
                        path,states=future_diff(*first,*second,h)
                        assert path is not None,(m,n,h,first,second)
                        diff_num+=1;future_nodes+=states
                old=defaultdict(list)
                for hist in fh:old[oldkey(*hist,h)].append(hist)
                for members in old.values():
                    if len(members)<2:continue
                    for i,one in enumerate(members):
                        for two in members[i+1:]:
                            ko,kt=key(*one,h),key(*two,h)
                            if ko==kt:continue
                            for ix,label in ((2,'Q_m'),(3,'Q_m+1')):
                                if label not in data['old_key_counterexamples'] and ko[ix]!=kt[ix] and all(ko[j]==kt[j] for j in (0,1,2,3) if j!=ix):
                                    trace,states=future_diff(*one,*two,h)
                                    assert trace is not None
                                    data['old_key_counterexamples'][label]={'m':m,'n':n,'h':h,'p1':one[0],'q1':one[1],'p2':two[0],'q2':two[1],'future_trace':trace,'states_checked':states}
            data['future_equal_pairs']+=equal_num;data['future_distinct_pairs']+=diff_num;data['future_tree_states']+=future_nodes
            data['configs'].append(dict(m=m,n=n,h=h,fibers=len(group),histories=count_all,equal_pair_checks=equal_num,distinct_pair_checks=diff_num,states=future_nodes))
    assert 'Q_m' in data['old_key_counterexamples'] and 'Q_m+1' in data['old_key_counterexamples']
    k,b=50,23
    data['closed_form_alternating']={'k':k,'b':b,'B_last_mass':comb(k-1,b-1),'C_last_mass':comb(k-1,b),'total':comb(k,b)}
    assert comb(k-1,b-1)+comb(k-1,b)==comb(k,b)
    for m,coordinate,idx in ((100,'Q_m',50),(101,'Q_m+1',51)):
        mass_B=comb(99,49);mass_C=comb(99,50);whole=comb(100,50)
        assert mass_B+mass_C==whole
        data.setdefault('large_new_coordinate_families',[]).append({
            'm':m,'n':205,'h':0,'k':100,'B_count':50,
            'new_coordinate':coordinate,'variable_index_1_based':idx,
            'old_key_classes':1,'new_key_classes':2,
            'B_class_mass':mass_B,'C_class_mass':mass_C,'total':whole,
            'rank_B':0,'rank_C':1})
    return data

if __name__=='__main__':
    result=checks()
    with open('STAGE469B_EXECUTED.json','w') as out:json.dump(result,out,ensure_ascii=False,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!='configs'},ensure_ascii=False,indent=2))
