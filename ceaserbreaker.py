message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345
      67890 !?.'
for key in range(len(SYMBOLS)):
     translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
             translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
     print('Key #%s: %s' % (key, translated))