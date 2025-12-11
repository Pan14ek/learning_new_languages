package cars
import "fmt"

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	/*
      productionRate - successRate
         x           - 100%
    */

    return float64(productionRate) * (successRate / float64(100))
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	var carsPersHour float64 = CalculateWorkingCarsPerHour(productionRate, successRate)
    const minutesInHour = 60
    
    return int(carsPersHour) / minutesInHour
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	var carCount uint = 0
    var cost uint = 0

    for carsCount != 0 {
       var num int = carsCount % 10

        fmt.Println(num)

        if(carCount == 0) {
            cost += uint(num) * 10000
        } else if(carCount == 1) {
            cost += uint(num) * 95000
        } else if(carCount == 2) {
            cost += uint(num) * 950000
        }
        
        carCount++ 

        carsCount /= 10
    }

    return cost
}
