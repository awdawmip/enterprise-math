#!/usr/bin/env python3
"""PREFIX-853 exact finite oracle for fixed-modulus dynamic named BRC recovery.
All arithmetic is exact integer arithmetic over a typed auxiliary positive Q-observer.
"""
import itertools, json


def difference_witness(p, jmask, r, q):
    kmask=((1<<p)-1)^jmask
    for eps in itertools.product((-1,0,1),repeat=p):
        if not any(eps):continue
        if sum(eps[i]!=0 for i in range(p) if (kmask>>i)&1)>2*r:continue
        d=abs(sum(e*(1<<i) for i,e in enumerate(eps)))
        if d and d%q==0:return {'d':d,'eps':list(eps)}
    return None


def bit_neighbors(x,p,h):
    out=[]
    for k in range(min(h,p)+1):
        for positions in itertools.combinations(range(p),k):
            mask=sum(1<<j for j in positions)
            out.append(x^mask)
    return out


def terminal_oracle(p,jmask,r,h,q,w):
    n=1<<p
    kmask=(n-1)^jmask
    neighbors=[bit_neighbors(x,p,h) for x in range(n)]
    for old_k in range(n):
        if old_k&jmask:continue
        admissible=[x for x in range(n) if (((x^old_k)&kmask).bit_count()<=r)]
        indistinguishable={(x,y) for x in admissible for y in admissible if (x-y)%q==0}
        for step in range(1,w):
            indistinguishable={(a,b) for x,y in indistinguishable
                               for a in neighbors[x] for b in neighbors[y]
                               if (a-b)%q==0}
        if any(a!=b for a,b in indistinguishable):
            return False, {'old_known_mask':old_k,
                           'terminal_pair':list(min((a,b) for a,b in indistinguishable if a!=b))}
    return True,None


def all_checks():
    tested=0; checked_observations=0; passcases=0; negative=0
    # Complete all J and parameters p<=3, select representative p=4 J shapes.
    for p in (1,2,3,4):
        jmasks=range(1<<p) if p<=3 else (0,1,2,3,8,12,15)
        for jmask in jmasks:
            for r in range(0,min(2,p)+1):
                for h in range(0,min(2,p)+1):
                    for q in range(3,(1<<p)+2,2):
                        initial = difference_witness(p,jmask,r,q)
                        local = difference_witness(p,0,h,q)
                        for w in (1,2,3):
                            predicted = initial is None and (w==1 or local is None)
                            actual, witness=terminal_oracle(p,jmask,r,h,q,w)
                            assert actual==predicted,(p,jmask,r,h,q,w,predicted,actual,witness,initial,local)
                            checked_observations+=1
                        tested+=1
                        if initial is None and local is None:passcases+=1
                        else:negative+=1
    # Illustrative edge: initial read inexpensive; post-read evolution requires more.
    p,jmask,r,h=4,1,0,1
    q_initial=next(q for q in range(3,(1<<p)+2,2) if difference_witness(p,jmask,r,q) is None)
    q_perpetual=next(q for q in range(3,(1<<p)+2,2)
          if difference_witness(p,jmask,r,q) is None and difference_witness(p,0,h,q) is None)
    assert (q_initial,q_perpetual)==(3,11)
    # If r>=h, initial decoder alone suffices; p6 J={3} r=h=1.
    p,jmask,r,h=6,8,1,1
    q_recover=next(q for q in range(3,(1<<p)+2,2)
                  if difference_witness(p,jmask,r,q) is None)
    assert q_recover==27
    example_bad=25
    assert difference_witness(p,jmask,r,example_bad) is not None
    return {
      'status':'ALL_EXACT_ASSERTIONS_PASSED',
      'arithmetic':'exact integers only; all state-pair paths enumerated without sampling',
      'model':'U(x)=sum(2^i*x_i), x_i in {0,1}; odd fixed q with c_t a power of 2; initial R(z_K;J,r); at most h coordinate flips per later update, including no-op',
      'coverage':{'p':[1,2,3,4],'J':'all subsets if p<=3; p=4 masks 0,1,2,3,8,12,15',
                  'r':'0..min(2,p)','h':'0..min(2,p)','q':'odd 3..2^p+1', 'windows':[1,2,3]},
      'parameter_modulus_cases':tested,'terminal_window_assertions':checked_observations,
      'cases_passing_uniform_lifetime_condition':passcases,
      'cases_failing_uniform_lifetime_condition':negative,
      'examples':{
        'p4_J0_r0_h1':{'initial_single_sample_minimal_odd_q':q_initial,'all_future_samples_minimal_odd_q':q_perpetual},
        'p6_J3_r1_h1':{'fixed_odd_q_minimum':q_recover,'failed_q':example_bad,
                          'divisibility_witness_for_failed_q':difference_witness(p,jmask,r,example_bad)}},
      'universal_proof':'See PREFIX-853 paper: persistence of initial aliases; common-predecessor divergence for local aliases; induction on exact state after successful first observation.'
    }

if __name__=='__main__':
    print(json.dumps(all_checks(),ensure_ascii=False,indent=2,sort_keys=True))
