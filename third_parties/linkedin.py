import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # headers = {"Authorization": "Bearer " + os.environ.get("PROXYCURL_API_KEY")}
    #
    # response = requests.get(
    #     api_endpoint, params={"url": linkedin_profile_url}, headers=headers
    # )

    url = "https://api.prospeo.io/linkedin-email-finder"
    api_key = os.environ.get("PROSPEO_API_KEY")

    required_headers = {"Content-Type": "application/json", "X-KEY": api_key}

    data = {"url": linkedin_profile_url}

    response = requests.post(url, json=data, headers=required_headers)

    data = response.json()
    data = data["response"]

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    #
    # if data.get("picture"):
    #     data.pop("picture")

    # if data.get("groups"):
    #     for group_dict in data.get("groups"):
    #         group_dict.pop("profile_pic_url")

    return data
