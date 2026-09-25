# Klasyfikacja typów zdjęć profilowych z wykorzystaniem CNN

Projekt z zakresu widzenia komputerowego porównujący architektury **ResNet18** oraz **MobileNetV2** w wieloklasowej klasyfikacji typów zdjęć profilowych.

## Cel

Analiza wpływu:

- danych rzeczywistych i syntetycznych,
- czterech wariantów augmentacji,
- dwóch architektur CNN

na jakość klasyfikacji pięciu klas: `selfie`, `mirror`, `outdoor`, `group`, `full_body`.

## Dane

Cały zbiór: **220 obrazów**:

- 120 syntetycznych,
- 100 rzeczywistych.

Stały zbiór testowy: **20 obrazów rzeczywistych**, po 4 na klasę.

Pula treningowa: **200 obrazów**:

- 120 syntetycznych,
- 80 rzeczywistych.

Pełny dataset nie jest publikowany w repozytorium ze względu na różne zasady redystrybucji źródeł obrazów.

## Eksperymenty

- E1 - wszystkie dane treningowe
- E2 - tylko syntetyczne
- E3 - tylko rzeczywiste
- E4 - tylko liczniejszy typ danych, przycięty do liczności typu mniej licznego

Augmentacje:

- A0 - brak augmentacji
- A1 - geometryczna
- A2 - fotometryczna
- A3 - mieszana

Łącznie: **32 eksperymenty**.

## Wyniki

Najwyższe accuracy: **0,95**.

Najlepsze rezultaty uzyskiwał MobileNetV2, szczególnie w scenariuszach wykorzystujących dane rzeczywiste lub dane mieszane.

Szczegóły znajdują się w `results/results_summary.csv`, `results/results_summary.xlsx` oraz w raporcie PDF.
