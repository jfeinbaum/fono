document.addEventListener("DOMContentLoaded", () => {
    const nodePositions = {};
    document.querySelectorAll('.node').forEach(el => {
        const id = el.dataset.id;
        const rect = el.getBoundingClientRect();
        nodePositions[id] = {
            x: rect.left + rect.width / 2 + window.scrollX,
            y: rect.top + rect.height / 2 + window.scrollY
        };
    });

    const edges = window.edgeData || [];
    const svg = document.getElementById('edges');

    edges.forEach(([a, b]) => {
        const nodeA = nodePositions[a];
        const nodeB = nodePositions[b];
        if (!nodeA || !nodeB) return;

        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", nodeA.x);
        line.setAttribute("y1", nodeA.y);
        line.setAttribute("x2", nodeB.x);
        line.setAttribute("y2", nodeB.y);
        line.setAttribute("stroke", "black");
        line.setAttribute("stroke-width", "2");
        svg.appendChild(line);
    });
});


let audioURL = null;
let lastPath = null;
let clickedNodes = [];

function handleNewSoundBtn() {
  const encodedLast = lastPath ? encodeURIComponent(lastPath) : '';
  clickedNodes.length = 0;
  updateClickedNodesDisplay();
  clearResponse();

  fetch(`/get-audio?last=${encodedLast}`)
    .then(response => {
      const newPath = response.headers.get('X-Audio-Path');
      lastPath = newPath;

      return response.blob();
    })
    .then(blob => {
      if (audioURL) {
        URL.revokeObjectURL(audioURL);
      }
      audioURL = URL.createObjectURL(blob);
      new Audio(audioURL).play();
    })
    .catch(err => console.error('Error loading audio:', err));
}

function handlePlaySoundBtn() {
  if (audioURL) {
    const audio = new Audio(audioURL);
    audio.play();
  } else {
    console.warn("No audio loaded yet.");
    handleNewSoundBtn();
  }
}

function handleSubmitBtn() {
    if (clickedNodes.length === 0) return;
    fetch('/validate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sequence: clickedNodes })
    })
    .then(response => response.json())
    .then(data => {
        if (data.correct) {
            displayCorrect();
        } else {
            displayIncorrect();
        }
    })

}

function handleNodeClick(el) {
    const nodeId = el.getAttribute("data-id");
    clickedNodes.push(nodeId);
    updateClickedNodesDisplay();

}

function handleDotClick(event, nodeId) {
    event.stopPropagation();
    clickedNodes.push(nodeId);
    updateClickedNodesDisplay();
}

function updateClickedNodesDisplay() {
    document.getElementById('clicked-nodes').textContent = clickedNodes.join(' ');
}

function displayCorrect() {
    const responseDiv = document.getElementById('response-message');
    responseDiv.textContent = 'Correct!';
    responseDiv.className = 'correct-response';
}

function displayIncorrect() {
    const responseDiv = document.getElementById('response-message');
    responseDiv.textContent = 'Incorrect.';
    responseDiv.className = 'incorrect-response';
    clickedNodes.length = 0;
    updateClickedNodesDisplay();
}

function clearResponse() {
    const responseDiv = document.getElementById('response-message');
    responseDiv.textContent = '';
    responseDiv.className = '';
}