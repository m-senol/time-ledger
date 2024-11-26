document.addEventListener("DOMContentLoaded", () => {
    // Check-In
    const checkInForm = document.getElementById("check-in-form");
    checkInForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const messageDiv = document.getElementById("message");

        const response = await fetch(checkInForm.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCsrfToken(),
            },
        });

        const data = await response.json();
        messageDiv.textContent = data.message || "An error occurred.";
        messageDiv.style.color = response.ok ? "green" : "red";
    });

    // Check-Out
    const checkOutForm = document.getElementById("check-out-form");
    checkOutForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const messageDiv = document.getElementById("message");

        const response = await fetch(checkOutForm.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCsrfToken(),
            },
        });

        const data = await response.json();
        messageDiv.textContent = data.message || "An error occurred.";
        messageDiv.style.color = response.ok ? "green" : "red";
    });

    function getCsrfToken() {
        const cookies = document.cookie.split(";").map(cookie => cookie.trim());
        const csrfCookie = cookies.find(cookie => cookie.startsWith("csrftoken="));
        return csrfCookie ? csrfCookie.split("=")[1] : "";
    }
});
