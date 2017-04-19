import requests
from eos import *
from xml.dom.minidom import parse, parseString

def get_skills(key, verification_code, character):	
	path = "/char/Skills.xml.aspx"
	authentication= "?keyID=" + key + "&vCode=" + verification_code
	connection_string = "https://api.eveonline.com" + path + authentication
	connection_string += "&characterID=" + character
	
	response = requests.get(connection_string)
	
	dom = parseString(response.text)
	skill_list = dom.getElementsByTagName("row");
	new_list = []
	
	for skill in skill_list:
		skill_id = skill.attributes['typeID'].value
		skill_level = skill.attributes['level'].value
		skill_name =skill.attributes['typeName'].value
		new_list.append({"id": skill_id, "level": skill_level})
		
		#print("id:", skill_id, "name:", skill_name , "level:", skill_level)
	
	return new_list
	
def add_skills_to_fit(fit, skills):
	
	for skill in skills:
		fit.skills.add(Skill(int(skill['id']), level=int(skill['level'])))

	
	

	
	
