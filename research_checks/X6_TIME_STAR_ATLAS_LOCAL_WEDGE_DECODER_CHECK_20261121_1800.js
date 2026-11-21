"use strict";
// Unit239: all local STAR order choices, no claim of a physical Port sensor.
const stars=[[0,2,5],[0,3,4],[1,2,4],[1,3,5]]; // K4 STAR atlas: A,B,C,D
const vec=(axis,sign=1)=>Array.from({length:6},(_,i)=>i===axis?sign:0);
const eq=(x,y)=>x.length===y.length&&x.every((v,i)=>v===y[i]);
const key=x=>x.join(',');
const neg=x=>x.map(v=>-v);
const add=(x,y)=>x.map((v,i)=>v+y[i]);
const wedge=(x,y)=>{let z=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)z.push(x[i]*y[j]-x[j]*y[i]);return z;};
const perm=(a)=>a.length===1?[[a[0]]]:a.flatMap((v,i)=>perm(a.filter((_,j)=>j!==i)).map(r=>[v,...r]));
const perms=stars.map(perm);
const cycle=p=>[...p.map(i=>vec(i)),...p.map(i=>vec(i,-1))];
let assertions=0, configurations=0, directedOptions=0, reverseWitnesses=0;
function check(x,m){assertions++;if(!x)throw Error(m);}
for(const pa of perms[0])for(const pb of perms[1])for(const pc of perms[2])for(const pd of perms[3]){
  const rings=[pa,pb,pc,pd].map(cycle);configurations++;
  for(let axis=0;axis<6;axis++)for(let sign of [-1,1]){
    const a=vec(axis,sign),opts=[];
    for(let star=0;star<4;star++){
      const ring=rings[star], r=ring.findIndex(v=>eq(v,a));
      if(r<0)continue;
      for(const dir of [-1,1]){
        const b=ring[(r+dir+6)%6];
        for(let branch of [0,1]){
          const steps=branch?[b,neg(a)]:[neg(a),b];
          const J=wedge(...steps);
          const mid=add(a,steps[0]);
          check(eq(add(mid,steps[1]),b),'endpoint identity');
          check(eq(mid,branch?add(a,b):vec(0,0)),'midpoint identity');
          check(eq(J,wedge(a,b).map(z=>branch?z:-z)),'ordered wedge branch identity');
          check(J.filter(Boolean).length===1,'single signed bivector coefficient');
          opts.push({b,star,dir,branch,J});directedOptions++;
        }
      }
    }
    check(opts.length===8,'exactly eight labeled possibilities at known signed Cell');
    check(new Set(opts.map(x=>key(x.J))).size===8,'J injective on eight choices');
    const nonzero=opts.filter(x=>x.branch===1);
    check(nonzero.length===4 && new Set(nonzero.map(x=>key(x.J))).size===4,'outer gate four possible outgoing choices');
    check(new Set(nonzero.map(x=>x.J.findIndex(v=>v!==0))).size===4,'outer gate unsigned wedge axis-pair support is enough');
    for(const x of opts){
      const decoded=opts.find(y=>eq(y.J,x.J));
      check(decoded===x,'unique full inverse with known start Cell');
      // When start Cell is not included, reversing macroedge + swapping branch collides exactly.
      check(eq(wedge(x.b,a).map(v=>x.branch?-v:v),x.J),'opposite start branch-swapped collision');
      reverseWitnesses++;
    }
  }
}
console.log(JSON.stringify({schema:'X6_STAR_ATLAS_LOCAL_WEDGE_DECODER_CERT_V1',unit:'Unit239',frozen_source:'a72226e2430ffa4786321ac86e7f0c599d5f0389',star_sets:stars.map(s=>s.map(i=>i+1)),orientation_choices_per_star:6,all_independent_star_order_configurations:configurations,known_signed_starts_per_configuration:12,choices_per_start:8,outer_choices_per_start:4,all_directed_branch_options:directedOptions,opposite_start_ambiguity_witnesses:reverseWitnesses,integer_assertions:assertions,failed_assertions:0,conclusion:'With current signed shell Cell a, one ordered bivector J reconstructs outgoing STAR, chirality, next signed shell Cell, and INNER/OUTER branch within the declared four-STAR local shortest-path graph. Under source-proved nonzero intermediate phase gate, branch is OUTER, leaving four outcomes and an unsigned bivector support sufficient. Physical Port readout remains unproved.'},null,2));
