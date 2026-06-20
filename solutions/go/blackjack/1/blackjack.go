package blackjack

func ParseCard(card string) int {
	switch card {
	case "ace":
		return 11
	case "two":
		return 2
	case "three":
		return 3
	case "four":
		return 4
	case "five":
		return 5
	case "six":
		return 6
	case "seven":
		return 7
	case "eight":
		return 8
	case "nine":
		return 9
	case "ten", "jack", "queen", "king":
		return 10
	default:
		return 0
	}
}

func FirstTurn(card1, card2, dealerCard string) string {
	var firstCardValue = ParseCard(card1)
    var secondCardValue = ParseCard(card2)
    var dealerCardValue = ParseCard(dealerCard)

    var hasDealerHighCard = dealerCardValue == 11 || dealerCardValue == 10

	var hasTwoAces = firstCardValue == 11 && secondCardValue == 11
	var playerSum = firstCardValue + secondCardValue
    
    switch {
    case hasTwoAces:
        return "P"
    case playerSum == 21:
        if !hasDealerHighCard {
            return "W"
        }
        return "S"
    case playerSum >= 17:
        return "S"
    case playerSum >= 12 && playerSum <= 16:
        if dealerCardValue >= 7 {
            return "H"
        }
        return "S"
    default:
        return "H"
    }
}
