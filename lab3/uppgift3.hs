main :: IO ()
main = do
    let secret = 63
    putStrLn "Guess a number between 1 and 99: "
    guessStr <- getLine
    let guess = read guessStr :: Integer
    if (guess < 1 || guess >99)
        then do
            putStrLn "You must guess a number between 1 and 99!"
            main
    else if (guess < secret)
        then do
            putStrLn("Too low!")
            main
    else if (guess > secret)
        then do
            putStrLn("Too High!")
            main
    else putStrLn("Correct!")
