% Alla deluppgifter lösta
check(_,X,int) :- integer(X), !.
check(G,X+Y,int) :- check(G,X,int), check(G,Y,int).
check(G,X*Y,int) :- check(G,X,int), check(G,Y,int).

check(G,(M,N),(A,B)) :- check(G,M,A), check(G,N,B).
check(G,fst(M),A) :- check(G,M,(A,_)).
check(G,snd(N),B) :- check(G,N,(_,B)).

check(G,lambda(X,M),A->B) :- check([X::A|G],M,B).
check(G,app(M,N),B) :- check(G,M,A->B), check(G,N,A).

check([X::B|_],X,A) :- unify_with_occurs_check(B, A).
check([_::_|XS],X,A) :- check(XS,X,A).


:- op(100, xfy, ->).
:- op(1000, xfx, ::).

::(X,Y) :- check([],X,Y).


% tm ::= number  | tm + tm | tm * tm        <- tal
%      | (tm,tm) | fst(tm) | snd(tm)        <- par
%      | lambda(X,tm) | app(tm,tm)          <- funktioner
%
% ty ::= int | (ty,ty) | ty -> ty

% check(X,int) :- integer(X), !.
% check(X+Y,int) :- check(X,int), check(Y,int).
% check(X*Y,int) :- check(X,int), check(Y,int).
%
% check((M,N),(A,B)) :- check(M,A), check(N,B).
% check(fst(M),A) :- check(M,(A,_)).
% check(snd(N),B) :- check(N,(_,B)).
