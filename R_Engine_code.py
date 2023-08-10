from flask import Flask, render_template
import App
import pickle
# Route handler for nearest branches
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Branch Locator!"

@app.route('/nearest-branches')

def nearest_branches():
    customer_location = (37.7749, -122.4194)
    desired_time = 12
    facility = 'cashier check'
    branch_data = App.predict_nearest_branch(customer_location, desired_time, facility)

    if branch_data.empty:
        suggestion = "No suitable branches available."
    else:
        with open('weather_scores.pkl', 'rb') as file:
            weather_scores = pickle.load(file)
        branch_data['WeatherScore'] = branch_data['WeatherCondition'].map(weather_scores)

        with open('Combined_Score_Model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        branch_data['CombinedScore'] = loaded_model.predict(branch_data[['WeatherScore', 'Distance']])

        branch_data = branch_data.sort_values('CombinedScore', ascending=False)
        sorted_branch_names = branch_data['BranchName'].tolist()
        

    return render_template('nearest_branches.html', branches=sorted_branch_names)


if __name__ == '__main__':

    app.run(debug=True)
