import requests

# https://www.google.com/search?q=wagon
# PROTOCOL://HOST/PATH?QUERY_PARAMS

# # GitHub API

# url = "https://api.github.com/users/akira2818430850"
# response = requests.get(url)
# user_dict = response.json()

# print(f"{user_dict['name']} is located in {user_dict['location']}")

# # Open Library API


def get_book_title(isbn):
    url = "https://openlibrary.org/api/books"
    key = f"ISBN:{isbn}"
    response = requests.get(
        url, params={"bibkeys": key, "format": "json", "jscmd": "data"}
    ).json()

    print(response[key]["title"])


get_book_title("9780747532699")
get_book_title("9780980200447")
