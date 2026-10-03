function analyze_results(outdir)
  if nargin<1,outdir=fullfile(fileparts(mfilename('fullpath')),'output');end
  spec=jsondecode(fileread(fullfile(outdir,'experiment.json')));
  results=jsondecode(fileread(fullfile(outdir,'brc_results.json')));
  statusfile=fullfile(outdir,'analysis_checks.json');
  fid=fopen(statusfile,'w');fprintf(fid,'%s\n',jsonencode(struct('status','RUNNING_OR_FAILED','run_id',results.run_id)));fclose(fid);
  for key={'input_artifacts','output_artifacts'}
    artifacts=results.(key{1});
    for a=1:numel(artifacts)
      assert(strcmp(hash('sha256',fileread(fullfile(outdir,artifacts(a).name))),artifacts(a).sha256),'Input/output artifact hash mismatch');
    end
  end
  h=spec.h;rows={};equivalence_max=0;coarse_bound_ratio=0;
  assert(any(strcmp(results.status,{'PASS','BOUNDED_PARTIAL'})),'Failed scientific run cannot become analysis PASS');
  assert(~results.smoke,'Smoke evidence is not full-pilot evidence');
  assert(results.completed==numel(results.records),'Record count mismatch');
  assert(results.completed>0,'No completed exact trajectory to analyze');
  if strcmp(results.status,'PASS'),assert(results.completed==results.schedule_count);end
  for ri=1:numel(results.records)
    r=results.records(ri);ci=find(strcmp({spec.cases.name},r.case));c=spec.cases(ci);
    tr=r.trajectory;K=c.K;coupling=c.coupling;if tr==13,K=1.15*K;coupling=1.15*coupling;end
    truth=dlmread(fullfile(outdir,sprintf('%s_truth_%02d.csv',r.case,tr)),',');
    brc=dlmread(fullfile(outdir,[r.stem '_brc.csv']),',');
    cellq=dlmread(fullfile(outdir,[r.stem '_cell.csv']),',');
    drop=dlmread(fullfile(outdir,[r.stem '_drop.csv']),',');
    full=dlmread(fullfile(outdir,sprintf('%s_n%d_floatfull_%02d.csv',r.case,r.noise_index,tr)),',');
    diagonal=dlmread(fullfile(outdir,sprintf('%s_n%d_diagonal_%02d.csv',r.case,r.noise_index,tr)),',');
    n=size(brc,1);assert(n==r.horizon_steps+1 && n==spec.steps+1,'Artifact horizon mismatch');
    assert(all(isfinite([brc(:);cellq(:);drop(:)])),'Nonfinite prediction');
    truth=truth(1:n,:);full=full(1:n,:);diagonal=diagonal(1:n,:);
    v=c.variants(r.noise_index+1);T=v.theta_numerators/spec.coefficient_denominator;
    rq=zeros(n,6);rq(1:2,:)=floor(truth(1:2,2:7)*r.delta_denominator+0.5)/r.delta_denominator;
    for k=2:n-1,rq(k+1,:)=(T*[rq(k,:)';rq(k-1,:)'])';end
    eq=max(abs(rq(:)-brc(:,2:7)(:)));equivalence_max=max(equivalence_max,eq);
    cb=max(abs(cellq(:,2:7)(:)-brc(:,2:7)(:)))*r.delta_denominator;
    coarse_bound_ratio=max(coarse_bound_ratio,cb);
    assert(cb<=0.5+1e-9,'Coarse readout exceeded quantizer half-cell bound');
    fm=rq;dm=rq;
    for k=2:n-1,fm(k+1,:)=(v.theta*[fm(k,:)';fm(k-1,:)'])';dm(k+1,:)=(v.diagonal_theta*[dm(k,:)';dm(k-1,:)'])';end
    predictions={brc(:,2:7),cellq(:,2:7),drop(:,2:7),rq,fm,dm,full(:,2:7),diagonal(:,2:7)};
    labels={'BRC_retained','BRC_cell_only_readout','BRC_discard_feedback','same_dof_rational_float','full_AR2_matched_initial','diagonal_AR2_matched_initial','full_AR2_highres_initial','diagonal_AR2_highres_initial'};
    for mi=1:numel(predictions)
      q=predictions{mi};assert(all(isfinite([q(:);truth(:)])),'Nonfinite model or truth');m=metrics(q,truth(:,2:7),K,coupling,h,spec.train_end_time);
      assert(all(isfinite([m.nrmse,m.last_rmse,m.energy_relative_mae,m.phase_rmse_deg,m.phase_unwrapped_final_rms_deg])),'Nonfinite metric');
      if coupling~=0,assert(isfinite(m.exchange_nrmse));end
      rows(end+1,:)={r.case,r.noise_index,r.delta_denominator,tr,r.role,labels{mi},m.nrmse,m.last_rmse,m.energy_relative_mae,m.phase_rmse_deg,m.exchange_nrmse,eq,r.max_fraction_bits,r.runtime_seconds,m.phase_unwrapped_final_rms_deg};
    end
  end
  fid=fopen(fullfile(outdir,'metrics.csv'),'w');
  fprintf(fid,'case,noise_index,delta_denominator,trajectory,role,model,holdout_nrmse,last_quarter_rmse,energy_relative_mae,phase_rmse_deg,exchange_nrmse,exact_vs_float_maxabs,max_fraction_bits,trajectory_pipeline_reference_seconds,phase_unwrapped_final_rms_deg\n');
  for i=1:size(rows,1)
    fprintf(fid,'%s,%d,%d,%d,%s,%s',rows{i,1:6});
    fprintf(fid,',%.17g',rows{i,7:15});fprintf(fid,'\n');
  end
  fclose(fid);
  render_figures(spec,results,rows,outdir);
  score_all_float_holdouts(spec,outdir);
  fid=fopen(fullfile(outdir,'analysis_checks.json'),'w');
  fprintf(fid,'%s\n',jsonencode(struct('status',results.status,'run_id',results.run_id,'record_count',size(rows,1),...
    'coarse_bound_max_fraction_of_cell',coarse_bound_ratio,'exact_vs_same_dof_float_maxabs',equivalence_max,...
    'equivalence_claim','Exact integer recurrence certificate for executed finite trajectories; floating readout is only numerical comparison')));fclose(fid);
  disp(['OCTAVE_ANALYSIS_' results.status]);
