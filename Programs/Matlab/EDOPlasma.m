% mu=1
% fp=@(t,x)[mu*x];
% 
% [t,x]=ode45(fp,[0 2],1) 
% r=0:0.1:2
% s=exp(r)
% plot(t,x,r,s,'--')
% xlabel("Temps t")
% ylabel("Fonction x")

% for mu=[0.1,1,2,3,4]
%     
% t=0:0.01:20;
% h=0.01;
% p=length(t);
% f=@(t,b)[mu*b*(1-b)];
% 
% b(1)= 2;
% 
% for k=1:p-1 
%     b(k+1)=b(k)+h*[(1/4)*f(t(k),b(k)) + (3/4)*f(t(k)+(2/3)*h,b(k)+(2/3)*h*f(t(k)+(h/3),b(k)+(h/3)*f(t(k),b(k))))] ;
% end
% 
% plot(t,b,'--','DisplayName',"HEUN mu = "+num2str(mu))
% 
% xlabel("Temps t")
% ylabel("Fonction x")
% legend()
% hold on
% end

hold off

clear all
for mu=0.1
%ODE45 %%%%%%%%%%%%%%%%

fp=@(t,x)[1*x*(1-x)];
[t,x]=ode45(fp,0:0.002:50,0.1) ;

%Méthode de Heun %%%%%%%%%%%%%%%%%%%
% h=1;
% t=0:h:200;
% 
% p=length(t);
% f=@(t,x)[mu*x*(1-x)];
% 
% x(1)= 0.999;
% 
% for k=1:p-1 
%     x(k+1)=x(k)+h*[(1/4)*f(t(k),x(k)) + (3/4)*f(t(k)+(2/3)*h,x(k)+(2/3)*h*f(t(k)+(h/3),x(k)+(h/3)*f(t(k),x(k))))] ;
% end

%
%Boucle qui va trouver le premier maximum de la fonction 
% i=1
% F=1
% while F>0
%     F=x(i+1)-x(i)
%     i=i+1
% end
%On retire toutes les valeurs avant ce premier maximum

%x2=x(i:length(x))
%t2=t(i:length(t))

plot(t,x,'-','DisplayName',"mu = "+num2str(mu));

xlabel("Temps t");
ylabel("Fonction x");
legend();
hold on;
end

fr=abs(fft(x));
