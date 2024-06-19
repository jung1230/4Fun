import json
from os import system, name
import sys
import time

def clear_terminal():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

def load_following(jsonFile):
    with open(jsonFile, 'r') as file:
        data = json.load(file)

    following_list = []

    for entry in data['relationships_following']:
        for item in entry['string_list_data']:
            following_list.append(item['value'])

    return following_list

def load_followers(jsonFile):
    with open(jsonFile, 'r') as file:
        data = json.load(file)

    follower_list = []

    for entry in data:
        for item in entry['string_list_data']:
            follower_list.append(item['value'])

    return follower_list

def test_loading(following_list, follower_list):
    # test if load_following & load_followers are working properly
    print("-------------------- following: --------------------")
    for username in following_list:
        print(username, end=", ")
    print("\n\n-------------------- follower: --------------------")
    for username in follower_list:
        print(username, end=", ")

def compare_following_follower(following_list, follower_list):
    following_set = set(following_list)
    follower_set = set(follower_list)

    not_following_me_back = list(following_set - follower_set)
    Im_not_following_back = list(follower_set - following_set)

    return not_following_me_back, Im_not_following_back

def save(not_following_me_back, Im_not_following_back):
    with open("output.txt", 'w') as file:
        file.write(f'Number of users not following me back: {len(not_following_me_back)}\n')
        for i in range(len(not_following_me_back)):
            file.write(f'{i}: {not_following_me_back[i]}\n')
        
        file.write(f'------------------------------------------------\n\nNumber of users I am not following back: {len(Im_not_following_back)}\n')
        for i in range(len(Im_not_following_back)):
            file.write(f'{i}: {Im_not_following_back[i]}\n')

def main():
    following_list = load_following('following.json')
    follower_list = load_followers('followers_1.json')
    following_list.sort()
    follower_list.sort()
    # test_loading(following_list, follower_list)

    not_following_me_back, Im_not_following_back = compare_following_follower(following_list, follower_list)

    save(not_following_me_back, Im_not_following_back)

if __name__ == '__main__':
    while True:
        clear_terminal()
            
        print("Are you prepared to end many friendships? Please press 'Y' for yes or 'N' for no.")
        answer = input("Y/N: ")

        if answer == "Y":
            print("The result will be out soon.")
            main()
            time.sleep(3)
            print("The program has completed. Please check output.txt for the result. Enjoy!")
            break
        elif answer == "N":
            print("You coward!")
            time.sleep(3)
        else:
            print("Please press 'Y' for yes or 'N' for no.")
            time.sleep(3)

