from flask import Flask, jsonify, render_template
import pandas as pd
from sqlalchemy import create_engine

db_string = "postgres://postgres:postgres@localhost:5432/boston_marathon_db"

db = create_engine(db_string)


#for r in result_set:  
#   print(r)

app = Flask(__name__)

#usa runners API
@app.route("/api/runners/us")
def runners_usa():
     result_set = db.execute("SELECT * FROM boston_marathon_2017 WHERE country = 'USA'")
     all_runners_usa = []
     for runner in result_set:
        runner_dict = {}
        runner_dict['bib'] = runner.bib
        runner_dict['name'] = runner.name
        runner_dict['age'] = runner.age
        runner_dict['gender'] = runner.gender
        runner_dict['city'] = runner.city
        runner_dict['state'] = runner.state
        runner_dict['country'] = runner.country
        runner_dict['age_groups'] = runner.age_groups
        runner_dict['official_time_hrs'] = runner.official_time_hrs
        runner_dict['pace_mins'] = runner.pace_mins
        runner_dict['mph @ 5k'] = runner.five_k
        runner_dict['mph @ 10k'] = runner.ten_k
        runner_dict['mph @ 15k'] = runner.fifteen_k
        runner_dict['mph @ 20k'] = runner.twenty_k
        runner_dict['mph @ half'] = runner.half
        runner_dict['mph @ 25k'] = runner.twenty_five_k
        runner_dict['mph @ 30k'] = runner.thirty_k
        runner_dict['mph @ 35k'] = runner.thirty_five_k
        runner_dict['mph @ 40k'] = runner.forty_k
        runner_dict['hardest_part'] = runner.hardest_section

        all_runners_usa.append(runner_dict)
     return jsonify(all_runners_usa)

@app.route("/api/runners/foreign")
def runners_foreign():
     result_set = db.execute("SELECT * FROM boston_marathon_2017 WHERE country != 'USA'")
     all_runners_foreign = []
     for runner in result_set:
        runner_dict = {}
        runner_dict['bib'] = runner.bib
        runner_dict['name'] = runner.name
        runner_dict['age'] = runner.age
        runner_dict['gender'] = runner.gender
        runner_dict['city'] = runner.city
        runner_dict['state'] = runner.state
        runner_dict['country'] = runner.country
        runner_dict['age_groups'] = runner.age_groups
        runner_dict['official_time_hrs'] = runner.official_time_hrs
        runner_dict['pace_mins'] = runner.pace_mins
        runner_dict['mph @ 5k'] = runner.five_k
        runner_dict['mph @ 10k'] = runner.ten_k
        runner_dict['mph @ 15k'] = runner.fifteen_k
        runner_dict['mph @ 20k'] = runner.twenty_k
        runner_dict['mph @ half'] = runner.half
        runner_dict['mph @ 25k'] = runner.twenty_five_k
        runner_dict['mph @ 30k'] = runner.thirty_k
        runner_dict['mph @ 35k'] = runner.thirty_five_k
        runner_dict['mph @ 40k'] = runner.forty_k
        runner_dict['hardest_part'] = runner.hardest_section

        all_runners_foreign.append(runner_dict)
     return jsonify(all_runners_foreign)

#male API
@app.route("/api/runners/male")
def runners_male():
     result_set = db.execute("SELECT * FROM boston_marathon_2017 WHERE gender = 'M'")
     all_runners_male = []
     for runner in result_set:
        runner_dict = {}
        runner_dict['bib'] = runner.bib
        runner_dict['name'] = runner.name
        runner_dict['age'] = runner.age
        runner_dict['gender'] = runner.gender
        runner_dict['city'] = runner.city
        runner_dict['state'] = runner.state
        runner_dict['country'] = runner.country
        runner_dict['age_groups'] = runner.age_groups
        runner_dict['official_time_hrs'] = runner.official_time_hrs
        runner_dict['pace_mins'] = runner.pace_mins
        runner_dict['mph @ 5k'] = runner.five_k
        runner_dict['mph @ 10k'] = runner.ten_k
        runner_dict['mph @ 15k'] = runner.fifteen_k
        runner_dict['mph @ 20k'] = runner.twenty_k
        runner_dict['mph @ half'] = runner.half
        runner_dict['mph @ 25k'] = runner.twenty_five_k
        runner_dict['mph @ 30k'] = runner.thirty_k
        runner_dict['mph @ 35k'] = runner.thirty_five_k
        runner_dict['mph @ 40k'] = runner.forty_k
        runner_dict['hardest_part'] = runner.hardest_section

        all_runners_male.append(runner_dict)
     return jsonify(all_runners_male)

