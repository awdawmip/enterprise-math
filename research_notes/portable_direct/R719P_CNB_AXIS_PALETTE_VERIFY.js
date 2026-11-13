// R719P: cyclic non-backtracking X6/J(3+q,3) exact integer palette verification.
// Node.js 18+; enumerates BRC-positive path branches with no signed cancellation.
const verify = function verify(){
 const labels=["012","021","102","120","201","210"], S="012";
 const C=(x,m)=>{let r=[];function rec(t,z){if(z.length===3){r.push(z.join(""));return}for(let i=t;i<x;i++)rec(i+1,z.concat(i))}rec(0,[]);return r};
 const neigh=(v,vs)=>vs.filter(w=>w!==v&&[...v].filter(a=>w.includes(a)).length===2);
 const mv=(frame,next)=>{const gone=[...frame].find(c=>!next.includes(c));const enter=[...next].find(c=>!frame.includes(c));if(gone===undefined||enter===undefined)throw Error("bad transport");return frame.replace(gone,enter)};
 const hist=(map)=>Object.fromEntries(labels.map(k=>[k,String(map.get(k)||0n)]));
 function dyn(n,limit){const vs=C(n),A=Object.fromEntries(vs.map(v=>[v,neigh(v,vs)]));let d=new Map(),res={};for(const w of A[S])d.set([S,w,mv(S,w),w].join("|"),1n);for(let m=2;m<=limit;m++){let nd=new Map(),h=new Map();for(const [k,v] of d){const [prev,cur,frame,first]=k.split("|");for(const w of A[cur]){if(w===prev)continue;const newf=mv(frame,w);if(w===S&&cur!==first)h.set(newf,(h.get(newf)||0n)+v);const key=[cur,w,newf,first].join("|");nd.set(key,(nd.get(key)||0n)+v)}}res[m]=hist(h);d=nd}return res}
 function brute(n,m){const vs=C(n),A=Object.fromEntries(vs.map(v=>[v,neigh(v,vs)])),h=new Map();function walk(prev,cur,first,frame,steps){if(steps===m){if(cur===S&&prev!==first)h.set(frame,(h.get(frame)||0n)+1n);return}for(const w of A[cur]){if(w===prev)continue;walk(cur,w,first===null?w:first,mv(frame,w),steps+1)}}walk(null,S,null,S,0);return hist(h)}
 const D4=dyn(4,17),D5=dyn(5,12),D6=dyn(6,6);
 const sum=h=>labels.reduce((s,k)=>s+BigInt(h[k]),0n);
 const supp=h=>labels.filter(k=>BigInt(h[k])>0n);
 const eq=(x,y,msg)=>{if(JSON.stringify(x)!==JSON.stringify(y))throw Error(msg+" "+JSON.stringify(x)+" vs "+JSON.stringify(y))};
 for(const n of [4,5,6]){const d=n===4?D4:n===5?D5:D6;const top=n===4?8:6;for(let m=3;m<=top;m++)eq(d[m],brute(n,m),`dp/dfs n=${n} m=${m}`)}
 const parity=h=>{let a=[...h].map(Number),inv=0;for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)inv+=(a[i]>a[j]);return inv%2};
 for(let m=3;m<=17;m++)for(let k of supp(D4[m])){if(parity(k)!==m%2)throw Error("parity violation "+m+" "+k)}
 eq(supp(D4[3]),["021","102","210"],"n4 length3");
 eq(supp(D4[4]),["120","201"],"n4 length4");
 if(sum(D4[5])!==0n)throw Error("n4 length5");
 for(let m=6;m<=17;m++){if(supp(D4[m]).length!==3)throw Error("n4 support size m"+m)}
 for(let m=4;m<=12;m++){if(supp(D5[m]).length!==6)throw Error("n5 six coverage m"+m)}
 const e=[[3,"18","6","0"],[4,"54","48","9"],[5,"360","252","198"],[6,"2934","2064","2133"]];
 for(const [m,id,tr,cy] of e){let h=D6[m];if(h["012"]!==id||["021","102","210"].some(k=>h[k]!==tr)||["120","201"].some(k=>h[k]!==cy))throw Error("R718 mismatch length "+m)}
 return {schema:"R719P_CNB_AXIS_PALETTE_EXACT_V1",status:"R719P_CNB_AXIS_PALETTE_EXACT_PASS",methods:["exact_BigInt_DP","independent_full_DFS"],root:S,axes_by_palette:[4,5,6],checked_dp_max_length:{"4":17,"5":12,"6":6},dfs_checked:{"4":"3..8","5":"3..6","6":"3..6"},histograms:{"4":D4,"5":D5,"6":D6},assertions:["q=1 holonomy parity equals walk length parity","q=1 length 5 no CNB paths","q=1 each allowed parity class has 3 states for lengths 6..17","q=2 all six for lengths 4..12","q=3 matches R718 at lengths 3..6"]};
};
console.log(JSON.stringify(verify(), null, 2));
