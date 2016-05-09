# Część 2#

Folder zawiera grę "Polscy Logicy" , w której gracz musi wykazać się znajomością logiki trójwartościowej i umiejętnością rozwiązynia zagadek logicznych.
Gracz ma na początku 1 000 000 zł i w każdej rundzie musi obstawić aktualnie posiadaną kwotę na jedną z trzech odpowiedzi. Pieniądze postawione na odpowiedzi
nieprawidłowe trafiają do niszczarki, a aktualna kwota gracza wynosi tyle co kwota postawiona na odpowiednią odpowiedź.
Gra kończy się kiedy stan konta wyniesie 0zł lub kiedy gracz odpowie na wszystkie z 5 pytań. Kwota pozostała na koncie po 5 pytaniach jest wygraną w grze.

### Uruchomienie gry ###

python main.py --add (ścieżka do pliku and.txt) --or (ścieżka do pliku or.txt) --impl (ścieżka do pliku or.txt) --not (ścieżka do pliku or.txt)

Nazwy plików muszą odpowiadać wybranej opcji i są określone w pliku globalVar.py. Nie można podawać dwa razy tej samej opcji, w przeciwnym razie program nie będzie funkcjonował poprawnie.

### Dodawanie pytania do bazy ###

Aby dodać pytanie do bazy pytań należy w pliku gameEngine.py dodać kolejny element do list. Każdy z element listy to lista składająca się kolejno z [pytanie,odp1,odp2,odp3,poprawnaOdp].
Należy przestrzegać zapisu przedstawionego w pliku, w przeciwnym razie program nie będzie funkcjonował poprawnie.

### Zmiana parametrów gry ###

Możliwa jest zmiana maksymalnej wygranej i liczby pytań. Należy tego dokonać w pliku gameEngine.py przy odpowiednich zmiennich w warunkach początkowych.

### Rekordy gry ###

Gra zapamiętuje najlepsze wyniki wraz z nickami graczy w pliku highestScore.txt. Pliku tego nie wolno edytować. Musi on znajdować się w tym samym folderze co gameEngine.py.

Wykonał: Mateusz Danieluk