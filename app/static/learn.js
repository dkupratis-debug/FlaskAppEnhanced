const tracks = {
  beginner: {
    nextAction: "Open docs/FIRST_10_MINUTES.md and complete Exercise 1.",
    nextResult: "You open your first PR in your fork and checks pass.",
    steps: [
      "Read README.md",
      "Open docs/FIRST_10_MINUTES.md",
      "Open Start Here issue (#9)",
      "Complete Week 1 challenge (#18)",
      "Watch a green CI run in Actions"
    ]
  },
  intermediate: {
    nextAction: "Complete Exercises 4, 5, and 8 in docs/PRACTICE_EXAMPLES.md.",
    nextResult: "You can write a small test and review a PR confidently.",
    steps: [
      "Open docs/PRACTICE_EXAMPLES.md",
      "Complete Exercise 4 (doc improvement)",
      "Complete Exercise 5 (PR review)",
      "Complete Exercise 8 (local quality check)",
      "Explain CI jobs in your own words"
    ]
  },
  maintainer: {
    nextAction: "Use docs/TRAINING_OPERATIONS.md to run one weekly challenge cycle.",
    nextResult: "You can track learners and respond consistently.",
    steps: [
      "Read docs/TRAINING_OPERATIONS.md",
      "Use docs/LEARNER_PROGRESS_TEMPLATE.md",
      "Create or run a weekly challenge issue",
      "Reply using docs/COACHING_REPLY_TEMPLATES.md",
      "Review Insights -> Traffic and summarize outcomes"
    ]
  }
};

const storageKey = "flaskappenhanced-learning-progress";
const trackSelect = document.getElementById("track-select");
const nextAction = document.getElementById("next-action");
const nextResult = document.getElementById("next-result");
const checklist = document.getElementById("checklist");

function loadProgress() {
  try {
    return JSON.parse(localStorage.getItem(storageKey) || "{}");
  } catch (_) {
    return {};
  }
}

function saveProgress(progress) {
  localStorage.setItem(storageKey, JSON.stringify(progress));
}

function renderChecklist(trackName) {
  const progress = loadProgress();
  const trackProgress = progress[trackName] || {};
  const data = tracks[trackName];

  nextAction.textContent = data.nextAction;
  nextResult.textContent = data.nextResult;
  checklist.innerHTML = "";

  data.steps.forEach((step, index) => {
    const row = document.createElement("label");
    row.className = "check-row";

    const box = document.createElement("input");
    box.type = "checkbox";
    box.checked = !!trackProgress[index];
    box.addEventListener("change", () => {
      const latest = loadProgress();
      if (!latest[trackName]) latest[trackName] = {};
      latest[trackName][index] = box.checked;
      saveProgress(latest);
    });

    const text = document.createElement("span");
    text.textContent = step;

    row.appendChild(box);
    row.appendChild(text);
    checklist.appendChild(row);
  });
}

trackSelect.addEventListener("change", (e) => {
  renderChecklist(e.target.value);
});

renderChecklist(trackSelect.value);
