import matplotlib.pyplot as plt
from matplotlib import rcParams, cycler
import numpy as np


def is_dose_safe(doses, dose_limit):
    return sum(doses.values()) <= dose_limit


def show_pie_chart(doses, dose_limit):
    entries = len(doses)
    explode = np.full(shape=entries, fill_value=0.07)

    fig, ax = plt.subplots(num="RadPy")
    wedges, texts, autotexts = ax.pie(doses.values(), labels=doses.keys(), explode=explode,
                                      autopct=lambda pct: autopct_func(pct, doses.values()))
    plt.setp(autotexts, size=12, weight="bold")

    total_dose = sum(doses.values())
    if is_dose_safe(doses, dose_limit):
        ax.set_title(f"Your total dose is less than the recommended dose! ({total_dose:.2f}/{dose_limit:.2f} mSv)")

    else:
        ax.set_title(f"Your total dose is more than the recommended dose! ({total_dose:.2f}/{dose_limit:.2f} mSv)")
    plt.show()


def autopct_func(pct, allvalues):
    allvalues = [*allvalues]
    absolute = pct / 100.*np.sum(allvalues)
    return "{:.1f}%\n({:.2f} mSv)".format(pct, absolute)


def default_plot_settings():
    '''Impostazioni di default per i plot destinati al paper.
    '''
    rcParams["figure.autolayout"] = True
    rcParams['savefig.bbox'] = 'tight'
    rcParams["font.family"] = 'sans-serif'
    rcParams["mathtext.fontset"] = "dejavuserif"
    rcParams['figure.figsize'] = [10, 7]
    rcParams['font.size'] = 16
    rcParams['legend.fontsize'] = 'large'
    custom_palette = ['#713e5a', '#63a375', '#edc79b', '#d57a66', '#ca6680']
    rcParams['axes.prop_cycle'] = cycler(color=custom_palette)
    rcParams['toolbar'] = 'None'


default_plot_settings()

if __name__ == '__main__':
    dict = {
        'altitude': 0.1,
        'living': 0.5,
        'diagnostic': 1.5,
    }
    dose_limit = 1
    show_pie_chart(dict, dose_limit)