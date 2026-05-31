"""
As an engineer at X net newspaper. you have been tasked to develop a program aids jounalist in their field work reporting. The program allows the journalist report an incidence, article into the program.
The journalist is to supply
Title of article
content
date should be in string
reported by......
"""
 
import json
import os

JOURNALIST_FILE = 'C:/Users/CHIDI/OneDrive/Desktop/Pythonfolder/journalist.json'


def load_articles():
    if not os.path.exists(JOURNALIST_FILE):
        return []
    with open(JOURNALIST_FILE, 'r') as f:
        return json.load(f)


def save_articles(articles):
    with open(JOURNALIST_FILE, 'w') as f:
        json.dump(articles, f, indent=4)


class Article:
    def __init__(self, title, content, date, reported_by):
        self.title = title
        self.content = content
        self.date = date
        self.reported_by = reported_by

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "date": self.date,
            "reported_by": self.reported_by
        }

    def display(self):
        print(
            "\n" + "=" * 50 + "\n"
            "  X NET NEWSPAPER\n"
            + "=" * 50 + "\n"
            f"Title      : {self.title}\n"
            f"Date       : {self.date}\n"
            f"Reported By: {self.reported_by}\n"
            + "-" * 50 + "\n"
            f"Content:\n{self.content}\n"
            + "=" * 50
        )


def display_article(article_dict):
    print(
        "\n" + "=" * 50 + "\n"
        "  X NET NEWSPAPER\n"
        + "=" * 50 + "\n"
        f"Title      : {article_dict['title']}\n"
        f"Date       : {article_dict['date']}\n"
        f"Reported By: {article_dict['reported_by']}\n"
        + "-" * 50 + "\n"
        f"Content:\n{article_dict['content']}\n"
        + "=" * 50
    )


def report_article():
    print("=== X Net Newspaper — Field Report System ===\n")

    title = input("Enter article title: ")
    content = input("Enter article content: ")
    date = input("Enter date (e.g. May 15, 2026): ")
    reported_by = input("Reported by: ")

    article = Article(title, content, date, reported_by)
    article.display()

    articles = load_articles()
    articles.append(article.to_dict())
    save_articles(articles)
    print("Article saved successfully to journalist.json")


def search_articles():
    print("\n=== Search Articles ===")
    print("Search by: 1) Title  2) Content  3) Date  4) Reported By")
    choice = input("Choose an option (1-4): ").strip()

    field_map = {"1": "title", "2": "content", "3": "date", "4": "reported_by"}
    if choice not in field_map:
        print("Invalid option.")
        return

    field = field_map[choice]
    keyword = input(f"Enter {field.replace('_', ' ')} to search: ").strip().lower()

    articles = load_articles()
    results = [a for a in articles if keyword in a[field].lower()]

    if not results:
        print("No articles found matching your search.")
    else:
        print(f"\n{len(results)} article(s) found:\n")
        for article in results:
            display_article(article)


def main():
    while True:
        print("\n=== X Net Newspaper ===")
        print("1) Report a new article")
        print("2) Search articles")
        print("3) Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            report_article()
        elif choice == "2":
            search_articles()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


main()
