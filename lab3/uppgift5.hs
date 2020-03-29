--Alla deluppgifter lösta
data IntExpr = Const Int
             | Var String
             | Add IntExpr IntExpr
             | Mul IntExpr IntExpr
    deriving (Eq,Show)

data Instr = Assign String IntExpr
           | If BoolExpr [Instr] [Instr]
           | While BoolExpr [Instr]
    deriving (Eq,Show)

data BoolExpr = IntEq IntExpr IntExpr
              | BoolNot BoolExpr
    deriving (Eq,Show)

findVar :: String -> [(String,Int)] -> Int
findVar s e
    | s == fst (head e) = snd (head e)
    | otherwise = findVar s (tail e)

evalIntExpr :: IntExpr -> [(String,Int)] -> Int
evalIntExpr (Const i) _ = i
evalIntExpr (Var s) e = findVar s e
evalIntExpr (Add e1 e2) e = (evalIntExpr e1 e) + (evalIntExpr e2 e)
evalIntExpr (Mul e1 e2) e = (evalIntExpr e1 e) * (evalIntExpr e2 e)

isVarInEnv :: String -> [(String,Int)] -> Bool
isVarInEnv s e
    | e == [] = False
    | s == fst (head e) = True
    | otherwise = isVarInEnv s (tail e)

addToEnv :: (String,Int) -> [(String,Int)] -> [(String,Int)]
addToEnv x e
    | not (isVarInEnv (fst x) e) = e ++ [x]
    | otherwise = map (\y -> if (fst y) /= (fst x) then y else x) e

eval :: [Instr] -> [(String,Int)] -> [(String,Int)]
eval [] e = e
eval (Assign s i:xs) e = eval xs (addToEnv (s, evalIntExpr i e) e)
eval (If b p1 p2:xs) e
    | evalBoolExpr b e = eval xs (eval p1 e)
    | otherwise = eval xs (eval p2 e)
eval (While b p:px) e
    | evalBoolExpr b e = eval (While b p:px) (eval (p ++ px) e)
    | otherwise = e

run :: [Instr] -> [(String,Int)]
run xs = eval xs []

evalBoolExpr :: BoolExpr -> [(String,Int)] -> Bool
evalBoolExpr (IntEq e1 e2) e = (evalIntExpr e1 e) == (evalIntExpr e2 e)
evalBoolExpr (BoolNot b) e = not (evalBoolExpr b e)


prog1 :: [Instr]
prog1 = [ Assign "x" (Const 1)
        , Assign "y" (Add (Var "x") (Var "x"))
        , Assign "y" (Mul (Var "y") (Add (Var "x") (Const 1)))
        , Assign "z" (Add (Var "x") (Mul (Var "y") (Const 4)))
        ]
-- x := 0
-- if (x == 0)
--    y := 1
-- else
--    y := 2
-- if (y != 2)
--    z := 2
-- else
--    z := 1
prog2 :: [Instr]
prog2 = [ Assign "x" (Const 0)
        , If (IntEq (Var "x") (Const 0))
             [ Assign "y" (Const 1) ]
             [ Assign "y" (Const 2) ]
        , If (BoolNot (IntEq (Var "y") (Const 2)))
             [ Assign "z" (Const 2) ]
             [ Assign "z" (Const 1) ]
        ]

-- x := 0
-- y := 1
-- if (x != y)
--    x := y
--    if (x == y)
--       z := 0
--    else
--       z := 1
--    y := 5
-- else
--   z := 2
-- w := z
prog3 :: [Instr]
prog3 = [ Assign "x" (Const 0)
        , Assign "y" (Const 1)
        , If (BoolNot (IntEq (Var "x") (Var "y")))
             [ Assign "x" (Var "y")
             , If (IntEq (Var "x") (Var "y"))
                  [ Assign "z" (Const 0) ]
                  [ Assign "z" (Const 1) ]
             , Assign "y" (Const 5) ]
             [ Assign "z" (Const 2) ]
        , Assign "w" (Var "z")
        ]

-- x := 5
-- y := 1
-- while (x != 0)
--   y := y * x
--   x := x - 1
progfac :: [Instr]
progfac = [ Assign "x" (Const 5)
          , Assign "y" (Const 1)
          , While (BoolNot (IntEq (Var "x") (Const 0)))
                  [ Assign "y" (Mul (Var "y") (Var "x"))
                  , Assign "x" (Add (Var "x") (Const (-1)))
                  ]
          ]
