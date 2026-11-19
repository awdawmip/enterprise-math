"""Independent integer certificate checker for the frozen R11 eight-node orbit."""
import argparse
from collections import Counter
from functools import lru_cache
import gzip
import hashlib
import json
from itertools import product
import os
from pathlib import Path
import sys
import zipfile

HERE = Path(__file__).resolve().parent
ARCHIVE_SHA = 'e5f24f3777233ec7597d1f7e50a720bbcc097a6f3d6ec9f2567f08bc01b6f344'
MEMBER_INDEX = 'b57ffb2672ee1e4e11a8c8eb75bbaf18bd9578d9aa7d4143df07094c6d5dfef0'
SITES = 5832
MATERIAL = tuple(range(728, 736))
WALL = (0,)*9
CLASSES = ('RECOVERED', 'NEW_CYCLE', 'UNKNOWN_BUDGET', 'NOT_RUN','INPUT_UNAVAILABLE')
GATE = {'site_count': SITES, 'material_indices': list(MATERIAL), 'gate':[0],
        'feedback':[1,2,0], 'port_delays':[1,2,3], 'closed_material_cube':True,
        'initial_reference_clock':1, 'field_order':['q','pending','wall','b'],
        'exterior_background':'absolute_time_mod_3',
        'flow_labels':['groups:vertex:precontact','commit:vertex:port:role','handoff:vertex:port:role']}


class Rejected(ValueError):
    def __init__(self, code, detail=''):
        self.code = code
        super().__init__(code + (' '+str(detail) if detail else ''))


def require(ok, code, detail=''):
    if not ok:
        raise Rejected(code,detail)


def unique_object(pairs):
    result={}
    for key, value in pairs:
        require(key not in result,'duplicate_json_key',key)
        result[key]=value
    return result


def parse(text):
    return json.loads(text,object_pairs_hook=unique_object)


def digest(value):
    return hashlib.sha256(value).hexdigest()


def check_manifest(manifest, archive=None):
    require(manifest['schema']=='r11-delay-certificate-v1' and
            manifest['task_id']=='RS-R11-ONE-TICK-DELAY-ATLAS-LOCAL-REPAIR-20260930' and
            manifest['input_repository_revision']=='88e814717bd60144e6a5add07fc4ab596d483b62',
            'source_revision')
    for key, expected in GATE.items():
        require(manifest['observer'].get(key)==expected, 'model_'+key)
    require(manifest['budget']=={'cases':144,'ticks_per_case':256,'cpu_seconds':1800,
                                'rss_bytes':1073741824}, 'budget')
    receipt = manifest['archive']
    require(receipt['sha256']==ARCHIVE_SHA and receipt['bytes']==4930674,
            'archive_receipt')
    members=receipt['members']
    require(len(members)==42 and digest(json.dumps(members,sort_keys=True,
             separators=(',',':')).encode())==MEMBER_INDEX,'archive_member_index')
    if archive:
        path=Path(archive)
        require(path.stat().st_size==receipt['bytes'] and digest(path.read_bytes())==ARCHIVE_SHA,
                'original_archive_bytes')
        with zipfile.ZipFile(path) as bundle:
            require(len(bundle.infolist())==42 and set(bundle.namelist())==set(members),
                    'original_archive_directory')
            for name, item in members.items():
                raw=bundle.read(name)
                require(len(raw)==item['bytes'] and digest(raw)==item['sha256'],
                        'original_member_bytes',name)

            coords=parse(bundle.read(next(n for n in members if n.endswith('/COORDINATES.json'))))['cells']
            positions={tuple(v['z']):index for index,v in enumerate(coords)}
            require(len(coords)==SITES and
                    tuple(positions[(1,1,1,*v)] for v in product((0,1),repeat=3))==MATERIAL,
                    'original_material_addresses')
            prefix='residual_cycle_R11/run1/'
            records=parse(gzip.decompress(bundle.read(prefix+'CERTIFICATES.json.gz')))
            unperturbed=next(record for record in records if record['case']=='uniform-0')
            for phase in range(6):
                short=unperturbed['prefix_and_cycle'][phase+1]
                q,pending,w,b=orbit_field(phase)
                require(short=={'t':phase+1,'waiting':[list(z) for z in q],
                                'pending':[list(z) for z in pending],'wall':[list(z) for z in w],
                                'background_at_network':[b[i] for i in MATERIAL]},
                        'original_periodic_fields',phase)
            for t in (1000000,1000000000007):
                snapshot=parse(gzip.decompress(bundle.read(prefix+f'FULL_STATE_{t}.json.gz')))
                require(snapshot['t']==t and len(snapshot['cells'])==SITES,'original_snapshot_length')
                nodes,outer=baseline((t-1)%6)
                network=dict(zip(MATERIAL,nodes))
                empty=((0,0,0),(),WALL,outer)
                for i,(got,coordinate) in enumerate(zip(snapshot['cells'],coords)):
                    q,slots,wall,b=network.get(i,empty)
                    want=[coordinate['N'],*q,list(wall),[list(s) for s in slots],
                          int(b==0),int(b==1),int(b==2)]
                    require(got==want,'original_full_observer_row',i)


