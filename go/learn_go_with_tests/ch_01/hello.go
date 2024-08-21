package main

const (
	dutch = "Dutch"
	french = "French"
	spanish = "Spanish"

	englishHelloPrefix = "Hello, "
	dutchHelloPrefix = "Hallo, "
	frenchHelloPrefix = "Bonjour, "
	spanishHelloPrefix = "Hola, "
)


func Hello(name, language string) string {
	if name == "" {
		name = "World"
	}

	return greetingPrefix(language) + name
}


func greetingPrefix(language string) (prefix string) {
	switch language {
	case spanish:
		prefix = spanishHelloPrefix
	case french:
		prefix = frenchHelloPrefix
	case dutch:
		prefix = dutchHelloPrefix
	default:
		prefix = englishHelloPrefix
	}
    return
}



