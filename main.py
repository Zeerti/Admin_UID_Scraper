import argparse
from SeleniumDriver import SeleniumDriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
#https://github.com/jmcarp/robobrowser

#Settings Editor
#javascript:location.href='/Support/LocationSettingsEditor/{}/?groupid={}'.format(location_id, group_id)


parser1 = argparse.ArgumentParser(description="Username for Admin Portal")
parser1.add_argument("username")
args = parser1.parse_args()

login_url = "https://admin2.brinkpos.net/Public/Login"

#Set values
args.password = getpass("Password: ")
values = {'Username':args.username, "Password":args.password}


#RegEx to find SiteID and GroupID
#.*(.{8}[-].{4}[-].{4}[-].{4}[-].{12})
#re.search(r'.{8}(?:-.{4}){3}-.{12}', s).group(0)


group_array = []
location_array = []
# test group id
current_group_id = None
new_group_id_list = []
new_group_name_list = []

#Opens pane for group details, 
### TURN INTO FUNCTION
	#Group Name
	#Group ID
	#Loyalty
	#Token
	#Franchised
open_group_panel = 'javascript:groupDetails(\'{{{}}}\')'.format(current_group_id)


##################################################################################################
#			GET THE GROUP ID FUNCTION AND GROUP NAME APPEND IN DICT
#Group to Location URL 
group_url_home = "https://admin2.brinkpos.net/Support/Groups/"

#location_url = "https://admin2.brinkpos.net/Support/Locations/{}".format(current_group_id)
browser.open(group_url_home)

buttonList = browser.find_all('a', class_='btn btn-small dropdown-toggle')
group_id_list = browser.find_all('a', href= re.compile('javascript:location.href=\'/Support/'))
parsed_group_id_list = {}

for counter, id in enumerate(group_id_list):
	if id.text == " Dashboard":
		#print("COUNTER: {},\tID: {}".format(counter, id.text))
		new_group_id_list.append(re.search(r'.*(.{8}[-].{4}[-].{4}[-].{4}[-].{12})', str(id.attrs)).group(1))
	else:
		pass

for i in new_group_id_list:
	print(i)
####################################################################################################



####################################################################################################

newLink = browser.get_link(class_="dxp-num")
print(type(newLink))
browser.follow_link(newLink[1])


group_id_list = browser.find_all('a', href= re.compile('javascript:location.href=\'/Support/'))
parsed_group_id_list = {}

for counter, id in enumerate(group_id_list):
	if id.text == " Dashboard":
		#print("COUNTER: {},\tID: {}".format(counter, id.text))
		new_group_id_list.append(re.search(r'.*(.{8}[-].{4}[-].{4}[-].{4}[-].{12})', str(id.attrs)).group(1))
	else:
		pass

for i in new_group_id_list:
	print(i)

#			GET THE GROUP NAME
buttonList = browser.find_all('a', class_='btn btn-small dropdown-toggle')
for button in buttonList:
	new_group_name_list.append(button.text)
	print(button.text)



#Need to click and follow this link
#<a class="dxp-num" >2</a>


#Login
#navigate to groups
#Get list of groups (names of store)
#Parse through ALL groups on admin server
	#get group ID for each group
	#get group name for each group
	#Save group ID and name into DB
#select first group in array group_array[]
	#navigate to https://admin.brinkpos.net/Support/Locations/group_array[0] (CONFIRM HOW POPS WORK)
#pop group off group_array, set current_group_id to group_array[0]

###################
#TESTING NONSENSE
###################

#soup = BeautifulSoup(browser.parsed.text, "html.parser")
#print(soup.prettify())
#
##table = soup.find_all(class_='dxgvTable table table-striped table-bordered dataTable')
#
#print(len(soup.find_all('a')))
#for iter in soup.find_all('table'):
#	print(iter.text)
#
#table = soup.find_all('table', id='gvGroups_DXMainTable')
#table_body = table[0].find('tbody')
#
#rows = table_body.find_all('tr')
#for row in rows:
#	cols = row.find_all('td')
#	cols = [ele.text.strip() for ele in cols]
#	print(cols)
#	data.append([ele for ele in cols if ele])





#for divs in div:
	#print(divs)

#for div1 in modal:
	
	#print(tr)


#get list of all locations @ prior group (names of site)
		#<div class="modal-body" id="location_details" style="max-height: 260px; overflow: auto;">
		#<table class="table">
		#<tbody>
		#<tr style="border-top: none;">
		#    <td style="border-top: none; font-weight: bold;">Name</td>
		#    <td style="border-top: none;">Agra Culture ** LAB **</td>
		#</tr>
		#<tr>
		#    <td style="font-weight: bold;">Id</td>
		#    <td>fd48a048-f7e8-4f51-bf20-4ff178977a53</td>
		#</tr>
		#<tr>
		#    <td style="font-weight: bold;">Number</td>
		#    <td>0</td>
		#</tr>
		#<tr>
		#    <td style="font-weight: bold;">Business Date</td>
		#    <td>Wednesday, May 3, 2017</td>
		#</tr>
		#    <tr>
		#        <td style="font-weight: bold;">Status</td>
		#        <td>Enabled</td>
		#    </tr>
		#    <tr>
		#        <td style="font-weight: bold;">Franchisee</td>
		#        <td>No</td>
		#    </tr>
		#</tbody>
		#</table>
		#</div>
	#Store all UID in location_array[]
	#Save to respective DB Table
#pop location off array
#repeat until all locations for group completed
#associate all UID to Group ID
	#Write to DB or something

# START LOOP #
#Navigate back to https://admin.brinkpos.net/Support/Groups/
#pop off group_array[0]
#get list of all locations
#associate with group ID
# END LOOP #

#loop until all groups have been popped off group array

#logout





