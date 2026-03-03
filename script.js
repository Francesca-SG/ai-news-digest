document.getElementById("btn").addEventListener("click", async () => {
    console.log("Button clicked");

    const region = document.getElementById("region").value;
    const topic = document.getElementById("topic").value;

    const response = await fetch("/digest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ region, topic })
    });

    const data = await response.json();
    document.getElementById("output").textContent = data.digest;
});