def form(mass, pending, wall, phase):
    return (tuple(mass),tuple(sorted(pending)),tuple(wall),phase)


@lru_cache(maxsize=6)
def baseline(phase):
    t=phase+1
    if t%2:
        node=form((2,1,1),[(1,1,1,1),(2,2,2,1)],WALL,2)
    else:
        node=form((1,1,0),[(0,0,1,1),(1,1,2,1),(2,2,1,1),(2,2,3,1)],WALL,1)
    return (node,)*8, t%3


def inject(start,v,j,role,r):
    nodes, outer=start
    mass,slots,wall,phase=nodes[v]
    pending=Counter({(a,b,c):n for a,b,c,n in slots})
    require(pending[j,role,r]>0, 'injection_positive_slot')
    pending[j,role,r]-=1
    pending[j,role,r+1]+=1
    node=form(mass,[(*slot,n) for slot,n in pending.items() if n],wall,phase)
    return nodes[:v]+(node,)+nodes[v+1:],outer


def tick(state):
    nodes, outer=state
    qs=[list(q) for q,slots,wall,phase in nodes]
    next_slots=[Counter() for _ in nodes]
    inc=Counter()
    for v,(_,slots,_,_) in enumerate(nodes):
        for j,role,r,n in slots:
            if r==1:
                qs[v ^ (4>>j)][role]+=n
                inc[f'handoff:{v}:{j}:{role}']+=n
            else:
                next_slots[v][j,role,r-1]+=n
    after=[]
    for v,(oldq,oldp,wall,phase) in enumerate(nodes):
        phase=(phase+1)%3
        if phase==0 and min(qs[v])>0:
            qs[v]=[n-1 for n in qs[v]]
            inc[f'groups:{v}:0']+=1
            phase=1
            for j in range(3):
                next_slots[v][j,j,j+1]+=1
                inc[f'commit:{v}:{j}:{j}']+=1
        after.append(form(qs[v],[(*s,n) for s,n in next_slots[v].items()],wall,phase))
    return (tuple(after),(outer+1)%3),inc


def full_field(state):
    nodes,bext=state
    b=[bext]*SITES
    for location,node in zip(MATERIAL,nodes):
        b[location]=node[3]
    return (tuple(node[0] for node in nodes),
            tuple((v,*slot) for v,node in enumerate(nodes) for slot in node[1]),
            tuple(node[2] for node in nodes),tuple(b))


def equal_field(left,right,locator=None):
    if locator is not None and locator(left)!=locator(right):
        return False
    return left==right


@lru_cache(maxsize=6)
def orbit_field(phase):
    return full_field(baseline(phase))


@lru_cache(maxsize=6)
def orbit_flux(phase):
    following,counts=tick(baseline(phase))
    require(following==baseline((phase+1)%6),'baseline_transition')
    return counts


