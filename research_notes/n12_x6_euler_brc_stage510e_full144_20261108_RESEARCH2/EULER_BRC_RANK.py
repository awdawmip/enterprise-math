"""Euler–BRC exact lexicographic rank/unrank of native-direction words.
All 12 signed X6 direction symbols and all 144 ordered edges active.
Unlabeled parallel edges are indistinguishable; directed last-exit arborescence
count via exact Bareiss determinant and factorial quotient.
"""
import hashlib, itertools, json, math, random, resource, time
from functools import lru_cache

Q=12

def det(a):
    n=len(a)
    if n==0:return 1
    a=[row[:] for row in a]
    sign=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*piv-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
            a[i][k]=0
        prev=piv
    return sign*a[-1][-1]

def count_flat(flat,s,t,q):
    edges=sum(flat)
    if edges==0:return int(s==t)
    out=[sum(flat[i*q+j] for j in range(q)) for i in range(q)]
    inn=[sum(flat[i*q+j] for i in range(q)) for j in range(q)]
    if any(out[i]-inn[i] != int(i==s)-int(i==t) for i in range(q)):
        return 0
    active=[i for i in range(q) if out[i]+inn[i]]
    if t not in active:return 0
    nonroot=[i for i in active if i!=t]
    mat=[]
    for i in nonroot:
        row=[]
        for j in nonroot:
            row.append(sum(flat[i*q+k] for k in active if k!=i) if i==j
                       else -flat[i*q+j])
        mat.append(row)
    tau=det(mat)
    if tau==0:return 0
    num=tau
    for i in active:
        exponent=out[i]-1+int(i==t)
        assert exponent>=0
        num *= math.factorial(exponent)
    den=1
    for x in flat:den*=math.factorial(x)
    assert num%den==0,(num,den,s,t,flat)
    return num//den

def brute(m,s,t,q):
    if not any(any(row) for row in m):return int(s==t)
    result=0
    for x in range(q):
        if m[s][x]:
            m[s][x]-=1
            result+=brute(m,x,t,q)
            m[s][x]+=1
    return result

def flat(m):return tuple(x for row in m for x in row)

def build_word(m,s):
    m=[row[:] for row in m]
    stack=[s];out=[];q=len(m)
    while stack:
        v=stack[-1]
        j=next((j for j in range(q) if m[v][j]),None)
        if j is None:out.append(stack.pop())
        else:m[v][j]-=1;stack.append(j)
    assert all(x==0 for row in m for x in row)
    return out[::-1]

def rank_word(m,w,end,completions):
    q=len(m);m=[row[:] for row in m];rank=0
    for v,x in zip(w,w[1:]):
        for j in range(x):
            if m[v][j]:
                m[v][j]-=1
                rank+=completions(flat(m),j,end,q)
                m[v][j]+=1
        assert m[v][x]>0
        m[v][x]-=1
    assert w[-1]==end and sum(map(sum,m))==0
    return rank

def unrank_word(m,s,t,rank,completions):
    q=len(m);m=[row[:] for row in m];w=[s];l=sum(map(sum,m))
    for _ in range(l):
        v=w[-1]
        for j in range(q):
            if m[v][j]:
                m[v][j]-=1
                c=completions(flat(m),j,t,q)
                if rank<c:
                    w.append(j);break
                rank-=c;m[v][j]+=1
        else:raise AssertionError('rank out of range')
    assert rank==0 and w[-1]==t
    return w

def test_small():
    tests=0
    for q,base in ((2,3),(3,2)):
        for digits in itertools.product(range(base),repeat=q*q):
            if sum(digits)>7:continue
            matrix=[list(digits[i*q:(i+1)*q]) for i in range(q)]
            for s in range(q):
                for t in range(q):
                    actual=brute(matrix,s,t,q)
                    formula=count_flat(digits,s,t,q)
                    assert actual==formula,(q,digits,s,t,actual,formula)
                    tests+=1
    return tests

