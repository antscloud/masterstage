t=0:0.001:10;
Fmu=3*t;
x0=0.5
C=1-1/x0
x=(exp(Fmu))./(-C+exp(Fmu));

plot(t,x)