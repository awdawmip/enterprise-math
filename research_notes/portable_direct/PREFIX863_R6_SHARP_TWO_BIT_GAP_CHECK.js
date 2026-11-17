function integerSqrt(n){if(n<0n)throw Error("negative sqrt");if(n<2n)return n;let x=1n<<BigInt((n.toString(2).length+1)>>1);for(;;){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}

function bitWidth(n){return n.toString(2).length;}

function gcdBig(a,b){while(b!==0n){[a,b]=[b,a%b];}return a;}

function hOf(g){let y=1;for(let d=1;d<=100000;d++){y=(2*y)%g;if(y===1||y===g-1)return d;}throw Error("h loop");}

function g3(p){let t=1;while(t<p)t*=3;return 3*t;}

function construct(p,g){const N=1n<<BigInt(p),G=BigInt(g);let a=integerSqrt((N+G-1n)/G+1n);a=a>1n?a-1n:1n;if(a%2n===0n)a++;while(G*a*(a+2n)<N)a+=2n;while(a>=3n&&G*(a-2n)*a>=N)a-=2n;const q1=G*a,q2=G*(a+2n);return {p,g,a:a.toString(),q1:q1.toString(),q2:q2.toString(),B:bitWidth(q2),L:Math.ceil(bitWidth(N*BigInt(p+1)-1n)/2)};}

function testPair(p,q1,q2){const N=1<<p,seen=new Map();for(let u=0;u<N;u++){const ru=u%q1;for(let i=-1;i<p;i++){const v=i===-1?u:u^(1<<i),key=ru*q2+(v%q2),first=seen.get(key);if(first!==undefined)return {ok:false,witness:[[first.u,first.v],[u,v]],residues:[ru,v%q2]};seen.set(key,{u,v});}}return {ok:true,transitions:N*(p+1),distinct:seen.size};}

function exhaustiveFailure(p,B){let candidates=0,passed=0,firstUnexpected=null,example=null;for(let q1=3;q1<(1<<B);q1+=2){for(let q2=3;q2<(1<<B);q2+=2){candidates++;const r=testPair(p,q1,q2);if(r.ok){passed++;if(!firstUnexpected)firstUnexpected=[q1,q2];}else if(!example)example={q1,q2,...r};}}return {p,peakWidthBound:B,oddModulusPairs:candidates,collisionFreePairs:passed,firstUnexpected,firstCollisionWitness:example};}

function runCheck(){const constructions=[];for(let p=1;p<=128;p++){const g=p===5?11:p===7?19:g3(p);const c=construct(p,g);if(hOf(g)<p)throw Error("unsafe transition labels p="+p);const {q1,q2,B,L}=c,N=1n<<BigInt(p);if(gcdBig(BigInt(q1),BigInt(q2))!==BigInt(g))throw Error("gcd");if(BigInt(q1)*BigInt(q2)/BigInt(g)<N)throw Error("lcm");if(p>=5&&B>L+2)throw Error("2-bit failure p="+p);if(p>=15&&!((36n*BigInt(p)+1n)**2n<BigInt(p)*N))throw Error("analytic inequality");if(p<=32)constructions.push({...c,additiveGap:B-L});if(p<=12){const r=testPair(p,Number(q1),Number(q2));if(!r.ok)throw Error("direct trajectory collision p="+p);}}
const targets=[{p:5,B:5,witness:[11,33],opt:6},{p:6,B:5,witness:[25,63],opt:6},{p:7,B:6,witness:[27,127],opt:7},{p:8,B:6,witness:[57,95],opt:7},{p:9,B:7,witness:[57,209],opt:8}];const exhaustions=[];for(const t of targets){const e=exhaustiveFailure(t.p,t.B);if(e.collisionFreePairs!==0)throw Error("unexpected small-width pair p="+t.p);const v=testPair(t.p,t.witness[0],t.witness[1]);if(!v.ok)throw Error("bad witness p="+t.p);exhaustions.push({...e,optimalWidth:t.opt,optimalWitness:t.witness,distinctTransitions:v.transitions});}
return {schema:"PREFIX863_EXACT_CERTIFICATE_V1",model:"fixed ordered odd moduli, before/after, no-op or flip exactly one named bit",status:"ALL_EXACT_ASSERTIONS_PASSED",universalConstructionChecked:"p=1..128 using exact BigInt and h(g)",completeTrajectoryChecks:"p=1..12",finiteOddPairExhaustion:"p=5..9 at one below exact optimal B",constructions,exhaustions};}

const certificate = runCheck();
console.log(JSON.stringify(certificate, null, 2));
