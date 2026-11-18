/* Run with node triad_check.js. All computed integers in this fixed finite
   certificate are exactly representable; no sampled or floating probabilities.
   Ported transport_slots from the immutable V38 blob 328c328d76e5766261f590afa710671b0a81f0cb. */
"use strict";
const assert = require("node:assert/strict");
const roots = ["014","015","023","123"];
const frames = ["012","021","102","120","201","210"];
const orbitNames = ["013","014","024","124","023","123"];
const orbit = x => ({"015":"014","025":"024","125":"124"}[x] || x);
const ports = [];
for (let a=0;a<6;a++) for (let b=a+1;b<6;b++) for (let c=b+1;c<6;c++)
    ports.push(""+a+b+c);
const adjacent = (s,t) => [...s].filter(x=>t.includes(x)).length===2;
const midpoint = (s,t) => ports.filter(u=>adjacent(s,u)&&adjacent(u,t));
function transport(previous,s,t) {
    assert.ok(adjacent(s,t));
    const removed = [...s].find(x=>!t.includes(x)), next = {};
    for (const x of t) next[x] = s.includes(x) ? previous[x] : previous[removed];
    return next;
}
assert.deepEqual(midpoint("012","013"),roots);
const branches=roots.map(u=>{
    const out=[];
    for (const v of midpoint("012",u)) for (const w of midpoint(u,"013")) {
        const route=["012",v,u,w,"013"];
        let mapping={"0":"0","1":"1","2":"2"};
        for (let i=1;i<route.length;i++) mapping=transport(mapping,route[i-1],route[i]);
        const frame=[..."013"].map(i=>mapping[i]).join("");
        out.push({u,v,w,frame,key:frames.indexOf(frame),bin:orbitNames.indexOf(orbit(v))});
    }
    return out;
});
assert.equal(new Set(branches.flat().map(x=>[x.u,x.v,x.w,x.frame].join("."))).size,64);
assert.ok(branches.flat().every(x=>x.key>=0 && x.bin>=0));
const unmarked=branches.map(group=>frames.map(f=>group.filter(e=>e.frame===f).length));
assert.deepEqual(unmarked,[[6,4,0,1,1,4],[6,4,0,1,1,4],[4,5,2,2,2,1],[4,1,2,2,2,5]]);
const marked=frames.map(f=>4*branches[0].filter(e=>e.v==="124"&&e.frame===f).length);
assert.deepEqual(marked,[4,0,0,0,4,8]);

// Weights have common denominator den; the marking parameter is s/m.
function laws(weights,s,m) {
    const den=weights.reduce((x,y)=>x+y,0), singleDen=16*m*den, pairDen=256*m*m*den;
    const P=Array(6).fill(0), anonymous=Array(6).fill(0);
    const anonymousFrame=Array(36).fill(0), same=Array(36).fill(0);
    for (let i=0;i<4;i++) {
        const mass=e=>i===0 ? m-s+4*s*Number(e.v==="124") : m;
        for (const e of branches[i]) {
            const w=weights[i]*mass(e);
            P[e.key]+=w;
            anonymous[e.bin]+=w;
            anonymousFrame[6*e.bin+e.key]+=w;
            for (const g of branches[i]) same[6*e.key+g.key]+=w*mass(g);
        }
    }
    const [a,b,c,d]=weights,z=a*s;
    assert.equal(P.reduce((x,y)=>x+y),singleDen);
    assert.equal(same.reduce((x,y)=>x+y),pairDen);
    assert.equal(den*8*P[2],(c+d)*singleDen);
    assert.equal(4*(P[4]-P[3]),16*z);
    assert.equal(4*(P[1]-P[5])+32*z,16*m*(c-d));
    const expectedAnonymous=[den*m-z,(a+b)*m-z,(a+b+2*c)*m-z,
                             (a+b+2*d)*m+3*z,d*m,c*m];
    assert.deepEqual(anonymous,expectedAnonymous.map(k=>4*k));
    assert.equal(16*signedPair(same)*den*m*m,a*s*s*pairDen);
    return {den,singleDen,pairDen,P,anonymous,anonymousFrame,same};
}
function signedPair(joint) {
    return joint[6*4+4]-joint[6*4+3]-joint[6*3+4]+joint[6*3+3];
}
function mixture(law,k,l) {
    const {den,singleDen,P,same}=law;
    const mass=same.map((x,i)=>k*den*x+(l-k)*P[Math.floor(i/6)]*P[i%6]);
    return {mass,denom:l*singleDen*singleDen};
}
const firstClasses=new Map(),secondClasses=new Map();
function bind(map,key,vector) {
    const previous=map.get(key);
    if(previous!==undefined) assert.equal(previous,vector);
    map.set(key,vector);
}
let count=0, mixedChecks=0;
for (let a=0;a<=6;a++) for(let b=0;a+b<=6;b++) for(let c=0;a+b+c<=6;c++) {
    const d=6-a-b-c,den=6,m=4,S=c+d;
    for(let s=0;s<=m;s++) {
        const law=laws([a,b,c,d],s,m);
        const singleKey=[c,d,a*s].join(","),pairKey=[c,d,a*s,a*s*s].join(",");
        bind(firstClasses,singleKey,[law.P,law.anonymous,law.anonymousFrame].join("|"));
        bind(secondClasses,pairKey,law.same.join(","));
        for (const k of [0,1,2]) {
            const l=2, {mass,denom}=mixture(law,k,l);
            // 64 P(102,102) = rho*S+(1-rho)*S^2, for S the normalized bend mass.
            assert.equal(64*mass[6*2+2]*l*den*den,
                         (k*S*den+(l-k)*S*S)*denom);
            // 16 E(h1 h2) = rho*a*t^2+(1-rho)*(a*t)^2.
            assert.equal(16*signedPair(mass)*l*den*den*m*m,
                         (k*a*s*s*den+(l-k)*a*a*s*s)*denom);
            mixedChecks++;
        }
        count++;
    }
}
assert.deepEqual([count,firstClasses.size,new Set(firstClasses.values()).size,
                  secondClasses.size,new Set(secondClasses.values()).size,mixedChecks],
                 [420,182,182,252,252,1260]);
const caseA=laws([1,1,1,1],1,2),caseB=laws([3,1,2,2],1,3);
assert.ok(caseA.P.every((v,i)=>v*caseB.singleDen===caseB.P[i]*caseA.singleDen));
assert.equal(256*signedPair(caseA.same),caseA.pairDen);
assert.equal(384*signedPair(caseB.same),caseB.pairDen);
const pureA=mixture(laws([1,1,0,0],1,2),1,1);
const pureB=mixture(laws([1,2,0,0],3,4),1,2);
assert.ok(pureA.mass.every((v,i)=>v*pureB.denom===pureB.mass[i]*pureA.denom));
console.log("64 named histories; 1024 ordered same-root pairs per parameter.");
console.log("420 grid parameters; 182 anonymous/single classes; 252 same-root classes.");
console.log("1260 mixed-root checks; both discrimination and 36-cell collision passed.");
