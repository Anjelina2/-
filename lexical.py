import identificat


# в конце каждого условия находится else, который в случае не совпадения state выводит REJECT
def lexer(symbols):
    words = []
    currentChain = ['', 'None']
    state = "start"
    for s in symbols:
        if s.class_ == "letter":
            if state == "start":
                currentChain[0] += s.symbol
                state = "var"
            elif state == "var":
                currentChain[0] += s.symbol
            elif state == "spaceForIdentifierWithCommaOrNot":
                currentChain[0] += s.symbol
                state = "identifierWithCommaOrNot"
            elif state == "identifierWithCommaOrNot":
                currentChain[0] += s.symbol
            elif state == "identifierWithCommaCompleted":
                currentChain[0] += s.symbol
                state = "identifierWithCommaOrNot"
            elif state == "afterColon":
                currentChain[0] += s.symbol
                state = "array"
            elif state == "array":
                currentChain[0] += s.symbol
            elif state == "afterSqrbrkt1":
                currentChain[0] += s.symbol
                state = "firstBorderLetter"
            elif state == "firstBorderLetter":
                currentChain[0] += s.symbol
            elif state == "afterDots":
                currentChain[0] += s.symbol
                state = "secondBorderLetter"
            elif state == "secondBorderLetter":
                currentChain[0] += s.symbol
            elif state == "afterSqrbrkt2":
                currentChain[0] += s.symbol
                state = "of"
            elif state == "of":
                currentChain[0] += s.symbol
            elif state == "afterOf":
                currentChain[0] += s.symbol
                state = "type"
            elif state == "type":
                currentChain[0] += s.symbol
            else:
                dataOutput(0)
                exit(0)

        elif s.class_ == "space":
            if state == "var":
                currentChain[1] = "identifier"
                words.append(Lexeme(*currentChain))
                currentChain = ['', 'None']
                state = "spaceForIdentifierWithCommaOrNot"

            elif state == "start":
                state = "start"

            elif state == "spaceForIdentifierWithCommaOrNot":
                state = "spaceForIdentifierWithCommaOrNot"

            elif state == "identifierWithCommaOrNot":
                state = "afterIdentifierWithCommaOrNot"

            elif state == "afterIdentifierWithCommaOrNot":
                state = "afterIdentifierWithCommaOrNot"

            elif state == "identifierWithCommaCompleted":
                state = "identifierWithCommaCompleted"

            elif state == "afterColon":
                state = "afterColon"

            elif state == "array":
                currentChain[1] = "identifier"
                words.append(Lexeme(*currentChain))
                currentChain = ['', 'None']
                state = "afterArray"

            elif state == "afterArray":
                state = "afterArray"

            elif state == "afterSqrbrkt1":
                state = "afterSqrbrkt1"

            elif state == "afterSqrbrkt1Sign":
                state = "afterSqrbrkt1Sign"

            elif state == "firstBorderLetter":
                words.append(Lexeme(currentChain[0], "identifier"))
                currentChain = ['', "None"]
                state = "afterFirstBorder"

            elif state == "firstBorderDigit":
                words.append(Lexeme(currentChain[0], "digit"))
                currentChain = ['', "None"]
                state = "afterFirstBorder"

            elif state == "afterFirstBorder":
                state = "afterFirstBorder"

            elif state == "afterDots":
                state = "afterDots"

            elif state == "afterDotsSign":
                state = "afterDotsSign"

            elif state == "secondBorderLetter":
                words.append(Lexeme(currentChain[0], "identifier"))
                currentChain = ['', "None"]
                state = "afterSecondBorder"

            elif state == "secondBorderDigit":
                words.append(Lexeme(currentChain[0], "digit"))
                currentChain = ['', "None"]
                state = "afterSecondBorder"

            elif state == "afterSecondBorder":
                state = "afterSecondBorder"

            elif state == "afterSqrbrkt2":
                state = "afterSqrbrkt2"

            elif state == "of":
                words.append(Lexeme(currentChain[0], "identifier"))
                currentChain = ['', "None"]
                state = "afterOf"

            elif state == "afterOf":
                state == "afterOf"

            elif state == "type":
                words.append(Lexeme(currentChain[0], "identifier"))
                currentChain = ['', 'None']
                state = "afterType"

            elif state == "afterType":
                state = "afterType"

            elif state == "afterSemicolon":
                state = "afterSemicolon"

            else:
                dataOutput(0)
                exit(0)

        elif s.class_ == "digit":
            if state == "identifierWithCommaOrNot":  # state is set in section "letter"
                currentChain[0] += s.symbol
            elif (state == "afterSqrbrkt1") or (state == "afterSqrbrkt1Sign"):
                currentChain[0] += s.symbol
                state = "firstBorderDigit"
            elif state == "firstBorderDigit":
                currentChain[0] += s.symbol
            elif state == "firstBorderLetter":
                currentChain[0] += s.symbol
            elif state == "afterDots" or (state == "afterDotsSign"):
                currentChain[0] += s.symbol
                state = "secondBorderDigit"
            elif state == "secondBorderDigit":
                currentChain[0] += s.symbol
            elif state == "secondBorderLetter":
                currentChain[0] += s.symbol
            else:
                dataOutput(0)
                exit(0)

        elif s.class_ == "comma":
            if (state == "identifierWithCommaOrNot") or (state == "afterIdentifierWithCommaOrNot"):
                currentChain[0] += s.symbol
                words.append(Lexeme(currentChain[0], "identifierWithComma"))
                currentChain = ['', 'None']
                state = "identifierWithCommaCompleted"
            else:
                dataOutput(0)
                exit(0)

        elif s.class_ == "colon":
            if (state == "identifierWithCommaOrNot") or (state == "afterIdentifierWithCommaOrNot"):
                words.append(Lexeme(currentChain[0], "identifier"))
                words.append(Lexeme(":", "colon"))
                currentChain = ['', 'None']
                state = "afterColon"
            else:
                dataOutput(0)
                exit(0)
        elif s.class_ == "sqrbrkt1":
            if state == "array":
                currentChain[1] = "identifier"
                words.append(Lexeme(*currentChain))
                words.append(Lexeme("[", "sqrbrkt1"))
                currentChain = ['', 'None']
                state = "afterSqrbrkt1"

            elif state == "afterArray":
                currentChain[0] = "["
                currentChain[1] = "sqrbrkt1"
                words.append(Lexeme(*currentChain))
                currentChain = ['', 'None']
                state = "afterSqrbrkt1"
            else:
                dataOutput(0)
                exit(0)

        elif s.class_ == "sign":
            if (state == "afterSqrbrkt1") or (state == "afterDots"):
                currentChain[0] += s.symbol
                state = state + "Sign"

        elif s.class_ == "dots":
            if state == "firstBorderLetter":
                words.append(Lexeme(currentChain[0], "identifier"))
                currentChain[0] = s.symbol
                words.append(Lexeme(currentChain[0], "dots"))
                currentChain = ["", "None"]
                state = "afterDots"

            elif state == "firstBorderDigit":
                words.append(Lexeme(currentChain[0], "digit"))
                currentChain[0] = s.symbol
                words.append(Lexeme(currentChain[0], "dots"))
                currentChain = ["", "None"]
                state = "afterDots"

            elif (state == "afterFirstBorder"):
                currentChain[0] = s.symbol
                words.append(Lexeme(currentChain[0], "dots"))
                currentChain = ["", "None"]
                state = "afterDots"
            else:
                dataOutput(0)
                exit(0)

        elif s.class_ == "sqrbrkt2":
            if state == "secondBorderLetter":
                words.append(Lexeme(currentChain[0], "identifier"))
                currentChain[0] = "]"
                currentChain[1] = "sqrbrkt2"
                words.append(Lexeme(*currentChain))
                currentChain = ['', 'None']
                state = "afterSqrbrkt2"

            elif state == "secondBorderDigit":
                words.append(Lexeme(currentChain[0], "digit"))
                currentChain[0] = "]"
                currentChain[1] = "sqrbrkt2"
                words.append(Lexeme(*currentChain))
                currentChain = ['', 'None']
                state = "afterSqrbrkt2"

            elif (state == "afterSecondBorder"):
                currentChain[0] = "]"
                currentChain[1] = "sqrbrkt2"
                words.append(Lexeme(*currentChain))
                currentChain = ['', 'None']
                state = "afterSqrbrkt2"
            else:
                dataOutput(0)
                exit(0)

        elif s.class_ == "semicolon":
            if state == "type":
                words.append(Lexeme(currentChain[0], "identifier"))
                words.append(Lexeme(";", "semicolon"))
                currentChain = ['', "None"]
                state = "afterSemicolon"

            elif (state == "afterType"):
                currentChain[0] += s.symbol
                words.append(Lexeme(currentChain[0], "semicolon"))
                currentChain = ['', "None"]
                state = "afterSemicolon"
            else:
                dataOutput(0)
                exit(0)

        else:
            dataOutput(0)
            exit(0)

    return words