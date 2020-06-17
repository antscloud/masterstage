function [Rtot] = Resistinter2(nmbre,mapnumspot,dS,resline,rescol,gamma1,k,L,courant)

%histosurf=zeros(nmbre,1);
%---------- Nettoyage des spots monopixels --------------------%



numb=0;
for l=1:nmbre
    
               spotiso=sum(mapnumspot(:)==l);
                
                 
    if  spotiso>1
             numb=numb+1;
             nonmono(numb)=l;
             surfspot(numb(end))=spotiso*dS;
             %histosurf(l)=spotiso*dS;
 
    else
     %histosurf(l)=0;            %historique de la taille de chaque spot (permet une étude stat sur la distribution des tailles)
    end
end 


if numb~=0
            longz=zeros(1,length(nonmono));
            Rspot=zeros(numb,1);

   %%%% fin nettoyage monopixels
   
   %%% boucle pour chaque étape de temps sur tous les spots de taille > 1 px
       
    for nu=1:numb
        
clear Rspot
clear row col spotlist



        spotiso=(mapnumspot==nonmono(nu));     %%%%%%%%%%% Considération d'un spot individuel  
        [row,col]=find(spotiso==1);       %%%%%% extraction des coordonnées de tous les pixels constituant le spot considéré.
        clear spotiso
        
        spotlist=zeros(length(row),2);   
        spotlist(1:length(row),1)=row;
        spotlist(1:length(col),2)=col;              % on met les coordonnées des spot dans une variable
            
        
    clear longz longz2
     for testk=1:size(spotlist,1)
        
        longz2=abs((((repmat(spotlist(testk,:),[size(spotlist,1) 1])-spotlist(:,:)))));
        longz2(testk,:)=[];
        longz2(:,1)=longz2(:,1)*resline;
        longz2(:,2)=longz2(:,2)*rescol;
        longz2=longz2.^2;
        longz(testk)=sum(repmat(dS,[length(longz2) 1])./sqrt(sum(longz2,2)));
     end
        long(nu)=sum(longz.*dS)./((surfspot(nu)')*4*pi);                    

  if nu==numb
           surfacetemps=sum(surfspot);
  end
    
  
    end
  
    %%%%%%%%%%%% Sortie de la boucle sur tous les spots

 
    gamma=repmat(gamma1,[1,nu]);                        %vectorisation de gamma pour faciliter les calculs
    nmbre=nu;
    surfaces{1,1}=surfspot;
    surfacestot=sum(surfspot);
    
    
    Ic=k*(surfspot(:)')./(long*sqrt(L));

    Tspots=300./(1-(courant^2)./(Ic.^2));

     Rspot=long./(gamma.*surfspot(:)');                 %%%%%%%%%%%% Resistances individuelles de chaque spot, selon le modèle de Robert
     Rtot=1./sum(1./Rspot);                             %%%%%% Resistance totale à temps fixé selon le modèle de Robert


    

    if numb==0
        surfspot=0;
    end
elseif numb==0
    Rtot=inf;
end


%%%%%%%%%%%%%%%%%%%%%%%%%%% Fin calcul résistance%%%%%%%%%%%%%%%%%%%%%


end
