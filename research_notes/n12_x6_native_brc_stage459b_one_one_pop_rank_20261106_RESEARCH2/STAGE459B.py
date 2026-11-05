from STAGE459B_CORE import *
def native_observer(p,q):
    V=[];J=[]
    for word in (p,q):
        vv=[0]*6; jj=[0]*144
        for a in word:
            axis=a%6; s=1 if a<6 else -1
            vv[axis]+=s
        for a,b in zip(word,word[1:]):jj[12*a+b]+=1
        V.append(tuple(vv));J.append(tuple(jj))
    return (len(p),len(q),*V,*J,sum(x==y for x,y in zip(p,q)))

def native_word(binary):
    # A=+E1 is letter 0, B=-E1 is letter 6.
    return tuple(0 if x==A else 6 for x in binary)

@lru_cache(None)
def future_tree(p,q,a,b,rp,rq):
    children=[]
    if a and p:children.append(('P_POP',future_tree(p[:-1],q,a-1,b,rp,rq)))
    if b and q:children.append(('Q_POP',future_tree(p,q[:-1],a,b-1,rp,rq)))
    if rp:
        for z in range(12):children.append((('P_APPEND',z),future_tree(p+(z,),q,a,b,rp-1,rq)))
    if rq:
        for z in range(12):children.append((('Q_APPEND',z),future_tree(p,q+(z,),a,b,rp,rq-1)))
    return (native_observer(p,q),tuple(children))


def run():
    instances=nonempty=total_keys=rank_checks=pop_checks=0
    for m in range(2,8):
        for n in range(m+1,min(m+5,10)):
            for kp in range(0,min((m-1)//2,3)+1):
                for kq in range(0,min((n-1)//2,3)+1):
                    for d in range(m+1):
                        F=fiber_histories(m,n,kp,kq,d)
                        for r in (0,1,2):
                            instances+=1
                            C=Counter(m,n,kp,kq,d,r)
                            observed=defaultdict(int)
                            for p,q in F:observed[C.key(p,q)]+=1
                            classes,population=C.total()
                            assert classes==len(observed) and population==len(F),(m,n,kp,kq,d,r,classes,len(observed),population,len(F))
                            if observed:nonempty+=1
                            for key,num in sorted(observed.items()):
                                rank=C.rank(key)
                                assert C.unrank(rank)==key
                                state=(A,A,A,0)
                                qm=qt=qn1=A;v=0
                                for i,z in zip(C.positions,key[1:]):
                                    if i==m:qm=z
                                    if i==C.t:qt=z
                                    if i==n-1:qn1=z
                                    v+=z
                                assert C.mass(key[0],qm,qt,qn1,v)==num,(m,n,kp,kq,d,r,key,num)
                                total_keys+=1;rank_checks+=1;pop_checks+=1
                            assert [C.unrank(i) for i in range(classes)]==sorted(observed)
    # Complete labeled future trees on small nonempty fibers incl 12 append labels.
    future_configs=future_pairs=0
    for m in (3,4,5):
        for n in (m+1,m+2):
            for kp in range(2):
                for kq in range(2):
                    for d in range(0,min(m,3)):
                        F=fiber_histories(m,n,kp,kq,d)
                        if len(F)<2:continue
                        for rp,rq in ((0,0),(1,0),(0,1)):
                            C=Counter(m,n,kp,kq,d,rp)
                            sigs=[future_tree(native_word(p),native_word(q),1,1,rp,rq) for p,q in F]
                            for i in range(len(F)):
                                for j in range(i):
                                    assert (sigs[i]==sigs[j])==(C.key(*F[i])==C.key(*F[j]))
                                    future_pairs+=1
                            future_configs+=1
    big=[]
    for params in ((64,80,15,17,1,0),(64,80,15,17,1,3),(64,80,15,17,1,12),(92,126,20,25,3,15)):
        C=Counter(*params);total=C.total()
        # Boundary ranks of exact class index, confirming no exponential enumeration.
        samples=tuple((i,C.unrank(i)) for i in sorted(set((0,total[0]//2,total[0]-1))) if total[0])
        assert all(C.rank(key)==i for i,key in samples)
        big.append({'params':params,'classes':total[0],'population':total[1],
                    'rank_roundtrip_samples':len(samples),'visible_key_coordinates':1+len(C.positions)})
    result={'marker':'STAGE459B_ONE_ONE_POP_GROUPED_RANK_PASS',
            'small_parameter_runs':instances,'nonempty_runs':nonempty,
            'small_supported_classes_checked':total_keys,'small_rank_roundtrips':rank_checks,
            'small_population_checks':pop_checks,
            'full_future_fibers_checked':future_configs,'full_future_pairs_checked':future_pairs,
            'cached_future_states':future_tree.cache_info().currsize,
            'big_instances':big,
            'model':'native X6 two-source ordered-history observer; binary isolated original defects; positive source-distinct BRC carriers',
            'provenance':'exact standard-library integer execution; 12 signed future APPEND directions; no physical dynamics'}
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':run()