@lru_cache(maxsize=1)
def expected_labels():
    return {(a,v,j,role,r) for a in range(6) for v in range(8)
            for j,role,r,n in baseline(a)[0][v][1] if n>0}


def patch_for(state,base):
    return [[v,list(node[0]),[list(t) for t in node[1]],list(node[2]),node[3]]
            for v,node in enumerate(state[0]) if node!=base[0][v]]


def rehydrate(base,patch):
    require(type(patch) is list,'patch_not_list')
    nodes=list(base[0])
    seen=set()
    for row in patch:
        require(type(row) is list and len(row)==5,'patch_node_layout')
        v,q,slots,wall,b=row
        require(type(v) is int and 0<=v<8 and v not in seen,'patch_material_address')
        seen.add(v)
        require(type(q) is list and len(q)==3 and all(type(x) is int and 0<=x<=48 for x in q),'q_layout')
        require(type(wall) is list and len(wall)==9 and all(type(x) is int and 0<=x<=48 for x in wall),'wall_layout')
        require(type(b) is int and 0<=b<3,'b_layout')
        require(type(slots) is list,'pending_layout')
        keys=set()
        for slot in slots:
            require(type(slot) is list and len(slot)==4 and all(type(x) is int for x in slot),
                    'pending_layout')
            j,role,r,n=slot
            require(0<=j<3 and 0<=role<3 and 1<=r<=4 and 1<=n<=48 and
                    (j,role,r) not in keys,'pending_slot')
            keys.add((j,role,r))
        nodes[v]=form(q,slots,wall,b)
    return tuple(nodes),base[1]


def check_flow(got,expected,kind):
    require(type(got) is dict and all(type(n) is int and n!=0 for n in got.values()),
            kind+'_schema')
    require(got=={k:n for k,n in expected.items() if n},kind)


def check_case(row,cap,locator=None):
    label=tuple(row[k] for k in ('a','v','j','role','r'))
    require(all(type(x) is int for x in label) and label in expected_labels(),'case_label',label)
    a,v,j,role,r=label
    require(row.get('budget')==256,'case_budget')
    status=row['classification']
    require(status in CLASSES,'classification')
    ticks=row['ticks']
    require(type(ticks) is int and 0<=ticks<=cap,'executed_ticks')
    steps=row['steps']
    if status in ('NOT_RUN','INPUT_UNAVAILABLE'):
        require(ticks==0 and steps==[],'unexecuted_prefix')
        return label,0,0,status
    require(type(steps) is list and len(steps)==ticks+1 and ticks>0,'executed_prefix')
    live=inject(baseline(a),v,j,role,r)
    ledger=Counter()
    inc=Counter()
    max_distance=max_support=0
    past={}
    previous_support=None
    terminal=None
    for h,step in enumerate(steps):
        phase=(a+h)%6
        base=baseline(phase)
        require(type(step.get('h')) is int and step['h']==h,'tick_clock')
        actual=full_field(live)
        claimed=full_field(rehydrate(base,step['patch']))
        require(equal_field(actual,claimed,locator),'complete_field',h)
        require(step['patch']==patch_for(live,base),'canonical_positive_patch',h)
        check_flow(step['inc_delta'],inc,'incremental_flux')
        check_flow(step['flow_delta'],ledger,'cumulative_flux')
        support={vrow[0] for vrow in step['patch']}
        if previous_support is not None:
            cone=previous_support | {w ^ (4>>port) for w in previous_support for port in range(3)}
            require(support<=cone,'one_tick_dependency_cone',h)
        previous_support=support
        max_support=max(max_support,len(support))
        max_distance=max(max_distance,max(((v^w).bit_count() for w in support),default=0))
        matches=[i for i in range(6) if equal_field(actual,orbit_field(i),locator)]
        if matches:
            require(len(matches)==1,'background_phase_not_unique')
            shift=(matches[0]-phase)%6
            require(shift in (0,3),'background_phase_congruence')
            terminal=('RECOVERED',shift)
        elif live in past:
            terminal=('NEW_CYCLE',(past[live],h-past[live]))
        if terminal:
            require(h==ticks,'first_classification',h)
            break
        past[live]=h
        if h<ticks:
            live,movement=tick(live)
            base_next,bmovement=tick(base)
            require(base_next==baseline((phase+1)%6),'baseline_transition')
            inc=movement.copy()
            inc.subtract(bmovement)
            ledger.update(inc)
    if terminal is None:
        require(ticks==cap,'truncated_executed_prefix')
        terminal=('UNKNOWN_BUDGET',None)
    require(status==terminal[0],'classification_certificate')
    if status=='RECOVERED':
        require(type(row.get('phase_shift')) is int and row['phase_shift']==terminal[1],'recovery_phase')
        require(row.get('full_checks')==cap and row.get('aligned_tail')=='same_clock_cycle'
                and terminal[1]==0,'tail_contract')
        require(not any(ledger.values()),'nonzero_recovered_ledger')
        for h in range(ticks+1,cap+1):
            live,increment=tick(live)
            phase=(a+h)%6
            require(equal_field(full_field(live),orbit_field(phase),locator),
                    'expanded_tail_field',h)
            require(increment==orbit_flux((phase-1)%6),'expanded_tail_increment',h)
    if status=='NEW_CYCLE':
        require([row.get('cycle_start'),row.get('cycle_length')]==list(terminal[1]),'new_cycle')
    require(row['max_support']==max_support and row['max_distance']==max_distance,'support_distance')
    return label,ticks,len(steps),status


