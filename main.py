import numpy as np
import pyedflib
import os


def get_sch_files(directory='datasets/siamese/sch'):
    eea_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.eea')]
    return eea_files


def get_norm_files(directory='datasets/siamese/norm'):
    eea_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.eea')]
    return eea_files


def read_eea(file_name, samples=7680, channels=16):
    data = []

    eea = open(file_name, 'r')

    lines = eea.readlines()

    for c in range(channels):
        channel = []
        for s in range(samples):
            channel += [float(lines[c + s][:-2])]
        data += [channel]

    eea.close()

    data = np.array(data)

    return np.transpose(data)

def get_sch_instances(directory='datasets/siamese/sch'):
    scz_files = get_sch_files(directory)
    instances = [read_eea(os.path.join(directory, scz_file)) for scz_file in scz_files]
    return instances


def get_norm_instances(directory='datasets/siamese/norm'):
    hc_files = get_norm_files(directory)
    instances = [read_eea(os.path.join(directory, hc_file)) for hc_file in hc_files]
    return instances


def get_edf_files(directory='datasets/edf'):
    edf_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.edf')]
    return edf_files


def read_edf(file_name):
    with pyedflib.EdfReader(file_name) as edf:
        n = edf.signals_in_file
        signal_labels = edf.getSignalLabels()
        sigbufs = np.zeros((n, edf.getNSamples()[0]))
        for i in range(n):
            sigbufs[i, :] = edf.readSignal(i)
    return sigbufs, signal_labels


def get_edf_instances(directory='datasets/edf'):
    edf_files = get_edf_files(directory)
    instances = []
    labels = None
    for edf_file in edf_files:
        data, signal_labels = read_edf(os.path.join(directory, edf_file))
        instances.append(data)
        if labels is None:
            labels = signal_labels
    return instances, labels


def print_dataset_comparison(sch_instances, norm_instances, edf_instances, signal_labels_edf):
    print('-------')
    print('Porównanie datasetów')
    print('http://brain.bio.msu.ru/eeg_schizophrenia.htm')
    print('Opis ze strony: Each file contains an EEG record for one subject. Each TXT file contains a column with EEG '
          'samples from 16 EEG channels (electrode positions). Each number in the column is an EEG amplitude (mkV) at '
          'distinct sample. First 7680 samples represent 1st channel, then 7680 - 2nd channel, ets. The sampling rate '
          'is 128 Hz, thus 7680 samples refer to 1 minute of EEG record.')
    print('Data set numer 3 - siamese:')
    print(f'Liczba instancji schizofrenii: {len(sch_instances)}')
    print(f'Liczba instancji normy: {len(norm_instances)}')
    print(f'Całkowita liczba instancji siamese: {len(sch_instances) + len(norm_instances)}')
    if sch_instances:
        print(f'Liczba kanałów na instancję siamese: {sch_instances[0].shape[1]}')
        print(f'Liczba próbek na kanał siamese: {sch_instances[0].shape[0]}')

    print('-------')
    print('https://repod.icm.edu.pl/dataset.xhtml?persistentId=doi:10.18150/repod.0107441')
    print('Opis ze strony: The dataset comprised 14 patients with paranoid schizophrenia and 14 healthy controls. '
          'Data were acquired with the sampling frequency of 250 Hz using the standard 10-20 EEG montage with 19 EEG '
          'channels: Fp1, Fp2, F7, F3, Fz, F4, F8, T3, C3, Cz, C4, T4, T5, P3, Pz, P4, T6, O1, O2. The reference '
          'electrode was placed between electrodes Fz and Cz')
    print('Data set numer 2 - edf:')
    print(f'Wczytano {len(edf_instances)} instancji plików EDF.')
    if signal_labels_edf is not None:
        print(f'Nazwy kanałów EDF: {signal_labels_edf}')
    if edf_instances:
        print(f'Liczba kanałów na instancję EDF: {len(edf_instances[0])}')
        print(f'Liczba próbek na kanał EDF: {len(edf_instances[0][0])}')


def main():
    # Data set numer 3 - siamese
    sch_instances = get_sch_instances()
    norm_instances = get_norm_instances()

    # Data set numer 2 - edf
    edf_instances, signal_labels_edf = get_edf_instances()

    print_dataset_comparison(sch_instances, norm_instances, edf_instances, signal_labels_edf)


if __name__ == "__main__":
    main()
