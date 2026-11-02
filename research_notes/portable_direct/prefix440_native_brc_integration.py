#!/usr/bin/env python3
"""Run in verified Enterprise Math checkout: PYTHONPATH=src python <this-file>."""
from fractions import Fraction
from enterprise_math.brc_transport import Affine, MomentState, explicit_moment
from enterprise_math.brc_control_port import ControlPacket
ZERO=(0,0,0,0,0,0)
def tr(x):
    return Affine(Affine.identity(6).a,(Fraction(x),Fraction(0),Fraction(0),Fraction(0),Fraction(0),Fraction(0)))
def packet(nstates,target,duration,hist):
    return ControlPacket.from_edges(nstates,0,duration,[(0,target,1,tr(x),count) for x,count in hist])
def dist(result,target):
    return {int(p[0]):h.count for (t,p),h in result.items() if t==target}
E=((3,1),(-1,3));O=((1,3),(-3,1))
pe=packet(1,0,3,E);po=packet(1,0,3,O)
assert dist(pe.evaluate(0,ZERO),0)=={3:1,-1:3}
assert dist(po.evaluate(0,ZERO),0)=={1:3,-3:1}
seed=MomentState.from_point(ZERO)
me=pe.moment_action({0:seed})[0];mo=po.moment_action({0:seed})[0]
assert me==mo and me.to_matrix()[0][0]==12
assert me.to_matrix()[0][6]==0 and me.to_matrix()[6][6]==4
assert me.to_matrix()==explicit_moment({p:h for (t,p),h in pe.evaluate(0,ZERO).items()})
assert mo.to_matrix()==explicit_moment({p:h for (t,p),h in po.evaluate(0,ZERO).items()})
split=ControlPacket.from_edges(3,0,3,[(0,1,1,tr(x),c) for x,c in E]+[(0,2,1,tr(x),c) for x,c in O])
assert dist(split.evaluate(0,ZERO),1)=={3:1,-1:3}
assert dist(split.evaluate(0,ZERO),2)=={1:3,-3:1}
assert split.moment_action({0:seed})[1]==split.moment_action({0:seed})[2]==me
later=ControlPacket.deterministic((0,1,2),start=3,duration=1,effects=tuple(tr(1) for _ in range(3)))
serial=split.then(later)
assert serial.duration==4 and serial.end==4
assert dist(serial.evaluate(0,ZERO),1)=={4:1,0:3}
assert dist(serial.evaluate(0,ZERO),2)=={2:3,-2:1}
assert serial.moment_action({0:seed})[1]==serial.moment_action({0:seed})[2]
two=pe.alternatives(pe)
assert dist(two.evaluate(0,ZERO),0)=={3:2,-1:6}
assert two.moment_action({0:seed})[0].to_matrix()[6][6]==8
merged=ControlPacket.from_edges(3,0,2,[(0,0,1,tr(0),1),(0,0,1,tr(0),1)])
kept=ControlPacket.from_edges(3,0,2,[(0,1,1,tr(0),1),(0,2,1,tr(0),1)])
assert merged.blocks[0][2].entries[0][2]==2
assert {t for _,t,_ in kept.blocks}=={1,2}
print("PASS: genuine upstream ControlPacket, EffectHistogram, MomentState: from_edges/then/alternatives/evaluate/moment_action")
