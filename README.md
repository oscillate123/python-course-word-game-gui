# Ordspelet

För att starta spelet, krävs att du har python3 och pip installerat, samt uppdaterat. Programmets funktionella beroenden
finns listade i requirements.txt

För att installera de funktionella beroendena som finns i requirements.txt, krävs det att du:

1. Öppnar en terminal
2. Navigerar till mappen som requirements.txt filen ligger i.
3. Skriver följande i terminal fönstret.
`pip install -r requirements.txt`
4. Kontrollera att appJar och dess funktionella beroenden har installerats, genom att skriva `pip list`. 
I listan ska appJar finnas.


När ovanstående steg har genomförts, så kör filen `__main__.py`.
Du kör filen antingen i en IDE eller genom en terminal på följande sätt.
1. Navigera till mappen där `__main__.py` ligger.
2. Skriv `python3 __main__.py`

Regler för spelet:
1. Spelet kan endast köra en av spellägena åt gången, dvs inte samtidigt.
2. Om du vill byta spelläge, klicka på "Återställ"-knappen först, innan du startar.
3. I Skynet vs. User, så ska användaren gissa vilket ord som Skynet tänker på.
4. I User vs. Skynet, så ska Skynet gissa vilket ord som User tänker på.
5. I User vs. Skynet så svarar med du på Skynets gissning med formatet: `11` eller `02`.

Dvs att om Skynet gissar Polis och ordet User tänker på är Pirat. Då är det `1` bokstav som är på rätt plats,
 och `1` bokstav som är rätt men på fel plats. P är på rätt plats och I finns i ordet Pirat, men I:et är inte 
 på samma plats i orden Polis och Pirat. Då säger User till Skynet, `11` för att en siffra är för antal rätta platser
 och en siffra är för antal rätta bokstäver som inte är på rätt plats.