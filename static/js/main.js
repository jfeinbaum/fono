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

function handleClick(el) {
    const nodeId = el.getAttribute("data-id");

    fetch('/api/node_click', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ node_id: nodeId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('clicked-nodes').textContent = data.clicked_nodes.join(' ');
            console.log(data.message);
        } else {
            console.error('Failed to process node click');
        }
    })
    .catch(error => {
        console.error('Error during fetch:', error);
    });
}

function handleDotClick(event, nodeId) {
    event.stopPropagation();

    fetch('/api/node_dot_click', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ node_id: nodeId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('clicked-nodes').textContent = data.clicked_nodes.join(' ');
            console.log(data.message);
        } else {
            console.error('Failed to process node dot click');
        }
    })
    .catch(error => {
        console.error('Error during fetch:', error);
    });
}
