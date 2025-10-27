def build_profile():
    profile = {
        "age": 0,
        "hobbies": []
    }
    profile["age"] = int(input("Enter the profile age"))
    # split for better testing
    more_hobbies = True
    while more_hobbies:
        profile["hobbies"].append(input("Enter a hobby:"))
        more = input("More hobbies? type y for yes, n for no")
        if more.casefold() == 'n':
            more_hobbies = False
    return profile

def match(profile_1, profile_2):
    match_quality = 0
    age_diff = abs(profile_1["age"] - profile_2["age"])#abs works with neg or pos numbers
    # age_diff = age_diff if age_diff > 0 else - age_diff # without abs
    if age_diff <= 5:
        match_quality += 1
        # make sets instead and look at INTERSECTION of them
    profile_1["hobbies_set"] = set(profile_1["hobbies"])
    profile_2["hobbies_set"] = set(profile_2["hobbies"])
    hobbies_intersection = profile_1["hobbies_set"].intersection(profile_2["hobbies_set"])
    match_quality += len(hobbies_intersection)
    return match_quality
