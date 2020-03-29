-- Alla deluppgifter. <Körs i ghci>
data Matrix a = Empty | Cons a [a] [a] (Matrix a)
    deriving (Eq,Show)

matrixFirstRow :: Matrix a -> [a]
matrixFirstRow Empty = []
matrixFirstRow (Cons x xs xy m) = x:xs

matrixRemoveFirstRow :: Matrix a -> Matrix a
matrixRemoveFirstRow Empty = Empty
matrixRemoveFirstRow (Cons _ _ [] _) = Empty
matrixRemoveFirstRow (Cons _ _ (x:xs) m) = Cons x (matrixFirstRow m) xs (matrixRemoveFirstRow m)

matrixToList :: Matrix a -> [[a]]
matrixToList Empty = []
matrixToList m = [matrixFirstRow m] ++ matrixToList(matrixRemoveFirstRow m)


listToMatrix :: [[a]] -> Matrix a
listToMatrix [] = Empty
listToMatrix r = Cons a fr fc (listToMatrix cleanUp)
        where
            a = head (head r)
            fr = tail (head r)
            fc = map (\x -> head x) (tail r)
            cleanUp = filter (\x -> (length x) /= 0) (map (\x -> tail x) (tail r))

mapMatrix :: (a -> b) -> Matrix a -> Matrix b
mapMatrix _ Empty = Empty
mapMatrix f m = listToMatrix(map (\x -> (map f x)) (matrixToList m))

negMatrix :: Num a => Matrix a -> Matrix a
negMatrix m = mapMatrix (\x -> - x) m

scalarMul :: Num a => a -> Matrix a -> Matrix a
scalarMul a m = mapMatrix (a *) m

scalarDiv :: Integral a => a -> Matrix a -> Matrix a
scalarDiv a m = mapMatrix (\x -> div x a) m

addMatrix :: Num a => Matrix a -> Matrix a -> Matrix a
addMatrix m1 m2 = listToMatrix (map (\r -> zipWith (+) (fst r)(snd r)) (zip (matrixToList m1) (matrixToList m2)))

subMatrix :: Num a => Matrix a -> Matrix a -> Matrix a
subMatrix m n = addMatrix m (negMatrix n)

mulColRow :: Num a => [a] -> [a] -> Matrix a
mulColRow v1 v2 = listToMatrix (map (\e ->  (map (\x -> x*e) v2)) v1)

detRec :: Integral a => a -> Matrix a -> a
detRec d Empty = d
detRec d (Cons a r c m) = detRec a m'
    where m' = scalarDiv d (subMatrix (scalarMul a m) (mulColRow c r))

det :: Integral a => Matrix a -> a
det m = detRec 1 m

--   1 2
--   3 4
m1 :: Matrix Integer
m1 = Cons 1 [2] [3] (Cons 4 [] [] Empty)

--   42 1 -2
--    3 1  2
--   -9 3  4
m2 :: Matrix Integer
m2 = Cons 42 [1,-2] [3,-9] m1

--   2.0  1.0    3.2    4.1
--   3.2  9.9    5.323 56.4123
--   1.4 15.323  0      0
--   1.0  7.4993 0      1
m3 :: Matrix Double
m3 = Cons 2.0 [1.0,3.2,4.1] [3.2,1.4,1.0]
         (Cons 9.9 [5.323,56.4123] [15.323,7.4993]
               (Cons 0 [0] [0] (Cons 1 [] [] Empty)))

--   1 2 3 4
m4 :: Matrix Integer
m4 = Cons 1 [2,3,4] [] Empty

--   1
--   2
--   3
--   4
m5 :: Matrix Integer
m5 = Cons 1 [] [2,3,4] Empty

--   1 2
--   3 4
--   5 6
m6 :: Matrix Integer
m6 = Cons 1 [2] [3,5] (Cons 4 [] [6] Empty)
