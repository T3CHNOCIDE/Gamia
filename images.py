import json
import wikiapi
import requests
import regex as re

def pull_listed_wikis(site, username, password):
	"""
	Pulls all listed wikis from the interlanguage map page 
	in order to update each international page number
	"""
	
	wikiapi.login(site, username, password)
	
	print "Collecting images to complete ..."
	
	allpages = wikiapi.allpages(limit=5000, namespace=6)
	
	print "%s images to complete!" % len(allpages)
	i = 1
	
	for file in allpages:
	
		print "[%s/%s]" % (i, len(allpages))
	
		try:
			file_page = wikiapi.view(file)
		except:
			with open("report.txt", "a") as file:
				file.write(str(file) + "\n")
			file.close()
			continue
				
		
		if file_page:
		
			if any(ext in file.lower() for ext in [".png", ".gif", ".jpg", ".jpeg", ".ico", ".svg"]):
		
				if "{{image}}" not in file_page.lower():
				
					file_page = "{{Image}}\n" + file_page
					print "\tImage template added!"
					
				else:
				
					print "\tImage template already on page!"
					
				edit_summary = "{{Image}} template added to page."
		
			elif any(ext in file.lower() for ext in [".ogg", ".ogv", ".oga"]):
		
				if "{{audio}}" not in file_page.lower():
				
					file_page = "{{Audio}}\n" + file_page
					print "\tAudio file template added!"
					
				else:
				
					print "\tAudio file template already on page!"
			
				edit_summary = "{{Audio}} template added to page."
		
			elif any(ext in file.lower() for ext in [".odt", ".ods", ".odp", ".odg", ".odc", ".odf", ".odi", ".odm", ".pdf"]):
		
				print "\tDocument file??"
				
			else:
		
				if "{{video}}" not in file_page.lower():
				
					file_page = "{{Video}}\n" + file_page
					print "\tVideo template added!"
					
				else:
				
					print "\tVideo template already on page!"
					
				edit_summary = "{{Video}} template added to page."
				
		else:
		
			if any(ext in file.lower() for ext in [".png", ".gif", ".jpg", ".jpeg", ".ico", ".svg"]):
		
				file_page = "{{Image}}"
				print "\tImage template added!"
				edit_summary = "{{Image}} template added to page."
		
			elif any(ext in file.lower() for ext in [".ogg", ".ogv", ".oga"]):
		
				file_page = "{{Audio}}"
				print "\tAudio file template added!"
				edit_summary = "{{Audio}} template added to page."
		
			elif any(ext in file.lower() for ext in [".odt", ".ods", ".odp", ".odg", ".odc", ".odf", ".odi", ".odm", ".pdf"]):
		
				print "\tDocument file??"
				
			else:
		
				file_page = "{{Video}}"
				print "\tVideo template added!"
				edit_summary = "{{Video}} template added to page."
		
		wikiapi.edit(file, file_page, summary=edit_summary, bot=True)
			
		i += 1
		
if __name__ == "__main__":
	
	pull_listed_wikis("WIKI", "USERNAME", "PASSWORD")
