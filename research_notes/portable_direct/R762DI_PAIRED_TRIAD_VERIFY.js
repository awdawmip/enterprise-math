"use strict";
// R762DI: exact six-dimensional native-step verification, Node.js >=16.
const assert=require("node:assert/strict");
const P=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
const six=[0,1,2,3,4,5], pairs=[];
for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)pairs.push([i,j]);
function g(a,b){while(b){const t=a%b;a=b;b=t;}return a;}
function area(w) {
  const out=[];
  for(const [i,j] of pairs) {
    let z=0;
    for(let s=0;s<w.length;s++)for(let t=s+1;t<w.length;t++)
      z += (w[s][0]===i?w[s][1]:0)*(w[t][0]===j?w[t][1]:0)
         -(w[s][0]===j?w[s][1]:0)*(w[t][0]===i?w[t][1]:0);
    out.push(z);
  }
  return out;
}
const prediction={2:[1,{"36":1},1],4:[8,{"4":6,"6":2},18]};
const ordinary=[19,{"1":6,"2":12,"6":1},36];
let configurations=0, words=0, modulusChecks=0;
for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++){
  const S=[i,j,k];
  for(let bits=0;bits<8;bits++){
    const signs=S.map((_,a)=>(bits&(1<<a))?-1:1);
    const outcomes=[];
    for(const u of P)for(const v of P){
      const word=[...u.map(a=>[S[a],signs[a]]),...v.map(a=>[S[a],-signs[a]])];
      const disp=Array(6).fill(0);
      for(const [a,s] of word)disp[a]+=s;
      assert(disp.every(x=>x===0));
      const A=area(word);
      for(let l=0;l<pairs.length;l++){
        const [a,b]=pairs[l], ai=S.indexOf(a),bi=S.indexOf(b);
        let want=0;
        if(ai>=0&&bi>=0){
          const su=u.indexOf(ai)<u.indexOf(bi)?1:-1;
          const sv=v.indexOf(ai)<v.indexOf(bi)?1:-1;
          want=signs[ai]*signs[bi]*(su+sv);
        }
        assert.equal(A[l],want);
      }
      outcomes.push(A);words++;
    }
    for(let q=2;q<=16;q++){
      const counts=new Map();
      for(const A of outcomes){
        const key=A.map(x=>(x%q+q)%q).join(",");
        counts.set(key,(counts.get(key)||0)+1);
      }
      const sizeHist={};
      for(const c of counts.values())sizeHist[c]=(sizeHist[c]||0)+1;
      const gcd=[...counts.values()].reduce(g,0);
      const [states,hist,minSeeds]=prediction[q]||ordinary;
      assert.equal(counts.size,states);
      assert.deepEqual(sizeHist,hist);
      assert.equal(36/gcd,minSeeds);
      modulusChecks++;
    }
    configurations++;
  }
}
const report={status:"PASS",scope:"paired candidate triad path blocks, not licensed force events",supports:20,sign_patterns:8,configurations,words,moduli:"2..16",modulus_histograms:modulusChecks,word_modulus_assignments:words*15,classes_q2:1,classes_q4:8,classes_other:19,min_uniform_seeds:{q2:1,q4:18,other:36},independent_review:"NOT_REVIEWED"};
console.log(JSON.stringify(report,null,2));
