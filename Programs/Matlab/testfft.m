

% t = 0:0.01:1000;   
% h=t(2)-t(1);
% x = cos(2*pi*50*t);
% x = x + 2*randn(size(t));

fp=@(t,x)[cos(2*pi*50*t)];
[t,x]=ode45(fp,0:0.001:11,0) ;

h=t(2)-t(1);
plot(t,x)
y = fft(x);     
f = (0:length(t)-1)*(1/h)/length(t);

% n = length(x);                         
% fshift = (-n/2:n/2-1)*((1/h)/n);
% yshift = fftshift(y);
% plot(fshift,abs(yshift))

plot(f,abs(y))
title('Magnitude')

t=1:0.1:100
y=0.33*abs(cos(130*t)+cos(70*t).^2++cos(33*t).^3)
plot(t,y)