async function getCareer() {
    const skills = document.getElementById("skills").value
        .split(",").map(s => s.trim().toLowerCase());

    const interests = document.getElementById("interests").value
        .split(",").map(i => i.trim().toLowerCase());

    const strengths = document.getElementById("strengths").value
        .split(",").map(st => st.trim().toLowerCase());

    if (!skills[0]) {
        alert("Please enter at least one skill");
        return;
    }

    const loading = document.getElementById("loading");
    const resultsDiv = document.getElementById("results");

    loading.classList.remove("hidden");
    resultsDiv.innerHTML = "";

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/recommend-career",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    skills: skills,
                    interests: interests,
                    strengths: strengths
                })
            }
        );

        const data = await response.json();
        loading.classList.add("hidden");

        data.recommended_roles.forEach(role => {
            const card = document.createElement("div");
            card.className = "career-card";

            card.innerHTML = `
                <h3>${role.role}</h3>
                <p class="score">Fit Score: ${role.score}%</p>
                <p><b>Why:</b> ${role.reason}</p>
                <p><b>Missing Skills:</b> ${role.missing_skills.join(", ") || "None"}</p>
                <p><b>Next Steps:</b> ${role.next_steps.join(", ") || "You are on track"}</p>
            `;

            resultsDiv.appendChild(card);
        });

    } catch (err) {
        loading.classList.add("hidden");
        alert("Backend not running");
    }
}
