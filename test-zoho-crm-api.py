from zcrmsdk import ZCRMRecord,ZCRMRestClient,ZohoOAuth,ZCRMModule
config =  { 'currentUserEmail':'YOUR_ZOHO_EMAIL',
            'sandbox':'False',
            'applicationLogFilePath':'./log',
            'client_id':'YOUR_CLIENT_ID',
            'client_secret':'YOUR_CLIENT_SECRET',
            'redirect_uri':'YOUR_REDIRECT_URI',
            'accounts_url':'YOUR_ACCOUNTS_URL',
            'token_persistence_path':"."}
ZCRMRestClient.initialize(config)
oauth_client = ZohoOAuth.get_client_instance()
grant_token = "Authorization_Grant_Code"
oauth_tokens = oauth_client.generate_access_token(grant_token)
print(oauth_tokens)


record = ZCRMRecord.get_instance('Leads',id)
resp = record.get()
print(resp.data.field_data['Email'])

module_ins = ZCRMModule.get_instance('Leads') 
resp=module_ins.get_records(page=3,per_page=100)
for records in resp.data:
    print(records)