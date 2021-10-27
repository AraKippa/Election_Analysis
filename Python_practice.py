counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

for county in counties:
    print(county)

for num in range(5):
    print(num)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for voters in counties_dict.values():
    print (voters)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Multiline print with f
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You recieved {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total votes. "
)

print(message_to_candidate)

#Skill Drill fprint multiple dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f'{county_dict["county"]} county has {county_dict["registered_voters"]:,} registered voters.')
