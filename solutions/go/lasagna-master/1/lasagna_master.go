package lasagna

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, layerNumber int) int {
	numberOfLayers := len(layers)
    
    if(layerNumber == 0) {
        layerNumber = 2
    }
    
    return numberOfLayers * layerNumber
}
// TODO: define the 'Quantities()' function
func Quantities(layers []string) (int, float64) {
    noodleCounter := 0
    sauceCounter := 0

    for i := 0; i < len(layers); i++ {
        if(layers[i] == "sauce") {
            sauceCounter++
        }

        if(layers[i] == "noodles") {
            noodleCounter++
        }
    }

    return noodleCounter * 50, float64(sauceCounter) * 0.2
}
// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendsList []string, ownRecipe []string) {
	ownRecipe[len(ownRecipe)-1] = friendsList[len(friendsList)-1]
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantities []float64, portions int) []float64 {
	factor := float64(portions) / 2.0

	result := make([]float64, len(quantities))

	for i, q := range quantities {
		result[i] = q * factor
	}

	return result
}
// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.
