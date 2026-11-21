"use strict";
// Independent, exact integer audit of conditional X6 C12 shared-Port exclusions.
// Run: node X6_TIME_UNIT242_MULTITRIAD_C12_EXCLUSION_WINDING_CHECK_20261121_2000.js
const check = function runCheck(){
const n=12, mod=(x)=>((x%n)+n)%n;let assertions=0, legal=0,blocked=0,masks=0,moves=0,walks=0;
function check(cond,message){assertions++;if(!cond)throw Error("FAILED:"+message);}
const a=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]];
const xy=[];for(let r=0;r<6;r++){xy.push(a[r]);xy.push(a[r].map((v,i)=>v+a[(r+1)%6][i]));}
check(new Set(xy.map(x=>x.join(","))).size===12,"native cells distinct");
for(let q=0;q<n;q++)for(const s of [-1,1]){
const diff=xy[mod(q+s)].map((v,i)=>v-xy[q][i]);check(diff.reduce((u,v)=>u+Math.abs(v),0)===1,"each C12 arc native signed unit");
}
for(let A=0;A<n;A++)for(let B=0;B<n;B++){if(A===B)continue;let d=mod(B-A);check(d>=1&&d<=11,"initial gap");
for(let mover=0;mover<2;mover++)for(let s of [-1,1]){
let nextA=mover===0?mod(A+s):A,nextB=mover===1?mod(B+s):B;
if(nextA===nextB){blocked++;check((d===1||d===11),"blocked only adjacent");continue;}
legal++;let d2=mod(nextB-nextA);check(d2-d===(mover===0?-s:s),"gap coboundary");
}}
check(legal===480,"legal transitions count");check(blocked===48,"blocked transitions count");
for(let mask=0;mask<(1<<12);mask++){
const start=[];for(let q=0;q<n;q++)if(mask&(1<<q))start.push(q);let k=start.length;if(k<2||k>11)continue;masks++;
for(let s of [-1,1]){
const pos=start.slice();let displacement=new Array(k).fill(0);
for(let r=1;r<=12;r++){
let moved=new Set();
while(moved.size<k){
let chosen=-1;
for(let i=0;i<k;i++)if(!moved.has(i)&&!pos.includes(mod(pos[i]+s))){chosen=i;break;}
check(chosen!==-1,"unblocked single-occupancy transfer exists");
const before=pos[chosen],after=mod(before+s);
check(after!==before && !pos.includes(after),"occupied target excluded");
const diff=xy[after].map((v,j)=>v-xy[before][j]);
check(diff.reduce((t,v)=>t+Math.abs(v),0)===1,"primitive signed transfer");
pos[chosen]=after;displacement[chosen]+=s;moved.add(chosen);moves++;
}
for(let i=0;i<k;i++)check(pos[i]===mod(start[i]+s*r),"round realizes common translation");
}
for(let i=0;i<k;i++){check(pos[i]===start[i],"closed label-native return");check(displacement[i]===s*12,"all winding equal");}
walks++;
}
}
check(masks===4082,"all occupied masks from k2..11");check(walks===8164,"both directions for each mask");check(moves===589248,"all carried primitive moves");
return {n,distinct_cells:12,ordered_two_token_states:132,legal_directed_transitions:legal,guard_blocked_transitions:blocked,occupancy_masks_k2_to_11:masks,constructive_closed_histories:walks,verified_primitive_transfers:moves,assertions,failures:0,model:"conditional signed Port; one indivisible labeled F per Cell; one-at-a-time single occupancy; twelve-cell OUTER ring"};
};
console.log(JSON.stringify(check(), null, 2));
