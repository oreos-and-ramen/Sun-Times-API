default_keeps = ["latitude","longitude","daily"]

def clean_data(raw_data, info_keep=default_keeps):
  clean_data = {}

  for k in raw_data:
    if k in info_keep:
      clean_data[k] = raw_data[k]

  return clean_data

def fix_times(data, chosen_variables=["sunrise", "sunset"]):                                                                     
    for var in chosen_variables:                                                                                                 
        if var in data["daily"]: # check if the daily variable is either sunset sunrise, ignore otherwise                        
            data["daily"][var] = [t.split("T")[1] for t in data["daily"][var]]                                                   
