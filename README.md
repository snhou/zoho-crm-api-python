## Overview

Zoho provides a Python SDK that can be integrated with Zoho CRM, but it seems a bit complicated. Hence, this repo shows how to set up Python for Zoho CRM and fetch Zoho CRM data with Python. 


### step1 Create application
#### 1.sign in zoho
![](https://i.imgur.com/hpXPsBA.png)

#### 2.Visit the page https://api-console.zoho.com/ and click **ADD CLIENT**

![](https://i.imgur.com/cDAfxEi.png)

#### 3.choose Server-based Application
(the easiest way to setup api)

![](https://i.imgur.com/QI5ChuL.png)

#### 4.fill data
Enter Client Name, Homepage URL, and Authorized Redirect URI. Click **CREATE**.You can fill your personal or company homepage url in these two url fields.

(Not recommended)if you don't have any url, you can fill any website you trust, maybe such as google.
![](https://i.imgur.com/9zlab3e.png =300x400)

#### 5.get Client ID and Client Secret
![](https://i.imgur.com/FGJa7Yp.png =280x350)


### step2 Send Authorization Request to Generate 「code」

#### 1.visiting the specific url
```
https://accounts.zoho.com/oauth/v2/auth?response_type=code&client_id={your_client_id}&scope=AaaServer.profile.Read,ZohoCRM.Modules.ALL&redirect_uri={your_redirect_uri}
```
Make sure the scope contains"AaaServer.profile.Read". 
And if you have to get all zoho data, you can add the scope"ZohoCRM.Modules.ALL".

#### 2.After visiting the url, you can see this page contains your service.

**click Submit**

![](https://i.imgur.com/h24xO1l.png)

#### 3.get authorization grant code

After you click **submit**, you will redirect to the website you fill in the previous step.

And you have to get the authorization grant code on url(after"code=")

![](https://i.imgur.com/MVosrHy.png)

**Warning:** Authorization Grant Code Lifetime : **one minute**.

### step3 Setting Up Python Environment

#### 1.Install SDK 

```python
pip install zcrmsdk
```
#### 2.set up config to initialize

```python
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
```
currentUserEmail: you have to check your zoho email
client_id and client_secret: in the [previous step](#5.get-Client-ID-and-Client-Secret)
redirect_uri: in the [previous step](#4.fill-data)
accounts_url: Based on your domain，default:https://accounts.zoho.com
Authorization_Grant_Code:in the [previous step](#3.get-authorization-grant-code)


### step4 Fetch Zoho Data With Python

* Get a Record by Id
```python
record = ZCRMRecord.get_instance('Lead',id)
resp = record.get()
print(resp.data.field_data['Email'])
```

* Get Module Records
```python
module_ins = ZCRMModule.get_instance('Lead') 
resp=module_ins.get_records(page=3,per_page=100)
for records in resp.data:
    print(records)
```
> ## Reference
> 
> [OAuth Authentication](https://www.zoho.com/creator/help/api/v2/oauth-overview.html)
> [Zoho CRM Python SDK Doc](https://www.zoho.com/crm/developer/docs/server-side-sdks/py-overview.html)
> [Zoho CRM Python SDK repo](https://github.com/zoho/zcrm-python-sdk)
> [Web Server Applications](https://www.zoho.com/accounts/protocol/oauth/web-server-applications.html)
> [Get Records API](https://www.zoho.com/crm/developer/docs/api/v2/get-records.html)