import pandas as pd

# Preview data sets using these functions
crew = pd.read_csv("crew.csv")

roles = ['Director', 'Producer', 'Writer', 'Casting', 'Editor', 'Cinematography',
 'Assistant director', 'Additional directing', 'Executive producer',
 'Lighting', 'Camera operator', 'Additional photography', 'Production design',
 'Art direction', 'Set decoration', 'Special effects', 'Visual effects',
 'Stunts', 'Choreography', 'Composer', 'Songs', 'Sound', 'Costume design',
 'Makeup', 'Hairstyling', 'Story', 'Original writer', 'Title design',
 'Co-director']

for role in roles:
    num = (crew['role'] == role).sum()
    if num > 100000:
        print(f"Number of {role}s: {num}")

'''
In the crew.csv file, here are all of the listed roles:




 '''