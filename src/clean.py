default_keeps = ["latitude","longitude","daily"]

def clean_data(raw_data, info_keep=default_keeps):
  clean_data = {}

  for k in raw_data:
    if k in info_keep:
      clean_data[k] = raw_data[k]

  return clean_data

"""---------"""

def fix_times(data, chosen_variables="sunrise,sunset"):
    for var in chosen_variables.split(","):
        if var in data["daily"]: # will need to make daily a variable later to implement forecast options

            # This goes through all of the date-times in the data and cleans it up to just times
            data["daily"][var] = [t.split("T")[1] for t in data["daily"][var]]                                                   
