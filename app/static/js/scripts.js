// Ensure JavaScript is Loaded
console.log("JavaScript is working!");

// Multitext Effect (Typed.js)
document.addEventListener("DOMContentLoaded", () => {
    if (typeof Typed !== "undefined") {
        // Initialize Typed.js effect on elements with class 'multiText'
        const typingEffect = new Typed(".multiText", {
            strings: ["D.O.H", "The Good Music Fellas", "Defenders Of House"],
            loop: true,
            typeSpeed: 100,
            backSpeed: 80,
            backDelay: 1500,
        });
    } else {
        console.warn("Typed.js library is missing or not loaded.");
    }
});

// Gallery Fullscreen Functionality
function toggleFullScreen(element) {
    if (!document.fullscreenElement) {
        // Enter fullscreen mode
        element.requestFullscreen().catch((err) => {
            console.error(
                `Error attempting to enable full-screen mode: ${err.message} (${err.name})`
            );
        });
    } else {
        // Exit fullscreen mode
        document.exitFullscreen().catch((err) => {
            console.error(
                `Error attempting to exit full-screen mode: ${err.message} (${err.name})`
            );
        });
    }
}

// Optional: Event Listener for Gallery Images
document.addEventListener("click", (event) => {
    const target = event.target;
    if (target && target.classList.contains("gallery-image")) {
        toggleFullScreen(target);
    }
});
