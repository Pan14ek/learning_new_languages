// Package weather provides information about forecast.
package weather

var (
    // CurrentCondition is responsible for providing condition.
	CurrentCondition string
    // CurrentLocation is responsible for providing location.
	CurrentLocation  string
)

// Forecast is responsible for providing the forecast for the particular location with condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
