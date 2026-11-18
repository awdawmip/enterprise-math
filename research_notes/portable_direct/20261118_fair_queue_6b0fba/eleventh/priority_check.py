"""Exact U27F-02 checks on public inputs, optionally replay the frozen archive."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys
import tempfile
import zipfile

AB,BC,CD = (0,1),(1,2),(2,3)
ARCHIVE = 'a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7'
BRC = '3f205696709e847909958a153f8fe10d3f6b70f0'
PINS = {'base_case':'e5c8f069391bf8acefefe52853ce70ae53e78180c4f33b693d66100f34ad3434',
        'carry_Q':'acd915da997e0703ae72395e805126b29d841d47a68a435e75af379e40f76708'}


def gitblob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def record(cwm):
    return [cwm.count,str(cwm.total),str(cwm.dominant)]


def advance(x,p):
    v=list(x)
    v[p//2] += 1 if p%2==0 else -1
    return v


def check_local(frames,p):
    reserve,carry,commit=(r['frame'] for r in frames[1:4])
    b=reserve['body_cells'][1]
    bp=advance(b,p)
    assert reserve['held']=={'2':b} and carry['held']=={'2':bp}
    assert reserve['bound']==carry['bound'] and reserve['free']==carry['free']==commit['free']=={}
    assert carry['body_cells'][1]==bp and carry['body_cells']==commit['body_cells']
    assert all(reserve['body_cells'][i]==carry['body_cells'][i] for i in (0,2,3))
    assert str(AB) not in frames[2]['complete'] and str(AB) in frames[3]['complete']
    assert commit['bound']=={**carry['bound'],'2':{'cell':bp,'edge':[0,1],'port':p^1,'side':1}}
    assert commit['held']=={} and frames[2]['modes']==frames[3]['modes']
    # All potential directions except the selected axis fail to appear at B'.
    assert all(r['cell']!=bp for r in carry['bound'].values())
    return {'before_material_B':b, 'after_carry_B':bp, 'after_bind_B':commit['body_cells'][1],
            'body_and_resource_move_port':p, 'registered_word_port':p^1,
            'other_bound_records_at_B_after_carry':0, 'body_moves_during_binding':0}


def role_examples(frames):
    """Two causal decorations of one old positive opportunity, not native laws."""
    carry,commit=(r['frame'] for r in frames[2:4])
    def projection(frame):
        return {key:copy.deepcopy(frame[key]) for key in ('body_cells','held','bound','free')}
    examples=[]
    for named_support in ('a','b'):
        for removed in (None,'a','b'):
            available={'a','b'}-{removed}
            applied=named_support in available
            end=projection(commit if applied else carry)
            state={x:('withdrawn' if x==removed else
                      'spent' if x==named_support and applied else 'ready') for x in ('a','b')}
            assert end['body_cells']==carry['body_cells']
            assert ('2' in end['bound'])==applied and ('2' in end['held'])!=applied
            examples.append(dict(selected=named_support,removed=removed,attached=applied,
                                 support_after=state,ready_for_same_source=(state[named_support]=='ready'),
                                 material_position=end['body_cells'][1],
                                 id2_role='bound_AB' if applied else 'held',
                                 field_successor='UNKNOWN',mechanical_reaction='UNKNOWN'))
    factual=[x for x in examples if x['removed'] is None]
    assert len(factual)==2 and all(x['attached'] for x in factual)
    assert factual[0]['support_after']!=factual[1]['support_after']
    off=[x for x in examples if x['removed']=='a']
    assert [x['attached'] for x in off]==[False,True]
    return examples


def before_move_and_inverse(base, examples, brc):
    """Test both intervention times and both explicit reuse clauses."""
    b = base['body_cells'][1]
    moved = advance(b,4)
    rows = []
    for selected in ('a','b'):
        output = []
        for old_accept,weight in ((True,Q(1,49)),(False,Q(48,49))):
            grew = old_accept and selected != 'a'
            output.append((grew,weight,moved if grew else b))
        success = brc.cwm_from_positive_weights(w for grew,w,pos in output if grew)
        rows.append({'selected':selected,'remove_a_before_move':str(success.total),
                     'material_B_on_old_ACCEPT':output[0][2],'material_B_on_old_REJECT':output[1][2]})
    assert [r['remove_a_before_move'] for r in rows] == ['0','1/49']
    trials = []
    for factual in (r for r in examples if r['removed'] is None):
        name = factual['selected']
        for refund in (False,True):
            state = dict(factual['support_after'])
            assert state[name] == 'spent'
            if refund:
                state[name] = 'ready'
            trials.append({'selected':name,'refund_on_inverse':refund,
                           'support_after_inverse':state,'can_same_source_reenter':state[name]=='ready'})
    assert [t['can_same_source_reenter'] for t in trials] == [False,True,False,True]
    return rows,trials


def exact_brc(brc):
    # Conditional label clock; unconditioned raw proposal has weight 1/384.
    proposal=brc.cwm_edge(Q(1,384))
    accept=brc.cwm_propagate(proposal,brc.cwm_edge(Q(1,49)))
    reject=brc.cwm_propagate(proposal,brc.cwm_edge(Q(48,49)))
    assert (accept.total,reject.total)==(Q(1,18816),Q(1,392))
    mixed=brc.cwm_from_positive_weights([accept.total/2]*2)
    assert mixed.total==accept.total and mixed.count==2 and mixed.dominant<accept.dominant
    fixed=brc.cwm_recoalesce(accept,reject)
    assert fixed.count==2 and fixed.total==Q(1,384) and fixed.dominant==reject.total
    weights=[Q(1,49),Q(48,49)]
    coupling_counts={}
    for case,ws in [('old',weights),('tied',[Q(1,2)]*2),
                    ('multiset',[Q(1,6),Q(1,6),Q(1,3),Q(1,3)])]:
        # Each first-margin singleton admits exactly one partner in the second.
        # Check C/W/M at every opposite bin with the actual source library.
        ok=0
        for pairing in product(range(len(ws)),repeat=len(ws)):
            if all(brc.cwm_from_positive_weights(ws[i] for i,j in enumerate(pairing) if j==k)
                   ==brc.cwm_edge(w) for k,w in enumerate(ws)):
                ok+=1
        coupling_counts[case]=ok
    assert coupling_counts=={'old':1,'tied':2,'multiset':4}
    masks=[]
    for result in product((False,True),repeat=2):
        m=brc.cwm_from_positive_weights(w for keep,w in zip(result,weights) if keep)
        masks.append({'response_on_ACCEPT_REJECT':list(result),'accept_CWM':record(m),
                      'withdrawal_never_enables_old_reject':not result[1]})
    assert {x['accept_CWM'][1] for x in masks if x['withdrawal_never_enables_old_reject']}=={'0','1/49'}
    possible=[(i,j) for i,j in combinations(range(12),2) if len({4//2,i//2,j//2})==3]
    assert len(possible)==40 and len({xy for pair in possible for xy in permutations(pair)})==80
    return {'growth_ACCEPT':record(accept),'growth_REJECT':record(reject),'merged_label':record(fixed),
            'hypothetical_two_way_equal_split_of_ACCEPT':record(mixed),
            'singleton_margin_couplings':coupling_counts,'same_tape_response_maps':masks,
            'unordered_other_signed_ports_in_distinct_axis_candidate':len(possible),
            'ordered_other_signed_ports_in_distinct_axis_candidate':80}


def replay(archive, public):
    assert hashlib.sha256(archive.read_bytes()).hexdigest()==ARCHIVE
    with tempfile.TemporaryDirectory() as td, zipfile.ZipFile(archive) as z:
        assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
        z.extractall(td)
        root=Path(td)/'em_u27_followup'
        unit=root/'baseline/cell_u27'
        assert gitblob((unit/'reuse/sources/brc_weighted.py').read_bytes())==BRC
        for k in PINS:
            assert json.loads((root/'fixtures'/(k+'.json')).read_bytes())==public[k]
        sys.path.insert(0,str(unit))
        h=importlib.import_module('work_exposure')
        budget=h.v.Capped(4,Q(1,16))
        def normalize(data): return json.loads(json.dumps(h.v.encode(data)))
        count=0
        for p in range(4,12):
            ledger=h.v.Ledger(h.f.root_state(),4)
            prep=h.ONE
            for lab in [('mode',BC),('contact',BC,0),('mode',CD)]:
                a,w=h.v.accepted(budget,ledger.s,lab)
                ledger.commit(lab,a)
                prep=h.r.serial(prep,w)
            old=ledger.s
            ids=ledger.validate(stable=True)
            frees=dict(ledger.free)
            assert record(prep)==[1,'1/802816','1/802816']
            label=('body',1,p,True)
            terms=budget.transition(old,label,dict(budget.proposals)[label])
            live=[(t,record(w)) for y,w,t in terms if w.live]
            assert live==[('ACCEPT',[1,'1/18816','1/18816']),('REJECT',[1,'1/392','1/392'])]
            accepted=next(y for y,w,t in terms if t=='ACCEPT')
            refused=next(y for y,w,t in terms if t=='REJECT')
            assert refused==old
            assert h.m.material(old.paths,1,p,True)==accepted.paths
            n=len(ledger.log)
            ledger.commit(label,accepted)
            frames=normalize(list(h.references(old,accepted,ledger.log[n:])))
            if p==4: assert frames==public['carry_Q']['data']
            check_local(frames,p)
            assert len(role_examples(frames))==6
            inv=('body',1,p^1,False)
            restored,back=h.v.accepted(budget,ledger.s,inv)
            assert h.m.material(accepted.paths,1,p^1,False)==restored.paths==old.paths
            assert restored==old and record(back)==[1,'1/392','1/392']
            ledger.commit(inv,restored)
            assert ledger.validate(stable=True)==ids and ledger.free==frees
            count+=1
        return {'archive_sha256':ARCHIVE,'signed_transverse_directions':count,
                'growth_labels_with_two_live_singleton_branches':count,
                'geometric_material_inverses':count,'full_stable_ledger_inverses':count,
                'source_preparation_weight':'1/802816','source_inverse_accept_weight':'1/392',
                'native_support_intervention_in_source':'NOT_DEFINED'}


def write(path,obj):
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path)
    parser.add_argument('--archive',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--details',type=Path)
    a=parser.parse_args()
    candidates=[Path.cwd(),*Path(__file__).resolve().parents]
    repo=a.repo or next((p for p in candidates if (p/'research_inputs/U27F_20261012/fixtures').is_dir()),None)
    if repo is None: parser.error('use --repo PATH to the public enterprise-math checkout')
    assert gitblob((repo/'src/enterprise_math/brc_weighted.py').read_bytes())==BRC
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    fixtures=repo/'research_inputs/U27F_20261012/fixtures'
    pub={}
    for k,v in PINS.items():
        raw=(fixtures/(k+'.json')).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==v
        pub[k]=json.loads(raw)
    d=pub['base_case']; seq=pub['carry_Q']['data']
    assert d['inventory_B']==4 and d['lambda']=='1/48' and d['grow_label']==['body',1,4,True]
    detail=check_local(seq,4)
    examples=role_examples(seq)
    before,inverse=before_move_and_inverse(d,examples,brc)
    raw=(repo/'definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json').read_bytes()
    assert gitblob(raw)=='94a02d067be2b039ca4c0f7ffedb5ebde8430e08'
    world=json.loads(raw)
    p000=json.loads((repo/'p000_reality_foundation.json').read_bytes())
    assert world['signed_primitive_direction_count']==12 and world['time_is_spatial_axis'] is False
    assert p000['typed_semantics']['primitive_force_balance']['primitive_stable_balance_predicate']=='NONZERO_FORCE_COUNT_EQ_3_AND_TRIADIC_CLOSURE_E'
    out={'task_id':'RS-CELL-U27F-02-NATIVE-TRIAD-20261012','public_fixture_sha256':PINS,
         'brc_blob':BRC,'local_geometry':detail,'finite_CWM':exact_brc(brc),
         'conditional_decorations_checked':len(examples),'named_before_move_controls':len(before),
         'conditioned_support_inverse_rules_checked':len(inverse)}
    if a.archive: out['frozen_source_replay']=replay(a.archive,pub)
    if a.details:
        a.details.mkdir(parents=True,exist_ok=True)
        write(a.details/'material_field_support_successor.json',
              {'scope':'Declared comparison extensions only. A native joint successor is not supplied.',
               'postcarry_same_input':detail,'counterfactuals':examples,
               'withdraw_before_move':before,'reuse_after_geometric_inverse':inverse})
        write(a.details/'native_incidence_checks.json',
              {'event':'Q/LOCAL_CARRY to RELATION_COMMITTED','incidence':'UNKNOWN',
               'geometry':detail,'conditional_axes':{'signed_visible':'+E3','hypothesis':'one separately qualified occurrence and three different underlying axes',
               'unordered_partners':40,'ordered_partners':80,'certified_occurrence_triples':0},
               'old_observer':'body cells, identified record slots, explicit path words and modes',
               'scope_of_inverse':'body, path words, mode, free position and resource identity only'})
    if a.output: write(a.output,out)
    else: print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
