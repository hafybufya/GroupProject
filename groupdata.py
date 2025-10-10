import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

# Fetch the data.
# retirement_df = pd.read_csv('GroupProject/Retirement_Age.csv')
# print(retirement_df)

def read_retirement_data():
    '''
    reads Retirement_Age.csv file and parses the year column as a date and sets it as an index
    '''
    retirement_df = pd.read_csv('GroupProject/Retirement_Age.csv', parse_dates=['Year'],  index_col='Year')
    return retirement_df
    
retirement_df =read_retirement_data()


#mask to get OECD data for men and women
OECD_average = retirement_df[retirement_df['Entity'] == 'OECD average'].copy()

#mask to get United Kingdom data for men and women
UK_average = retirement_df[retirement_df['Entity'] == 'United Kingdom'].copy()


#choosing based on when dates overlap in the dataset for OECD and UK
#improvement is so that the code dynamically selects when this overlap happens and fills up?
st_date=date(1970, 1, 1)
end_date=date(2018, 1, 1) 


#plotting both OECD women and UK same graph
plot_retirement_women= OECD_average[st_date:end_date].plot(kind='line',y='Average effective age of retirement, women (OECD)', label='"Average effective age of retirement, women (OECD)"')
#ax = puts both lines on the same plot
UK_average[st_date:end_date].plot(kind='line',y='Average effective age of retirement, women (OECD)', label="Average effective age of retirement, women (UK)" ,ax = plot_retirement_women)
plot_retirement_women.set_title("Retirement Age Over Time - Women (1970-2018)")

plt.show()


#retirement age women oecd #FUNCTIONAL
# retirement_women= OECD_average[st_date:end_date].plot(kind='line',y='Average effective age of retirement, women (OECD)', label='"Average effective age of retirement, women (OECD)"')
# retirement_women.set_title("Retirement Age Over Time - Women (1970-2018)")
# plt.figtext(0.5, -0.03, "Figure 1: Time series showing average annual working hours per worker in South Korea",
#             wrap=True, horizontalalignment='center', fontsize=10)

# #plt.show()

#retirement age women UK #FUNCTIONAL
# retirement_women= UK_average[st_date:end_date].plot(kind='line',y='Average effective age of retirement, women (OECD)', label='"Average effective age of retirement, women (UK)"')
# retirement_women.set_title("Retirement Age Over Time - Women (1970-2018)")
# plt.figtext(0.5, -0.03, "Figure 1: Time series showing average annual working hours per worker in South Korea",
#             wrap=True, horizontalalignment='center', fontsize=10)

#plt.show()
