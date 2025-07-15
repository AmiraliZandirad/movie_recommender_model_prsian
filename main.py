import pandas as pd

#--------------- md = movies dataset -----------------------
md = pd.read_csv("dataset.csv")

def create_textual_representation(row):
    textual_representation = f"""عنوان انگلیسی :{row["EN_title"]},
عنوان فارسی : {row['PERSIAN_title']},
ژانر : {row['Genre']},
سال:  {row['Year']},
زمان : {row['Time']},
امتیاز : {row['Score']},
لینک : {row['Link']},

خلاصه انگلیسی : {row['Content_2']},
خلاصه فارسی : {row['Content_1']}"""
    return textual_representation

md['textual_representation'] = md.apply(create_textual_representation, axis=1)
