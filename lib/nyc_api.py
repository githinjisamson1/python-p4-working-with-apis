
import requests
import json

class GetPrograms:
  # initialize method + instance var to accept any URL
  
  # get_response_body
  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  
  # load_json
  def program_school(self):
    # initialize empty list
    program_list=[]
    
    # friendly json
    programs=json.loads(self.get_programs())
    
    for program in programs:
      # get agency
      program_list.append(program["agency"])
    
    return program_list


# programs = GetPrograms().get_programs()
# print(programs)

# instantiate
programs=GetPrograms()
programs_schools=programs.program_school()

# iterate unique set of schools
for school in set(programs_schools):
  print(school)