% tic
% n=100000;
% x=1:n;
% 
% M=zeros(length(x),length(x));
% M(1,:)=x;
% for i=1:n-1
% M(i+1,:)=circshift(x,i);
% end
% toc
% 
% P=zeros(size(M));
% Id=eye(size(M));
% RowNeg=-ones(length(x));