end

function m=metrics(q,truth,K,kappa,h,train_end)
  n=size(q,1);ix=max(2,round(train_end/h)+2):n-1;late=max(2,floor(.75*n)):n-1;
  e=q-truth;m.nrmse=sqrt(mean(e(ix,:)(:).^2))/sqrt(mean(truth(ix,:)(:).^2));
  m.last_rmse=sqrt(mean(e(late,:)(:).^2));
  v=zeros(size(q));vt=v;v(2:n-1,:)=(q(3:n,:)-q(1:n-2,:))/(2*h);
  vt(2:n-1,:)=(truth(3:n,:)-truth(1:n-2,:))/(2*h);
  E=.5*sum(v.^2,2)+.5*sum((q*K).*q,2);
  Et=.5*sum(vt.^2,2)+.5*sum((truth*K).*truth,2);
  m.energy_relative_mae=mean(abs(E(ix)-Et(ix)))/mean(Et(ix));
  [V,D]=eig(K);w=sqrt(diag(D))';mq=q*V;mt=truth*V;mv=v*V;mvt=vt*V;
  phase=atan2(-mv./w,mq)-atan2(-mvt./w,mt);phase=mod(phase+pi,2*pi)-pi;
  m.phase_rmse_deg=sqrt(mean(phase(late,:)(:).^2))*180/pi;
  dp=unwrap(atan2(-mv(2:n-1,:)./w,mq(2:n-1,:)),[],1)-unwrap(atan2(-mvt(2:n-1,:)./w,mt(2:n-1,:)),[],1);
  dp=dp-2*pi*round(dp(1,:)/(2*pi));
  m.phase_unwrapped_final_rms_deg=sqrt(mean(dp(end,:).^2))*180/pi;
  if kappa==0,m.exchange_nrmse=NaN;else
    J=zeros(n,6);Jt=J;
    for a=1:6,b=mod(a,6)+1;J(:,a)=kappa/2*(q(:,a)-q(:,b)).*(v(:,a)+v(:,b));Jt(:,a)=kappa/2*(truth(:,a)-truth(:,b)).*(vt(:,a)+vt(:,b));end
    m.exchange_nrmse=sqrt(mean((J(ix,:)-Jt(ix,:))(:).^2))/max(1e-15,sqrt(mean(Jt(ix,:)(:).^2)));
  end