#female API
@app.route("/api/runners/female")
def runners_female():
     result_set = db.execute("SELECT * FROM boston_marathon_2017 WHERE gender = 'F'")
     all_runners_female = []
     for runner in result_set:
        runner_dict = {}
        runner_dict['bib'] = runner.bib
        runner_dict['name'] = runner.name
        runner_dict['age'] = runner.age
        runner_dict['gender'] = runner.gender
        runner_dict['city'] = runner.city
        runner_dict['state'] = runner.state
        runner_dict['country'] = runner.country
        runner_dict['age_groups'] = runner.age_groups
        runner_dict['official_time_hrs'] = runner.official_time_hrs
        runner_dict['pace_mins'] = runner.pace_mins
        runner_dict['mph @ 5k'] = runner.five_k
        runner_dict['mph @ 10k'] = runner.ten_k
        runner_dict['mph @ 15k'] = runner.fifteen_k
        runner_dict['mph @ 20k'] = runner.twenty_k
        runner_dict['mph @ half'] = runner.half
        runner_dict['mph @ 25k'] = runner.twenty_five_k
        runner_dict['mph @ 30k'] = runner.thirty_k
        runner_dict['mph @ 35k'] = runner.thirty_five_k
        runner_dict['mph @ 40k'] = runner.forty_k
        runner_dict['hardest_part'] = runner.hardest_section

        all_runners_female.append(runner_dict)
     return jsonify(all_runners_female)

#top 50 female API
@app.route("/api/runners/top_female")
def runners_top_female():
     result_set = db.execute("SELECT * FROM boston_marathon_2017 WHERE gender = 'F' ORDER BY official_time_hrs LIMIT 50")
     all_runners_top_female = []
     for runner in result_set:
        runner_dict = {}
        runner_dict['bib'] = runner.bib
        runner_dict['name'] = runner.name
        runner_dict['age'] = runner.age
        runner_dict['gender'] = runner.gender
        runner_dict['city'] = runner.city
        runner_dict['state'] = runner.state
        runner_dict['country'] = runner.country
        runner_dict['age_groups'] = runner.age_groups
        runner_dict['official_time_hrs'] = runner.official_time_hrs
        runner_dict['pace_mins'] = runner.pace_mins
        runner_dict['mph @ 5k'] = runner.five_k
        runner_dict['mph @ 10k'] = runner.ten_k
        runner_dict['mph @ 15k'] = runner.fifteen_k
        runner_dict['mph @ 20k'] = runner.twenty_k
        runner_dict['mph @ half'] = runner.half
        runner_dict['mph @ 25k'] = runner.twenty_five_k
        runner_dict['mph @ 30k'] = runner.thirty_k
        runner_dict['mph @ 35k'] = runner.thirty_five_k
        runner_dict['mph @ 40k'] = runner.forty_k
        runner_dict['hardest_part'] = runner.hardest_section

        all_runners_top_female.append(runner_dict)
     return jsonify(all_runners_top_female)

#top 50 male API
@app.route("/api/runners/top_male")
def runners_top_male():
     result_set = db.execute("SELECT * FROM boston_marathon_2017 WHERE gender = 'M' ORDER BY official_time_hrs LIMIT 50")
     all_runners_top_male = []
     for runner in result_set:
        runner_dict = {}
        runner_dict['bib'] = runner.bib
        runner_dict['name'] = runner.name
        runner_dict['age'] = runner.age
        runner_dict['gender'] = runner.gender
        runner_dict['city'] = runner.city
        runner_dict['state'] = runner.state
        runner_dict['country'] = runner.country
        runner_dict['age_groups'] = runner.age_groups
        runner_dict['official_time_hrs'] = runner.official_time_hrs
        runner_dict['pace_mins'] = runner.pace_mins
        runner_dict['mph @ 5k'] = runner.five_k
        runner_dict['mph @ 10k'] = runner.ten_k
        runner_dict['mph @ 15k'] = runner.fifteen_k
        runner_dict['mph @ 20k'] = runner.twenty_k
        runner_dict['mph @ half'] = runner.half
        runner_dict['mph @ 25k'] = runner.twenty_five_k
        runner_dict['mph @ 30k'] = runner.thirty_k
        runner_dict['mph @ 35k'] = runner.thirty_five_k
        runner_dict['mph @ 40k'] = runner.forty_k
        runner_dict['hardest_part'] = runner.hardest_section

        all_runners_top_male.append(runner_dict)
     return jsonify(all_runners_top_male)

#full API
@app.route("/api/runners")
def runners():
    result_set = db.execute("SELECT * FROM boston_marathon_2017")
    all_runners = []
    for runner in result_set:
        runner_dict = {}
        runner_dict['bib'] = runner.bib
        runner_dict['name'] = runner.name
        runner_dict['age'] = runner.age
        runner_dict['gender'] = runner.gender
        runner_dict['city'] = runner.city
        runner_dict['state'] = runner.state
        runner_dict['country'] = runner.country
        runner_dict['age_groups'] = runner.age_groups
        runner_dict['official_time_hrs'] = runner.official_time_hrs
        runner_dict['pace_mins'] = runner.pace_mins
        runner_dict['mph @ 5k'] = runner.five_k
        runner_dict['mph @ 10k'] = runner.ten_k
        runner_dict['mph @ 15k'] = runner.fifteen_k
        runner_dict['mph @ 20k'] = runner.twenty_k
        runner_dict['mph @ half'] = runner.half
        runner_dict['mph @ 25k'] = runner.twenty_five_k
        runner_dict['mph @ 30k'] = runner.thirty_k
        runner_dict['mph @ 35k'] = runner.thirty_five_k
        runner_dict['mph @ 40k'] = runner.forty_k
        runner_dict['hardest_part'] = runner.hardest_section

        all_runners.append(runner_dict)
    
    return jsonify(all_runners) 

