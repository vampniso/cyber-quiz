quiz_data = {
    "en": [
        {"question": "What does 'https' stand for?", "answer": "Hypertext Transfer Protocol Secure", "hint": "It's a secure version of HTTP."},
        {"question": "What is phishing?", "answer": "A fraudulent attempt to obtain sensitive information", "hint": "It’s like fake emails or websites to trick you."},
        {"question": "What is a strong password?", "answer": "A combination of letters, numbers, and symbols", "hint": "It should be long and hard to guess."},
        {"question": "What does a firewall do?", "answer": "It blocks unauthorized access", "hint": "It protects your network."},
        {"question": "What is two-factor authentication?", "answer": "A security process with two steps", "hint": "Like password + code to phone."},
        {"question": "What is malware?", "answer": "Malicious software", "hint": "Includes viruses, spyware, etc."},
        {"question": "Should you click on unknown links?", "answer": "No", "hint": "Think before you click."},
        {"question": "Is public Wi-Fi safe?", "answer": "No", "hint": "Avoid banking or sensitive info on it."},
        {"question": "What is encryption?", "answer": "The process of encoding information", "hint": "Used to protect data."},
        {"question": "What is a VPN?", "answer": "Virtual Private Network", "hint": "It hides your IP and encrypts connection."}
    ],
    "ru": [
        {"question": "Что означает 'https'?", "answer": "Безопасный протокол передачи гипертекста", "hint": "Это защищённая версия HTTP."},
        {"question": "Что такое фишинг?", "answer": "Мошенническая попытка получить личные данные", "hint": "Часто используют фейковые письма или сайты."},
        {"question": "Что такое надёжный пароль?", "answer": "Сочетание букв, цифр и символов", "hint": "Он должен быть длинным и сложным."},
        {"question": "Что делает межсетевой экран?", "answer": "Блокирует несанкционированный доступ", "hint": "Он защищает сеть."},
        {"question": "Что такое двухфакторная аутентификация?", "answer": "Процесс защиты в два этапа", "hint": "Например, пароль + код на телефон."},
        {"question": "Что такое вредоносное ПО?", "answer": "Злонамеренное программное обеспечение", "hint": "Вирусы, шпионы и прочее."},
        {"question": "Нужно ли нажимать на неизвестные ссылки?", "answer": "Нет", "hint": "Думай, прежде чем кликнуть."},
        {"question": "Общественный Wi-Fi безопасен?", "answer": "Нет", "hint": "Избегай операций с личными данными."},
        {"question": "Что такое шифрование?", "answer": "Процесс кодирования информации", "hint": "Нужно для защиты данных."},
        {"question": "Что такое VPN?", "answer": "Виртуальная частная сеть", "hint": "Скрывает IP и шифрует соединение."}
    ],
    "kg": [
        {"question": "'https' эмнени билдирет?", "answer": "Коопсуз гипертекст өткөрүү протоколу", "hint": "HTTP’нин коопсуз версиясы."},
        {"question": "Фишинг деген эмне?", "answer": "Жеке маалыматты алдоо менен алуу аракети", "hint": "Көбүнчө жасалма сайт же кат."},
        {"question": "Күчтүү сырсөз деген эмне?", "answer": "Тамгалар, сандар жана белгилер аралашмасы", "hint": "Узун жана татаал болушу керек."},
        {"question": "Firewall эмнеге керек?", "answer": "Уруксатсыз кирүүнү тосот", "hint": "Тармакты коргойт."},
        {"question": "Эки кадамдуу текшерүү эмне?", "answer": "Коопсуздуктун эки этаптуу процесси", "hint": "Мисалы, сырсөз + код."},
        {"question": "Зыяндуу программа деген эмне?", "answer": "Зыяндуу программалык камсыздоо", "hint": "Вирус, тыңшоочу ж.б."},
        {"question": "Белгисиз шилтемени басуу керекпи?", "answer": "Жок", "hint": "Башында ойлон!"}, 
        {"question": "Ачык Wi-Fi коопсузбу?", "answer": "Жок", "hint": "Жеке маалымат колдонбо."},
        {"question": "Шифрлөө деген эмне?", "answer": "Маалыматты коддоо процесси", "hint": "Маалыматты коргоо үчүн."},
        {"question": "VPN деген эмне?", "answer": "Виртуалдык жеке тармак", "hint": "IP’ни жашырат жана байланыш шифрлейт."}
    ]
}

def start_quiz():
    print("Choose language / Выберите язык / Тилди тандаңыз: (en/ru/kg)")
    lang = input("Language: ").strip().lower()

    if lang not in quiz_data:
        print("Invalid language. Try again.")
        return

    questions = quiz_data[lang]
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        while True:
            user_input = input("Your answer (or type 'hint' or 'answer'): ").strip()
            if user_input.lower() == "hint":
                print("Hint:", q["hint"])
            elif user_input.lower() == "answer":
                print("Correct answer:", q["answer"])
                break
            elif user_input.lower() == q["answer"].lower():
                print("✅ Correct!")
                score += 1
                break
            else:
                print("❌ Incorrect. Try again or type 'hint'.")

    print(f"\n🎉 Quiz finished! Your score: {score} out of {len(questions)}")

start_quiz()

