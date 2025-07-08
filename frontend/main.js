async function generateCode() {
  const logicInput = document.getElementById("logicInput").value.trim();

  const reasoningBox = document.getElementById("reasoningOutput");
  const codeBox = document.getElementById("codeOutput");
  const edgeBox = document.getElementById("edgeCaseOutput");

  if (!logicInput) {
    reasoningBox.innerText = "⚠️ Please enter your logic first.";
    codeBox.innerText = "";
    edgeBox.innerText = "";
    return;
  }

  reasoningBox.innerText = "BuddyCode is thinking... 🧠";
  codeBox.innerText = "";
  edgeBox.innerText = "";

  try {
    const res = await fetch("/generate", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ logic: logicInput })
    });

    const data = await res.json();

    // If the backend returned a string instead of structured output
    if (typeof data.response === "string") {
      reasoningBox.innerText = data.response;
      codeBox.innerText = "";
      edgeBox.innerText = "";
    } else if (typeof data.response === "object") {
      reasoningBox.innerText = data.response.reasoning || "No reasoning provided.";
      codeBox.innerText = data.response.code || "No code provided.";
      edgeBox.innerText = data.response.edge_cases || "No edge cases identified.";
    } else {
      reasoningBox.innerText = "⚠️ Unexpected response format.";
    }

  } catch (error) {
    reasoningBox.innerText = `❌ Failed to reach backend:\n${error.message}`;
    codeBox.innerText = "";
    edgeBox.innerText = "";
  }
}
