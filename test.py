import google.generativeai as genai

genai.configure(api_key="AIzaSyCDoZA3H0Fz0keDpvBhVhVD9U2gVwkeTgs")

for m in genai.list_models():
    print(m.name)