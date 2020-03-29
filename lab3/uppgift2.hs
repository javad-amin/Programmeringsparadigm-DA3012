mulString :: Integer -> String -> String
mulString _ "" = ""
mulString i s
    |i<= 0    = ""
    |otherwise = s ++ mulString (i-1) s
