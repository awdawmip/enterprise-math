"""Public JSON probes and optional replay of the separately supplied U27 archive."""
import argparse
import ast
import copy
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib
import importlib
import json
import sys
import tempfile
import zipfile

ARCHIVE='a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7'
AB=(0,1)
CD=(2,3)


def edge(s):
    return tuple(ast.literal_eval(s))


def advance(location,port):
    z=list(location)
    z[port//2]+=1 if port%2==0 else -1
    return tuple(z)


def slots(item):
    fr=item['frame']
    rows={}
    ends={}
    for a,b,left,right in item['reference']['paths']['links']:
        e=(a,b)
        rows[e]=[]
        tips=[]
        for side,word in enumerate((left,right)):
            at=tuple(fr['body_cells'][e[side]])
            for letter in word:
                rows[e].append((e,side,at,letter))
                at=advance(at,letter)
            tips.append(at)
        ends[e]=tips[0]==tips[1]
    return rows,ends


def slot(rec):
    return tuple(rec['edge']),rec['side'],tuple(rec['cell']),rec['port']


def components(edges):
    parts=[{v} for v in range(4)]
    for a,b in edges:
        u=next(x for x in parts if a in x)
        v=next(x for x in parts if b in x)
        if u!=v:
            parts.remove(v)
            u.update(v)
    return sorted(tuple(sorted(i)) for i in parts)


def inspect(item):
    fr=item['frame']
    ids=[k for group in ('bound','free','held') for k in fr[group]]
    assert sorted(ids)==list('0123')
    words,ends=slots(item)
    actual=Counter(slot(v) for v in fr['bound'].values())
    complete=set()
    missing={}
    for e,word in words.items():
        have=Counter({k:n for k,n in actual.items() if k[0]==e})
        need=Counter(word)
        if ends[e] and need==have:
            complete.add(e)
        if ends[e] and not have-need:
            missing[e]=list((need-have).elements())
    assert complete=={edge(s) for s in item['complete']}
    return complete,missing


def pending_bridge(previous,current,route_start=None):
    """Evidence of a specific one-letter transfer in the single actor-B edit."""
    strict,missing=inspect(current)
    if len(components(strict))==1: return None
    fr=current['frame']
    if fr.get('automatic_cached_commit_permitted') is False: return None
    k,actor,p,grow=fr['label']
    if (k,actor)!=('body',1) or len(missing.get(AB,[]))!=1: return None
    occurrence=missing[AB][0]
    _,side,head,port=occurrence
    if side!=1 or head!=tuple(fr['body_cells'][1]): return None
    if fr['held']!={'2':list(head)}: return None
    old=previous['frame']
    if grow:
        if fr['kind']!='LOCAL_CARRY' or old['kind']!='RESERVE_OR_DETACH' or not route_start: return None
        if old['label']!=fr['label'] or port!=(p^1): return None
        orig=tuple(old['body_cells'][1])
        if old['held']!={'2':list(orig)} or advance(orig,p)!=head: return None
        hop=route_start['frame']
        if hop['kind']!='FREE_NATIVE_HOP' or hop['token']!=2 or hop['free'].get('2')!=list(orig): return None
        if AB not in inspect(previous)[0]: return None
    else:
        if fr['kind']!='RESERVE_OR_DETACH' or old['kind']!='STABLE_COMMIT': return None
        if port!=p or slot(old['bound']['2'])!=occurrence: return None
    return '2',occurrence


def public(fixtures):
    data={}
    pins={'base_case':'15ccb3ad4037d60193a9d9b06ff4865754b8e6ec',
          'carry_P':'cce12ccf9ac48710ec316a4d127f442c66152ab5',
          'carry_Q':'5b2d36c91051a6e561186aeb5792b7982919b972',
          'interrupted_after_carry':'e35281e64806f3dd9e1f2ad6520449c7bf0e2416'}
    for name,digest in pins.items():
        raw=(fixtures/(name+'.json')).read_bytes()
        assert hashlib.sha1(('blob '+str(len(raw))+chr(0)).encode()+raw).hexdigest()==digest
        data[name]=json.loads(raw)
    assert data['base_case']['inventory_B']==4
    assert (data['base_case']['lambda'],data['base_case']['pre_release_epsilon'])==('1/48','1/16')
    for name in ('carry_P','carry_Q'):
        seq=data[name]['data']
        assert [item['frame']['kind'] for item in seq]==data['base_case']['frame_order']
        assert [len(components(inspect(t)[0])) for t in seq]==[1,1,2,1,1]
        assert pending_bridge(seq[1],seq[2],seq[0])==('2',(AB,1,(1,0,1,0,0,0),5))
        fault=copy.deepcopy(seq[2])
        fault['frame']['free']['2']=fault['frame']['held'].pop('2')
        assert pending_bridge(seq[1],fault,seq[0]) is None
        assert pending_bridge(seq[1],seq[2],None) is None
    p,q=(data[k]['data'][2] for k in ('carry_P','carry_Q'))
    assert p['frame']==q['frame'] and p['reference']['paths']==q['reference']['paths']
    assert {edge(k) for k in p['eligible']}==set() and {edge(k) for k in q['eligible']}=={CD}
    stop=data['interrupted_after_carry']['data']
    assert stop['automatic_cached_commit_permitted'] is False and stop['released_token']==3
    assert stop['free']['3']==[1,1,0,0,0,0] and stop['held']==q['frame']['held']
    return {'frozen_json_frames':10,'matched_third_frame_inputs':2,'third_strict_components':[[0,2,3],[1]],
            'frozen_interrupted_record_checked':True}


def checksum(b):
    return hashlib.sha256(b).hexdigest()


def validate_manifest(root):
    spec=json.loads((root/'PACKAGE_MANIFEST.json').read_text())['files']
    for f,s in spec.items():
        b=(root/f).read_bytes()
        assert len(b)==s['bytes'] and checksum(b)==s['sha256']
        assert hashlib.sha1(('blob '+str(len(b))+'\0').encode()+b).hexdigest()==s['git_blob_sha1']
    return len(spec)


def frozen_replay(p,fixtures):
    assert checksum(p.read_bytes())==ARCHIVE
    with zipfile.ZipFile(p) as z,tempfile.TemporaryDirectory() as tmp:
        assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
        z.extractall(tmp)
        root=Path(tmp)/'em_u27_followup'
        baseline=root/'baseline'/'cell_u27'
        for name in ('base_case','carry_P','carry_Q','interrupted_after_carry'):
            assert json.loads((fixtures/(name+'.json')).read_bytes())==json.loads((root/'fixtures'/(name+'.json')).read_bytes())
        counts=Counter(archive_manifest_items=validate_manifest(root),u27_manifest_items=validate_manifest(baseline))
        sys.path.insert(0,str(baseline))
        h=importlib.import_module('work_exposure')
        budget=h.v.Capped(4,F(1,16))
        stage_eligibility={}
        quot=Counter()
        for p in range(4,12):
            directions=[]
            for name,dormant in [('P',AB),('Q',CD)]:
                ledger=h.v.Ledger(h.f.root_state(),4)
                prep=h.ONE
                for lab in [('mode',h.f.EDGE),('contact',h.f.EDGE,0),('mode',dormant)]:
                    y,w=h.v.accepted(budget,ledger.s,lab)
                    prep=h.r.serial(prep,w)
                    ledger.commit(lab,y)
                assert prep.total==F(1,802816)
                stable_before=ledger.s
                original_ids=ledger.validate(stable=True)
                seqs=[]
                for label in [('body',1,p,True),('body',1,p^1,False)]:
                    old=ledger.s
                    y,weight=h.v.accepted(budget,old,label)
                    assert weight.total==(F(1,18816) if label[-1] else F(1,392))
                    start=len(ledger.log)
                    ledger.commit(label,y)
                    counts['stable_validations']+=int(ledger.validate(stable=True) is not None)
                    original=list(h.references(old,y,ledger.log[start:]))
                    seq=json.loads(json.dumps(h.v.encode(original)))
                    if p==4 and label[-1]:
                        declared=json.loads((root/'fixtures'/('carry_'+name+'.json')).read_text())['data']
                        assert seq==declared
                    assert len(seq)==5
                    last=(None if label[-1] else seqs[0][-1])
                    gap_index=2 if label[-1] else 0
                    for i,(item,raw) in enumerate(zip(seq,original)):
                        base,_=inspect(item)
                        assert h.connected(raw['complete']) == (len(components(base))==1)
                        counts['strict_connected']+=int(h.connected(raw['complete']))
                        counts['frames_checked']+=1
                        if i==gap_index:
                            bridge=pending_bridge(seq[i-1] if i else last, item, seq[0] if label[-1] else None)
                            assert bridge and bridge[0]=='2' and bridge[1][0]==AB
                            assert len(components(base|{AB}))==1
                            counts['certified_one_slot_bridges']+=1
                        else:
                            assert len(components(base))==1
                        for released in raw['eligible']:
                            stopped=h.freeze_loss(raw,released)
                            token=stopped['released_token']
                            assert token not in stopped['bound'] and token in stopped['free']
                            assert stopped['automatic_cached_commit_permitted'] is False
                            assert not h.connected(base-{released})
                            if i==gap_index:
                                assert name=='Q' and released==CD
                                assert len(components((base-{CD})|{AB}))==2
                                counts['stopped_gaps_with_irreparable_cut_by_AB_alone']+=1
                            if p==4 and name=='Q' and label[-1] and i==gap_index:
                                declared=json.loads((root/'fixtures'/'interrupted_after_carry.json').read_bytes())['data']
                                assert json.loads(json.dumps(h.v.encode(stopped)))==declared
                            counts['source_release_stops_checked']+=1
                    law=[len(item['eligible']) for item in seq]
                    stage_eligibility[name+('_grow' if label[-1] else '_shrink')]=law
                    # Ask the actual BRC stage observer, keeping other 437/438
                    # labels alive as specified by the model.
                    for raw in original:
                        safe,loss=h.stage_law(raw['eligible'],F(1,16))
                        assert safe.total==1-F(len(raw['eligible']),784)
                        assert all(term.total==F(1,784) for term in loss.values())
                        counts['typed_hazard_checks']+=1
                    seqs.append(seq)
                assert ledger.s==stable_before and ledger.validate(stable=True)==original_ids
                assert set(ledger.free)=={2}
                grow,shrink=seqs
                a,b=grow[2],shrink[0]
                assert a['reference']==b['reference'] and a['modes']==b['modes']
                assert a['complete']==b['complete'] and a['eligible']==b['eligible']
                geom=('body_cells','free','held','bound')
                assert all(a['frame'][k]==b['frame'][k] for k in geom)
                for seq,gap in [(grow,a),(shrink,b)]:
                    fr=next(t['frame'] for t in seq if t['frame']['kind']=='RELATION_COMMITTED')
                    out=(('bound',slot(fr['bound']['2'])) if '2' in fr['bound'] else ('free',tuple(fr['free']['2'])))
                    can_release=CD in {edge(k) for k in gap['eligible']}
                    quot[out,can_release]+=1
                    directions.append((out,can_release))
            assert len(set(directions))==4
        assert sorted(quot.values())==[1]*16+[8,8]
        return dict(counts,archive_sha256=ARCHIVE,full_probe_classes=len(quot),
                    class_size_histogram=dict(Counter(quot.values())),local_classes_per_direction=4,
                    eligibility=stage_eligibility,typed_calls=dict(h.r.CALLS))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--fixtures',type=Path,required=True,help='published U27F fixture directory')
    parser.add_argument('--archive',type=Path,help='separately supplied frozen em_u27_followup_tasks.zip')
    a=parser.parse_args()
    result={'public_fixture_tests':public(a.fixtures)}
    if a.archive: result['frozen_replay']=frozen_replay(a.archive,a.fixtures)
    print(json.dumps(result,indent=2))
