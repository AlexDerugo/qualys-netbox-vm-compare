import requests
from .config_parser import qualys_filter, qualys_password, qualys_username

# get qualys token
def get_tocken_access():
    # check your api url
    url_auth        = "https://gateway.qg1.apps.qualys.eu/auth"
    headers_auth    = {"ContentType": "application/x-www-form-urlencoded"}
    data_auth       = {
        "username"  : qualys_username,
        "password"  : qualys_password,
        "token"     : "true",
    }
    response_auth   = requests.post(url_auth, headers=headers_auth, data=data_auth)
    token           = response_auth.text
    return token


# request in global asset
def get_assets(access_token):
    headers_asset   = {
        "Authorization" : f"Bearer {access_token}",
        "Content-Type"  : "application/json",
    }

    # url to get assets. the filter is substituted from the variable
    url_asset_filter    = f"https://gateway.qg1.apps.qualys.eu/am/v1/assets/host/filter/list?filter={qualys_filter}"
    # this query can be used to get all assets
    #url_asset_list     = "https://gateway.qg1.apps.qualys.eu/am/v1/assets/host/list"

    # a null variable for the first request to pass. lastSeenAssetId this parameter shows the largest asset id of all in this request.
    # if the asset id is passed to the next request, then we will get the following assets with larger id than in the previous request
    asset_id            = 0
    list_vm_from_qualys = []
    # 100 assets in one request. is the maximum number for qualys
    # the hasMore parameter means whether there are any more assets that are not included in this request. if == 0, then there is no longer an asset with a higher id than in the current request
    try:
        while True:
            params_asset    = {
                    "pageSize": "100",  
                    "lastSeenAssetId": asset_id,
            }
            response        = requests.post(url_asset_filter,params=params_asset , headers=headers_asset)
            response_json   = response.json()
            asset_id        = response_json["lastSeenAssetId"]
            assets          = response_json["assetListData"]["asset"]
            for asset in assets:
                list_vm_from_qualys.append(asset["assetName"])
            if response_json["hasMore"] == 0:
                break
    except:
        print("request error to asset")
    return list_vm_from_qualys


access_token        = get_tocken_access()
list_vm_from_qualys = get_assets(access_token)

if __name__ == "__main__":
    # when starting the module, print the list of VMs to the terminal
    print(list_vm_from_qualys)