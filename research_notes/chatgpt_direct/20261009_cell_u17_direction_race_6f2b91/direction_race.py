"""U17: competing source-derived tickets and one material occurrence.

The earliest valid returned ticket rule is a declared local selector. It is
not a native force law. Distinct channels use distinct input resources.
Positive weights execute the unchanged U16/U13/BRC dependency chain.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib, importlib.util, sys
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'causal_actuation.py'
if not SRC.exists():SRC=ROOT.parent/'20261009_cell_u16_causal_actuation_52a7d9'/'causal_actuation.py'
b=SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()!='701bb1c3e287f7c0d438815dcc187731a60befff':
    raise RuntimeError('U16 source pin mismatch')
spec=importlib.util.spec_from_file_location('u17_pinned_u16',SRC)
u=importlib.util.module_from_spec(spec);sys.modules[spec.name]=u;spec.loader.exec_module(u)
f,r,m,v=u.f,u.r,u.m,u.v
ZERO,ONE=f.ZERO,f.ONE

def plans(body,channel,port,support_length=1,detour=6,support=8):
    if type(support_length)is not int or support_length<1:raise ValueError('positive route length')
    if len({r.axis(port),r.axis(detour),r.axis(support)})!=3:raise ValueError('three arrival axes')
    x=body.cells[0];y=r.advance(x,port)
    if y in body.cells:raise ValueError('occupied proposed cell')
    source=y
    for _ in range(support_length):source=r.advance(source,support^1)
    stem=f'channel:{channel}'
    return (f.Plan(stem+':signal',x,(port,)),f.Plan(stem+':record',x,(detour^1,port,detour)),
            f.Plan(stem+':support',source,(support,)*support_length))

class Race:
    """Same fixed downstream delay5; first accepted source tuple wins.

    Window is the effective arrival tolerance W=H-8, or None. Each source
    tuple has its own one-use U13 protocol. The race terminates observation
    on the first READY, but the physical bookkeeping of losing/in-flight
    inputs is retained by the separate transcript. Expiry does not free IDs.
    """
    def __init__(self,left_plans,right_plans,window=None,probs=(Q(1,2),)*6):
        ids=[p.identity for p in tuple(left_plans)+tuple(right_plans)]
        if len(set(ids))!=6:raise ValueError('distinct resources, not duplicated source occurrences')
        if len(probs)!=6:raise ValueError('six explicitly independent advance probabilities')
        self.channels=(f.Protocol(left_plans,probs[:3],window),f.Protocol(right_plans,probs[3:],window))
        self.initial=tuple(c.initial() for c in self.channels)
        self.records=[]
        self.row=lru_cache(None)(self._row);self.solve=lru_cache(None)(self._solve)
    def outcome(self,x):
        done=[i for i,s in enumerate(x) if s.outcome=='READY_RESERVED']
        if len(done)==2:return 2 # tie
        if done:return done[0]
        if all(s.outcome=='EXPIRED_RETAINED' for s in x):return 3 # no motion
        return None
    def _row(self,x):
        if self.outcome(x)is not None:return ()
        pieces=[c.row(s) if s.outcome=='PENDING' else ((None,s,ONE),) for c,s in zip(self.channels,x)]
        ans=[]
        for (b0,y0,w0),(b1,y1,w1) in product(*pieces):
            w=r.serial(w0,w1)
            if w.live:ans.append(((b0,b1),(y0,y1),w))
        if r.total(w for _,_,w in ans).total!=1:raise AssertionError('lost trial weight')
        return tuple(ans)
    def _solve(self,x):
        terminal=self.outcome(x)
        if terminal is not None:return tuple(Q(int(i==terminal)) for i in range(4))
        ell=ZERO;off=[ZERO]*4
        for bits,y,w in self.row(x):
            if y==x:ell=r.merge(ell,w)
            else:
                for i,z in enumerate(self.solve(y)):off[i]=r.merge(off[i],r.serial(w,f.lift(z)))
        factor=ONE
        if ell.live:
            r.CALLS['one_state_recurrent_cwm']+=1
            cert=r.brc.one_state_recurrent_cwm([ell.total])
            if not cert.total_mass_stable:raise AssertionError('nonterminating race loop')
            factor=r.edge(cert.total_mass_closure)
        vals=tuple(r.serial(z,factor).total for z in off)
        if sum(vals)!=1:raise AssertionError('outcome weight')
        self.records.append((x,ell.total,vals))
        return vals
    def law(self):
        a,b,t,n=self.solve(self.initial)
        return (r.total((f.lift(a),r.serial(f.lift(t),r.edge(Q(1,2))))).total,
                r.total((f.lift(b),r.serial(f.lift(t),r.edge(Q(1,2))))).total,n)
    def prefixes(self,horizon):
        live={self.initial:ONE};hits=[]
        for _ in range(horizon):
            nxt={};hit=[ZERO]*4
            for x,w in live.items():
                for bits,y,q in self.row(x):
                    ww=r.serial(w,q);z=self.outcome(y)
                    if z is None:f.add(nxt,y,ww)
                    else:hit[z]=r.merge(hit[z],ww)
            live=nxt;hits.append(tuple(hit))
        return {'hits':hits,'live':live}

def standard_race(long=1,window=None,probs=(Q(1,2),)*6):
    body=u.standard_body()
    return Race(plans(body,'plus',4,1),plans(body,'minus',5,long),window,probs)

def encode(x):
    if isinstance(x,dict):return {str(k):encode(vv) for k,vv in x.items()}
    if isinstance(x,(tuple,list)):return [encode(vv) for vv in x]
    return u.encode(x)

def material_trace(arrival_pair=((1,3,1),(1,3,3)),H=None,tie_choice=0,
                   body=None,ports=(4,5),support_lengths=(1,3),detour=6,support=8,k=4):
    """Execute one finite representative source history and selected actuation.

    Every channel has its own signal, record resource and support. Both
    candidates address ONE body occurrence. The sole local arbiter accepts
    the first valid returned ticket; a simultaneous tie uses a declared fair
    branch. All later tickets are retained without a second body update.
    Losing carriers continue their recorded routes; none is reset or erased.
    """
    body=u.standard_body() if body is None else body
    if H is not None and (type(H)is not int or H<0):raise ValueError('lifetime')
    if tie_choice not in (0,1):raise ValueError('tie branch index')
    pp=tuple(plans(body,str(i),p,n,detour,support) for i,(p,n) in enumerate(zip(ports,support_lengths)))
    routes=[];cals=[];returns=[];weight=ONE
    for i,(pl,tt) in enumerate(zip(pp,arrival_pair)):
        protocol=f.Protocol(pl,window=None)
        tr=protocol.trace(u.prescribed_choices(tt,protocol.lengths));routes.append(tr)
        weight=r.serial(weight,tr[-1]['weight'])
        tau=max(tt);valid=H is None or tau-min(tt)+8<=H
        returns.append(tau+5 if valid else None)
        if valid:
            reg=u.c.Registers(tuple((tau-t)%k for t in tt),(0,0),tuple(t%k for t in tt))
            cals.append(u.c.admission(reg,k,tau,tt,None,source_ids=tuple(p.identity for p in pl)))
        else:cals.append(None)
    ready=[(t,i) for i,t in enumerate(returns) if t is not None]
    tied=len(ready)==2 and ready[0][0]==ready[1][0]
    winner=tie_choice if tied else (min(ready)[1] if ready else None)
    if tied:weight=r.serial(weight,r.edge(Q(1,2)))
    L=body.length();x=body.cells[0];ys=tuple(r.advance(x,p) for p in ports)
    global_old=tuple(f'old:{i}' for i in range(L));records=('record:0','record:1')
    all_record_ids=frozenset(global_old+records)
    inv=out=before=None;steps=();used=None
    codec={i:f'old:{i}' for i in range(L)}
    if winner is not None:
        # Exactly the original bound resources plus the returned winner are
        # the local U11 subsystem. The other record is tracked OUTSIDE it.
        codec[L]=records[winner]
        inv=v.prepared(body,L+1,1,reservoir_cell=x)
        ticket=u.Ticket('one-body-choice',0,x,ys[winner],tuple(p.identity for p in pp[winner]),True)
        out,steps,consumed,status=one_body_apply(False,ticket,inv,ports[winner],L)
        if not consumed or status!='COMMITTED':raise AssertionError('winner not committed')
        used=u.Ticket(ticket.identity,ticket.actor,ticket.source,ticket.target,ticket.occurrences,True,True)
        back,rev=v.transaction(out,0,ports[winner]^1,False,(L,))
        if back!=inv:raise AssertionError('same-ID local inverse failed')
        reverse=rev
    else:reverse=[]
    end=max([max(t) for t in arrival_pair]+[t for t in returns if t is not None]+([returns[winner]+3] if winner is not None else []))
    base_tokens=v.prepared(body,L,1,reservoir_cell=x).tokens
    frames=[]
    for tick in range(end+1):
        carrier_positions=[];support_states=[]
        for i,tr in enumerate(routes):
            row=tr[min(tick,len(tr))-1] if tick else None
            cellrow=row['cells'] if row else tuple(p.source for p in pp[i])
            sigpos,recpos,cpos=cellrow
            if returns[i] is not None and tick>=returns[i]:recpos=x
            if winner==i and tick>=returns[i]+2:recpos=ys[i]
            carrier_positions.append((sigpos,recpos,cpos))
            status='TRAVELLING' if tick<max(arrival_pair[i]) else 'CAPTURED'
            if tick>=max(arrival_pair[i]) and cals[i] is None:status='WINDOW_BLOCKED_RETAINED'
            if returns[i] is not None and tick>=returns[i]:
                status='SELECTED_RECORD' if winner==i else ('NOT_SELECTED_RETAINED' if winner is not None else 'AVAILABLE')
            support_states.append(status)
        idx=(tick-returns[winner]-1) if winner is not None else -1
        if winner is not None and idx>=0:
            ss=steps[min(idx,2)];cells=ss['material_cells'];heads=ss['heads'];words=ss['words']
            bound={codec[j] for j in ss['bound']}
        else:
            cells=body.cells;heads=tuple(body.cells[(i,j)[side]] for i,j,a,b in body.links for side in (0,1))
            words=v.paths(body);bound=set(global_old)
        free=set();held=set()
        for i,identity in enumerate(records):
            if identity in bound:continue
            returned=returns[i] is not None and tick>=returns[i]
            reserved=winner==i and tick>=returns[i]+1
            if tick==0 or (returned and not reserved):free.add(identity)
            else:held.add(identity)
        if (bound&free or bound&held or free&held) or bound|free|held!=all_record_ids:
            raise AssertionError('global resource partition')
        path_tokens=out.tokens if winner is not None and idx>=2 else base_tokens
        record_locations={}
        for head,word,tokens in zip(heads,words,path_tokens):
            for j,token in enumerate(tokens):record_locations[codec[token]]=m.endpoint(head,word[:j])
        for i,identity in enumerate(records):record_locations[identity]=carrier_positions[i][1]
        if set(record_locations)!=all_record_ids:raise AssertionError('resource position missing')
        frames.append({'tick':tick,'record_locations':record_locations,'body_cells':cells,'path_heads':heads,'path_words':words,
                       'packet_cells':tuple(carrier_positions),'free':tuple(sorted(free)),
                       'held':tuple(sorted(held)),'bound':tuple(sorted(bound)),
                       'support_state':tuple(support_states),
                       'body_choice_consumed':winner is not None and tick>=returns[winner],
                       'visible_selected_channel':winner if winner is not None and tick>=returns[winner] else None,
                       'native_firing':False})
    final=out.state if out else body
    return {'plans':pp,'arrivals':arrival_pair,'window':H,'return_ticks':tuple(returns),'winner':winner,
            'tie':tied,'trial_weight':weight,'routes':routes,'calibrations':cals,
            'frames':frames,'body_before':body,'body_after':final,'resource_ids':tuple(sorted(all_record_ids)),
            'codec':codec,'winner_inventory_before':inv,'winner_inventory_after':out,
            'winner_local_inverse':reverse,'used_ticket':used,'body_move_count':int(winner is not None),
            'material_reaction_derived':False,'native_triads_certified':False}

def one_body_apply(consumed,ticket,inventory,port,token):
    """A one-attempt local latch, not authentication or a force certificate."""
    if type(consumed)is not bool:raise ValueError('Boolean one-attempt status')
    if consumed:return inventory,(),True,'LATE_RETAINED'
    out,tr,used=u.execute_ticket(ticket,inventory,port,token)
    return out,tr,bool(used.used),'COMMITTED' if used.used else 'DENIED_RETAINED'
