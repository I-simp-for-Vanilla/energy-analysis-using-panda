import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv').set_index('Année')
FR_used_energies = ['FR_gaz', 'FR_charbon_fioul', 'FR_nucléaire', 'FR_eolien', 'FR_solaire', 'FR_hydro', 'FR_biomasse_déchets']
US_used_energies = ['US_gaz', 'US_charbon_fioul', 'US_nucléaire', 'US_eolien', 'US_solaire', 'US_hydro', 'US_biomasse_déchets', 'US_petrole']
Emission = ['FR_CO2_Mt', 'US_CO2_Mt']
Emission_Charbon_US = ['US_charbon_fioul', 'US_CO2_Mt']
Emission_Gaz_US = ['US_gaz', 'US_CO2_Mt']
Emission_Petrole_US = ['US_petrole', 'US_CO2_Mt']

if __name__ == "__main__":
    print("\n\n\n\n")
    print(df)

    # vérification des valeurs pour les mix énergétiques
    print("\n========== Vérification des valeurs pour les mix énergétiques ==========\n")
    print(df[FR_used_energies].sum(axis=1))
    print("Min pourcentage : {}".format(df[FR_used_energies].sum(axis=1).min()))
    print("Max pourcentage : {}".format(df[FR_used_energies].sum(axis=1).max()))

    print("\n========== Vérification des valeurs pour les mix énergétiques ==========\n")
    print(df[US_used_energies].sum(axis=1))
    print("Min pourcentage : {}".format(df[US_used_energies].sum(axis=1).min()))
    print("Max pourcentage : {}".format(df[US_used_energies].sum(axis=1).max()))

    #affichage de l'évolution du mix énergétique en France par des courbes
    df[FR_used_energies].plot(kind='line', title='Évolution du mix énergétique en France', xlabel='Année', ylabel='Pourcentage (%)')
    plt.show()

    #affichage de l'évolution du mix énergétique aux États Unis par des courbes
    df[US_used_energies].plot(kind='line', title='Évolution du mix énergétique aux États Unis', xlabel='Année', ylabel='Pourcentage (%)')
    plt.show()

    #affichage de l'évolution du mix énergétique en France par des barres
    df[FR_used_energies].plot.barh(stacked = True, title='Évolution du mix énergétique en France', xlabel='Année', ylabel='Pourcentage (%)')
    plt.show()

    #affichage de l'évolution du mix énergétique aux États Unis par des barres
    df[US_used_energies].plot.barh(stacked = True, title='Évolution du mix énergétique aux États Unis', xlabel='Année', ylabel='Pourcentage (%)')
    plt.show()

    #affichage de l'évolution de l'empreinte carbone de la france en Millions de tonnes de CO2 équivalent
    df['FR_CO2_Mt'].plot(kind='line', title='Évolution de l\'empreinte carbone de la France', xlabel='Année', ylabel='Émissions de CO2 (Mt)')
    plt.show()

    #affichage de l'évolution de l'empreinte carbone des États Unis en Millions de tonnes de CO2 équivalent
    df['US_CO2_Mt'].plot(kind='line', title='Évolution de l\'empreinte carbone des États Unis', xlabel='Année', ylabel='Émissions de CO2 (Mt)')
    plt.show()

    #comparaison de l'empreinte carbone de la France et des États Unis
    df[Emission].plot(kind='line', title='Comparaison de l\'empreinte carbone de la France et des États Unis', xlabel='Année', ylabel='Émissions de CO2 (Mt)')
    plt.show()

    #affichage de l'évolution de l'empreinte carbone et de la place du charbon dans le mix énergétique des États Unis
    df[Emission_Charbon_US].plot(kind='line', title='Évolution de l\'empreinte carbone et du charbon dans le mix énergétique des États Unis', xlabel='Année', ylabel='Émissions de CO2 (Mt)')
    plt.show()

    #affichage de l'évolution de l'empreinte carbone et de la place du pétrole dans le mix énergétique des États Unis
    df[Emission_Petrole_US].plot(kind='line', title='Évolution de l\'empreinte carbone et du pétrole dans le mix énergétique des États Unis', xlabel='Année', ylabel='Émissions de CO2 (Mt)')
    plt.show()

    #affichage de l'évolution de l'empreinte carbone et de la place du gaz dans le mix énergétique des États Unis
    df[Emission_Gaz_US].plot(kind='line', title='Évolution de l\'empreinte carbone et du gaz dans le mix énergétique des États Unis', xlabel='Année', ylabel='Émissions de CO2 (Mt)')
    plt.show()

    #affichage de l'évolution de l'anomalie thermique dans le monde
    print("\n========== Affichage de l'évolution de la température moyenne en France ==========\n")
    print(df.filter(items=['Temp_anomalie_°C']))
    print(df['Temp_anomalie_°C'].describe())
    df['Temp_anomalie_°C'].plot(kind='line', title='Évolution de l\'anomalie thermique dans le monde', xlabel='Année', ylabel='Température (°C)')
    plt.show()

    #affichage du mix énergétique moyen de la france et des US sur la période 1990-2020
    print("\n========== Affichage du mix énergétique moyen de la France et des US sur la période 1990-2020 ==========\n")
    print(df[FR_used_energies].mean())
    #df[FR_used_energies].mean().plot.pie(title='Mix énergétique moyen de la France (1990-2020)')
    plt.show()

    print("\n")

    # affichage de la correlation entre l'utilisation de certaines sources d'énergie et les émissions de CO2 d'un pays
    print("Correlation entre petrole et CO2 aux États Unis : {}".format(df['US_petrole'].corr(df['US_CO2_Mt'])))
    print("Correlation entre charbon et CO2 aux États Unis : {}".format(df['US_charbon_fioul'].corr(df['US_CO2_Mt'])))
    print("Correlation entre gaz et CO2 aux États Unis : {}".format(df['US_gaz'].corr(df['US_CO2_Mt'])))

    print("\n\n\n\n")
