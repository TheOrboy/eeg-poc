
# EEG PoC

## Dataset "numer 3":

- http://brain.bio.msu.ru/eeg_schizophrenia.htm
- Nazwy kanałów: [F7, F3, F4, F8, T3, C3, Cz, C4, T4, T5, P3, Pz, P4, T6, O1, O2]
- Ilosć instancji schizofrenii: 45
- Ilość instancji normy: 39
- Ilosć kanałów: 16
- Ilość próbek: 7680
- Ilość pacjentów: 84

- Opis ze strony: Each file contains an EEG record for one subject. Each TXT file contains a column with EEG samples from 16 EEG channels (electrode positions). Each number in the column is an EEG amplitude (mkV) at distinct sample. First 7680 samples represent 1st channel, then 7680 - 2nd channel, ets. The sampling rate is 128 Hz, thus  7680 samples refer to 1 minute of EEG record.

## Dataset "numer 2":

- https://repod.icm.edu.pl/dataset.xhtml?persistentId=doi:10.18150/repod.0107441
- Nazwy kanałów EDF: ['Fp2', 'F8', 'T4', 'T6', 'O2', 'Fp1', 'F7', 'T3', 'T5', 'O1', 'F4', 'C4', 'P4', 'F3', 'C3', 'P3', 'Fz', 'Cz', 'Pz']
- Ilość kanałów: 19
- Ilość próbek: 231250
- Ilość pacjentów: 19
- Opis ze strony: The dataset comprised 14 patients with paranoid schizophrenia and 14 healthy controls. Data were acquired with the sampling frequency of 250 Hz using the standard 10-20 EEG montage with 19 EEG channels: Fp1, Fp2, F7, F3, Fz, F4, F8, T3, C3, Cz, C4, T4, T5, P3, Pz, P4, T6, O1, O2. The reference electrode was placed between electrodes Fz and Cz.

## Dataset "numer 1":

- https://www.kaggle.com/broach/buttontonesz2
- Nazwy kanałów EDF: ['Fp1', 'AF7', 'AF3', 'F1', 'F3', 'F5', 'F7', 'FT7', 'FC5', 'FC3', 'FC1', 'C1', 'C3', 'C5', 'T7', 'TP7', 'CP5', 'CP3', 'CP1', 'P1', 'P3', 'P5', 'P7', 'P9', 'PO7', 'PO3', 'O1', 'Iz', 'Oz', 'POz', 'Pz', 'CPz', 'Fpz', 'Fp2', 'AF8', 'AF4', 'AFz', 'Fz', 'F2', 'F4', 'F6', 'F8', 'FT8', 'FC6', 'FC4', 'FC2', 'FCz', 'Cz', 'C2', 'C4', 'C6', 'T8', 'TP8', 'CP6', 'CP4', 'CP2', 'P2', 'P4', 'P6', 'P8', 'P10', 'PO8', 'PO4', 'O2', 'VEOa', 'VEOb', 'HEOL', 'HEOR', 'Nose', 'TP10']
- Ilość kanałów: 64 (TYLKO dla podmiotu 21, reszta ma mniej)
- Ilość pacjentów: 36

Gotowy kod ad data set numer 1 -> https://www.kaggle.com/code/owaiskhan9654/training-of-eeg-schizophrenia-disorder-using-cnn


## Inne:
- https://github.com/meagmohit/EEG-Datasets
