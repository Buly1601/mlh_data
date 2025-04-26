import requests
import pandas as pd
from bs4 import BeautifulSoup
from lists import features, frameworks, langs, libraries

def count_from_csv(dataset):
    # read csv
    df = pd.read_csv(dataset)
    # filter to gemini usage only
    filtered_df = df[df["uses_gemini"] == True]
    # get the building tech used
    tech = filtered_df["submission_built_with"]
    
    # memory
    data = {"languages": {},
            "frameworks": {}}
    # check for languages used
    for i, row in enumerate(tech):
        for lang in langs:
            if lang in row:
                if lang not in data["languages"]:
                    data["languages"][lang] = 0
                data["languages"][lang] += 1
        for fw in frameworks:
            if fw in row:
                if fw not in data["frameworks"]:
                    data["frameworks"][fw] = 0
                data["frameworks"][fw] += 1
    return data


def get_links(dataset):
    # get links
    df = pd.read_csv(dataset)
    links = df["Link"]

    # data to be returned
    data = {"languages": {},
            "frameworks": {},
            "features": {},
            "libraries": {}}

    for num, link in enumerate(links):
        # parse the link
        res = requests.get(link)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")
            body = soup.get_text().lower()
            # check for languages used
            for lang in langs:
                if lang in body:
                    if lang not in data["languages"]:
                        data["languages"][lang] = 0
                    data["languages"][lang] += 1
                
            for key, value in frameworks.items():
                if key in data["languages"]:
                    for fw in value:
                        if fw in body:
                            if fw not in data["frameworks"]:
                                data["frameworks"][fw] = 0
                            data["frameworks"][fw] += 1
                    
            for ft in features:
                if ft in body:
                    if ft not in data["features"]:
                        data["features"][ft] = 0
                    data["features"][ft] += 1

            for key, value in libraries.items():
                if key in data["languages"]:
                    for lb in value:
                        if lb in body:
                            if lb not in data["libraries"]:
                                data["libraries"][lb] = 0
                            data["libraries"][lb] += 1

    return data


def write_dict_to_txt(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in data.items():
            f.write(f"{key}:\n")
            if isinstance(value, dict):
                for sub_key, sub_val in value.items():
                    f.write(f"  {sub_key}: {sub_val}\n")
            else:
                f.write(f"  {value}\n")
            f.write("\n")  # extra line between entries



if __name__ == "__main__":
    #write_dict_to_txt(count_from_csv("data_general.csv"), "general_data.txt")
    write_dict_to_txt(get_links("data_winners.csv"), "winners_data.txt")