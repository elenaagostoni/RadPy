import easygui as eg

eg.msgbox(msg='Ionizing radiation is a part of our daily life and it \
comes from both natural and artificial sources. The latter in \
particular can depend on our lifestyle, our health conditions, \
where we live…\n\n RadPy will give you the tools to calculate a \
personalized estimate of the effective dose you are subjected to each year.',
          title='Welcome to RadPy',
          ok_button='Let\'s jump right in!',
          image='img/logo.png')

categories = ['public', 'category B', 'category A']
category = eg.choicebox(msg='Are you a worker in...', title='Work category', choices=categories)

dose_limits = [1, 6, 20]  # mSv/year
dose_limit = dose_limits[categories.index(category)]

print(f"Dose limit: {dose_limit} mSv/year")

altitudes = ['sea level', 'altitude lower than 300 m', 'altitude between 300-600 m', 'altitude between 600-1200 m']
altitude = eg.choicebox(msg='Do you live at... (Da implementare)', title='Altitude', choices=altitudes)

altitude_doses = [0, 0, 0]  # mSv/year
altitude_dose = altitude_doses[altitudes.index(altitude)]

print(f"Average dose at your altitude: {altitude_dose} mSv/year")