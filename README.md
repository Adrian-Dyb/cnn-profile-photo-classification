# CNN Classification of Profile Photo Types

Projekt z zakresu computer vision dotyczący wieloklasowej
klasyfikacji typów zdjęć profilowych z wykorzystaniem danych
rzeczywistych i syntetycznych.

## Classes

- Selfie
- Mirror selfie
- Outdoor
- Group photo
- Full body

## Dataset

Łącznie: 220 obrazów

- 120 syntetycznych
- 100 rzeczywistych

Podział:

- trening: 200 obrazów
  - 120 syntetycznych
  - 80 rzeczywistych
- test: 20 rzeczywistych
  - 4 obrazy na każdą klasę

Stały zbiór testowy nie był wykorzystywany podczas treningu.

## Models

- ResNet18
- MobileNetV2

## Experiments

E1 — wszystkie dane treningowe  
E2 — tylko dane syntetyczne  
E3 — tylko dane rzeczywiste  
E4 — dane liczniejszego typu przycięte do liczności typu mniej licznego

## Data augmentation

A0 — brak augmentacji  
A1 — RandomHorizontalFlip + RandomRotation ±15°  
A2 — ColorJitter  
A3 — augmentacja geometryczna + fotometryczna

Łącznie przeprowadzono:

2 architektury × 4 scenariusze danych × 4 augmentacje = 32 eksperymenty.

## Best result

Najwyższe accuracy: 0.95.

Najlepsze wyniki uzyskano przy użyciu MobileNetV2,
szczególnie dla scenariuszy wykorzystujących dane rzeczywiste
lub mieszane.

## Technologies

- Python
- PyTorch
- torchvision
- scikit-learn
- pandas
- matplotlib
- Google Colab# cnn-profile-photo-classification
