"""Replay U21 positive transition weights and finite receipts from the pinned U27 package."""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from itertools import permutations
import json
from math import factorial, prod
from pathlib import Path
import sys

MANIFEST = 'e6a86c8ab44f674b126844358e893d893d0c58b6e16353c89660ff35adfafdb5'
ARCHIVE = 'a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7'

def load(root):
    blob=(root/'PACKAGE_MANIFEST.json').read_bytes()
    assert sha256(blob).hexdigest()==MANIFEST
    files=json.loads(blob)['files']
    for name,pin in files.items():
        assert sha256((root/name).read_bytes()).hexdigest()==pin['sha256'],name
    path=root/'baseline/cell_u27/reuse/contact_network.py'
    spec=importlib.util.spec_from_file_location('contact_u21_bound',path)
    c=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=c
    spec.loader.exec_module(c)
    return c,len(files)

def point(*axis):
    return tuple(axis)+(0,)*(6-len(axis))

def distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))

def encode(w):
    return dict(count=w.count,total=str(w.total),dominant=str(w.dominant))

def accepted(K,s,label):
    out=[(y,w) for y,w,decision in K.transition(s,label) if decision=='ACCEPT']
    assert len(out)==1
    return out[0]

def body(c,K,s,i,p):
    args=[accepted(K,s,('body',i,p,g)) for g in (False,True)]
    assert args[0][0]==args[1][0]
    y=args[0][0]
    w=c.r.total(w for _,w in args)
    assert w.total==F(1,192)
    return y,w

def pair(c,K,displacement):
    r=c.r
    origin=point()
    cells=(origin,tuple(displacement),point(50,60),point(-60,50))
    initial=c.m.make(cells,{})
    source_free=c.ContactInventory.empty(cells).free
    level={initial:c.ONE}
    L=distance(*cells[:2])
    for t in range(L-1):
        following={}
        for s,v in level.items():
            for i in (0,1):
                for p in r.PORTS:
                    after=r.advance(s.cells[i],p)
                    if distance(after,s.cells[1-i])!=L-t-1:
                        continue
                    y,w=body(c,K,s,i,p)
                    following[y]=r.merge(following.get(y,c.ZERO),r.serial(v,w))
        level=following
    ideal,paid=c.ZERO,c.ZERO
    probes=0
    for s,v in level.items():
        for side in (0,1):
            e=(0,1)
            y,w=accepted(K,s,('contact',e,side))
            ideal=r.merge(ideal,r.serial(v,w))
            local=[token for token,z in source_free.items() if z==s.cells[side]]
            if local:
                inv=c.ContactInventory.empty(cells)
                inv.state=s
                rec=inv.toggle(e,side,min(local))
                assert inv.state==y and rec['birth']
                probes+=1
                paid=r.merge(paid,r.serial(v,w))
    ways=factorial(L)//prod(factorial(abs(x)) for x in displacement)
    cap=F(1,48*49)
    assert ideal.total==2*ways*F(1,96)**(L-1)*cap
    assert paid.total==2*ways*F(1,192)**(L-1)*cap
    return dict(displacement=list(displacement),first_proposal=L,geodesic_direction_words=ways,
                ideal=encode(ideal),stationary_inventory=encode(paid),eligible_endpoint_sides=probes)

def four(c,K):
    cells=(point(),point(2),point(0,0,2),point(1,1))
    initial=c.m.make(cells,{})
    assert not any(c.contact_port(cells,e) is not None for e in c.PAIRS)
    # With only one body move and three births, every born edge must belong
    # to the geometric graph after that move, which is always disconnected.
    max_edges=0
    for i in range(4):
        for p in c.r.PORTS:
            y,w=body(c,K,initial,i,p)
            eligible=[e for e in c.PAIRS if c.contact_port(y.cells,e) is not None]
            max_edges=max(max_edges,len(eligible))
            graph=y
            for e in eligible:
                graph=c.toggle(graph,e,0)
            assert not c.connected(graph)
    assert max_edges==2
    def execute(order):
        inv=c.ContactInventory.empty(cells)
        v=c.ONE
        for name in order:
            if name in ('C','D'):
                i,p=(2,5) if name=='C' else (3,3)
                assert not any(i in e for e in inv.state.table())
                inv.state,w=body(c,K,inv.state,i,p)
                inv.validate()
            else:
                e={'AC':(0,2),'AD':(0,3),'BD':(1,3)}[name]
                y,w=accepted(K,inv.state,('contact',e,0))
                ids=sorted(i for i,z in inv.free.items() if z==inv.state.cells[e[0]])
                rec=inv.toggle(e,0,ids[0])
                assert inv.state==y and rec['birth']
                assert [q['kind'] for q in rec['phases']]==['RESERVE_OR_DETACH','CONTACT_COMMIT']
            v=c.r.serial(v,w)
        assert c.connected(inv.state)
        return inv,v
    family=c.ZERO
    extensions=0
    plan=('C','D','AC','AD','BD')
    for order in permutations(plan):
        if order.index('C')>order.index('AC') or any(order.index('D')>order.index(k) for k in ('AD','BD')):
            continue
        inv,v=execute(order)
        family=c.r.merge(family,v)
        extensions+=1
    assert extensions==20 and family.total==20*F(1,192)**2*F(1,48*49)**3
    inv,_=execute(plan)
    before=inv.state
    bound={str(e):rec['id'] for e,rec in inv.bound.items()}
    survivor=c.ZERO
    outcomes=Counter()
    for label,_ in K.proposals:
        for y,w,decision in K.transition(before,label):
            outcomes['branches']+=1
            if c.connected(y):
                survivor=c.r.merge(survivor,w)
    assert survivor.total==1-3*F(1,49)
    frozen_row=c.ContactOnly().row(before)
    freeze_survive=c.r.total(v for s,v in frozen_row.items() if c.connected(s))
    assert freeze_survive.total==F(37,49)
    assert [s for s in frozen_row if c.connected(s)]==[before]
    y,w=accepted(K,before,('contact',(0,3),0))
    rec=inv.toggle((0,3),0)
    assert y==inv.state and not c.connected(y) and sorted(c.components(y))==[(0,2),(1,3)]
    assert w.total==F(1,49)
    return dict(initial_cells=cells,max_new_neighbours_after_one_move=max_edges,shortest_complete_proposals=5,
                paid_family_orders=extensions,paid_family=encode(family),bound_ids=bound,
                full_first_layer=four_full(c,K,cells),
                resulting_cells=before.cells,resulting_tree=before.tree(),
                following_all_label_survival=encode(survivor),following_actual_branches=outcomes['branches'],
                fixed_positions_contact_only_survival=encode(freeze_survive),
                split_components=c.components(inv.state),release_label_probability=str(w.total),
                released_id=rec['token'],release_phases=[p['kind'] for p in rec['phases']])


