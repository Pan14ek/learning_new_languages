package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {
	var counter = 0

    for i := 0; i < len(birdsPerDay); i++ {
        counter += birdsPerDay[i]
    }

    return counter
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {
	startIndex := (week - 1) * 7
    endIndex := startIndex + 7

    sum := 0

	for _, birds := range birdsPerDay[startIndex:endIndex] {
        sum += birds
    }
    
    return sum
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {
	for i := 0; i < len(birdsPerDay); i++ {
        if(i % 2 == 0) {
            birdsPerDay[i]++;
        }
    }

    return birdsPerDay
}
