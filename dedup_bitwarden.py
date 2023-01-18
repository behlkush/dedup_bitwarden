import json

# you need to export your bitwarden data as json and put it in the same folder location 
# as the python script or give the full path here
file_handle = open('bitwarden_export.json')

#This is the best way to read a json file and store its contents in a dictionary in a single line
#json.load takes in a string and returns back json object
data = json.load(file_handle)

#Considering that Folders don't have any duplicates and we are only considering to remove duplicate
#items
items = data["items"]

#Set only stores unique values and is the best data structure for our use case
item_identities = set()

# create a list of deduped items
deduped_items = []


for item in items:
    item_id = item["id"]

    #This is the most important logic here. id values are different even for the duplicated entries. What i mean is 
    # if you have 2 entries for a website with same username and password values and same URL and other values, id for that 
    # item will still be different. Make it empty valued with counter that
    item["id"] = ""

    #item is a json object and to extract the string out of it use dumps. json.dumps takes a json object and returns a string
    #note that id value of this stringified item will be empty
    item_stringified = json.dumps(item)

    if item_stringified not in item_identities:
        item_identities.add(item_stringified)
        #put back the id which was emptied earlier
        item["id"] = item_id
        #add to the result
        deduped_items.append(item)

data["items"] = deduped_items
print(f"{len(items) - len(deduped_items)} duplicates removed.")
print(f"Exported file has {len(deduped_items)} login/password/secret items.")

file_handle.close()


#Write output file using dump function which will generate a json output
with open('bitwarden_deduped.json', encoding='utf-8', mode='w') as new_vault:
    json.dump(data, new_vault, indent=2, ensure_ascii=False)
