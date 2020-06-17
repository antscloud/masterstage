y(1)=0.1;
k=3.5;

for i=1:100
y(i+1)=k*y(i)*(1-y(i));
end
t=1:101;
plot(t,y)
