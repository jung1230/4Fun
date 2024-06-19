import json



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

def output_markdown(not_following_me_back, Im_not_following_back):
    output = ""

    # Users not following you back
    output += "### Users Not Following You Back:\n\n"
    output += f"- **Total**: {len(not_following_me_back)}\n\n"
    output += "| Username        |\n"
    output += "|-----------------|\n"
    for username in not_following_me_back:
        output += f"| {username}           |\n"
    output += "\n"

    # Users you are not following back
    output += "### Users You Are Not Following Back:\n\n"
    output += f"- **Total**: {len(Im_not_following_back)}\n\n"
    output += "| Username        |\n"
    output += "|-----------------|\n"
    for username in Im_not_following_back:
        output += f"| {username}           |\n"
    output += "\n"

    return output


def main():
    # Load following and followers lists from JSON files
    following_list = load_following('following.json')
    follower_list = load_followers('followers_1.json')
    following_list.sort()
    follower_list.sort()
    # test_loading(following_list, follower_list)

    # Compare two lists
    not_following_me_back, Im_not_following_back = compare_following_follower(following_list, follower_list)

    # Generate Markdown output
    markdown_output = output_markdown(not_following_me_back, Im_not_following_back)

    # Print or write Markdown output to a file
    print(markdown_output)



if __name__ == '__main__':
    main()