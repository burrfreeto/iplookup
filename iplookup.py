from requests import get

loc = get('https://ipapi.co/json/')
print(loc.json())
print("Check that the above is as expected.")
