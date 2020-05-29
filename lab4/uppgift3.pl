remove_odd([],[]).
remove_odd([H|T],[H|Y]) :-
    mod(H, 2) =:= 0,
    remove_odd(T, Y).
remove_odd([H|T], Y) :-
    mod(H, 2) =\= 0,
    remove_odd(T, Y).
