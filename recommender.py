movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "romance": ["Titanic", "The Notebook", "La La Land"],
    "comedy": ["Hangover", "Mr. Bean", "Deadpool"],
    "horror": ["Conjuring", "Insidious", "Annabelle"],
    "bitch":["Shravya"]
}

print("Welcome to Reco!")
print("Available categories: action, romance, comedy, horror,bitch")

user_choice = input("Enter your favorite category: ").lower()

if user_choice in movies:
    print("Recommended movies for you:")
    for movie in movies[user_choice]:
        print("-", movie)
else:
    print("Sorry, no recommendations available for this category.")