import requests
from cli.banner import show_banner

BASE_URL = "http://127.0.0.1:8000"
SHORTEN_API = f"{BASE_URL}/api/shorten"
HISTORY_API = f"{BASE_URL}/api/links"


def shorten_url():
    url = input("\nEnter URL: ").strip()

    if url.lower() == "exit":
        return

    if not url.startswith(("https://", "http://")):
        print("Please enter a URL beginning with http:// or https://")
        return

    try:
        response = requests.post(
            SHORTEN_API,
            json={"url": url},
            timeout=10,
        )

        if response.status_code == 201:
            data = response.json()
            print("\nShort URL :", data["short_url"])
            print("Original  :", data["target_url"])
        else:
            print("Error:", response.text)

    except requests.RequestException as error:
        print("Could not connect to LinkForge:", error)


def view_history():
    try:
        response = requests.get(HISTORY_API, timeout=10)
        response.raise_for_status()
        links = response.json()

        if not links:
            print("\nNo links saved yet.")
            return

        print("\n--- LINK HISTORY ---")
        for number, link in enumerate(links, start=1):
            print(f"\n{number}. {link['short_code']}")
            print(f"   Short URL : {link['short_url']}")
            print(f"   Target    : {link['target_url']}")
            print(f"   Created   : {link['created_at']}")
            print(f"   Clicks    : {link['clicks']}")

    except requests.RequestException as error:
        print("Could not load history:", error)


def view_statistics():
    try:
        response = requests.get(HISTORY_API, timeout=10)
        response.raise_for_status()
        links = response.json()

        total_links = len(links)
        total_clicks = sum(link["clicks"] for link in links)

        print("\n--- LINKFORGE STATISTICS ---")
        print("Total links  :", total_links)
        print("Total clicks :", total_clicks)

        if links:
            popular = max(links, key=lambda link: link["clicks"])
            print("Most clicked :", popular["short_code"])
            print("Click count  :", popular["clicks"])

    except requests.RequestException as error:
        print("Could not load statistics:", error)


def main():
    while True:
        show_banner()
        print("\n[1] Shorten a URL")
        print("[2] View link history")
        print("[3] View link statistics")
        print("[4] Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            shorten_url()
        elif choice == "2":
            view_history()
        elif choice == "3":
            view_statistics()
        elif choice == "4":
            print("Thanks for using LinkForge!")
            break
        else:
            print("Invalid option. Choose 1, 2, 3, or 4.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nLinkForge CLI closed.")
