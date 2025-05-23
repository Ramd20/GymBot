from bs4 import BeautifulSoup
import requests



#Fucntion will be used in main
def scrapeGym(gym):
    try:
        response = requests.get("https://connect.recsports.vt.edu/facilityoccupancy")
        response.raise_for_status()
        htmltext = response.text                           #This section is just for user display
    except requests.RequestException as e:
        return f"Request failed: {e}"


    soup = BeautifulSoup(htmltext, "lxml")   # This creates the parser

    canvas = soup.find_all("canvas", class_="occupancy-chart") # Finds all occupancy charts there are duplicates


    if canvas:
        WMHOccupancy = canvas[0].get("data-occupancy")
        McComasOccupancy = canvas[2].get("data-occupancy")

        if gym == "mccomas":
            return f"McComas Occupancy: {McComasOccupancy}"

        elif gym == "war":
            return f"War Memorial Occupancy: {WMHOccupancy}"

        else:
            return "Invalid Gym Name"
    else:
        output = "Canvas element not found"

    return output