def four_full(c,K,cells):
    # In five proposals exactly two successful body moves and three bridging births are needed.
    # Remaining L1 distances provide a necessary (optimistic) connectivity test.
    start=c.m.make(cells,{})
    def can_join(state,remaining_moves):
        seen={0}
        edges=[(i,j) for i,j in c.PAIRS if (i,j) in state.table() or
               distance(state.cells[i],state.cells[j])<=remaining_moves+1]
        for _ in range(3):
            for i,j in edges:
                if i in seen or j in seen:
                    seen.update((i,j))
        return len(seen)==4
    label_body=[x for x,_ in K.proposals if x[0]=='body']
    label_birth=[x for x,_ in K.proposals if x[0]=='contact']
    sites=c.ContactInventory.empty(cells).free
    # A mask records deposited receipts owned by prior births. -1 denotes a word
    # outside this receipt protocol. It is still included in the ideal measure.
    level={(start,0,0):c.ONE}
    sizes=[]
    for t in range(5):
        following={}
        for (s,moves,mask),w in level.items():
            table=s.table()
            labels=(label_body if moves<2 else [])+(label_birth if len(table)<3 else [])
            for label in labels:
                if label[0]=='contact' and label[1] in table:
                    continue
                y=K.proposal(s,label)
                if y is None:
                    continue
                is_body=label[0]=='body'
                nm=moves+int(is_body)
                if not can_join(y,2-nm):
                    continue
                if not is_body and len(c.components(y))!=len(c.components(s))-1:
                    continue
                mask2=mask
                if mask>=0:
                    if is_body and any(label[1] in e for e in table):
                        mask2=-1
                    elif not is_body:
                        pair,side=label[1:]
                        valid=[i for i,z in sites.items() if not (mask>>i)&1 and z==s.cells[pair[side]]]
                        mask2=mask | (1<<min(valid)) if valid else -1
                yy,v=accepted(K,s,label)
                assert y==yy
                key=(y,nm,mask2)
                following[key]=c.r.merge(following.get(key,c.ZERO),c.r.serial(w,v))
        level=following
        sizes.append(len(level))
    assert all(c.connected(s) and moves==2 for s,moves,_ in level)
    ideal=c.r.total(level.values())
    paid=c.r.total(w for (_,_,mask),w in level.items() if mask>=0)
    assert (ideal.count,ideal.total,paid.count,paid.total)==(1440,F(985,1468894169530368),80,F(5,119909728124928))
    return dict(ideal=encode(ideal),stationary_id_protocol=encode(paid),layer_keys=sizes)


def controls(c,K):
    cells=(point(),point(1),point(50,60),point(-60,50))
    init=c.m.make(cells,{})
    birth=loss=c.ZERO
    y=c.toggle(init,(0,1),0)
    for label,_ in K.proposals:
        for t,w,_ in K.transition(init,label):
            if (0,1) in t.table():
                birth=c.r.merge(birth,w)
        for t,w,_ in K.transition(y,label):
            if (0,1) not in t.table():
                loss=c.r.merge(loss,w)
    assert birth.total==F(1,1176) and loss.total==F(1,49)
    sub=c.ContactOnly()
    remote=c.m.make((point(),point(2),point(50,60),point(-60,50)),{})
    row=sub.row(remote)
    assert len(row)==1 and row[remote].total==1
    inv=c.ContactInventory.empty(cells)
    before=dict(inv.free)
    activate=inv.toggle((0,1),0,0)
    release=inv.toggle((0,1),0)
    assert inv.free==before and inv.state==init and activate['token']==release['token']
    return dict(full_adjacent_birth=encode(birth),full_existing_release=encode(loss),
                frozen_geometry_nonadjacent_self_loop=encode(row[remote]),
                original_inventory_after_attach_detach=inv.free)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bundle-dir',type=Path,required=True)
    args=p.parse_args()
    c,n=load(args.bundle_dir)
    K=c.Kernel()
    sample=[point(1),point(2),point(-1,1),point(2,1),point(1,1,-1),point(2,-1,1)]
    out=dict(manifest_sha256=MANIFEST,package_sha256=ARCHIVE,verified_files=n,
             full_labels=len(K.proposals),parameters=dict(eta=str(K.eta),lam=str(K.lam)),
             controls=controls(c,K),pair_cases=[pair(c,K,x) for x in sample],four_body=four(c,K))
    out['source_brc_calls']=dict(c.r.CALLS)
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':
    main()