end

function render_figures(spec,results,rows,outdir)
  graphics_toolkit('gnuplot');set(0,'defaultfigurevisible','off');
  f=figure('position',[0 0 1250 850]);
  for ci=1:3
    name=spec.cases(ci).name;stem=sprintf('%s_n0_d256_09',name);
    if ~any(strcmp({results.records.stem},stem)),continue;end
    t=dlmread(fullfile(outdir,sprintf('%s_truth_09.csv',name)),',');
    b=dlmread(fullfile(outdir,[stem '_brc.csv']),',');d=dlmread(fullfile(outdir,[stem '_drop.csv']),',');
    subplot(3,2,2*ci-1);plot(t(:,1),t(:,2),'k-',b(:,1),b(:,2),'b--',d(:,1),d(:,2),'r:');
    grid on;xlabel('External time');ylabel('Position component 1');title(name);
    if ci==1,legend('External ODE truth','BRC retained residual','Discard feedback','location','northeastoutside');end
    subplot(3,2,2*ci);semilogy(b(:,1),max(1e-14,sqrt(mean((b(:,2:7)-t(:,2:7)).^2,2))),'b-',d(:,1),max(1e-14,sqrt(mean((d(:,2:7)-t(:,2:7)).^2,2))),'r-');
    grid on;xlabel('External time');ylabel('Six-position RMS error');title('Free-running error, delta=1/256');
  end
  print(f,fullfile(outdir,'trajectories.png'),'-dpng','-r140');print(f,fullfile(outdir,'trajectories.svg'),'-dsvg');close(f);
  f=figure('position',[0 0 1150 450]);
  subplot(1,2,1);hold on;
  for ci=1:3
    errs=[];
    for den=[64,256,1024]
      keep=strcmp(rows(:,1),spec.cases(ci).name)&cell2mat(rows(:,2))==0&cell2mat(rows(:,3))==den&cell2mat(rows(:,4))<13&strcmp(rows(:,6),'BRC_retained');
      errs(end+1)=mean(cell2mat(rows(keep,7)));
    end
    loglog(1./[64,256,1024],errs,'o-','displayname',spec.cases(ci).name);
  end
  grid on;xlabel('Initial Cell grid delta');ylabel('Held-out normalized RMS error');legend('location','best');title('Initial-grid convergence; not new fitted dynamics');
  subplot(1,2,2);bits=[results.records.max_fraction_bits];secs=[results.records.runtime_seconds];plot(bits,secs,'o');grid on;xlabel('Maximum exact numerator/denominator bits');ylabel('Seconds per full validation pipeline');title('Exact arithmetic and validation resource cost');
  print(f,fullfile(outdir,'resolution_cost.png'),'-dpng','-r140');print(f,fullfile(outdir,'resolution_cost.svg'),'-dsvg');close(f);
end

function score_all_float_holdouts(spec,outdir)
  f=fopen(fullfile(outdir,'float_holdouts.csv'),'w');
  fprintf(f,'case,noise_index,trajectory,model,holdout_nrmse,energy_relative_mae,phase_rmse_deg,exchange_nrmse\n');
  labels={'floatfull','diagonal'};
  for ci=1:3,c=spec.cases(ci);for ni=0:1,for tr=9:12
    truth=dlmread(fullfile(outdir,sprintf('%s_truth_%02d.csv',c.name,tr)),',');
    for mi=1:2
      a=dlmread(fullfile(outdir,sprintf('%s_n%d_%s_%02d.csv',c.name,ni,labels{mi},tr)),',');
      assert(all(isfinite([a(:);truth(:)])),'Nonfinite extra float holdout');
      m=metrics(a(:,2:7),truth(:,2:7),c.K,c.coupling,spec.h,spec.train_end_time);
      fprintf(f,'%s,%d,%d,%s_highres_initial,%.17g,%.17g,%.17g,%.17g\n',c.name,ni,tr,labels{mi},m.nrmse,m.energy_relative_mae,m.phase_rmse_deg,m.exchange_nrmse);
    end
  end;end;end
  fclose(f);
end
