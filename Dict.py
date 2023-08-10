import pickle

# Assuming you have a dictionary of weather scores
weather_scores = {'Sunny': 1.1753125,
                  'Rainy':1,
 'Partly cloudy': 1.17179710867398,
 'Cloudy': 1.16830268389662,
 'Overcast': 1.16482903865213,
 'Mist': 1.14108009708738,
 'Patchy rain possible': 1.10565616180621,
 'Patchy snow possible': 1.10254455909944,
 'Patchy sleet possible': 1.09945042095416,
 'Patchy freezing drizzle possible': 1.09637360074627,
 'Thundery outbreaks possible': 1.08124425022999,
 'Blowing snow': 1.0550381508079,
 'Blizzard': 1.05220456580125,
 'Fog': 1.03551762114537,
 'Freezing fog': 1.0246839581517,
 'Patchy light drizzle': 1.02201086956522,
 'Light drizzle': 1.01935169124024,
 'Freezing drizzle': 1.00626070205479,
 'Heavy freezing drizzle': 1.00368274978651,
 'Patchy light rain': 0.996027542372881,
 'Light rain': 0.993501690617075,
 'Moderate rain at times': 0.990988617200675,
 'Moderate rain': 0.988488225399495,
 'Heavy rain at times': 0.986000419463087,
 'Heavy rain': 0.98352510460251,
 'Light freezing rain': 0.981062186978297,
 'Moderate or heavy freezing rain': 0.978611573688593,
 'Light sleet': 0.976173172757475,
 'Moderate or heavy sleet': 0.973746893123447,
 'Patchy light snow': 0.971332644628099,
 'Light snow': 0.968930338004946,
 'Patchy moderate snow': 0.966539884868421,
 'Moderate snow': 0.964161197703035,
 'Patchy heavy snow': 0.961794189852701,
 'Heavy snow': 0.959438775510204,
 'Ice pellets': 0.950131366208569,
 'Light rain shower': 0.947832661290323,
 'Moderate or heavy rain shower': 0.94554505229284,
 'Torrential rain shower': 0.943268459069021,
 'Light sleet showers': 0.941002802241793,
 'Moderate or heavy sleet showers': 0.938748003194888,
 'Light snow showers': 0.936503984063745,
 'Moderate or heavy snow showers': 0.93427066772655,
 'Light showers of ice pellets': 0.9320479777954,
 'Moderate or heavy showers of ice pellets': 0.929835838607595,
 'Patchy light rain with thunder': 0.923261979575805,
 'Moderate or heavy rain with thunder': 0.921091300940439,
 'Patchy light snow with thunder': 0.918930805316654,
 'Moderate or heavy snow with thunder': 0.916780421216849}

# Save the weather scores to a pickle file
with open('weather_scores.pkl', 'wb') as file:
    pickle.dump(weather_scores, file)