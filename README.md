# dedup_bitwarden
Remove duplicate entries from your BitWarden account

Step 1: Log in to your BitWarden Account: https://vault.bitwarden.com/

Step 2: Export your vault as JSON. Go to Tools -> Export Vault -> Json in dropdown -> Confirm Format -> Enter Master Password
Save the resulting json file in the location you will download the python script (Json file name should be: bitwarden_export.json)

Step 3: Run Python script and a new file bitwarden_deduped.json is generated

Step 4: Empty / reset your BitWarden vault by deleting all the passwords/folders

Step 5: Upload the new bitwarden_deduped.json using Tools -> Import Vault -> Bitwarden JSON -> Select Import


This would remove all duplicate entries from your Bitwarden password vault.

