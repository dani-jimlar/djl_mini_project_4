"""
This test tests if the barplot generated is saved in the rep

"""
import pandas as pd
import requests

def test_github_file_existence():
    name = "dani-jimlar" 
    repo = "djl_mini_project_1"  
    path_to_file = "source/bar_plot2.png"  
    url = f"https://api.github.com/repos/{name}/{repo}/contents/{path_to_file}"
    response1 = requests.get(url)
    assert response1.status_code == 200

if __name__ == "__main_

file_path = "djl_project2/source/bar_plot2.png"
if is_valid_png(file_path):
    print("The image is valid PNG image.")
else:
    print("The image is not valid PNG image.")

if __name__ == "__main__":
    test_github_file_existence()
