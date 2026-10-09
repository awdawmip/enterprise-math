"""U16: source-signal feedback before a material-prefix update.

Conditional controlled protocol, not a derived force law. All path weights use
unchanged U15 -> U14 -> ... -> weighted BRC. The material and its message have
DIFFERENT identities. Only the message traverses the preparation route.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
import hashlib, importlib.util, sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'check_u15.py'
if not SRC.exists():
    SRC = ROOT.parent/'20261009_cell_u15_sequential_cleanup_9d2f60'/'check_u15.py'
raw = SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() != '4ea6261cc786a79bf3b92939c4e36f95ab4fdcf0':
    raise RuntimeError('U15 dependency mismatch')
spec=importlib.util.spec_from_file_location('u16_pinned_u15',SRC)
c=importlib.util.module_from_spec(spec);sys.modules[spec.name]=c;spec.loader.exec_module(c)
p,f,r=c.p,c.p.f,c.r
sync=f.s;v=sync.v;m=f.m
ZERO,ONE=f.ZERO,f.ONE
POST_STAGES=8  # four calibration, one ticket/resource return, three U11 stages

@dataclass(frozen=True)
class Ticket:
    identity: str
    actor: int
    source: tuple[int,...]
    target: tuple[int,...]
    occurrences: tuple[str,...]
    authorized: bool
    used: bool=False


def standard_body():
    z=r.ZERO;e1=r.direction(0);e2=r.direction(2)
    return m.from_tree((z,e1,tuple(a+b for a,b in zip(e1,e2)),e2),((0,1),(1,2),(2,3)))


def plans_at(body,actor=0,port=4,detour=6,support=8):
    """A message from the material, one record resource, one support source.

    The pulse is an explicitly additional carrier, not the material itself.
    The record/support route is unchanged geometrically from the U12 example.
    """
    m.validate(body)
    if not 0<=actor<len(body.cells) or len(v.incident_slots(body,actor))!=1:
        raise ValueError('this one-record actuator is for a tree leaf')
    if len({r.axis(port),r.axis(detour),r.axis(support)})!=3:
        raise ValueError('three declared final transport axes')
    x=body.cells[actor];y=r.advance(x,port)
    if y in body.cells:raise ValueError('vacant proposed target required')
    plans=(f.Plan(f'actor:{actor}:signal:0',x,(port,)),
           f.Plan(f'record:{body.length()}:occurrence:0',x,(detour^1,port,detour)),
           f.Plan('support:C:occurrence:0',r.advance(y,support^1),(support,)))
    return plans


def prescribed_choices(arrivals,lengths=(1,3,1)):
    """One explicit positive advance/hold history for given first arrivals.

    Other histories with the same arrival tuple remain in first-arrival CWM
    families, rather than being identified with this representative.
    """
    if len(arrivals)!=3 or any(type(t)is not int or t<n for t,n in zip(arrivals,lengths)):
        raise ValueError('arrival tick at least route length')
    selected=[set(range(1,n))|{t} for t,n in zip(arrivals,lengths)]
    return tuple(tuple(int(t in ss) for ss in selected) for t in range(1,max(arrivals)+1))


def execute_ticket(ticket,inventory,port,token):
    """A deliberately chosen actuator map, with the original U11 inverse.

    No native incidence follows from a Ticket. Refusal keeps all input data.
    The input inventory is now physically back at the material's source Cell.
    """
    if not ticket.identity or len(ticket.occurrences)!=3 or len(set(ticket.occurrences))!=3:
        raise ValueError('three distinct source occurrences on a named ticket')
    if type(ticket.authorized) is not bool or type(ticket.used) is not bool:
        raise ValueError('Boolean command flags required')
    if ticket.used:raise ValueError('this command was already consumed')
    if inventory.state.cells[ticket.actor]!=ticket.source:
        raise ValueError('material moved since command preparation')
    if r.advance(ticket.source,port)!=ticket.target:
        raise ValueError('command direction/target mismatch')
    if not ticket.authorized:return inventory,(),ticket
    y,trace=v.transaction(inventory,ticket.actor,port,True,(token,))
    if y is None:raise ValueError('inventory, source or occupancy precondition failed')
    used=Ticket(ticket.identity,ticket.actor,ticket.source,ticket.target,ticket.occurrences,True,True)
    return y,tuple(trace),used


def controlled_trace(arrivals=(1,3,1),H=None,enable=True,k=4,
                     body=None,actor=0,port=4,detour=6,support=8,
                     probabilities=(Q(1,2),)*3):
    """One controlled, isolated forward trace with all resource locations.

    Inputs already include reserved R, one message carrier, support C and two
    blank scratch registers at the rendezvous Cell. Timing records accompany
    the captured signals. Preparation resources and the controller are added
    assumptions, not a claim that the earlier model had these for free.
    The lifetime only gates actuation: expired packets may remain as records.
    No first-expiry material trajectory is inferred from latent arrival tuples.
    """
    if type(enable) is not bool:raise ValueError('explicit Boolean control input')
    body=standard_body() if body is None else body
    plans=plans_at(body,actor,port,detour,support)
    proto=f.Protocol(plans,probabilities,None)
    route=proto.trace(prescribed_choices(arrivals))
    if route[-1]['state'].outcome!='READY_RESERVED':raise AssertionError('routes unfinished')
    tau=max(arrivals);x=body.cells[actor];y=r.advance(x,port)
    inv=v.prepared(body,body.length()+1,1,reservoir_cell=x)
    token=inv.free[0][0];old_bound=tuple(t for leg in inv.tokens for t in leg)
    ids=tuple(q.identity for q in plans);frames=[]
    baseweight=route[-1]['weight']
    def emit(t,stage,bodycells,packetcells,free,held,bound,phase=None,scratch=None,
             heads=None,words=None,command=None,record_move=None):
        frames.append({'tick':t,'stage':stage,'body_cells':bodycells,
          'packet_cells':packetcells,'record_free':free,'record_held':held,'record_bound':bound,
          'phases':phase,'scratch':scratch,'path_heads':heads,'path_words':words,
          'command':command,'record_move':record_move,
          'occurrence_ids':ids,'material_identity':f'actor:{actor}:body',
          'source_signal_is_material':False,'native_event':False})
    for row in route:
        emit(row['tick'],'PACKET_TRANSPORT',body.cells,row['cells'],(),(token,),old_bound)
    duration=tau-min(arrivals)+POST_STAGES
    if H is not None and (type(H)is not int or H<0):raise ValueError('nonnegative lifetime')
    if H is not None and duration>H:
        return {'status':'WINDOW_BLOCKED_RETAINED','frames':frames,'body_after':body,
                'moved':False,'arrivals':arrivals,'required_window':duration,
                'candidate_weight':baseweight,'native_firing':False,'ticket':None}
    regs=c.Registers(tuple((tau-t)%k for t in arrivals),(0,0),tuple(t%k for t in arrivals))
    calibration=c.admission(regs,k,tau,arrivals,None,source_ids=ids)
    for dt,row in enumerate(calibration['trace'],1):
        emit(tau+dt,row['operation'],body.cells,(y,y,y),(),(token,),old_bound,
             row['after'].phases,row['after'].scratch)
    ticket=Ticket('isolated-command:0',actor,x,y,ids,enable)
    # Decision is LOCAL at y. R physically carries the record of it back to x.
    frames[-1]['command']=ticket
    post=calibration['output']
    emit(tau+5,'RETURN_RECORD_AND_TICKET',body.cells,(y,x,y),(token,),(),old_bound,
         c.drift(post,k,1).phases,post.scratch,command=ticket,record_move=(y,x))
    out,steps,used=execute_ticket(ticket,inv,port,token)
    if enable:
        for j,row in enumerate(steps,1):
            offset=5+j;pos=x if j==1 else y
            emit(tau+offset,row['kind'],row['material_cells'],(y,pos,y),
                 tuple(t for t,_ in row['free']),row['held'],row['bound'],
                 c.drift(post,k,offset-4).phases,post.scratch,
                 row['heads'],row['words'],used if j==3 else ticket,row['hop'])
    else:
        for j in range(1,4):
            emit(tau+5+j,'DENIED_WAIT',body.cells,(y,x,y),(token,),(),old_bound,
                 c.drift(post,k,1+j).phases,post.scratch,command=ticket)
    # Composing deterministic stages does not square the original preparation.
    weight=baseweight
    for _ in range(POST_STAGES):weight=r.serial(weight,r.edge(1))
    return {'status':'COMMITTED_CANDIDATE' if enable else 'DENIED_RETAINED',
      'frames':frames,'body_after':out.state,'inventory_before':inv,'inventory_after':out,
      'moved':enable,'arrivals':arrivals,'finish_tick':tau+8,'move_tick':tau+7 if enable else None,
      'candidate_weight':weight,'ticket':used,'source_signal_retained_at':y,
      'support_after':{'identity':ids[2],'cell':y,'status':'USED_COMMAND_RECORD' if enable else 'DENIAL_RECORD',
                       'release_performed':False},
      'extra_signal_carrier':ids[0],'source_ids_reserved':ids,
      'native_firing':False,'mechanical_reaction_derived':False,'actuator_map_is_new_assumption':True}


def completion_law(H,probabilities=(Q(1,2),)*3):
    """Exact whole-future law for reliable fixed-cost controlled actuation.

    Only successful histories are reused from U13. Failure-path semantics may
    differ; this claims a first-commit observer, not equality of full processes.
    """
    if H is not None and H<POST_STAGES:return Q(0)
    effective=None if H is None else H-POST_STAGES
    pr=f.Protocol(plans_at(standard_body()),probabilities,effective)
    return pr.solve(pr.initial())[0]


def law_prefix(H,horizon,probabilities=(Q(1,2),)*3):
    if H is not None and H<POST_STAGES:return [ZERO]*horizon
    eff=None if H is None else H-POST_STAGES
    curve=f.joined_first_curve((1,3,1),probabilities,eff,max(0,horizon-8))
    return ([ZERO]*8+curve)[:horizon]


def encode(obj):
    if isinstance(obj,Ticket):return dict(identity=obj.identity,actor=obj.actor,source=obj.source,
        target=obj.target,occurrences=obj.occurrences,authorized=obj.authorized,used=obj.used)
    if isinstance(obj,dict):return {str(k):encode(x) for k,x in obj.items()}
    if isinstance(obj,(tuple,list)):return [encode(x) for x in obj]
    return c.encode(obj)
