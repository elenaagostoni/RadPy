import easygui as eg
import pandas as pd
from plot import show_pie_chart

df = pd.read_csv('data.csv', sep=';', index_col='name')
dose_mSv = 'dose (mSv/yr)'
doses_dict = {}

eg.msgbox(msg='Ionizing radiation is a part of our daily life and it \
comes from both natural and artificial sources. The latter in \
particular can depend on our lifestyle, our health conditions, \
where we live…\n\n RadPy will give you the tools to calculate a \
personalized estimate of the effective dose you are subjected to each year.',
          title='Welcome to RadPy',
          ok_button='Let\'s jump right in!',
          image='img/logo.png')

# Dose limit
dose_dataframe = df.loc[df['type'] == 'limit']
categories = dose_dataframe.index
category = eg.choicebox(msg='Are you part of...', title='Work category', choices=categories)
dose_limit = dose_dataframe.at[category, dose_mSv]

print(f"Dose limit: {dose_limit} mSv/year")

# Altitude
alt_dataframe = df.loc[df['type'] == 'altitude']
altitudes = alt_dataframe.index

altitude = eg.choicebox(msg='Do you live at...', title='Altitude', choices=altitudes)
altitude_dose = alt_dataframe.at[altitude, dose_mSv]
doses_dict['altitude'] = altitude_dose

print(f"Average dose at your altitude: {altitude_dose} mSv/year")

# Your home
living_dataframe = df.loc[df['type'] == 'living']
livings = living_dataframe.index

livings = eg.multchoicebox(msg='Do you live in a stone, brick, or concrete building?',
                           title='House materials', choices=livings)
living_dose = 0
if livings:
    for proximity in livings:
        living_dose += living_dataframe.at[proximity, dose_mSv]
doses_dict['living'] = living_dose

print(f"Average dose where you live: {living_dose} mSv/year")

# Power plant proximity
prox_dataframe = df.loc[df['type'] == 'proximity']
proximities = prox_dataframe.index

proximities = eg.multchoicebox(msg='Do you live under 80km from the power plant?',
                           title='Proximity hazards', choices=proximities)
proximity_dose = 0
if proximities:
    for proximity in proximities:
        proximity_dose += prox_dataframe.at[proximity, dose_mSv]
doses_dict['proximity'] = proximity_dose

print(f"Average dose where you live: {proximity_dose} mSv/year")

wants_plot = eg.ccbox("You’ve made it to checkpoint number 1: do you want \
to see how many doses you have accumulated just by where you live, or do \
you want to keep going?", title="Checkpoint", choices=("I'm curious, show me \
now!", "Let's keep going, please..."))

if wants_plot:
    show_pie_chart(doses_dict, dose_limit)

# Background
eg.msgbox("Some of the biggest radiation sources are natural: cosmic radiation \
coming from our Sun and universe, background radiation coming from Earth and the \
materials that compose it, and our body itself!", title="Radiation background...")

eg.msgbox("Every year you breathe around 3 million liters of air. Air contains Radon, \
which is naturally present especially under the surface of the Earth, meaning in \
caves, mines… but also in your basement!\n\
But don’t worry, the dose relative to it is very little…", title="...even from your basement")

background_dataframe = df.loc[df['type'] == 'background']
background_dose = 0
for source in background_dataframe.index:
    background_dose += background_dataframe.at[source, dose_mSv]
doses_dict['background'] = background_dose

# Diagnostic
diagnostic_dataframe = df.loc[df['type'] == 'diagnostic']
diagnostics = diagnostic_dataframe.index

diagnostics = eg.multchoicebox(msg="Health is always at the forefront of our priorities, \
and this shows also in the usage of ionizing radiation fields for diagnostic or therapeutic aims, \
even up to really high dosages. The motto one can think of is “the aim justifies the means”. \
And don’t worry, their usage is under the strict supervision of radiation protection experts, \
radiologists, medical physicists, and many more!\n In the last year, did you have health issues \
that required radiation in the diagnosis process?", title='Diagnostic', choices=diagnostics)
diagnostic_dose = 0
if diagnostics:
    for diagnostic in diagnostics:
        diagnostic_dose += diagnostic_dataframe.at[diagnostic, dose_mSv]
doses_dict['diagnostic'] = diagnostic_dose

print(f"Average dose at your altitude: {diagnostic_dose} mSv/year")

eg.msgbox("You’ve reached the end of our quiz, get ready for the results!")

show_pie_chart(doses_dict, dose_limit)