from pathlib import Path
data_dir = Path(r'C:\Users\Ryan_Weisner\Documents\Data_Science\Icestaviz\data')

# r_ prefix indicates raw, c_ prefix indicates clean
r_data = data_dir / 'raw'
r_crime_data = r_data / 'crime'
r_economy_data = r_data / 'economy'
r_education_data = r_data / 'education'
r_family_data = r_data / 'family'
r_health_data = r_data / 'health'
r_immigration_data = r_data / 'immigration'
r_income_data = r_data / 'income'
r_tourism_data = r_data / 'tourism'
r_women_lead_data = r_data / 'women_in_leadership'

c_data = data_dir / 'clean'
c_crime_data = c_data / 'crime'
c_economy_data = c_data / 'economy'
c_education_data = c_data / 'education'
c_family_data = c_data / 'family'
c_health_data = c_data / 'health'
c_immigration_data = c_data / 'immigration'
c_income_data = c_data / 'income'
c_tourism_data = c_data / 'tourism'
c_women_lead_data = c_data / 'women_in_leadership'