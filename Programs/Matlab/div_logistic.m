clear all
y(1)=0.1;
k=3.57;
N=100;
for i=1:N
y(i+1)=k.*y(i).*(1-y(i))
end
plot(y)

%x(1) = r.*x(1).*(1 - (1/1000)*k*x(1))