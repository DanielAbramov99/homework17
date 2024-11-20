country_dict = {"name": "Israel", "birth": 1948, "population_millions": 9.3, "Capital": "Jerusalem",
                "language": "hebrew",
                "cities": ['Jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
                "currency": "ils", "area_kilometer": 22_145, "gdp_billion": 450}

print(f"the capital of israel is {country_dict.get("Capital")}")
print(f"all the keys of this dictionary {list(country_dict.keys())}")
print(f"all the values of this dictionary {list(country_dict.values())}")
for key, value in country_dict.items():
    print(f"key; {key}, value: {value}")
country_dict_dup = country_dict.copy()
gdp_billion = country_dict_dup.pop("gdp_billion")
print(gdp_billion)
print(country_dict_dup)
new = dict.fromkeys(country_dict, None)
city_list: list[str] = []
counter: int = 0
for key in new:
    if key != "cities":
        value = input(f"Enter {key}: ")
        new[key] = value
    else:
        while key == "cities" and counter < 3:
            value = input(f"Enter {key}: ")
            city_list.append(value)
            counter += 1
            new['cities'] = city_list
print(new)