def run():
    t0=time.perf_counter();small=test_small();t_small=time.perf_counter()-t0
    q=Q
    m=[[1+((i*j+i+j)%3) for j in range(q)] for i in range(q)]
    assert all(m[i][j]==m[j][i] for i in range(q) for j in range(q))
    multiplicities={k:sum(x==k for row in m for x in row) for k in (1,2,3)}
    start=0;target=0
    cache=lru_cache(maxsize=None)(count_flat)
    t0=time.perf_counter();total=cache(flat(m),start,target,q);t_count=time.perf_counter()-t0
    assert total>0
    w=build_word(m,start)
    assert len(w)==1+sum(map(sum,m)) and w[-1]==target
    t0=time.perf_counter();rank=rank_word(m,w,target,cache);t_rank=time.perf_counter()-t0
    assert 0<=rank<total
    t0=time.perf_counter();restored=unrank_word(m,start,target,rank,cache);t_unrank=time.perf_counter()-t0
    assert restored==w
    # Three exact boundary values with same original full inventory.
    w_first=unrank_word(m,start,target,0,cache)
    w_last=unrank_word(m,start,target,total-1,cache)
    assert rank_word(m,w_first,target,cache)==0
    assert rank_word(m,w_last,target,cache)==total-1
    mid_rank=total//2
    t0=time.perf_counter();mid_word=unrank_word(m,start,target,mid_rank,cache)
    t_mid_unrank=time.perf_counter()-t0
    cold_rank_counter=lru_cache(maxsize=None)(count_flat)
    t0=time.perf_counter();mid_recovered_rank=rank_word(m,mid_word,target,cold_rank_counter)
    t_mid_rank=time.perf_counter()-t0
    assert mid_recovered_rank==mid_rank
    mid_info=cold_rank_counter.cache_info()
    random_rank=random.Random(20261108).randrange(total)
    random_unrank_counter=lru_cache(maxsize=None)(count_flat)
    t0=time.perf_counter();random_word=unrank_word(m,start,target,random_rank,random_unrank_counter)
    t_random_unrank=time.perf_counter()-t0
    random_rank_counter=lru_cache(maxsize=None)(count_flat)
    t0=time.perf_counter();recovered_random_rank=rank_word(m,random_word,target,random_rank_counter)
    t_random_rank=time.perf_counter()-t0
    assert recovered_random_rank==random_rank
    random_unrank_info=random_unrank_counter.cache_info()
    random_rank_info=random_rank_counter.cache_info()
    info=cache.cache_info()
    return {'stage':'510-E','status':'ALL_ASSERTIONS_PASS',
      'original_native_directions':12,'ordered_active_relations':144,
      'edge_multiplicities':multiplicities,'edges':len(w)-1,
      'lex_word_total_decimal_digits':len(str(total)),
      'lex_word_total_decimal':str(total),
      'lex_word_total_bit_length':total.bit_length(),
      'selected_word_rank_bit_length':rank.bit_length(),
      'mid_rank_bit_length':mid_rank.bit_length(),
      'mid_rank_roundtrip':mid_recovered_rank==mid_rank,
      'random_rank_bit_length':random_rank.bit_length(),
      'random_rank_decimal':str(random_rank),
      'random_word_sha256':hashlib.sha256(bytes(random_word)).hexdigest(),
      'random_word_length':len(random_word),
      'random_rank_roundtrip':recovered_random_rank==random_rank,
      'small_bruteforce_cases':small,
      'timing_seconds':{'small_independent_check':round(t_small,4),
          'count':round(t_count,4),'rank':round(t_rank,4),
          'unrank':round(t_unrank,4),
          'cold_mid_rank':round(t_mid_rank,4),'warm_mid_unrank':round(t_mid_unrank,4),
          'cold_random_rank':round(t_random_rank,4),
          'cold_random_unrank':round(t_random_unrank,4)},
      'cached_subproblem_states':info.currsize,'cache_hits':info.hits,
      'cold_mid_rank_cached_states':mid_info.currsize,
      'cold_random_rank_cached_states':random_rank_info.currsize,
      'cold_random_unrank_cached_states':random_unrank_info.currsize,
      'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      'first_word_head':w_first[:20],
      'last_word_head':w_last[:20],
      'reference_word_head':w[:20], 'mid_word_head':mid_word[:20],
      'random_word_head':random_word[:20],
      'full_inventory_recovered':restored==w,
      'rank_0_and_max_roundtrip':True}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
