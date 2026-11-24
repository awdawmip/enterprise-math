#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <iostream>
using namespace std;
using X=array<long long,8>;using I=long long;
I p(I a){return max(0LL,a);}
pair<I,I> dist(const X&x,I q,I a1,I a,I b,I a7){I U=x[3]-a,V=x[7]-a7,W=p(a1+b-q);I d2=max({0LL,p(U-q)+p(V-q)-q,W+p(x[2]-q)+p(x[6]-q)-q,W+p(U+x[2]-q)+p(V+x[6]-q)-2*q});I s=p(a1+a-q),l=p(s-a),h=min(s,a1);auto M=[&](I t,I z){return max({0LL,s-t-z,l-t,s-h-z});};return {d2,max(M(q,q),p(V-q)+M(q-x[6],q-x[4]-x[5]+b)-q)};}
bool endpoints(const X&x,I q,I r){auto [d,e]=dist(x,q,0,0,0,0);auto [f,g]=dist(x,q,x[1],x[3],x[5],x[7]);return min({d,e,f,g})>=r;}
bool scan(const X&x,I q,I r){if(!endpoints(x,q,r))return false;I B=x[5],P=x[1],V=x[7];auto bounds=[&](I a){I U=x[3]-a,k=max(0LL,p(U-q)+p(V-q)-q),c=max(p(x[2]-q)+p(x[6]-q)-q,p(U+x[2]-q)+p(V+x[6]-q)-2*q);I L=k>=r||c>=r?0:p(q-P+r-c);I s=p(P+a-q),l=p(s-a),h=min(s,P),t=p(V-q)-q,J=max({0LL,s-2*q,l-q,s-h-q,t+p(l-q+x[6])}),C=t+max(s-2*q+x[6]+x[4]+B,s-h-q+x[4]+B);return pair<I,I>{L,J>=r?B:min(B,C-r)};};for(I a=0;a<x[3];++a)if(bounds(a+1).first>bounds(a).second)return false;return true;}
bool closed(const X&x,I q,I r){if(!endpoints(x,q,r))return false;I A=x[3],B=x[5],P=x[1],V=x[7],t=p(V-q)-q,d=p(V+x[6]-q)-2*q,l=p(P-q);I K0=p(t),K1=t+A-q,C0=max(p(x[2]-q)+p(x[6]-q)-q,d),C1=d+A+x[2]-q,J0=max({0LL,l-q,t+p(l-q+x[6])}),J1=max(P-3*q,-2*q),E0=t+x[4]+B+max(x[6]-2*q,-q),E1=t+x[4]+B+max(P-3*q+x[6],-2*q);if(max({K0,C0,J0})>=r)return true;I lo=max({0LL,K1-r,C1-r}),hi=min(A-1,r-1-J1);if(lo>hi)return true;I m=max({C0+E0,C1-1+E1,C0+E1+lo,C1-1+E0-hi});return m>=q-P+2*r;}
X rotate(const X&x){X y{};for(int i=1;i<=7;i++){int b1=i&1,b2=(i>>1)&1,b3=(i>>2)&1,j=(b2^b1)|((b3^b1)<<1)|(b1<<2);y[j]=x[i];}return y;}
bool ge(const X&x,I q,I u){I A=x[3],B=x[5],C=x[6],r=q+4*u+1;return p(x[1]-q)+p(A-q)+p(B+x[7]-q)>=r&&p(x[2]-q)+p(C-q)+p(B+x[1]-q)>=r&&p(x[4]-q)+p(A-q)+p(B+x[2]-q)>=r&&p(x[7]-q)+p(C-q)+p(B+x[4]-q)>=r;}
bool opp(I a,I b,I c,I d,I q,I r){return max({a,b,c,d})>=2*q+r||max({a+b,c+d,a+c,b+d})>=3*q+r||a+b+c+d>=4*q+r;}
int main(int argc,char**argv){if(argc==1){I count=0,yes=0;X x{};for(int k=0;k<78125;k++){int z=k;for(int j=1;j<=7;j++){x[j]=z%5;z/=5;}for(I q=0;q<=4;q++)for(I r=1;r<=7;r++){bool a=scan(x,q,r),b=closed(x,q,r);assert(a==b);count++;yes+=b;}}cout<<"regression "<<count<<" safe "<<yes<<"\n";return 0;}
I u=stoll(argv[1]);I start=argc>2?stoll(argv[2]):u+1,end=argc>3?stoll(argv[3]):4*u-4;for(I q=start;q<=end;q++){I r=2*u+1,F=min(4*q+8*u+2,max(5*q+5*u+2,6*q+4*u+2)),n=F-1,T=2*q+r;I stable=0,geyes=0,fail[4]={},safe=0,partitions=0;X x{};auto ts=chrono::steady_clock::now();for(I A=0;A<=n;A++)for(I C=0;C<=n-A;C++)for(I B=0;B<=n-A-C;B++){I S=n-A-B-C;x[3]=A;x[5]=B;x[6]=C; // Both opposite pairs must satisfy cell, row/column, or full cut; filter by singleton-pair total.
for(I t=0;t<=S;t++){I v=S-t;auto possible=[&](I s){return max({A,C,s})>=T||max(A,C)+s>=3*q+r||A+C+s>=4*q+r;};if(!possible(t)||!possible(v))continue;for(I a=0;a<=t;a++){x[1]=a;x[4]=t-a;if(!opp(a,A,C,t-a,q,r))continue;for(I b=0;b<=v;b++){x[2]=b;x[7]=v-b;partitions++;if(!opp(b,A,C,v-b,q,r))continue;stable++;if(!ge(x,q,u))continue;geyes++;X y=x;int e=0;for(;e<4;e++){if(!closed(y,q,r))break;y=rotate(y);}if(e==4){safe++;cout<<"WITNESS ";for(int i=1;i<=7;i++)cout<<x[i]<<",";cout<<"\n";}else fail[e]++;}}}}cout<<"u="<<u<<" q="<<q<<" n="<<n<<" checked="<<partitions<<" opposite="<<stable<<" GE+opposite="<<geyes<<" fail="<<fail[0]<<","<<fail[1]<<","<<fail[2]<<","<<fail[3]<<" safe="<<safe<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-ts).count()<<endl;}}
