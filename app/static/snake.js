(function () {
  const gameRoot = document.getElementById("snake-game");
  if (!gameRoot) {
    return;
  }

  const config = JSON.parse(gameRoot.dataset.config || "{}");
  const grid = document.getElementById("snake-grid");
  const scoreEl = document.getElementById("snake-score");
  const statusEl = document.getElementById("snake-status");
  const pauseBtn = document.getElementById("snake-pause");
  const restartBtn = document.getElementById("snake-restart");
  const controlButtons = document.querySelectorAll(".snake-controls button");

  const cellCount = config.width * config.height;
  grid.style.gridTemplateColumns = `repeat(${config.width}, minmax(0, 1fr))`;

  function isOpposite(a, b) {
    return (
      (a === "up" && b === "down") ||
      (a === "down" && b === "up") ||
      (a === "left" && b === "right") ||
      (a === "right" && b === "left")
    );
  }

  function createInitialSnake() {
    const midX = Math.floor(config.width / 2);
    const midY = Math.floor(config.height / 2);
    return Array.from({ length: config.start_length }, (_, idx) => ({
      x: midX - idx,
      y: midY,
    }));
  }

  function randomFood(snake) {
    const occupied = new Set(snake.map((cell) => `${cell.x},${cell.y}`));
    const freeCells = [];
    for (let y = 0; y < config.height; y += 1) {
      for (let x = 0; x < config.width; x += 1) {
        const key = `${x},${y}`;
        if (!occupied.has(key)) freeCells.push({ x, y });
      }
    }
    if (freeCells.length === 0) return null;
    return freeCells[Math.floor(Math.random() * freeCells.length)];
  }

  function buildInitialState() {
    const snake = createInitialSnake();
    return {
      snake,
      direction: "right",
      pendingDirection: "right",
      food: randomFood(snake),
      score: 0,
      gameOver: false,
      paused: false,
    };
  }

  function nextHead(head, direction) {
    if (direction === "up") return { x: head.x, y: head.y - 1 };
    if (direction === "down") return { x: head.x, y: head.y + 1 };
    if (direction === "left") return { x: head.x - 1, y: head.y };
    return { x: head.x + 1, y: head.y };
  }

  function advance(state) {
    if (state.gameOver || state.paused) return;

    const direction = isOpposite(state.direction, state.pendingDirection)
      ? state.direction
      : state.pendingDirection;
    const head = nextHead(state.snake[0], direction);
    const outside =
      head.x < 0 || head.y < 0 || head.x >= config.width || head.y >= config.height;
    const ateFood = state.food && head.x === state.food.x && head.y === state.food.y;
    const body = ateFood ? state.snake : state.snake.slice(0, -1);
    const hitSelf = body.some((part) => part.x === head.x && part.y === head.y);

    if (outside || hitSelf) {
      state.gameOver = true;
      statusEl.textContent = "Game Over";
      return;
    }

    const nextSnake = [head, ...state.snake];
    if (!ateFood) {
      nextSnake.pop();
    } else {
      state.score += 1;
    }

    state.snake = nextSnake;
    state.direction = direction;
    state.food = ateFood ? randomFood(state.snake) : state.food;
    if (!state.food) {
      state.gameOver = true;
      statusEl.textContent = "You Win";
    }
  }

  function render(state) {
    scoreEl.textContent = String(state.score);
    if (!state.gameOver && !state.paused) {
      statusEl.textContent = "Running";
    }
    if (!state.gameOver && state.paused) {
      statusEl.textContent = "Paused";
    }

    const snakeCells = new Set(state.snake.map((cell) => `${cell.x},${cell.y}`));
    const foodKey = state.food ? `${state.food.x},${state.food.y}` : null;

    for (let idx = 0; idx < cellCount; idx += 1) {
      const x = idx % config.width;
      const y = Math.floor(idx / config.width);
      const key = `${x},${y}`;
      const cell = grid.children[idx];
      const isHead = state.snake[0].x === x && state.snake[0].y === y;

      cell.className = "snake-cell";
      if (snakeCells.has(key)) {
        cell.classList.add(isHead ? "snake-head" : "snake-body");
      } else if (foodKey === key) {
        cell.classList.add("snake-food");
      }
    }
  }

  function setDirection(direction) {
    if (direction && !isOpposite(state.direction, direction)) {
      state.pendingDirection = direction;
    }
  }

  function togglePause() {
    if (state.gameOver) return;
    state.paused = !state.paused;
    pauseBtn.textContent = state.paused ? "Resume" : "Pause";
    render(state);
  }

  function restart() {
    state = buildInitialState();
    pauseBtn.textContent = "Pause";
    render(state);
  }

  for (let idx = 0; idx < cellCount; idx += 1) {
    const cell = document.createElement("div");
    cell.className = "snake-cell";
    grid.appendChild(cell);
  }

  let state = buildInitialState();

  document.addEventListener("keydown", (event) => {
    const key = event.key.toLowerCase();

    if (key === "arrowup") {
      event.preventDefault();
      setDirection("up");
    }
    if (key === "arrowdown") {
      event.preventDefault();
      setDirection("down");
    }
    if (key === "arrowleft") {
      event.preventDefault();
      setDirection("left");
    }
    if (key === "arrowright") {
      event.preventDefault();
      setDirection("right");
    }

    if (key === "w") setDirection("up");
    if (key === "s") setDirection("down");
    if (key === "a") setDirection("left");
    if (key === "d") setDirection("right");
    if (key === " " || key === "p") {
      event.preventDefault();
      togglePause();
    }
    if (key === "r") restart();
  });

  controlButtons.forEach((button) => {
    button.addEventListener("click", () => {
      setDirection(button.dataset.direction);
    });
  });

  pauseBtn.addEventListener("click", togglePause);
  restartBtn.addEventListener("click", restart);

  setInterval(() => {
    advance(state);
    render(state);
  }, config.tick_ms);

  render(state);
})();

