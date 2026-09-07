bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[1])
print(bicycles[3])

# %%
bicycles = ["trek", "cannondale", "redline", "specialized"]
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
# %%


# %%
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")


# %%
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


# %%
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


# %%
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name][
            0
        ].title()  # Get first language from the list
        print(f"\t{name.title()}, I see you love {language}!")

# %%
if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
# %%
