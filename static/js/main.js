document.addEventListener("DOMContentLoaded", () => {
    const nodePositions = {};

    document.querySelectorAll('.circle-node').forEach(el => {
        const ipa = el.textContent.trim();
        const rect = el.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2 + window.scrollX;
        const centerY = rect.top + rect.height / 2 + window.scrollY;
        nodePositions[ipa] = { x: centerX, y: centerY };
    });
    
    document.querySelectorAll('.dot-node').forEach(dot => {
      const parentId = dot.dataset.parent;
      const parentEl = document.getElementById(parentId);
      if (!parentEl) return;

      const rect = parentEl.getBoundingClientRect();
      const scrollX = window.scrollX;
      const scrollY = window.scrollY;

      // Circle-node is 40x40, dot-node is 10x10
      const dotOffsetX = 30 - 5; // 75% of 40 = 30, minus half dot width
      const dotOffsetY = 10 - 5; // 25% of 40 = 10, minus half dot height

      const x = rect.left + dotOffsetX + scrollX;
      const y = rect.top + dotOffsetY + scrollY;

      dot.style.left = `${x}px`;
      dot.style.top = `${y}px`;
    });


    

    const svg = document.getElementById('edges');
    const edges = window.edgeData || [];

    edges.forEach(([ipaA, ipaB]) => {
        const nodeA = nodePositions[ipaA];
        const nodeB = nodePositions[ipaB];
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
    const nodeId = el.getAttribute("ipa");
    clickedNodes.push(nodeId);
    updateClickedNodesDisplay();

}

function updateClickedNodesDisplay() {
    document.getElementById('clicked-nodes').textContent = clickedNodes.join(' ');
    clearResponse();
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
}

function clearResponse() {
    const responseDiv = document.getElementById('response-message');
    responseDiv.textContent = '';
    responseDiv.className = '';
}

function handleBackBtn() {
    clickedNodes.pop();
    updateClickedNodesDisplay();
}