def get_weather_input():
    weather = input("What is the weather like today? (sunny, rainy, or cloudy): ")
    if weather.lower() not in ["sunny", "rainy", "cloudy"]:
        print("Invalid input. Please enter 'sunny', 'rainy', or 'cloudy'.")
        return get_weather_input()
    return weather.lower()

def get_clothing_suggestion(weather):
    suggestion = []
    
    # Suggest clothing based on the weather
    if weather == "sunny":
        suggestion.append("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        suggestion.append("Don't forget your umbrella and a raincoat.")
    elif weather == "cloudy":
        suggestion.append("Make sure to wear a warm coat and a scarf.")
    else:
        suggestion.append("Sorry, I don't have recommendations for this weather.")
        
    return suggestion

def main():
    try:
        weather_input = get_weather_input()
        
        recommendations = get_clothing_suggestion(weather_input)
        
        for i, recommendation in enumerate(recommendations, 1):
            print(f"{i}. {recommendation}")
            
    except ValueError:
        print("Please enter a valid answer for weather!")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__== "__main__":
    main()