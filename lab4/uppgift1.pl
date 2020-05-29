% Alla deluppgifter lösta
convert_int(A,B) :- convert_int_helper(A,B), !.

convert_int_helper(z,0).
convert_int_helper(s(Z), N) :-
    convert_int_helper(Z, Y),
    N is Y + 1.

plus(z, Y, Y).
plus(X, z, X).
plus(s(X),s(Y), s(s(Z))) :-
    plus(X, Y, Z).

times(z, _, z) :- !.
times(_, z, z) :- !.
times(X,Y,Z) :-
    times_helper(X, X, Y, z, Z), !.

% Input CopyOfX, X, Y, intial-res, end-res
times_helper(_, z, s(z), I, I).
times_helper(CX, z, s(Y), I, Z) :-
    times_helper(CX, CX, Y, I, Z).
times_helper(CX, s(X), Y, I, Z) :-
    plus(I, s(z), R),
    times_helper(CX, X, Y, R, Z).

% times using convert_int
% times2(X,Y,Z) :-
%     convert_int(X, XN),
%     convert_int(Y, YN),
%     ZN is XN * YN,
%     convert_int(Z, ZN).
