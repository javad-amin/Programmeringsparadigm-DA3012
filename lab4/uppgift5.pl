skyffla(X,Y) :- lets_skyffla(X,Y), !.

lets_skyffla([],[]) :- !.
lets_skyffla(X,R) :-
    append(O,Y,R),
    get_odds(X,O),
    get_evens(X,E),
    lets_skyffla(E,Y).

get_odds([],[]).
get_odds([Z],[Z]).
get_odds([H, _|T],[H|Y]) :-
    get_odds(T,Y).

get_evens([],[]).
get_evens(Z,[]) :- length(Z,L), L=:=1.
get_evens([_, H|T],[H|Y]) :-
    get_evens(T,Y).
