import requests

API_URL = "http://localhost/wordpress/wp-json/wp/v2/posts"

def get_latest_posts():
    response = requests.get(API_URL, params={"per_page": 3})

    if response.status_code == 200:
        posts = response.json()
        print("Τελευταία 3 Άρθρα:\n")
        for post in posts:
            title = post["title"]["rendered"]
            print(f"- {title}")
    else:
        print("Σφάλμα σύνδεσης με το WordPress API")

if __name__ == "__main__":
    get_latest_posts()
