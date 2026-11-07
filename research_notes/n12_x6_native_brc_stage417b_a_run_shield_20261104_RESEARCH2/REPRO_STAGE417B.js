// Stage417-B | exact typed native-X6 A-tail shielding certificate.
// Node.js (or standard ECMAScript); exact integer and categorical arithmetic.
const STAGE417B = (function() {
  const D = Array.from({length:6},(_,j)=>[j+1,-j-1]).flat(), A=1,B=-1;
  function need(ok,msg){if(!ok)throw Error(msg)}
  function fiber(n) {
    const out=[];
    for(let r=2;r<n-2;r++)for(let s=r+2;s<n;s++)for(const i of [r,s]){
      const P=Array(i-1).fill(A).concat([B],Array(n-i).fill(A));
      const Q=Array(r-1).fill(A).concat([B],Array(s-r-1).fill(A),[B],Array(n-s).fill(A));
      out.push({r,s,i,P,Q});
    }
    return out;
  }
  function obs(P,Q){
    function one(X){
      const z=Array.from({length:6},(_,k)=>X.filter(x=>x===k+1).length-X.filter(x=>x===-k-1).length);
      const J={};
      for(let k=0;k<X.length-1;k++){const e=X[k]+','+X[k+1];J[e]=(J[e]||0)+1}
      return [X.length,z,Object.entries(J).sort((a,b)=>a[0].localeCompare(b[0]))];
    }
    return [one(P),one(Q),P.reduce((k,x,i)=>k+(i<Q.length&&x===Q[i]?1:0),0)];
  }
  const V=[
    [['APP',B,B],['CANCEL'],['POP'],['POP'],['APP',B,B],['CANCEL']],
    [['APP',B,B],['CANCEL'],['APP',B,A],['POP'],['POP'],['CANCEL']],
    [['APP',B,B],['CANCEL'],['CANCEL'],['POP'],['POP']]
  ];
  function run(x,trace){
    let P=x.P.slice(),Q=x.Q.slice(),pop=2,cancel=2;
    const records=[['INIT',obs(P,Q)]];
    for(const t of trace){
      if(t[0]==='APP'){
        need(D.includes(t[1])&&D.includes(t[2]),'APP domain');
        P.push(t[1]);Q.push(t[2]);
      }else if(t[0]==='POP'){
        if(!pop||!Q.length){records.push(['DENIED_POP']);break}
        Q.pop();pop--;
      }else if(t[0]==='CANCEL'){
        if(!cancel||P.length<2||Q.length<2||P.at(-2)!==-P.at(-1)||Q.at(-2)!==-Q.at(-1)){
          records.push(['DENIED_CANCEL']);break;
        }
        P.splice(-2);Q.splice(-2);cancel--;
      }else throw Error('unknown operation');
      records.push(['OK',obs(P,Q)]);
    }
    return JSON.stringify(records);
  }
  const key=x=>JSON.stringify([x.P.slice(-6),x.Q.slice(-7)]);
  const signature=x=>JSON.stringify(V.map(t=>run(x,t)));
  const reps=new Map();
  for(const x of fiber(11))if(!reps.has(key(x)))reps.set(key(x),x);
  const keys=[...reps.keys()];
  need(keys.length===32,'32 suffix keys');
  const classes=new Map();
  keys.forEach((k,i)=>{
    const s=signature(reps.get(k));
    if(!classes.has(s))classes.set(s,[]);
    classes.get(s).push(i);
  });
  const groups=[...classes.values()].sort((a,b)=>a[0]-b[0]);
  const expectedGroups=[[0,1,2,3],[4,5,12,13],[6,14,20],[7,15,21],
    [8,16,22],[9,17],[10,18,24],[11,19],[23],[25],[26],[27],[28],[29],[30],[31]];
  need(JSON.stringify(groups)===JSON.stringify(expectedGroups),'16 partition');
  const keyGroup=new Map();
  groups.forEach((g,j)=>g.forEach(i=>keyGroup.set(keys[i],j)));
  for(let n=11;n<=60;n++){
    const f=fiber(n),count=Array(16).fill(0),shield=[];
    need(f.length===(n-3)*(n-4),'fiber formula n='+n);
    for(const x of f){
      count[keyGroup.get(key(x))]++;
      if(x.P.slice(-5).every(v=>v===A)&&x.Q.slice(-5).every(v=>v===A))shield.push(x);
    }
    const expect=[(n-7)*(n-8),2*(n-7),n-6,n-6,n-6,n-7,n-6,n-7,...Array(8).fill(1)];
    need(JSON.stringify(count)===JSON.stringify(expect),'class-count n='+n);
    need(shield.length===(n-7)*(n-8),'shield-size n='+n);
    need(shield.every(x=>keyGroup.get(key(x))===0),'shield in class zero n='+n);
    if(n<=15)for(const x of f){
      const y=reps.get(key(x)),h=n-11;
      const pad={P:Array(h).fill(A).concat(y.P),Q:Array(h).fill(A).concat(y.Q)};
      need(JSON.stringify(obs(x.P,x.Q))===JSON.stringify(obs(pad.P,pad.Q)),'padded O');
      need(signature(x)===signature(pad),'padded V');
    }
  }
  const G=fiber(11).filter(x=>x.P.slice(-5).every(v=>v===A)&&x.Q.slice(-5).every(v=>v===A));
  need(G.length===12,'G11 size');
  for(const a of D)for(const b of D){
    need(new Set(G.map(x=>run(x,[['APP',a,b]]))).size===1,'all 144 APP');
  }
  const traces=[
    [['APP',-2,2],['CANCEL'],['POP'],['APP',-3,3]],
    [['POP'],['POP'],['APP',B,B],['CANCEL'],['APP',4,-4]],
    [['APP',B,B],['CANCEL'],['APP',-2,2],['POP'],['CANCEL']],
    [['APP',-4,-4],['APP',4,4],['CANCEL'],['POP'],['APP',B,B]]
  ];
  for(const t of traces)need(new Set(G.map(x=>run(x,t))).size===1,'mixed trace');
  return {
    marker:'STAGE417B_A_RUN_SHIELD_AND_SIXTEEN_TEST_CLASS_PASS',
    input:'P000 typed signed-X6 D=+-E1..+-E6; 2 Q-POP, 2 paired inverse CANCEL; full O=(length,z,J,K)',
    n11:{histories:56,raw_keys:32,V_classes:16,A5_class:12,class_sizes:[12,8,5,5,5,4,5,4,...Array(8).fill(1)]},
    n16:{histories:156,A5_class:72,class_sizes:[72,18,10,10,10,9,10,9,...Array(8).fill(1)]},
    n60_A5_class:53*52,
    counts_coverage:'All F_n n=11..60; exact tests on all 56 F11; all 144 APP pairs for G11; four mixed traces',
    group_key_indices:groups,
    mathematically_proved_universal_upper_bound:29,
    established_lower_bound_stage415:16,
    science_pins:{global:'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',em:'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',p000_blob:'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'},
    interpretation:'Exact finite validation supplements symbolic all-horizon proof; author-side UNREVIEWED / NOT_ADMITTED'
  };
})();
if(typeof console !== 'undefined') console.log(JSON.stringify(STAGE417B,null,2));
STAGE417B;
