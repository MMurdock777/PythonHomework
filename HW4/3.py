def frame(line: str, symbol: str):
    print(symbol * (len(line) + 2))
    print(f"{symbol}{line}{symbol}")
    print(symbol * (len(line) + 2))


frame("Default line", '*')
