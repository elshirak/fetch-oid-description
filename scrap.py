import requests
import time
from bs4 import BeautifulSoup

def get_oid_info(oid):
    url = f"https://oid-base.com/get/{oid}"  # URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # get OID name
        name_tag = soup.find('font', size="+3")
        name = name_tag.get_text(strip=True) if name_tag else 'N/A'
        
        # get all <code> tags
        code_tags = soup.find_all('code')
        description = 'N/A'
        
        # usually there are 2 code tags on the web-page
        if len(code_tags) == 2:
            second_code_tag = code_tags[1]
            description = second_code_tag.get_text(separator='\n').strip()
            description = description.replace('\n', ' ')
        elif len(code_tags) == 3:
            second_code_tag = code_tags[2]
            description = second_code_tag.get_text(separator='\n').strip()
            description = description.replace('\n', ' ')
        
        return name, description

    except requests.exceptions.RequestException as e:
        print(f"Error fetching OID {oid}: {e}")
        return 'N/A', 'N/A'

def read_oids_from_file(file_path):
    with open(file_path, 'r') as file:
        oids = [line.strip() for line in file if line.strip()]
    return oids

def main():
    file_path = 'unique-oids-ready-for-scrapping'
    oids = read_oids_from_file(file_path)
    
    for oid in oids:
        name, description = get_oid_info(oid)
        print(f"OID: {oid}")
        print(f"Name: {name}")
        print(f"Description: {description}")
        print("-" * 40)
        
        time.sleep(10) # to avoid 429 too many requests error

if __name__ == "__main__":
    main()