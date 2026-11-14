// EC49EXQ complete exact finite census. Compile: g++ -O3 -std=c++17 SCREEN_ALL_EC49EXQ.cpp -o screen
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
struct K {int u,v,w,ty,L; bool operator==(const K&z)const{return u==z.u&&v==z.v&&w==z.w;}};
vector<K> S[9];
vector<K> keys(int h){vector<K>out;for(int w=1;w<=(h+1)/2;w++) for(int u=0;u<=2*h+2;u++)for(int v=0;v<=h+1;v++){
 int r=u+v-h-1,f=h+1-v-2*w,g=h+1-u;
 if(min({r,f,g})>=0&&(r>=1||(r==0&&f>=1&&g>=1)))out.push_back({u,v,w,r>=1?4:2,2*(u+v+w-1)});
 }return out;}
int typ(int h,const K&k){return k.u+k.v-h-1>=1?4:2;}
int cap(const K&a,const K&b){return 2*(min(a.u,b.u)+min(a.v,b.v)+min(a.w,b.w)-1);}
int match(const vector<int>&hs,const vector<int>&m){
 if(hs.size()==1)return 0;
 if(hs.size()==2)return hs[1]==hs[0]+1?min(m[0],m[1]):0;
 assert(hs.size()==3);
 bool x=hs[1]==hs[0]+1,y=hs[2]==hs[1]+1;
 if(x&&y)return min(m[1],m[0]+m[2]);
 if(x)return min(m[0],m[1]);
 if(y)return min(m[1],m[2]);return 0;
}
struct Cost{int oldb,newb;};
Cost bound(const array<K,5>&ks,const array<vector<int>,5>&hs){
 int maxlen=0;int M[5],R[5],lens[5];int caps[5][5]{};vector<int>breaks{1};
 for(int i=0;i<5;i++){
  lens[i]=ks[i].L; maxlen=max(maxlen,lens[i]);vector<int>m;
  for(int h:hs[i])m.push_back(typ(h,ks[i]));
  M[i]=accumulate(m.begin(),m.end(),0);R[i]=M[i]-match(hs[i],m);
  breaks.push_back(max(1,lens[i]-3));breaks.push_back(lens[i]-2);breaks.push_back(lens[i]+1);
  for(int j=0;j<i;j++){caps[j][i]=caps[i][j]=cap(ks[i],ks[j]);breaks.push_back(caps[i][j]+1);}
 }
 breaks.push_back(maxlen+1);sort(breaks.begin(),breaks.end());breaks.erase(unique(breaks.begin(),breaks.end()),breaks.end());
 int oldB=0,newB=0;
 for(size_t n=0;n+1<breaks.size();n++){
  int d=breaks[n], width=breaks[n+1]-d;if(d>maxlen||width<=0)continue;
  int q[5],r[5];for(int i=0;i<5;i++){
   q[i]=d>lens[i]?0:d>=lens[i]-2?M[i]:1;
   r[i]=d>lens[i]?0:d>=lens[i]-2?M[i]:d==lens[i]-3?R[i]:1;
  }
  int bestold=0,bestnew=0;
  for(int mask=1;mask<32;mask++){
   bool ok=true;int a=0,b=0;
   for(int i=0;i<5&&ok;i++)if(mask&(1<<i)){
    a+=q[i];b+=r[i];
    for(int j=i+1;j<5;j++)if((mask&(1<<j)) && caps[i][j]>=d && r[i]>0 && r[j]>0){ok=false;break;}
   }
   if(ok){bestold=max(bestold,a);bestnew=max(bestnew,b);}
  }
  oldB+=bestold*width;newB+=bestnew*width;
 }
 assert(newB>=oldB);return {oldB,newB};
}
struct Summary{long long n=0,oldless=0,newless=0,newle=0;int minB=9999,maxB=0;map<int,long long>hist;};
void append(Summary&x,Cost b){x.n++;x.oldless+=b.oldb<80;x.newless+=b.newb<80;x.newle+=b.newb<=80;x.minB=min(x.minB,b.newb);x.maxB=max(x.maxB,b.newb);x.hist[b.newb]++;}
void merge(Summary&all,const Summary&x){all.n+=x.n;all.oldless+=x.oldless;all.newless+=x.newless;all.newle+=x.newle;all.minB=min(all.minB,x.minB);all.maxB=max(all.maxB,x.maxB);for(auto [b,n]:x.hist)all.hist[b]+=n;}
void dump(const Summary&s){cout<<"{\"count\":"<<s.n<<",\"old_survivors_lt80\":"<<s.oldless<<",\"new_survivors_lt80\":"<<s.newless<<",\"new_survivors_le80\":"<<s.newle<<",\"excluded_E_lt80\":"<<(s.n-s.newless)<<",\"excluded_E_le80\":"<<(s.n-s.newle)<<",\"minLB\":"<<s.minB<<",\"maxLB\":"<<s.maxB<<",\"histogram\":{";bool first=true;for(auto [b,n]:s.hist){if(!first)cout<<",";first=false;cout<<"\""<<b<<"\":"<<n;}cout<<"}}";}
int main(){for(int h=2;h<=8;h++)S[h]=keys(h);int sizes[]={1,4,9,17,28,43,62};for(int h=2;h<=8;h++)assert(int(S[h].size())==sizes[h-2]);
 Summary triples,doubles;cout<<"{\"model\":\"H8_M5_S6\",\"status\":\"PASS\",\"triple_skeletons\":[";bool first=true;
 for(int a=2;a<=8;a++)for(int b=a+1;b<=8;b++)for(int c=b+1;c<=8;c++){
  vector<int>rem;for(int h=2;h<=8;h++)if(h!=a&&h!=b&&h!=c)rem.push_back(h);
  Summary group;
  for(auto k:S[a]){
   if(find(S[b].begin(),S[b].end(),k)==S[b].end()||find(S[c].begin(),S[c].end(),k)==S[c].end())continue;
   for(auto x:S[rem[0]])if(!(x==k))for(auto y:S[rem[1]])if(!(y==k)&&!(y==x))for(auto z:S[rem[2]])if(!(z==k)&&!(z==x)&&!(z==y))for(auto w:S[rem[3]])if(!(w==k)&&!(w==x)&&!(w==y)&&!(w==z)){
    array<K,5>ks={k,x,y,z,w};array<vector<int>,5>hs={vector<int>{a,b,c},vector<int>{rem[0]},vector<int>{rem[1]},vector<int>{rem[2]},vector<int>{rem[3]}};
    append(group,bound(ks,hs));
   }
  }
  if(group.n){if(!first)cout<<",";first=false;cout<<"{\"windows\":["<<a<<","<<b<<","<<c<<"],\"stats\":";dump(group);cout<<"}";merge(triples,group);}
 }
 cout<<"],\"double_skeletons\":[";first=true;
 for(int a=2;a<=8;a++)for(int b=a+1;b<=8;b++)for(int c=a+1;c<=8;c++)if(c!=b)for(int d=c+1;d<=8;d++)if(d!=b){
  vector<int>rem;for(int h=2;h<=8;h++)if(h!=a&&h!=b&&h!=c&&h!=d)rem.push_back(h);
  if(rem.size()!=3)continue;
  Summary group;
  for(auto ka:S[a])if(find(S[b].begin(),S[b].end(),ka)!=S[b].end())for(auto kb:S[c])if(!(ka==kb)&&find(S[d].begin(),S[d].end(),kb)!=S[d].end()){
   for(auto x:S[rem[0]])if(!(x==ka)&&!(x==kb))for(auto y:S[rem[1]])if(!(y==ka)&&!(y==kb)&&!(y==x))for(auto z:S[rem[2]])if(!(z==ka)&&!(z==kb)&&!(z==x)&&!(z==y)){
    array<K,5>ks={ka,kb,x,y,z};array<vector<int>,5>hs={vector<int>{a,b},vector<int>{c,d},vector<int>{rem[0]},vector<int>{rem[1]},vector<int>{rem[2]}};
    append(group,bound(ks,hs));
   }
  }
  if(group.n){if(!first)cout<<",";first=false;cout<<"{\"pairs\":[["<<a<<","<<b<<"],["<<c<<","<<d<<"]],\"stats\":";dump(group);cout<<"}";merge(doubles,group);}
 }
 cout<<"],\"triple\":";dump(triples);cout<<",\"double\":";dump(doubles);Summary all;merge(all,triples);merge(all,doubles);cout<<",\"all\":";dump(all);cout<<"}\n";
 if(triples.n!=123147||doubles.n!=1866362||triples.oldless!=16223||doubles.oldless!=494545){cerr<<"Prior verification mismatch\n";return 1;}
}
