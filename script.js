
const quizData = {
  en: [
    {
      question: "What does HTTPS stand for?",
      options: ["HyperText Transfer Protocol Secure", "High Text Transfer Protocol Secure", "HyperText Transfer Primary Secure", "HyperText Transfer Private Server"],
      answer: 0,
      hint: "It’s the secure version of HTTP."
    },
    {
      question: "What is phishing?",
      options: ["A sport", "Fake websites/emails to steal data", "A coding language", "An antivirus"],
      answer: 1,
      hint: "It's often done through email."
    }
    // Add 8 more...
  ],
  ru: [
    {
      question: "Что означает HTTPS?",
      options: ["Безопасный протокол передачи гипертекста", "Простой протокол данных", "Приватный сервер", "Защищённая сессия"],
      answer: 0,
      hint: "Это защищённая версия HTTP."
    },
    {
      question: "Что такое фишинг?",
      options: ["Вид спорта", "Мошенничество с сайтами/почтой", "Язык программирования", "Антивирус"],
      answer: 1,
      hint: "Обычно через e-mail."
    }
    // Add 8 more...
  ],
  kg: [
    {
      question: "HTTPS эмнени билдирет?",
      options: ["Коопсуз гипертекст протоколу", "Маалымат жүктөө системасы", "Приваттык сервер", "Код жазуу протоколу"],
      answer: 0,
      hint: "Бул HTTP'тун коопсуз версиясы."
    },
    {
      question: "Фишинг деген эмне?",
      options: ["Спорттун түрү", "Алдамчылык менен маалымат уурдоо", "Программалоо тили", "Антивирус"],
      answer: 1,
      hint: "Көбүнчө почта аркылуу."
    }
    // Add 8 more...
  ]
};

let currentLang = "en";

function setLanguage(lang) {
  currentLang = lang;
  loadQuiz();
}

function loadQuiz() {
  const quizContainer = document.getElementById("quiz-container");
  const questions = quizData[currentLang];
  quizContainer.innerHTML = "";
  questions.forEach((q, idx) => {
    const div = document.createElement("div");
    div.classList.add("question");
    div.innerHTML = \`
      <p><strong>\${idx + 1}. \${q.question}</strong></p>
      \${q.options.map((opt, i) =>
        \`<label><input type="radio" name="q\${idx}" value="\${i}" /> \${opt}</label><br>\`).join("")}
      <small><em>Hint: \${q.hint}</em></small>
    \`;
    quizContainer.appendChild(div);
  });
}

function submitQuiz() {
  const questions = quizData[currentLang];
  let score = 0;
  questions.forEach((q, idx) => {
    const selected = document.querySelector(\`input[name="q\${idx}"]:checked\`);
    if (selected && parseInt(selected.value) === q.answer) {
      score++;
    }
  });
  document.getElementById("result").innerText = \`You scored \${score} out of \${questions.length}.\`;
}

window.onload = () => {
  loadQuiz();
};
