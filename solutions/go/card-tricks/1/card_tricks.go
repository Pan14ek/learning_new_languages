package cards
import "fmt"

// FavoriteCards returns a slice with the cards 2, 6 and 9 in that order.
func FavoriteCards() []int {
	return []int{2,6,9}
}

// GetItem retrieves an item from a slice at given position.
// If the index is out of range, we want it to return -1.
func GetItem(slice []int, index int) int {
	var sliceIndexes = len(slice) - 1

	if(sliceIndexes >= index && index >= 0) {
        return slice[index]
    }
    
    return -1
}

// SetItem writes an item to a slice at given position overwriting an existing value.
// If the index is out of range the value needs to be appended.
func SetItem(slice []int, index, value int) []int {
	var sliceIndexes = len(slice) - 1

    if(index < 0 || index > sliceIndexes) {
        return append(slice, value)
    }

    slice[index] = value

    return slice
}

// PrependItems adds an arbitrary number of values at the front of a slice.
func PrependItems(slice []int, values ...int) []int {
	return append(values, slice...)
}

// RemoveItem removes an item from a slice by modifying the existing slice.
func RemoveItem(slice []int, index int) []int {
	var sliceIndexes = len(slice) - 1

	if(index > sliceIndexes || index < 0) {
        return slice
    }
    
	var firstPart = slice[:index]
    var secondPart = slice[index+1:]

	fmt.Println(firstPart)
    fmt.Println(secondPart)
    
    return append(firstPart, secondPart...)
}
