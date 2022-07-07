def syntax(words):
    state = "start"

    for word in words:
        if word.class_ == "var":
            if state == "start":
                state = "identifierWithCommaOrNot"
            else:
                return 0

        elif word.class_ == "identifierWithComma":
            if state == "identifierWithCommaOrNot":
                state = "identifierWithCommaOrNot"
            else:
                return 0

        elif word.class_ == "identifier":
            if state == "identifierWithCommaOrNot":
                state = "colon"
            elif state == "firstBorder":
                state = "dots"
            elif state == "secondBorder":
                state = "sqrbrkt2"
            else:
                return 0

        elif word.class_ == "digit":
            if state == "firstBorder":
                state = "dots"
            elif state == "secondBorder":
                state = "sqrbrkt2"

        elif word.class_ == "colon":
            if state == "colon":
                state = "array"
            else:
                return 0
        elif word.class_ == "array":
            if state == "array":
                state = "sqrbrkt1"
            else:
                return 0

        elif word.class_ == "sqrbrkt1":
            if state == "sqrbrkt1":
                state = "firstBorder"
            else:
                return 0

        elif word.class_ == "dots":
            if state == "dots":
                state = "secondBorder"
            else:
                return 0

        elif word.class_ == "sqrbrkt2":
            if state == "sqrbrkt2":
                state = "of"
            else:
                return 0
        elif word.class_ == "of":
            if state == "of":
                state = "type"
            else:
                return 0
        elif word.class_ == "type":
            if state == "type":
                state = "semicolon"
            else:
                return 0
        elif word.class_ == "semicolon":
            if state == "semicolon":
                state = "semicolonCompleted"
            else:
                return 0
# С‚РѕР»СЊРєРѕ РїСЂРё РґР°РЅРЅРѕРј СѓСЃР»РѕРІРёРё С†РµРїРѕС‡РєР° РїСЂРёР·РЅР°РµС‚СЃСЏ РІР°Р»РёРґРЅРѕР№
    if state == "semicolonCompleted":
        return 1
    return 0