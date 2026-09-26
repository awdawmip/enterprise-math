"""58 positive probes x15 exact updated operators against retained raw61 modes.
Local bounded implementation regression, not a full Shor circuit replay.
"""
from phase34_closure import *
from stage80.fixed_phase import h4_step,cp_step,reduce_state
from stage83.moving_reader import pointer_control_brc,recorded_row

ZPAIRS=tuple(combinations_with_replacement(range(2),2))
CPAIRS=tuple(combinations_with_replacement(range(10),2));INDEX={ij:k for k,ij in enumerate(CPAIRS)}
def main():
    start=time.perf_counter_ns();vendor=verify_vendor();data=decode(json.loads((OUT/'RESULTS.json').read_bytes()))
    B=data['B'];H=data['H'];native=dict(data['native_operators']);zero=tuple((F(0),)*5 for _ in range(5))
    native.update(I=(F(1),zero,ident(5)),O=(F(0),zero,zero))
    pairs={name:(name,name) for name in data['native_operators']}
    pairs.update({name:('I',name[1:]) for name in ('CV3','CV3inv','CV4','CV4inv')})
    pairs.update(Z0=('I','O'),Z1=('O','I'));actions=tuple(pairs)+('H',);maps={}
    for name in actions:
        mat=[[F(0)]*58 for _ in range(58)]
        if name=='H':
            signs=((1,1),(1,-1))
            for oi,(alpha,beta) in enumerate(ZPAIRS):
                for a in range(2):
                    for b in range(2):mat[oi][ZPAIRS.index(tuple(sorted((a,b))))]+=F(signs[alpha][a]*signs[beta][b],2)
            for oi,(ii,jj) in enumerate(CPAIRS,3):
                alpha,i=divmod(ii,5);beta,j=divmod(jj,5)
                for a in range(2):
                    for b in range(2):mat[oi][3+INDEX[tuple(sorted((5*a+i,5*b+j)))]]+=F(signs[alpha][a]*signs[beta][b],2)
        else:
            pair=pairs[name]
            for oi,(alpha,beta) in enumerate(ZPAIRS):
                sa,Ka,La=native[pair[alpha]];sb,Kb,Lb=native[pair[beta]]
                prod=mm(mm(transpose(Kb),H),Ka)
                T=tuple(tuple(mul(sb,Ka[i][j])+mul(sa,Kb[j][i])+prod[i][j] for j in range(5)) for i in range(5))
                mat[oi][oi]=mul(sa,sb)
                for i in range(5):
                    for j in range(5):mat[oi][3+INDEX[tuple(sorted((5*alpha+j,5*beta+i)))]]+=T[i][j]
            for oi,(ii,jj) in enumerate(CPAIRS,3):
                alpha,i=divmod(ii,5);beta,j=divmod(jj,5)
                La=native[pair[alpha]][2];Lb=native[pair[beta]][2]
                for k in range(5):
                    for l in range(5):mat[oi][3+INDEX[tuple(sorted((5*alpha+k,5*beta+l)))]]+=mul(La[i][k],Lb[j][l])
        mat=tuple(map(tuple,mat));nums,den,cols=rational_matrix_columns(mat);assert transpose(cols)==mat;maps[name]=mat
    doc=json.loads((SOURCE/'stage80/RESULTS.json').read_text())
    rotors={m:FixedRotor(tuple(map(int,doc['phase_gates'][str(m)]['integer_unit_vector'])),64,{'inherited_stage':80,'phase':m}) for m in (3,4)}
    pointer_control_brc()
    def raw_action(sd,name):
        st,den=sd
        if name=='H':return h4_step(st,den,0,61)
        if name[0]=='V':
            rot=rotors[int(name[1])];return reduce_state({k:tuple(rot.apply_numer(v,name.endswith('inv'))) for k,v in st.items()},den*rot.den)
        if name.startswith('CV'):return cp_step(st,den,0,0,rotors[int(name[2])],name.endswith('inv'))
        if name.startswith('Z'):return {k:v for k,v in st.items() if k[0]&1==int(name[-1])},den
        prefix,mode=((('neg',1),('h4',0,1,2,4)),2) if name[0]=='A' else ((('h4',2,3,59,60),),3)
        rows={};dens=[]
        for key,v in st.items():
            mid,md=apply_word(v,den,prefix);selected=recorded_row(mid,mode,int(name[-1]));back,bd=apply_word(selected,md,prefix,True)
            rows[key]=(back,bd);dens.append(bd)
        D=math.lcm(*dens) if dens else 1
        return reduce_state({k:tuple(x*(D//d) for x in v) for k,(v,d) in rows.items() if any(v)},D)
    def raw_vector(pair):
        den=math.lcm(*(x.denominator for row in pair for x in row))
        return {(a,0,0):tuple(int(x*den) for x in row) for a,row in enumerate(pair) if any(row)},den
    # Linear/quadratic extension of the certified BRC row pairings.
    def moments(sd):
        state,den=sd;sectors={}
        for (k,w,h),v in state.items():sectors.setdefault((w,h),{})[k]=tuple(F(x,den) for x in v)
        Z=[F(0)]*3;C=[F(0)]*55;z=(F(0),)*61
        for rows in sectors.values():
            v=(rows.get(0,z),rows.get(1,z));ys=tuple(dot(b,row) for row in v for b in B)
            for i,(a,b) in enumerate(ZPAIRS):Z[i]+=dot(v[a],v[b])
            for i,(a,b) in enumerate(CPAIRS):C[i]+=mul(ys[a],ys[b])
        return tuple(Z+C)
    def apply(q,name):return tuple(dot(row,q) for row in maps[name])
    z=(F(0),)*61;active=[(b,z) for b in B]+[(z,b) for b in B];probes=list(active)
    probes.extend(tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b)) for a,b in combinations(active,2))
    # The projector witness is rational with an odd denominator. The existing
    # raw fixed-word API accepts dyadic preparations only. Scale its ray to an
    # integer vector (same PSD spanning direction); do not weaken that API.
    comp,_=integer_row(data['second_state']['residual'])
    comp=tuple(map(F,comp));probes.extend(((comp,z),(z,comp),(comp,comp)));assert len(probes)==58
    counts={name:0 for name in actions};digests=[]
    for i,probe in enumerate(probes):
        sd=raw_vector(probe);q=moments(sd)
        for name in actions:
            got=apply(q,name);want=moments(raw_action(sd,name))
            assert got==want,('probe mismatch',i,name)
            counts[name]+=1
        digests.append(hashlib.sha256(json.dumps(encode(q),sort_keys=True).encode()).hexdigest())
        if i%10==0:print('positive probe',i,'of58; BRC',len(CALLS),flush=True)
    q=moments(raw_vector(probes[11]));roundtrips={}
    for name in ('V3','V4','CV3','CV4'):
        assert apply(apply(q,name),name+'inv')==q;roundtrips[name]=True
    assert apply(apply(q,'H'),'H')==q
    for name in ('A','D','Z'):
        q0,q1=apply(q,name+'0'),apply(q,name+'1');assert q0[0]+q0[2]+q1[0]+q1[2]==q[0]+q[2]
    result={'schema':'PHASE34_POSITIVE_PROBE_REGRESSION_V1','status':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED',
      'scope':'58 positive covariance probes spanning the reduced58-dimensional carrier;15 scoped actions',
      'positive_probe_count':58,'action_count':len(actions),'input_action_comparisons':sum(counts.values()),
      'counts':counts,'roundtrips':roundtrips,'H_square_identity':True,'outcome_mass_conservation':['A','D','Z'],
      'probe_input_moment_sha256':digests,'actual_BRC_core_calls':len(CALLS),'vendor':vendor,
      'elapsed_ns':time.perf_counter_ns()-start,'not_independent_physical_experiments':True,'full_Shor_regression':False}
    save('REGRESSION_RESULTS.json',result);save('MOMENT_MAPS_58.json',maps)
    save('REGRESSION_ARITHMETIC_CERTIFICATE.json',{'vendor':vendor,'actual_calls':CALLS,'bareiss':ARITHMETIC_AUDIT})
    print('PASS58 probes x15=',sum(counts.values()),'exact comparisons; BRC',len(CALLS),flush=True)

if __name__=='__main__':main()
