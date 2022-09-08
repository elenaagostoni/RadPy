import easygui as eg
import pandas as pd

df = pd.read_csv('data.csv', sep=';', index_col='name')
dose = 'dose (mSv/yr)'

eg.msgbox(msg='Ionizing radiation is a part of our daily life and it \
comes from both natural and artificial sources. The latter in \
particular can depend on our lifestyle, our health conditions, \
where we live…\n\n RadPy will give you the tools to calculate a \
personalized estimate of the effective dose you are subjected to each year.',
          title='Welcome to RadPy',
          ok_button='Let\'s jump right in!',
          image='img/logo.png')


### Dose limit ###
dose_dataframe = df.loc[df['type'] == 'limit']
categories = dose_df.index
category = eg.choicebox(msg='Are you a worker in...', title='Work category', choices=categories)
dose_limit = dose_dataframe.at[category, dose]

print(f"Dose limit: {dose_limit} mSv/year")

### Altitude ###
alt_dataframe = df.loc[df['type'] == 'altitude']
altitudes = alt_dataframe.index

altitude = eg.choicebox(msg='Do you live at...', title='Altitude', choices=altitudes)
altitude_dose = alt_dataframe.at[altitude, dose]

print(f"Average dose at your altitude: {altitude_dose} mSv/year")
