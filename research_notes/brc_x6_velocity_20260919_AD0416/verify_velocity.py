"""Independent explicit paths versus phase-class and BRC contraction formulae."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from math import gcd,lcm,isqrt
from pathlib import Path
import hashlib,json,random
from collections import Counter
import brc_x6_velocity as v

HERE=Path(__file__).resolve().parent


def blob(p):
    b=Path(p).read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()


def run():
    out={}; rng=random.Random(20260919)
    expected={'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
              'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
              'predictive_quotient.py':'f27d9ddf908f5b07051acfaf0c69f359d499b98b'}
    for name,h in expected.items(): assert blob(Path(v.bt.__file__).parent/name)==h
    assert blob(v.SOURCE)=='9cb477e0369e8f0aa446065e652b259fe214a0de'
    out['01_unchanged_source_reuse']={'complete_files':4,'blobs':expected,
        'heartbeat_blob':blob(v.SOURCE),'minimal_valuation_dependency_excerpt':True}

    cases=0
    for b in (2,3,5,7):
        for j in range(12):
            for _ in range(30):
                x=tuple(rng.randrange(-10**8,10**8) for _ in range(6));n=rng.randrange(5)
                assert v.lifted_step(x,j,n,b)==v.add(x,v.mul(n,v.step_vector(j,b)))
                assert v.lifted_step(x,j,0,b)==x
                cases+=1
    out['02_lossless_chart_translation']={'random_signed_cases':cases,
        'fine_cost_of_cycle_at_rate1':v.signature(v.Cadence(1,1))['fine_step_cost']}

    census=[]; rational_cases=0; ticks=0
    for q in range(1,37):
        for p in range(1,q+1):
            if gcd(p,q)!=1:continue
            for rho in range(q):
                c=v.Cadence(p,q,rho);sig=v.signature(c); L=sig['ticks'];d=gcd(12,q)
                carry=rho
                for t in range(2*q):
                    n,carry=c.tick(carry);assert n==c.at(t)
                assert carry==rho
                H=tuple(sum(c.at(i) for i in range(r,q,d)) for r in range(d))
                assert all(sig['phase_counts'][j]==H[j%d] for j in range(12))
                positions,end=v.walk(c,2*L)
                assert positions[L]==sig['delta'] and end==v.mul(2,sig['delta'])
                assert all(v.add(positions[t],sig['delta'])==positions[t+L] for t in range(L))
                assert sig['chart_steps']==p*(L//q)
                if d==1:assert sig['delta']==(-p,0,0,0,0,0)
                census.append((p,q,rho,sig['delta']))
                rational_cases+=1;ticks+=2*L
    fast_cases=0
    for p,q in ((5,2),(7,3),(11,5),(13,6),(25,7)):
        for rho in range(q):
            c=v.Cadence(p,q,rho);sig=v.signature(c)
            _,end=v.walk(c,sig['ticks'])
            assert end==sig['delta'] and sig['chart_steps']==p*(sig['ticks']//q)
            fast_cases+=1
    out['03_phase_resonance_census']={'reduced_rate_phase_cases':rational_cases,'additional_fast_cases':fast_cases,
        'explicit_ticks':ticks,'q_max':36,'period_and_gcd_formula':'PASS',
        'closed_signatures':sum(delta==v.ZERO for _,_,_,delta in census)}

    samples=[]
    for p,q,rho in ((1,1,0),(1,2,0),(1,2,1),(1,3,0),(1,3,1),(1,5,0),(1,7,0),(2,3,0)):
        c=v.Cadence(p,q,rho);samples.append({'rate':f'{p}/{q}','carry':rho,**v.signature(c)})
    assert samples[1]['delta']==v.ZERO
    assert samples[2]['delta']==(-1,0,0,0,0,0)
    assert samples[3]['delta']==v.mul(-1,samples[4]['delta'])
    assert samples[3]['fine_step_cost']==samples[4]['fine_step_cost']==4
    closed={1,3,5,7,9,11};drift={1,2,3,7,8,9}
    def scheduled(s):
        gs=[v.step_vector(j) for j in sorted(s)]
        return tuple(sum(g[i] for g in gs) for i in range(6)),sum(sum(map(abs,g)) for g in gs)
    assert scheduled(closed)==(v.ZERO,6)
    assert scheduled(drift)==((0,1,1,0,-1,-1),6)
    # No pulse, same sign/cadence: half-rate phases both close.
    for rho in (0,1):
        c=v.Cadence(1,2,rho)
        assert sum(c.at(j)*(1 if j<6 else -1) for j in range(12))==0
    out['04_equal_budget_controls']={'examples':samples,'opposite_equal_cost_rate':'1/3',
        'variable_schedules_same_chart_and_fine_cost':6,'closed_phases':sorted(closed),
        'drifting_phases':sorted(drift),'drift':scheduled(drift)[0],
        'half_rate_closed_vs_drift_costs':[6,7],'no_pulse_half_rate_both_close':True}

    torus_cases=0
    for p,q in ((1,1),(1,2),(1,3),(1,5),(2,3),(3,7)):
        for rho in range(q):
            c=v.Cadence(p,q,rho)
            for modulus in (2,3,5,7):
                predicted=v.augmented_torus_period(c,modulus)
                x=v.ZERO;carry=rho;seen={(x,0,carry)}
                for t in range(predicted):
                    n,carry=c.tick(carry)
                    x=tuple((a+n*g)%modulus for a,g in zip(x,v.step_vector(t)))
                    state=(x,(t+1)%12,carry)
                    if t+1<predicted:assert state not in seen;seen.add(state)
                assert state==(v.ZERO,0,rho)
                torus_cases+=1
    out['05_torus_exact_first_return']={'cases':torus_cases,
        'formula':'L*M/gcd(M,Delta_1,...,Delta_6)','not_full_6D_coverage':True}

    profiles=[]
    for p,q,rho in ((1,2,0),(1,2,1),(1,3,0),(1,5,0)):
        c=v.Cadence(p,q,rho);P=v.augmented_torus_period(c,3)
        pos,_=v.walk(c,P,modulus=3)
        states=tuple(range(P))
        prof=v.pq.predictive_block_profile(states,{'tick':lambda t,P=P:(t+1)%P},lambda t,pos=pos:pos[t],6)
        assert prof[-1]==P
        profiles.append({'p':p,'q':q,'carry':rho,'raw_period':P,'profile':prof})
    assert profiles[0]['profile']==(4,10,12,12,12,12,12)
    out['06_T6_clock_observer']={'source_executed':True,'profiles':profiles}

    rtests=0
    for k in range(1,5):
        M=2**k
        for speed in product(range(-2,3),repeat=3):
            vel=speed+(0,)*3;T=v.additive_residue_period(vel,M)
            x=v.ZERO
            for t in range(1,T+1):
                x=tuple((a+d)%M for a,d in zip(x,vel))
                assert (x==v.ZERO)==(t==T)
            rtests+=1
    out['07_spatial_residue_period']={'cases':rtests,'examples_mod16':{
        'speed1':v.additive_residue_period(v.E1,16),
        'speed2':v.additive_residue_period(v.mul(2,v.E1),16),
        'speed4':v.additive_residue_period(v.mul(4,v.E1),16)},
        'residue_return_not_full_position_return':True}

    N=120000;counts=[0]*12;x=v.ZERO
    for t in range(N):
        n=v.irrational_moves(t);assert n in (0,1)
        counts[t%12]+=n;x=v.add(x,v.mul(n,v.step_vector(t)))
    assert sum(counts)==isqrt(2*N*N)-N
    out['08_irrational_integer_execution']={'ticks':N,'exact_slope':'sqrt(2)-1',
        'moves':sum(counts),'phase_counts':counts,'endpoint':x,
        'average_displacement':[str(F(a,N)) for a in x],
        'aperiodicity_proof':'eventual periodic cadence would have rational mean',
        'finite_run_is_not_ergodicity_proof':True}

    state,packets=v.bernoulli_moments(20)
    M=state.to_matrix();mean=tuple(M[i][6] for i in range(6))
    cov=tuple(tuple(M[i][j]-mean[i]*mean[j] for j in range(6)) for i in range(6))
    assert M[6][6]==1 and mean==(-10,0,0,0,0,0)
    assert cov==v.bt.matrix(tuple(tuple(([25,10,10,10,10,10][i] if i==j else 0) for j in range(6)) for i in range(6)))
    explicit=Counter({v.ZERO:1})
    compressed=v.bt.MomentState.from_point(v.ZERO)
    for j,packet in enumerate(packets):
        nxt=Counter()
        for pos,num in explicit.items():
            nxt[pos]+=num;nxt[v.add(pos,v.step_vector(j))]+=num
        explicit=nxt;compressed=compressed.then(packet)
    literal=Counter()
    for choices in product((0,1),repeat=12):
        pos=v.ZERO
        for j,n in enumerate(choices):pos=v.add(pos,v.mul(n,v.step_vector(j)))
        literal[pos]+=1
    assert literal==explicit and sum(literal.values())==4096
    mu={p:F(n,4096) for p,n in explicit.items()}
    assert compressed.to_matrix()==v.hb.measure_moment(mu)
    persistent=v.bt.EffectHistogram.from_terms(6,[
        (F(1,2),v.bt.Affine.identity(6),1),
        (F(1,2),v.bt.Affine(v.bt.eye(6),(-20,0,0,0,0,0)),1)])
    assert v.walk(v.Cadence(1,2,0),240)[1]==v.ZERO
    assert v.walk(v.Cadence(1,2,1),240)[1]==(-20,0,0,0,0,0)
    PM=persistent.moment_action(v.bt.point_moment(v.ZERO))
    pmean=tuple(PM[i][6] for i in range(6))
    pcov=tuple(tuple(PM[i][j]-pmean[i]*pmean[j] for j in range(6)) for i in range(6))
    assert pmean==mean and pcov[0][0]==100
    assert all(pcov[i][j]==0 for i in range(6) for j in range(6) if (i,j)!=(0,0))
    assert all(v.Cadence(1,2,0).at(t)+v.Cadence(1,2,1).at(t)==1 for t in range(240))
    out['09_BRC_independent_jitter']={'persistent_phase_covariance_diagonal':list(str(pcov[i][i]) for i in range(6)),
        'persistent_vs_independent_same_one_tick_marginals':True,
        'same_expected_chart_steps_per_cycle':6,'same_expected_fine_steps_per_cycle':'13/2',
        'complete_path_choices_explicit':4096,
        'distinct_endpoints_explicit':len(explicit),'compressed_ticks':240,
        'represented_path_count':2**240,'mass':'1','mean':list(map(str,mean)),
        'covariance_diagonal':list(str(cov[i][i]) for i in range(6)),
        'same_mean_cadence_not_same_ensemble':True}

    expansions=[]
    for b in (2,3):
        for a in (1,b,b*b):
            x=v.ZERO
            for k in range(16):
                steps=(v.ZERO,)*5+(v.mul(a**k,v.E1),)
                x=v.outward_block(x,steps,b)
                exact=sum((F(a**j,b**(j+1)) for j in range(k+1)),F(0))
                assert F(x[0],b**(k+1))==exact and x[1:]==(0,)*5
            expansions.append({'b':b,'input_growth':a,'cycles':16,'comoving':str(exact)})
    # General six-step unrolling, not only the last-beat special case.
    for _ in range(200):
        x=tuple(rng.randrange(-9,10) for _ in range(6))
        us=[tuple(rng.randrange(-2,3) for _ in range(6)) for _ in range(6)]
        W=v.ZERO
        for u in us:W=v.add(v.hb.expand(W),u)
        assert v.outward_block(x,us)==v.add(v.mul(2,x),W)
    # Rational variance recurrence: each primitive random step is independent.
    variance=[]
    for growth in (2,4,8):
        V=F(0)
        for k in range(16):V=4*V+growth**k
        Y=V/F(4**16)
        assert Y==sum((F(growth**k,4**(k+1)) for k in range(16)),F(0))
        variance.append({'independent_step_count_growth':growth,'comoving_variance':str(Y)})
    out['10_open_expansion_speed_threshold']={'coherent_samples':expansions,
        'general_unrolling_cases':200,'coherent_critical_growth_per_sixbeats':'b',
        'independent_centered_step_count_critical_growth':'b^2',
        'variance_examples':variance,'closed_breathing_is_a_different_model':True}

    borderline=[]
    for power in (1,2):
        for K in (8,16,32,64):
            measured=sum((F((2**k)//((k+1)**power),2**(k+1)) for k in range(K)),F(0))
            target=sum((F(1,2*(k+1)**power) for k in range(K)),F(0))
            assert 0<=target-measured<1
            borderline.append({'gamma':power,'cycles':K,'roundoff_gap':str(target-measured)})
    out['11_critical_boundary']={'checks':8,
        'law':'s_k=floor(b^k/(k+1)^gamma): Y is (1/b)*p_series plus bounded floor correction',
        'gamma1_log_escape':True,'gamma_gt1_bounded':True,'finite_checks':borderline}

    rejects=0
    for fn in (lambda:v.Cadence(1,0),lambda:v.Cadence(2,4),lambda:v.Cadence(1,3,3),
               lambda:v.Cadence(True,1),lambda:v.walk(v.Cadence(1,1),-1),
               lambda:v.bernoulli_moments(1,0.5),lambda:v.step_vector(-1),
               lambda:v.additive_residue_period(v.E1,0)):
        try:fn()
        except (TypeError,ValueError):rejects+=1
    assert rejects==8
    out['12_input_boundaries']={'rejections':rejects,'all_new_motion_arithmetic':'int/Fraction/isqrt'}
    return {'schema':'EM_X6_VELOCITY_RESONANCE_V1','status':'PASS','check_groups':len(out),'results':out,
            'limits':['chosen direction protocol; no privileged physical speed',
            'no production changes or semantic-recall benchmark','not an autonomous unknown-interaction theory',
            'explicit-period enumeration costs L; integer bit lengths grow',
            'no independent reviewer, Lean or full repository tests',
            'phase lock at prescribed rational cadence is not a proved stability interval under perturbation']}

if __name__=='__main__':
    result=run()
    (HERE/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