@app.route("/")
def homepage(): 
    result_set = db.execute("SELECT * FROM boston_marathon_2017")  

    all_runners = []
    for runner in result_set:
         runner_dict = {}
    #     runner_dict['bib'] = runner.bib
         runner_dict['name'] = runner.name
         runner_dict['age'] = runner.age
         runner_dict['gender'] = runner.gender
    #     runner_dict['city'] = runner.city
    #     runner_dict['state'] = runner.state
         runner_dict['country'] = runner.country
         runner_dict['age_groups'] = runner.age_groups
         runner_dict['official_time_hrs'] = runner.official_time_hrs
         runner_dict['hardest_part'] = runner.hardest_section
         all_runners.append(runner_dict)
    #     runner_dict['pace_mins'] = runner.pace_mins
    #     runner_dict['mph @ 5k'] = runner.five_k
    #     runner_dict['mph @ 10k'] = runner.ten_k
    #     runner_dict['mph @ 15k'] = runner.fifteen_k
    #     runner_dict['mph @ 20k'] = runner.twenty_k
    #     runner_dict['mph @ half'] = runner.half
    #     runner_dict['mph @ 25k'] = runner.twenty_five_k
    #     runner_dict['mph @ 30k'] = runner.thirty_k
    #     runner_dict['mph @ 35k'] = runner.thirty_five_k
    #     runner_dict['mph @ 40k'] = runner.forty_k
    df = pd.DataFrame(all_runners)
        
    #print(all_runners)
    #number of participants by age group
    bins = [18, 34, 39, 44, 49, 54, 59, 64, 69, 74,  79, 100]
    group_names = ["18-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80+"]
    number_of_runner_by_age = list(pd.cut(df["age"], bins, labels=group_names, include_lowest=True).value_counts())    
    
    df_males = df[df.gender == 'M']
    df_females = df[df.gender == 'F']
    #average end time by age and gender
    male_times = df_males.groupby(pd.cut(df_males["age"], bins, labels=group_names))['official_time_hrs'].mean().to_list()
    female_times = df_females.groupby(pd.cut(df_females["age"], bins, labels=group_names))['official_time_hrs'].mean().to_list()

    #usa vs international
    usa = df[df.country == 'USA']
    usa['USA/International'] = 'USA'
    international = df[df.country != 'USA']
    international['USA/International'] = 'International'
    usa_foreign = pd.concat([usa, international])
    country_count = usa_foreign['USA/International'].value_counts().to_list()

    #average end time by age and country
    usa_times = usa.groupby(pd.cut(usa["age"], bins, labels=group_names))['official_time_hrs'].mean().to_list()
    international_times = international.groupby(pd.cut(international["age"], bins, labels=group_names))['official_time_hrs'].mean().to_list()

    #top 50 male data
    top_50_males = df_males.sort_values(by='official_time_hrs', ascending=True).head(50)
    top_50_male_names = top_50_males['name'].to_list()
    top_50_male_times = top_50_males['official_time_hrs'].to_list()
    top_50_male_country = top_50_males['country'].to_list()
    top_50_male_age = top_50_males['age_groups'].to_list()
    
    #top 50 female data
    top_50_females = df_females.sort_values(by='official_time_hrs', ascending=True).head(50)
    top_50_female_names = top_50_females['name'].to_list()
    top_50_female_times = top_50_females['official_time_hrs'].to_list()
    top_50_female_country = top_50_females['country'].to_list()
    top_50_female_age = top_50_females['age_groups'].to_list()

    ranking = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
#     print(top_50_male_times)
 
    #print(male_times)
    #print(male_times)

    #                   variable being send to html = data from db
    return render_template('index.html', bins=bins, group_names=group_names, number_of_runner_by_age=number_of_runner_by_age, male_times= male_times, female_times=female_times, top_50_male_names=top_50_male_names, top_50_male_times=top_50_male_times, ranking=ranking, top_50_male_country=top_50_male_country, top_50_male_age=top_50_male_age, top_50_female_names=top_50_female_names, top_50_female_times=top_50_female_times, top_50_female_country=top_50_female_country, top_50_female_age=top_50_female_age, country_count=country_count, usa_times=usa_times, international_times=international_times)

@app.route("/map")
def map_page ():

     return render_template('map.html')


if __name__ == "__main__":
    app.run(debug=True)
