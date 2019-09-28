def get_game_description(boolean):
    if boolean:
        description = """
        \n----------------------\n
        Spelet går ut på att spelare A tänker på ett ord och spelare B ska
        försöka räkna ut vilket ord A tänker på genom att gissa på ord och
        därigenom få ledtrådar. Dessa ledtrådar består av hur många
        bokstäver som är rätt och på rätt plats samt hur många bokstäver
        som är rätt men är på fel plats. Notera att bara antalet korrekta
        bokstäver ska anges till spelare B, inte vilka bokstäver som avses.
        Ordet som spelare A tänker på måste vara ett svenskt ord med 5
        bokstäver utan upprepade bokstäver och som inte är ett egennamn.
        Ordet får inte vara en tempus- eller pluralböjning. Ord som spelare
        B gissar på behöver inte följa dessa krav. Spelare B kan alltså gissa
        på ABCAB om hen så vill. Stora och små bokstäver ska behandlas på
        samma sätt, spelet ska alltså inte vara case-sensitive.
        \n----------------------\n
        """
        print(description)
        return
    else:
        return
