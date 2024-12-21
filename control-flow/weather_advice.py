def get_weather_input():
    weather = input("What's the weather like today? (sunny/rainy/cold): ")
    if weather.lower() not in ["sunny", "rainy", "cold"]:
        print("Invalid input. Please enter 'sunny', 'rainy', or 'cold'.")
        return get_weather_input()
    return weather.lower()

def get_recommendation(weather_input):
    suggestions = []
    if weather_input == "sunny":
        suggestions.append("Wear a t-shirt and sunglasses.")
    elif weather_input == "rainy":
        suggestions.append("Don't forget your umbrella and a raincoat.")
    elif weather_input == "cold":
        suggestions.append("Make sure to wear a warm coat and a scarf.")
    else:
        suggestions.append("Sorry, I don't have recommendations for this weather.")
    return suggestions
    
def main():
    try:
        weather_input = get_weather_input()
        recommendations = get_recommendation(weather_input)
        
        for suggestion in recommendations:
            print(suggestion)
            
    except ValueError:
        print("Invalid input. Please enter a valid choice.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()