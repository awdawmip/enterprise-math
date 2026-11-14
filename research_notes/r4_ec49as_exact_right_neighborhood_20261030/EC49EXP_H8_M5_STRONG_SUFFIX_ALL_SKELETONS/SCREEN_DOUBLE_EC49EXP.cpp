#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;
struct K{int u,v,w,ty,L;bool operator==(const K &z)const{return u==z.u&&v==z.v&&w==z.w;}};
vector<K> keys(int h){vector<K> out; for(int w=1;w<=(h+1)/2;w++)for(int u=0;u<=2*h+2;u++)for(int v=0;v<=h+1;v++){
 int r=u+v-h-1,f=h+1-v-2*w,g=h+1-u;
 if(min({r,f,g})>=0 && (r>=1||(r==0&&f>=1&&g>=1)))out.push_back({u,v,w,r>=1?4:2,2*(u+v+w-1)});
}return out;}
int cap(const K&a,const K&b){return 2*(min(a.u,b.u)+min(a.v,b.v)+min(a.w,b.w))-2;}
int B(const array<K,5>&ks, const array<int,5>&M){
 int Lmax=0;array<int,10> caps{}; int c=0;for(int i=0;i<5;i++){Lmax=max(Lmax,ks[i].L);for(int j=i+1;j<5;j++)caps[c++]=cap(ks[i],ks[j]);}
 vector<int> breaks{1,Lmax+1};for(int i=0;i<5;i++){breaks.push_back(max(1,ks[i].L-2));breaks.push_back(ks[i].L+1);}
 for(int v:caps)breaks.push_back(v+1);sort(breaks.begin(),breaks.end());breaks.erase(unique(breaks.begin(),breaks.end()),breaks.end());
 int total=0;
 for(int t=0;t+1<(int)breaks.size();t++){
   int d=breaks[t],next=breaks[t+1];if(d>Lmax||next<=d)continue;
   int q[5];for(int i=0;i<5;i++)q[i]=(d>ks[i].L?0:(d>=ks[i].L-2?M[i]:1));
   int best=0;
   for(int mask=1;mask<32;mask++){
     int weight=0;bool ok=true;
     for(int i=0;i<5&&ok;i++)if(mask&(1<<i)){
       weight+=q[i];if(q[i]==0)continue;
       for(int j=i+1;j<5;j++)if(mask&(1<<j)){
         if(q[j]==0)continue;
         if(cap(ks[i],ks[j])>=d){ok=false;break;}
       }
     }
     if(ok)best=max(best,weight);
   }
   total+=best*(next-d);
 }
 return total;
}
int main(){vector<K> S[9];for(int h=2;h<=8;h++)S[h]=keys(h);int expect[7]={1,4,9,17,28,43,62};for(int h=2;h<=8;h++)assert((int)S[h].size()==expect[h-2]);
 map<int,long long> hist;long long total=0,excluded80=0,excluded81=0;int bone=0;
 cout<<"{\"status\":\"PASS\",\"per_double\":[";bool first=true;
 for(int a=2;a<=8;a++)for(int b=a+1;b<=8;b++)for(int c=a+1;c<=8;c++)if(c!=b)for(int d=c+1;d<=8;d++)if(d!=b){
   vector<int> h;for(int i=2;i<=8;i++)if(i!=a&&i!=b&&i!=c&&i!=d)h.push_back(i);
   if(h.size()!=3)continue;
   long long cnt=0,ex80=0,ex81=0;int minb=10000,maxb=0;
   for(auto &ka:S[a]){
     if(find_if(S[b].begin(),S[b].end(),[&](auto &t){return t==ka;})==S[b].end())continue;
     for(auto &kb:S[c]){
       if(ka==kb||find_if(S[d].begin(),S[d].end(),[&](auto &t){return t==kb;})==S[d].end())continue;
       for(auto &k1:S[h[0]]){
         if(k1==ka||k1==kb)continue;
         for(auto &k2:S[h[1]]){
           if(k2==ka||k2==kb||k2==k1)continue;
           for(auto &k3:S[h[2]]){
             if(k3==ka||k3==kb||k3==k1||k3==k2)continue;
             array<K,5> ks={ka,kb,k1,k2,k3};array<int,5> M={ka.ty+S[b][0].ty,kb.ty+S[d][0].ty,k1.ty,k2.ty,k3.ty};
             // Correct shared key signature counts for each horizon.
             auto type_at=[&](int hh,const K &k)->int{int r=k.u+k.v-hh-1;return r>=1?4:2;};
             M[0]=type_at(a,ka)+type_at(b,ka);M[1]=type_at(c,kb)+type_at(d,kb);
             int lb=B(ks,M);hist[lb]++;cnt++;minb=min(minb,lb);maxb=max(maxb,lb);
             if(lb>=80)ex80++;if(lb>80)ex81++;
           }
         }
       }
     }
   }
   if(cnt){ if(!first)cout<<",";first=false;bone++;total+=cnt;excluded80+=ex80;excluded81+=ex81;
     cout<<"{\"pairs\":[["<<a<<","<<b<<"],["<<c<<","<<d<<"]],\"schedules\":"<<cnt<<",\"min_lb\":"<<minb<<",\"max_lb\":"<<maxb<<",\"E_lt_80_excluded\":"<<ex80<<",\"E_le_80_excluded\":"<<ex81<<"}";
   }
 }
 cout<<"],\"double_skeletons\":"<<bone<<",\"schedules\":"<<total<<",\"E_lt_80_excluded\":"<<excluded80<<",\"E_lt_80_survivors\":"<<(total-excluded80)<<",\"E_le_80_excluded\":"<<excluded81<<",\"histogram\":{";
 bool ff=true;for(auto [v,n]:hist){if(!ff)cout<<",";ff=false;cout<<"\""<<v<<"\":"<<n;}cout<<"}}\n";
 if(bone!=32||total!=1866362){cerr<<"census mismatch "<<bone<<" "<<total<<"\n";return 1;}return 0;
}