def verify(manifest_path,require_cases,max_ticks,strict,archive=None,locator=None):
    manifest=parse(manifest_path.read_text())
    check_manifest(manifest,archive)
    require(max_ticks==256 and require_cases==144,'requested_contract')
    require(manifest['certificate']=='CASES.jsonl','case_artifact_name')
    raw=(manifest_path.parent/manifest['certificate']).read_bytes()
    seen=set()
    counts=Counter()
    total_ticks=total_states=tail_ticks=0
    for number,line in enumerate(raw.splitlines(),1):
        require(line,'empty_case_row',number)
        try:
            label,ticks,states,status=check_case(parse(line),max_ticks,locator)
        except Rejected as e:
            raise Rejected(e.code,f'case line {number}: {e}') from e
        require(label not in seen,'duplicate_case',label)
        seen.add(label)
        counts[status]+=1
        total_ticks+=ticks
        total_states+=states
        if status=='RECOVERED':
            tail_ticks+=max_ticks-ticks
    require(len(seen)==require_cases and seen==expected_labels(),'incomplete_case_universe')
    if strict:
        require(not counts['NOT_RUN'] and not counts['INPUT_UNAVAILABLE'],'unexecuted_cases')
    if 'cases_sha256' in manifest:
        require(digest(raw)==manifest['cases_sha256'],'archived_cases_bytes')
    return {'case_count':len(seen),'classifications':{s:counts[s] for s in CLASSES},
            'explicit_prefix_transitions':total_ticks,'explicit_prefix_states':total_states,
            'expanded_periodic_tail_transitions':tail_ticks,
            'transitions_checked':total_ticks+tail_ticks,'full_states_checked':total_states+tail_ticks,
            'all_b_entries_per_state':SITES,'original_zip_bytes_checked':bool(archive),
            'archived_full_snapshot_rows_checked':2*SITES if archive else 0}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,default=HERE/'INPUT_MANIFEST.json')
    parser.add_argument('--require-cases',type=int,default=144)
    parser.add_argument('--max-ticks',type=int,default=256)
    parser.add_argument('--strict',action='store_true')
    parser.add_argument('--source-zip',default=os.environ.get('R11_SOURCE_ZIP'))
    a=parser.parse_args()
    try:
        result=verify(a.manifest,a.require_cases,a.max_ticks,a.strict,a.source_zip)
    except (ValueError,KeyError,OSError,TypeError,zipfile.BadZipFile) as exc:
        print(f'REJECTED {exc}',file=sys.stderr)
        return 1
    print(json.dumps(result,sort_keys=True))
    return 0


if __name__=='__main__':
    raise SystemExit(main())
