# The following are basic instructions of pushing a local app up to IBM Cloud
ibmcloud login -u <your email>
# Set the region and the owner
ibmcloud target --cf-api https://api.REGION.cf.cloud.ibm.com -r REGION -o OWNER
# Create an account space called translator
ibmcloud account space-create translator
# Set the target to the account space
ibmcloud target -s translator

## Change the manifest file to a name for your app

# Deploy your app
ibmcloud app push

# Check logs for your app
ibmcloud cf logs <appname> --recent

# Visit your app here:
https://englishfrenchtranslatorfromchris.mybluemix.net/

